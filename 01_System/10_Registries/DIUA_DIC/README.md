# DIUA_DIC — Content OS Universal Identifier Registry

## Purpose

This directory is the repository-side materialization of **BUS-16 — Universal Identifier Registry**: Content OS's own instance of a Universal Naming & Identification Registry, governing the `DIUA-DIC-<6DigitSequence>` namespace.

## Canonical Source

**The canonical authority for this registry is the Linear document, not this directory:**

> Content OS — Universal Identifier Registry (v1.4, CANONICAL)
> Linear document ID: `3cff66e7-5782-40c6-b373-f28b38215243`
> Related issue: [BUS-16](https://linear.app/bussiness-content-os/issue/BUS-16/universal-identifier-registry)

This directory does not restate that document's narrative content (purpose, scope, namespace rationale, registration process, open questions). It provides only:

- `registry.json` — a machine-readable mirror of the canonical document's §4 "Current Registered Objects" table and its declared next-available sequence.
- `validate_registry.py` — a dependency-free validator that mechanically checks `registry.json` for internal consistency: identifier format (derived from the registry's own declared `namespace`/`marker`, so the grammar and the format check can't silently drift apart), uniqueness, sequencing, required fields, and the declared boundary that only `Content OS Document` is an established object class (fails closed if that list is ever left empty).

Whenever the canonical Linear document is amended (a new `DIUA-DIC-*` allocation, a lifecycle-state change), `registry.json` must be updated to match, and `validate_registry.py` re-run. If this file and the Linear document ever disagree, **the Linear document governs** — this is a materialization, not a second source of truth.

## Scope Boundary

- This registry governs only the `DIUA-DIC-*` scheme.
- The legacy `DOC-*` scheme (`DOC-SYS-001`) is governed by the separate, closed-to-new-allocations sibling registry BUS-23 and is **not** represented here.
- The UNIR-CORE-001 / UNIR-REGISTRY-001 / UNIR-REGISTRATION-RECORD-001 material archived under `99_Archive/` is **reference/illustrative material only**. Its example `DIUA-DIC-000001`–`DIUA-DIC-000005` allocations belong to that external reference material's own illustrative subjects — they are not Content OS allocations and must never be merged into `registry.json`. Content OS's own numbering starts fresh at `DIUA-DIC-000001` per the canonical document's explicit instruction.

## Running Validation

```bash
python3 validate_registry.py
```

Exits `0` and prints `OK` on success; exits non-zero and prints every failure found otherwise.

## Navigation

### Parent

- [`../README.md`](../README.md) — 10_Registries orientation and authority boundary.

## Maintenance Rules

- Update `registry.json` only to reflect an allocation already recorded in the canonical Linear document — never allocate a new identifier from this repository directly (allocation is a Linear-side act per the canonical document's §5 Registration Process).
- Run `validate_registry.py` after every edit to `registry.json`.
- Do not add object classes, lifecycle states, or fields beyond what the canonical document has actually established.
- Do not create duplicate substantive authority in this README.
