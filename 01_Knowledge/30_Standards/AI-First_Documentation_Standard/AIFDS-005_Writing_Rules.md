# AIFDS-005 — Writing Rules

> **Identifier:** AIFDS-005
>
> **Title:** Writing Rules
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

This specification defines the canonical writing rules used by the AI-First Documentation Standard (AIFDS).

Its purpose is to ensure that documentation is consistent, explicit, machine-readable, human-readable, and maintainable.

---

# 2. Scope

This specification governs:

- Language
- Semantics
- Structure
- Formatting

These rules apply to all AI-DOC unless explicitly exempted by another AIFDS specification.

---

# 3. Design Principles

Writing governed by AIFDS shall be:

- Clear
- Explicit
- Consistent
- Concise
- Testable
- Machine-readable
- Human-readable

---

# 4. Writing Layers

AIFDS organizes writing rules into four canonical layers.

## 4.1 Language Rules

Defines language usage.

Includes:

- Primary Language
- Terminology
- Consistency
- Vocabulary

---

## 4.2 Semantic Rules

Defines meaning.

Includes:

- Normative Language
- Definitions
- Canonical Terms
- Requirement Statements

---

## 4.3 Structural Rules

Defines information organization.

Includes:

- Headings
- Sections
- Lists
- Tables
- Examples

---

## 4.4 Formatting Rules

Defines presentation.

Includes:

- Markdown
- Code Blocks
- Whitespace
- Line Breaks

---

# 5. Language Rules

## Primary Language

Each document shall use one primary language.

---

## Terminology

Canonical terminology shall originate from AIFDS-003.

A canonical term shall have one meaning.

---

## Consistency

The same concept shall always use the same canonical term.

Synonyms shall not be used within normative requirements.

---

# 6. Semantic Rules

Normative statements shall use standardized keywords.

| Keyword | Meaning |
|----------|---------|
| SHALL | Mandatory requirement |
| SHALL NOT | Prohibited |
| SHOULD | Strong recommendation |
| SHOULD NOT | Discouraged |
| MAY | Optional |
| MUST | Reserved only for externally mandated requirements |

Normative requirements shall be explicit and testable where practical.

---

# 7. Structural Rules

## Headings

- Hierarchical.
- Sequential.
- One topic per heading.

---

## Sections

Each section shall address one primary responsibility.

---

## Lists

Lists shall contain logically related items.

---

## Tables

Tables should be used for structured information.

---

## Examples

Examples are informative unless explicitly stated otherwise.

---

# 8. Formatting Rules

## Markdown

AI-DOC shall use standard Markdown.

Platform-specific extensions should be avoided unless explicitly required.

---

## Code Blocks

Code blocks shall include language identifiers whenever applicable.

---

## Whitespace

Whitespace shall improve readability without changing document meaning.

---

# 9. Conformance

Documents claiming compliance with AIFDS shall conform to this specification.

---

# 10. Change History

| Version | Status | Description |
|----------|--------|-------------|
| 1.0 | Canonical | Initial Writing Rules specification. |
