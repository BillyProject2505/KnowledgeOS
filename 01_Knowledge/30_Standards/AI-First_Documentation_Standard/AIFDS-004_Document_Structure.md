# AIFDS-004 — Document Structure

> **Identifier:** AIFDS-004
>
> **Title:** Document Structure
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

This specification defines the canonical internal structure of documents governed by the AI-First Documentation Standard (AIFDS).

Its purpose is to ensure that all AI-DOC documents are predictable, consistent, machine-readable, and human-readable.

---

# 2. Scope

This specification applies to all AI-DOC documents governed by AIFDS unless explicitly exempted.

Human Documentation (H-DOC) may adopt this structure where appropriate but is not required to do so.

---

# 3. Design Principles

The document structure shall:

- be consistent;
- be predictable;
- be modular;
- support AI parsing;
- support human navigation;
- minimise ambiguity.

---

# 4. Canonical Document Anatomy

## 4.1 Mandatory Sections

Every AI-DOC shall contain the following sections:

1. Metadata
2. Purpose
3. Scope
4. Rules
5. Change History

---

## 4.2 Optional Sections

The following sections should be included whenever applicable:

- Principles
- Rationale
- Examples
- Cross References

Additional sections may be introduced provided they comply with AIFDS.

---

# 5. Section Definitions

## Metadata

Metadata provides the canonical identity of the document.

Every AI-DOC shall define at minimum:

- Identifier
- Title
- Version
- Status
- Type

Additional metadata may be defined by other AIFDS specifications.

---

## Purpose

Defines why the document exists.

---

## Scope

Defines what the document governs and what it does not govern.

---

## Principles

Defines the guiding concepts governing the specification.

---

## Rules

Defines normative requirements.

Rules shall be explicit, testable where practical, and free from ambiguity.

---

## Rationale

Provides explanatory context supporting the rules.

Rationale is informative and shall not override normative requirements.

---

## Examples

Provides informative implementation examples.

Examples are non-normative unless explicitly stated otherwise.

---

## Cross References

Defines explicit relationships to other AIFDS specifications.

---

## Change History

Documents the revision history of the specification.

---

# 6. Section Ordering

Canonical sections shall appear in the order defined by this specification.

Additional sections may be inserted only if they preserve logical consistency.

---

# 7. Extensibility

Specifications may introduce additional sections provided that:

- mandatory sections remain present;
- canonical ordering is preserved where practical;
- compatibility with AIFDS is maintained.

---

# 8. Conformance

A document claiming compliance with AIFDS shall conform to the structural requirements defined in this specification.

---

# 9. Change History

| Version | Status | Description |
|----------|--------|-------------|
| 1.0 | Canonical | Initial Document Structure specification. |
