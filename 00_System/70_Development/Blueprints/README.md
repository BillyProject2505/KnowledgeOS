# 70_Development — Blueprints

## Purpose

Stores Architecture Blueprints produced during the Architecture Development Lifecycle (ADL) of KnowledgeOS.

---

## Scope

Blueprints transform validated discoveries into structured architectural proposals before formal review, freeze, and promotion to a Canonical Specification.

Blueprints are **non-canonical development artifacts**. They do not independently establish architectural authority.

---

## Canonical Function

The Blueprints layer provides the controlled intermediate stage between Discovery and Architecture Review.

```text
Discovery
    ↓
Blueprint
    ↓
Review
    ↓
Architecture Freeze
    ↓
Canonical Specification
```

---

## Rules

- Blueprints shall be derived from validated discovery work and preserve traceability to their sources.
- Blueprints may change during development and review.
- A Blueprint does not become authoritative merely because it is stored in this directory.
- Approved architecture shall be promoted through the applicable lifecycle before becoming a Canonical Specification.
- Blueprint changes shall preserve sufficient history and traceability for architectural review.

---

## Relationship to Other Development Layers

- `../Discovery` — source exploration and conceptual analysis.
- `../Reviews` — validation, review comments, and architectural decisions.
- `../../50_Specifications` — destination for formally promoted Canonical Specifications.

---

## Navigation

### Parent

`../`

### Related

- `../Discovery`
- `../Reviews`
- `../../10_Architecture`
- `../../20_Governance`
- `../../50_Specifications`

---

## Canonical Boundary Principle

`70_Development/Blueprints` is a controlled working layer. It supports architecture development but does not itself own canonical architectural authority.
