# AIFDS-007 — Cross References

> **Identifier:** AIFDS-007
>
> **Title:** Cross References
>
> **Version:** 1.0
>
> **Status:** Canonical (LOCK)
>
> **Type:** Core Specification
>
> **Parent Standard:** AI-First Documentation Standard (AIFDS)

---

# 1. Purpose

This specification defines the canonical cross-reference model used by the AI-First Documentation Standard (AIFDS).

Its purpose is to establish explicit, stable, machine-readable relationships between documentation objects.

---

# 2. Scope

This specification defines:

- Reference Principles
- Reference Types
- Relationship Types
- Reference Integrity
- Conformance Requirements

It does not define physical hyperlinks, repository layouts, or implementation-specific linking mechanisms.

---

# 3. Design Principles

Cross references shall be:

- explicit;
- stable;
- repository-agnostic;
- implementation-independent;
- machine-readable;
- human-readable.

---

# 4. Canonical Principles

Cross references shall identify documentation objects using canonical identifiers.

References shall never depend on:

- file paths;
- folder structures;
- repository locations;
- platform-specific URLs.

---

# 5. Reference Types

## Normative Reference

Required for correct interpretation or implementation.

---

## Informative Reference

Provides additional context.

---

## Related Reference

Indicates conceptual association without dependency.

---

# 6. Relationship Types

Every relationship shall have an explicit semantic type.

The canonical relationship types are:

| Relationship | Meaning |
|--------------|---------|
| depends_on | Requires another specification |
| implements | Implements another specification |
| extends | Extends another specification |
| replaces | Replaces another specification |
| supersedes | Supersedes an earlier canonical specification |
| related_to | Conceptually related |
| references | General informative reference |

Additional relationship types may be introduced by future specifications.

---

# 7. Reference Requirements

Every reference shall define:

- target identifier;
- reference type;
- relationship type.

Optional attributes may include:

- section identifier;
- rationale;
- implementation notes.

---

# 8. Reference Integrity

Every referenced identifier shall exist.

Broken references shall be corrected before publication.

Deprecated references should identify replacement specifications where applicable.

---

# 9. Relationship Semantics

Relationships are logical connections between documentation objects.

Relationship direction shall be explicit.

Circular dependencies should be avoided unless intentionally required.

---

# 10. Conformance

A document claiming compliance with AIFDS shall:

- use canonical identifiers;
- define relationship types;
- preserve reference integrity.

---

# 11. Relationship to Other Specifications

This specification builds upon:

- AIFDS-003 — Information Model
- AIFDS-004 — Document Structure
- AIFDS-006 — Document Templates

---

# 12. Change History

| Version | Status | Description |
|----------|--------|-------------|
| 1.0 | Canonical | Initial Cross References specification with typed relationships. |
