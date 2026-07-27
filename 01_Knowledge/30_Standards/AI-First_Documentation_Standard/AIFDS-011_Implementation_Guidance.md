# AIFDS-011 — Implementation Guidance

> **Identifier:** AIFDS-011
>
> **Title:** Implementation Guidance
>
> **Version:** 1.0
>
> **Status:** Canonical (LOCK)
>
> **Type:** Supporting Specification
>
> **Parent Standard:** AI-First Documentation Standard (AIFDS)

---

# 1. Purpose

This specification defines the canonical implementation guidance framework for the AI-First Documentation Standard (AIFDS).

Its purpose is to support consistent implementation across repositories, platforms, and documentation systems while preserving the repository-agnostic architecture of AIFDS.

---

# 2. Scope

This specification defines:

- Implementation Principles
- Repository Organization Guidance
- Naming Guidance
- Migration Guidance
- Tool Integration Guidance
- Platform Guide Framework

This specification does not define platform-specific implementation details.

---

# 3. Design Principles

Implementations shall preserve:

- Canonical Identifiers
- Logical Relationships
- Information Integrity
- Repository Independence
- Platform Independence

Implementation choices shall not modify the logical architecture defined by AIFDS.

---

# 4. Implementation Framework

This specification defines the general implementation framework.

Platform-specific implementation guidance shall be defined in independent implementation guides.

---

# 5. Repository Organization Guidance

Repositories should organize documentation in a maintainable manner.

Folder hierarchy is implementation-specific.

Logical relationships shall not depend upon physical folder structures.

---

# 6. Naming Guidance

File names should:

- align with canonical identifiers;
- remain stable where practical;
- be descriptive.

Renaming files shall not change canonical identifiers.

---

# 7. Migration Guidance

Migration processes should preserve:

- Canonical Identifiers
- Cross References
- Version History
- Governance Records

Migration should minimize disruption to documentation consumers.

---

# 8. Tool Integration Guidance

Implementations may integrate with:

- Version Control Systems
- Documentation Generators
- Search Systems
- AI Assistants
- Knowledge Management Platforms

Tool integrations shall preserve the logical architecture defined by AIFDS.

---

# 9. Platform Guides

Platform-specific guidance shall be published as independent implementation guides.

Examples include:

- GitHub Implementation Guide
- GitLab Implementation Guide
- Obsidian Implementation Guide
- Local Filesystem Implementation Guide

Additional implementation guides may be created without modifying this specification.

---

# 10. Conformance

Implementations claiming alignment with AIFDS shall preserve the intent of all normative specifications.

Implementation-specific adaptations shall not alter canonical identifiers, logical relationships, or governance semantics.

---

# 11. Relationship to Other Specifications

This specification complements:

- AIFDS-004 — Document Structure
- AIFDS-006 — Document Templates
- AIFDS-009 — Governance
- AIFDS-010 — Registry Model

---

# 12. Change History

| Version | Status | Description |
|----------|--------|-------------|
| 1.0 | Canonical | Initial Implementation Guidance framework specification. |
