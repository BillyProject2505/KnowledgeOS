# Knowledge Object Registry

## Purpose

The Knowledge Object Registry (KOR) is the authoritative registry of all Knowledge Objects (KOs) within the Knowledge Operating System (KOS).

A Knowledge Object represents the smallest independently identifiable unit of knowledge managed by the repository.

The registry provides a unique identifier for every Knowledge Object and serves as the primary reference for discovery, indexing, and relationship mapping.

---

## Scope

This registry includes:

- Specifications
- Sections
- Parts
- Standards
- Policies
- Templates
- Reference Objects
- Any future Knowledge Object types

---

## Identifier Format

```
KO-000001
KO-000002
KO-000003
```

Identifiers are permanent.

Once assigned, an identifier must never be reused.

---

## Registry Fields

| Field | Description |
|---------|-------------|
| KO ID | Unique Knowledge Object Identifier |
| Name | Official object name |
| Type | Object classification |
| Parent | Parent object (if applicable) |
| Status | Draft / Review / Canonical / Deprecated |
| Current Version | Latest approved version |

---

## Rules

- Every Knowledge Object must have exactly one KO ID.
- KO IDs are immutable.
- Objects may change status but never identity.
- Deprecated objects remain in the registry.

---

## Example

| KO ID | Name | Type | Status |
|--------|------|------|--------|
| KO-000001 | KOS-AS | Specification | Canonical |
| KO-000002 | PRS | Specification | Canonical |
| KO-000003 | IP | Specification | Draft |
