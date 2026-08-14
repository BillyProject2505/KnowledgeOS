# 70_Development

## Purpose

Provides the controlled non-canonical workspace for developing architectural artifacts before they are promoted into canonical system artifacts.

---

## Scope

`70_Development` contains exploratory and iterative architecture-development artifacts governed by the applicable Architecture Development Lifecycle (ADL).

Artifacts in this workspace do not independently establish canonical architectural authority.

---

## Current Structure

```text
70_Development/
└── 20_Blueprints/
```

### `20_Blueprints`

Contains Architecture Blueprints that transform validated discovery work into structured architectural proposals before formal review, freeze, and promotion to `50_Specifications`.

Additional development stages may be materialized as numbered child directories when their canonical workspace structure and artifacts are established.

---

## Artifact Lifecycle

```text
Discovery
    ↓
20_Blueprints
    ↓
Review
    ↓
Architecture Freeze
    ↓
50_Specifications
```

Discovery and Review are lifecycle stages; their dedicated repository directories are not currently materialized under `70_Development`.

---

## Rules

- Development artifacts are non-canonical unless formally promoted through the applicable lifecycle.
- Development work shall preserve traceability to its source, decisions, and resulting canonical artifact.
- A development artifact shall not silently replace or override an existing canonical artifact.
- Folder numbering shall reflect established lifecycle order and shall not be used to imply the existence of an unmaterialized stage.
- Canonical artifacts belong in their applicable system layer after formal approval and promotion.

---

## Relationship to Other System Layers

- `../10_Architecture` — canonical architectural authority.
- `../20_Governance` — governance and change-control mechanisms.
- `../50_Specifications` — destination for formally promoted canonical specifications.
- `../60_Releases` — publication and release traceability.
- `../80_Planning` — implementation planning.

---

## Navigation

### Parent

`../`

### Child

- `20_Blueprints`

### Related

- `../10_Architecture`
- `../20_Governance`
- `../50_Specifications`
- `../60_Releases`
- `../80_Planning`
- `../../01_Knowledge`

---

## Canonical Boundary Principle

`70_Development` is a controlled working layer. It supports system development but does not itself own canonical architectural, governance, standards, registry, specification, or release authority.
