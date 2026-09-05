#!/usr/bin/env python3
"""Mechanical validator for the DIUA-DIC registration record (BUS-17).

Checks registration_record.json against the rules established by the
canonical Content OS Universal Identifier Registration Record document
(Linear, v1.6), and cross-validates it against the sibling BUS-16 registry
state (registry.json) in this same directory:

  - required fields:      allocation_act_id, identifier, target_document,
                          allocation_basis, allocation_state present and
                          non-empty (issue may be null)
  - allocation_act_id:    format CONTENT-OS-ALLOC-<3DigitSequence>, unique,
                          and its sequence number matches the identifier's
                          own sequence number (acts are allocated 1:1 and
                          in the same order as identifiers)
  - identifier:           format DIUA-DIC-<6DigitSequence>, unique (no
                          duplicate registration of the same identifier)
  - referential integrity: every registration-record identifier must exist
                          in registry.json (no orphan/unknown identifier),
                          and every registry.json allocation must have a
                          corresponding registration record (no allocation
                          left without evidence)
  - non-contradiction:    target_document, issue, and allocation_state must
                          match the corresponding registry.json allocation's
                          registered_document, issue, and lifecycle_state
  - canonical closure:    allocations_recorded, range_start/end, and
                          next_available_sequence in registration_record.json
                          match what is actually recorded

This script has no third-party dependencies. It does not talk to Linear;
it only checks internal consistency and consistency with registry.json.
Linear remains the canonical source of truth for both (see README.md in
this directory). BUS-16's registry.json remains authoritative for current
registry state; this document is evidence/traceability only.
"""

import json
import re
import sys
from pathlib import Path

ACT_ID_RE = re.compile(r"^CONTENT-OS-ALLOC-(\d{3})$")
IDENTIFIER_RE = re.compile(r"^DIUA-DIC-(\d{6})$")
REQUIRED_ACT_FIELDS = (
    "allocation_act_id",
    "identifier",
    "target_document",
    "allocation_basis",
    "allocation_state",
)


def fail(errors, message):
    errors.append(message)


def load_json(path, errors):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"could not read/parse {path}: {exc}")
        return None


