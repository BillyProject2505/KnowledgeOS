#!/usr/bin/env python3
"""Mechanical validator for the DIUA-DIC registry state (BUS-16).

Checks registry.json against the rules established by the canonical
Content OS Universal Identifier Registry document (Linear, v1.4):

  - namespace self-consistency: registry.grammar is derived from
                         registry.namespace + registry.marker, so the
                         identifier format check can never silently drift
                         from the declared metadata (§3)
  - identifier format:   <namespace>-<marker>-<6DigitSequence>
                         (currently DIUA-DIC-<6DigitSequence>, §3)
  - uniqueness:          no identifier allocated twice
  - sequencing:          allocations form a contiguous run starting at
                         DIUA-DIC-000001 (per the registry's own
                         "next available sequence" allocation model, §4)
  - required fields:     identifier, registered_document, object_class,
                         lifecycle_state present and non-empty
  - object class:        every allocation's object_class must be one of
                         registry.established_object_classes, which must
                         itself be non-empty — §6 excludes any object
                         class other than "Content OS Document" as not
                         established, so an empty/missing list is a
                         registry defect, not a reason to skip the check
  - next_available_sequence: matches (max allocated + 1)

This script has no third-party dependencies. It does not talk to Linear;
it only checks the internal consistency of registry.json. Linear remains
the canonical source of truth (see README.md in this directory).
"""

import json
import re
import sys
from pathlib import Path

REQUIRED_FIELDS = ("identifier", "registered_document", "object_class", "lifecycle_state")


def fail(errors, message):
    errors.append(message)


def main():
    registry_path = Path(__file__).parent / "registry.json"
    errors = []

    try:
        data = json.loads(registry_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: could not read/parse {registry_path}: {exc}")
        return 1

    registry = data.get("registry", {})
    allocations = data.get("allocations", [])
    established_classes = set(registry.get("established_object_classes", []))

    namespace = registry.get("namespace")
    marker = registry.get("marker")
    if not namespace or not isinstance(namespace, str):
        fail(errors, "registry.namespace is missing or empty")
    if not marker or not isinstance(marker, str):
        fail(errors, "registry.marker is missing or empty")

    if namespace and marker:
        expected_grammar = f"{namespace}-{marker}-<6DigitSequence>"
        declared_grammar = registry.get("grammar")
        if declared_grammar != expected_grammar:
            fail(
                errors,
                f"registry.grammar '{declared_grammar}' does not match the grammar derived "
                f"from namespace/marker ('{expected_grammar}') — these must not drift apart",
            )
        identifier_re = re.compile(rf"^{re.escape(namespace)}-{re.escape(marker)}-(\d{{6}})$")
    else:
        identifier_re = None

    if not established_classes:
        fail(
            errors,
            "registry.established_object_classes is missing or empty — per canonical §6, "
            "\"Content OS Document\" must be declared as the (sole) established object class; "
            "an empty list must fail closed, not silently skip the object-class check",
        )

    if not allocations:
        fail(errors, "no allocations found in registry.json")

    seen_sequences = set()
    for i, entry in enumerate(allocations):
        label = entry.get("identifier", f"<entry {i}>")

        for field in REQUIRED_FIELDS:
            value = entry.get(field)
            if not isinstance(value, str) or not value.strip():
                fail(errors, f"{label}: missing or empty required field '{field}'")

        identifier = entry.get("identifier", "")
        if identifier_re is None:
            continue
        match = identifier_re.match(identifier)
        if not match:
            fail(errors, f"{label}: identifier does not match {namespace}-{marker}-<6DigitSequence> grammar")
            continue

        sequence = int(match.group(1))
        if sequence in seen_sequences:
            fail(errors, f"{label}: duplicate allocation of sequence {match.group(1)}")
        seen_sequences.add(sequence)

        object_class = entry.get("object_class")
        if object_class not in established_classes:
            fail(
                errors,
                f"{label}: object_class '{object_class}' is not an established object class "
                f"({sorted(established_classes)}) — per canonical §6, no other class is established",
            )

    prefix = f"{namespace}-{marker}" if (namespace and marker) else "DIUA-DIC"

    if seen_sequences:
        ordered = sorted(seen_sequences)
        expected = list(range(1, len(ordered) + 1))
        if ordered != expected:
            fail(
                errors,
                f"sequencing gap or non-contiguous allocation: got {ordered}, "
                f"expected a contiguous run {expected} starting at {prefix}-000001",
            )

        computed_next = f"{prefix}-{ordered[-1] + 1:06d}"
        declared_next = registry.get("next_available_sequence")
        if declared_next != computed_next:
            fail(
                errors,
                f"next_available_sequence mismatch: registry.json declares "
                f"'{declared_next}', computed '{computed_next}' from current allocations",
            )

    if errors:
        print(f"FAIL: {len(errors)} issue(s) found in {registry_path}")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK: {len(allocations)} allocation(s) valid, format/uniqueness/sequencing/fields consistent")
    print(f"    next available sequence: {registry.get('next_available_sequence')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
