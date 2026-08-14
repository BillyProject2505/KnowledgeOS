# 20_Blueprints

## Purpose

Stores Architecture Blueprints produced during the Architecture Development Lifecycle (ADL) of KnowledgeOS.

---

## Scope

Blueprints transform validated discoveries into structured architectural proposals before formal review, freeze, and promotion to a Canonical Specification.

Blueprints are **non-canonical development artifacts**. They do not independently establish architectural authority.

---

## Canonical Function

The `20_Blueprints` layer provides the controlled intermediate stage between Discovery and Architecture Review.

```text
10_Discovery
    ↓
20_Blueprints
    ↓
30_Reviews
    ↓
Architecture Freeze
    ↓
50_Specifications
```

---

## Rules

- Blueprints shall be derived from validated discovery work and preserve traceability to their sources.
- Blueprints may change during development and review.
- A Blueprint does not become authoritative merely because it is stored in this directory.
- Approved architecture shall be promoted through the applicable lifecycle before becoming a Canonical Specification.
- Blueprint changes shall preserve sufficient history and traceability for architectural review.
- A Blueprint shall not silently replace or override an existing canonical Architecture artifact.

---

## Relationship to Other Development Layers

- `../10_Discovery` — source exploration and conceptual analysis.
- `../30_Reviews` — validation, review comments, and architectural decisions.
- `../../50_Specifications` — destination for formally promoted Canonical Specifications.

---

## Navigation

### Parent

`../`

### Related System Layers

- `../../10_Architecture`
- `../../20_Governance`
- `../../30_Standard`
- `../../40_Registries`
- `../../50_Specifications`
- `../../60_Releases`
- `../../80_Planning`

### Related Knowledge Layer

- `../../../01_Knowledge`

---

## Canonical Boundary Principle

`70_Development/20_Blueprints` is a controlled working layer. It supports architecture development but does not itself own canonical architectural authority.
