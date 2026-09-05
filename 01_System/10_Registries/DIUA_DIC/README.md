# DIUA_DIC — Content OS Universal Identifier Registry & Registration Record

## Purpose

This directory is the repository-side materialization of two related but distinct canonical documents governing the `DIUA-DIC-<6DigitSequence>` namespace:

- **BUS-16 — Universal Identifier Registry**: the authoritative current registry state (which identifiers exist and what they are currently allocated to).
- **BUS-17 — Universal Identifier Registration Record**: allocation-act-level evidence and traceability for each identifier issued by the Registry (why and when it was allocated). This is evidence, not a second registry — it must never be treated as authoritative for current state.

## Canonical Sources

**The canonical authority for both artifacts is their respective Linear document, not this directory:**

> Content OS — Universal Identifier Registry (v1.4, CANONICAL)
> Linear document ID: `3cff66e7-5782-40c6-b373-f28b38215243`
> Related issue: [BUS-16](https://linear.app/bussiness-content-os/issue/BUS-16/universal-identifier-registry)

> Content OS — Universal Identifier Registration Record (v1.6, CANONICAL)
> Linear document ID: `2e441d54-3ad5-4d52-810a-695a11d6dc43`
> Related issue: [BUS-17](https://linear.app/bussiness-content-os/issue/BUS-17/universal-identifier-registration-record)

This directory does not restate either document's narrative content (purpose, scope, namespace rationale, registration process, allocation boundary, open questions). It provides only:

- `registry.json` — a machine-readable mirror of the BUS-16 document's §4 "Current Registered Objects" table and its declared next-available sequence.
- `validate_registry.py` — a dependency-free validator that mechanically checks `registry.json` for internal consistency (identifier format, uniqueness, sequencing, required fields, and the declared boundary that only `Content OS Document` is an established object class).
- `registration_record.json` — a machine-readable mirror of the BUS-17 document's §3 "Allocation Acts" and its §4 "Canonical Closure" summary.
- `validate_registration_record.py` — a dependency-free validator that mechanically checks `registration_record.json` for internal consistency and cross-validates it against `registry.json`: every allocation act must reference an identifier that exists in the Registry, every Registry allocation must have a corresponding allocation act (no allocation without evidence), and the target document, issue, and lifecycle state recorded in each must not contradict the Registry.

Whenever a canonical Linear document is amended (a new `DIUA-DIC-*` allocation, a lifecycle-state change, a new allocation act), the corresponding JSON file must be updated to match, and its validator re-run. If a file and its canonical Linear document ever disagree, **the Linear document governs** — these are materializations, not a second source of truth. Between the two files themselves, `registry.json` (BUS-16) is authoritative for current state; `registration_record.json` (BUS-17) supplies evidence only and must never override it.

## Scope Boundary

- This registry governs only the `DIUA-DIC-*` scheme.
- The legacy `DOC-*` scheme (`DOC-SYS-001`) is governed by the separate, closed-to-new-allocations sibling registry BUS-23 and is **not** represented here.
- The UNIR-CORE-001 / UNIR-REGISTRY-001 / UNIR-REGISTRATION-RECORD-001 material archived under `99_Archive/` is **reference/illustrative material only**. Its example `DIUA-DIC-000001`–`DIUA-DIC-000005` allocations belong to that external reference material's own illustrative subjects — they are not Content OS allocations and must never be merged into `registry.json`. Content OS's own numbering starts fresh at `DIUA-DIC-000001` per the canonical document's explicit instruction.

## Running Validation

```bash
python3 validate_registry.py
python3 validate_registration_record.py
```

Run both after any edit to either JSON file — `validate_registration_record.py` reads `registry.json` for its cross-validation. Each exits `0` and prints `OK` on success; exits non-zero and prints every failure found otherwise.

## Navigation

### Parent

- [`../README.md`](../README.md) — 10_Registries orientation and authority boundary.

## Maintenance Rules

- Update `registry.json` only to reflect an allocation already recorded in the canonical BUS-16 Linear document — never allocate a new identifier from this repository directly (allocation is a Linear-side act per that document's §5 Registration Process).
- Update `registration_record.json` only to reflect an allocation act already recorded in the canonical BUS-17 Linear document — never fabricate, guess, or backfill allocation-act evidence.
- Run `validate_registry.py` after every edit to `registry.json`, and `validate_registration_record.py` after every edit to either JSON file.
- Do not add object classes, lifecycle states, or fields beyond what the canonical documents have actually established.
- Do not let `registration_record.json` become a second registry: it must not be treated as authoritative for current allocation state, and it must not introduce an identifier that does not already exist in `registry.json`.
- Do not create duplicate substantive authority in this README.
