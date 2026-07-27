# AIFDS-010 — Registry Model

> **Identifier:** AIFDS-010
>
> **Title:** Registry Model
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

This specification defines the canonical registry model of the AI-First Documentation Standard (AIFDS).

Its purpose is to establish a consistent mechanism for registering, identifying, discovering, and maintaining documentation objects.

---

# 2. Scope

This specification defines:

- Registry Model
- Registry Principles
- Registry Entry Model
- Registry Integrity
- Registry Relationships

This specification does not define the contents of individual registries.

---

# 3. Design Principles

Registries shall be:

- canonical;
- repository-agnostic;
- implementation-independent;
- machine-readable;
- human-readable;
- extensible.

---

# 4. Registry Model

A registry is a canonical collection of logical documentation objects.

The Registry Model defines how registries are structured.

Individual registries shall be defined independently.

---

# 5. Registry Objects

The Registry Model supports registration of objects including:

- Specifications
- Standards
- Frameworks
- Principles
- Templates
- Registries
- Decisions
- References

Additional object categories may be introduced by future specifications.

---

# 6. Registry Entry Model

Every registry entry shall define at minimum:

- Canonical Identifier
- Object Type
- Title
- Version
- Status

Additional metadata may be introduced by specialised registry specifications.

---

# 7. Registry Integrity

Every registered object shall:

- possess one unique canonical identifier;
- belong to one primary object type;
- remain traceable throughout its lifecycle.

Registry entries shall not be silently removed.

Deprecated and superseded entries shall remain registered.

---

# 8. Registry Relationships

Registry entries may define relationships using the canonical cross-reference model defined by AIFDS-007.

Relationship semantics shall remain explicit.

---

# 9. Registry Instances

Concrete registries are independent specifications implementing this Registry Model.

Examples include:

- Specification Registry
- Template Registry
- Decision Registry
- Principle Registry
- Framework Registry
- Standard Registry
- Reference Registry

Additional registry instances may be created without modifying this specification.

---

# 10. Conformance

Registries claiming compliance with AIFDS shall comply with this specification.

---

# 11. Relationship to Other Specifications

This specification builds upon:

- AIFDS-003 — Information Model
- AIFDS-007 — Cross References
- AIFDS-008 — Versioning
- AIFDS-009 — Governance

---

# 12. Change History

| Version | Status | Description |
|----------|--------|-------------|
| 1.0 | Canonical | Initial Registry Model specification. |
