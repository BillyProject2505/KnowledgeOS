#!/usr/bin/env python3
"""Mechanical validator for the DIUA-DIC registry state (BUS-16).

Checks registry.json against the rules established by the canonical
Content OS Universal Identifier Registry document (Linear, v1.4):

  - identifier format:   DIUA-DIC-<6DigitSequence>
  - uniqueness:          no identifier allocated twice
  - sequencing:          allocations form a contiguous run starting at
                         DIUA-DIC-000001 (per the registry's own
                         "next available sequence" allocation model)
  - required fields:     identifier, registered_document, object_class,
                         lifecycle_state present and non-empty
  - object class:        only classes the canonical document has actually
                         established (registry.established_object_classes)
  - next_available_sequence: matches (max allocated + 1)

This script has no third-party dependencies. It does not talk to Linear;
it only checks the internal consistency of registry.json. Linear remains
the canonical source of truth (see README.md in this directory).
"""

import json
import re
import sys
from pathlib import Path

IDENTIFIER_RE = re.compile(r"^DIUA-DIC-(\d{6})$")
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
        match = IDENTIFIER_RE.match(identifier)
        if not match:
            fail(errors, f"{label}: identifier does not match DIUA-DIC-<6DigitSequence> grammar")
            continue

        sequence = int(match.group(1))
        if sequence in seen_sequences:
            fail(errors, f"{label}: duplicate allocation of sequence {match.group(1)}")
        seen_sequences.add(sequence)

        object_class = entry.get("object_class")
        if established_classes and object_class not in established_classes:
            fail(
                errors,
                f"{label}: object_class '{object_class}' is not an established object class "
                f"({sorted(established_classes)}) — per canonical §6, no other class is established",
            )

    if seen_sequences:
        ordered = sorted(seen_sequences)
        expected = list(range(1, len(ordered) + 1))
        if ordered != expected:
            fail(
                errors,
                f"sequencing gap or non-contiguous allocation: got {ordered}, "
                f"expected a contiguous run {expected} starting at DIUA-DIC-000001",
            )

        computed_next = f"DIUA-DIC-{ordered[-1] + 1:06d}"
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
