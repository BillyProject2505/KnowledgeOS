# AIFDS-008 — Versioning

> **Identifier:** AIFDS-008
>
> **Title:** Versioning
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

This specification defines the canonical versioning model used by the AI-First Documentation Standard (AIFDS).

Its purpose is to ensure that documentation evolves in a predictable, traceable, and backward-aware manner.

---

# 2. Scope

This specification defines:

- Version Format
- Version Lifecycle
- Change Classification
- Status Values
- Compatibility Rules

---

# 3. Design Principles

Versioning shall be:

- predictable;
- explicit;
- traceable;
- repository-agnostic;
- implementation-independent.

---

# 4. Version Format

Every specification shall declare its version using the format:

**MAJOR.MINOR**

Examples:

- 1.0
- 1.1
- 2.0

Patch versions are not part of the canonical document version.

Editorial corrections that do not change normative meaning shall not require a version increment.

---

# 5. Change Classification

## Major Change

A change that modifies normative behaviour, interpretation, or compatibility.

Major Changes increment the MAJOR version.

Examples include:

- Removing normative requirements
- Changing mandatory behaviour
- Breaking backward compatibility

---

## Minor Change

A change that preserves compatibility while extending or clarifying the specification.

Minor Changes increment the MINOR version.

Examples include:

- Clarifying wording
- Adding informative examples
- Introducing backward-compatible requirements

---

# 6. Status Values

Every specification shall declare one canonical status.

Allowed status values are:

- Draft
- Review
- Approved
- Canonical
- Deprecated
- Superseded
- Archived

Status values are mutually exclusive.

---

# 7. Compatibility

Backward compatibility should be preserved whenever practical.

Breaking compatibility shall require a Major version increment.

Superseded specifications shall explicitly identify their replacement.

---

# 8. Change History

Every specification shall maintain a Change History.

Each entry shall include:

- Version
- Status
- Summary of Changes

---

# 9. Conformance

A document claiming compliance with AIFDS shall:

- declare its version;
- declare its status;
- maintain a Change History;
- comply with this specification.

---

# 10. Relationship to Other Specifications

This specification builds upon:

- AIFDS-000 — Specification Taxonomy
- AIFDS-003 — Information Model
- AIFDS-007 — Cross References

---

# 11. Change History

| Version | Status | Description |
|----------|--------|-------------|
| 1.0 | Canonical | Initial Versioning specification. |