def main():
    base_dir = Path(__file__).parent
    record_path = base_dir / "registration_record.json"
    registry_path = base_dir / "registry.json"
    errors = []

    record_data = load_json(record_path, errors)
    registry_data = load_json(registry_path, errors)
    if record_data is None or registry_data is None:
        print(f"FAIL: {len(errors)} issue(s) found")
        for e in errors:
            print(f"  - {e}")
        return 1

    acts = record_data.get("allocation_acts", [])
    closure = record_data.get("registration_record", {}).get("canonical_closure", {})
    registry_allocations = {
        a.get("identifier"): a for a in registry_data.get("allocations", [])
    }

    if not acts:
        fail(errors, "no allocation_acts found in registration_record.json")

    seen_act_sequences = set()
    seen_identifier_sequences = set()
    covered_identifiers = set()

    for i, act in enumerate(acts):
        label = act.get("allocation_act_id", f"<entry {i}>")

        for field in REQUIRED_ACT_FIELDS:
            value = act.get(field)
            if not isinstance(value, str) or not value.strip():
                fail(errors, f"{label}: missing or empty required field '{field}'")
        # 'issue' is a required key but may be null (SDOH acts predate an issue link)
        if "issue" not in act:
            fail(errors, f"{label}: missing required field 'issue' (may be null)")

        act_id = act.get("allocation_act_id", "")
        act_match = ACT_ID_RE.match(act_id)
        if not act_match:
            fail(
                errors,
                f"{label}: allocation_act_id does not match CONTENT-OS-ALLOC-<3DigitSequence> grammar",
            )
        else:
            act_seq = int(act_match.group(1))
            if act_seq in seen_act_sequences:
                fail(errors, f"{label}: duplicate allocation_act_id sequence {act_match.group(1)}")
            seen_act_sequences.add(act_seq)

        identifier = act.get("identifier", "")
        id_match = IDENTIFIER_RE.match(identifier)
        if not id_match:
            fail(errors, f"{label}: identifier '{identifier}' does not match DIUA-DIC-<6DigitSequence> grammar")
            continue

        id_seq = int(id_match.group(1))
        if id_seq in seen_identifier_sequences:
            fail(errors, f"{label}: duplicate registration of identifier {identifier} (uniqueness violation)")
        seen_identifier_sequences.add(id_seq)

        if act_match and int(act_match.group(1)) != id_seq:
            fail(
                errors,
                f"{label}: allocation_act_id sequence ({act_match.group(1)}) does not match "
                f"identifier sequence ({id_match.group(1)})",
            )

        registry_entry = registry_allocations.get(identifier)
        if registry_entry is None:
            fail(
                errors,
                f"{label}: identifier {identifier} is not present in registry.json "
                f"(BUS-16) — unknown/orphan identifier, not a valid current allocation",
            )
            continue

        covered_identifiers.add(identifier)

        if act.get("target_document") != registry_entry.get("registered_document"):
            fail(
                errors,
                f"{label}: target_document '{act.get('target_document')}' contradicts registry.json "
                f"registered_document '{registry_entry.get('registered_document')}' for {identifier}",
            )

        if act.get("issue") != registry_entry.get("issue"):
            fail(
                errors,
                f"{label}: issue '{act.get('issue')}' contradicts registry.json issue "
                f"'{registry_entry.get('issue')}' for {identifier}",
            )

        if act.get("allocation_state") != registry_entry.get("lifecycle_state"):
            fail(
                errors,
                f"{label}: allocation_state '{act.get('allocation_state')}' contradicts registry.json "
                f"lifecycle_state '{registry_entry.get('lifecycle_state')}' for {identifier}",
            )

    # Every registry allocation must be covered by a registration record (evidence completeness).
    for identifier in registry_allocations:
        if identifier not in covered_identifiers:
            fail(
                errors,
                f"registry.json allocation {identifier} has no corresponding allocation act in "
                f"registration_record.json — allocation without evidence/traceability",
            )

    if seen_identifier_sequences:
        ordered = sorted(seen_identifier_sequences)
        expected = list(range(1, len(ordered) + 1))
        if ordered != expected:
            fail(
                errors,
                f"sequencing gap or non-contiguous registration: got {ordered}, "
                f"expected a contiguous run {expected} starting at DIUA-DIC-000001",
            )

        recorded_count = closure.get("allocations_recorded")
        if recorded_count != len(ordered):
            fail(
                errors,
                f"canonical_closure.allocations_recorded ({recorded_count}) does not match "
                f"actual count of allocation acts ({len(ordered)})",
            )

        expected_start = f"DIUA-DIC-{ordered[0]:06d}"
        expected_end = f"DIUA-DIC-{ordered[-1]:06d}"
        if closure.get("range_start") != expected_start:
            fail(
                errors,
                f"canonical_closure.range_start '{closure.get('range_start')}' does not match "
                f"computed '{expected_start}'",
            )
        if closure.get("range_end") != expected_end:
            fail(
                errors,
                f"canonical_closure.range_end '{closure.get('range_end')}' does not match "
                f"computed '{expected_end}'",
            )

        expected_next = f"DIUA-DIC-{ordered[-1] + 1:06d}"
        if closure.get("next_available_sequence") != expected_next:
            fail(
                errors,
                f"canonical_closure.next_available_sequence '{closure.get('next_available_sequence')}' "
                f"does not match computed '{expected_next}'",
            )

    if errors:
        print(f"FAIL: {len(errors)} issue(s) found")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK: {len(acts)} allocation act(s) valid and consistent with registry.json (BUS-16)")
    print(f"    covered identifiers: {len(covered_identifiers)} of {len(registry_allocations)} registry allocations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
