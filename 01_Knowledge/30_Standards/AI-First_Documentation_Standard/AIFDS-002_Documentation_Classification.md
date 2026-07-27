# AIFDS-002 — Documentation Classification

> **Identifier:** AIFDS-002
>
> **Title:** Documentation Classification
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

This specification defines the canonical documentation classification model used by the AI-First Documentation Standard (AIFDS).

Documentation Classification establishes how documentation shall be categorized according to its primary purpose and intended audience.

---

# 2. Scope

This specification defines:

- Documentation Classes
- Classification Principles
- Canonical Rules
- Selection Rules
- Writing Characteristics

This specification does not define document structure, writing rules, or document templates.

---

# 3. Canonical Principle

Documentation shall be classified according to its primary purpose rather than its implementation technology.

Classification shall never be determined by:

- file format;
- programming language;
- storage location;
- repository structure;
- software platform.

---

# 4. Documentation Classes

AIFDS defines two canonical documentation classes.

---

## 4.1 AI Documentation (AI-DOC)

### Purpose

Optimized for AI consumption.

### Primary Audience

- Large Language Models (LLMs)
- AI Agents
- Retrieval-Augmented Generation (RAG)
- Knowledge Graphs
- Automation Systems
- Future AI Systems

### Optimization Targets

- AI Readability
- AI Parsing
- AI Retrieval
- AI Maintainability
- Git Diff Friendliness
- Explicit Relationships

### Typical Documents

- Production Bible
- Standard
- Specification
- Framework
- Registry
- Architecture
- Governance
- Policy
- Decision Record
- Technical Reference

### Writing Characteristics

- Flat structure
- One Concept per Section
- One Responsibility per Section
- Explicit identifiers
- Normative language
- Minimal prose
- Machine-friendly Markdown

---

## 4.2 Human Documentation (H-DOC)

### Purpose

Optimized for human consumption.

### Primary Audience

- Contributors
- Designers
- Writers
- Editors
- Trainers
- Public Readers

### Optimization Targets

- Readability
- Learning
- Onboarding
- Narrative
- Examples
- Tutorials

### Typical Documents

- README
- Tutorial
- User Guide
- Quick Start
- FAQ
- Manual
- Walkthrough
- Public Documentation

### Writing Characteristics

- Narrative explanation
- Context-rich
- Learning-oriented
- Rich examples
- Illustrations
- Human-first organization

---

# 5. Canonical Rules

The documentation class shall be determined by the document's primary purpose.

Examples:

- Markdown may be AI-DOC or H-DOC.
- YAML may be AI-DOC.
- JSON may be AI-DOC.
- HTML may be H-DOC.

File format shall not determine documentation class.

---

# 6. Selection Rules

The documentation class shall be selected before authoring begins.

Each document shall have one primary documentation class.

When a document serves both AI and human audiences, its primary optimization target shall determine its classification.

---

# 7. Relationship to Other Specifications

This specification defines only documentation classification.

Related specifications include:

- AIFDS-001 — Foundation
- AIFDS-003 — Information Model
- AIFDS-004 — Document Structure
- AIFDS-005 — Writing Rules
- AIFDS-006 — Document Templates

---

# 8. Conformance

A document claiming compliance with AIFDS shall:

- declare its primary documentation class;
- comply with the rules of that class;
- avoid conflicting optimization objectives.

---

# 9. Change History

| Version | Status | Description |
|----------|--------|-------------|
| 1.0 | Canonical | Initial Documentation Classification specification. |
