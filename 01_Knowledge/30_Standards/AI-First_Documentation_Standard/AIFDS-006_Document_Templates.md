# AIFDS-006 — Document Templates

> **Identifier:** AIFDS-006
>
> **Title:** Document Templates
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

This specification defines the canonical template framework used by the AI-First Documentation Standard (AIFDS).

The framework establishes how document templates are defined, organized, selected, and maintained.

---

# 2. Scope

This specification defines:

- Template Framework
- Template Principles
- Template Inheritance
- Template Selection
- Template Conformance
- Template Specification Model

It does not define the contents of individual templates.

---

# 3. Design Principles

Templates shall be:

- reusable;
- modular;
- repository-agnostic;
- implementation-independent;
- AI-friendly;
- human-readable.

---

# 4. Template Framework

A template is a reusable blueprint for creating documents that conform to AIFDS.

Templates define document structure rather than document content.

Individual templates shall be defined as independent specifications.

---

# 5. Template Components

Templates may define:

- Metadata placeholders
- Mandatory sections
- Optional sections
- Recommended ordering
- Author guidance
- Example placeholders

Author guidance is informative and shall not become part of the resulting normative document.

---

# 6. Template Inheritance

Templates may inherit from more general templates.

Inheritance shall preserve compatibility with parent templates.

Specialized templates may introduce additional sections without violating inherited mandatory requirements.

---

# 7. Template Library

The canonical template library consists of independent template specifications.

Examples include:

- Constitutional Specification Template
- Core Specification Template
- Supporting Specification Template
- Registry Template
- Decision Record Template
- Reference Template

Additional templates may be introduced without modifying this specification.

---

# 8. Template Selection

Template selection shall be based on:

- document type;
- document purpose;
- specification taxonomy.

Template selection shall occur before document authoring begins.

---

# 9. Template Conformance

A document created from a template shall:

- preserve all mandatory template requirements;
- comply with AIFDS-004 (Document Structure);
- comply with AIFDS-005 (Writing Rules).

Placeholder guidance may be removed after authoring.

---

# 10. Relationship to Other Specifications

This specification builds upon:

- AIFDS-000 — Specification Taxonomy
- AIFDS-004 — Document Structure
- AIFDS-005 — Writing Rules

Individual templates are specified separately.

---

# 11. Change History

| Version | Status | Description |
|----------|--------|-------------|
| 1.0 | Canonical | Initial Document Templates framework specification. |
