# Version Registry

## Purpose

The Version Registry records the lifecycle of every official document and Knowledge Object.

It provides a complete audit trail of version history.

---

## Scope

Tracks:

- Initial releases
- Minor revisions
- Major revisions
- Deprecation

---

## Version Format

```
v1.0
v1.1
v2.0
```

---

## Registry Fields

| Field | Description |
|---------|-------------|
| Object | Referenced object |
| Version | Version number |
| Date | Release date |
| Status | Active / Superseded |
| Notes | Summary of changes |

---

## Rules

- Versions are chronological.
- Previous versions are never deleted.
- Every canonical release must be recorded.

---

## Example

| Object | Version | Status |
|----------|----------|---------|
| KOS-AS | v1.0 | Active |
| PRS | v1.0 | Active |
| IP | v0.1 | Draft |
