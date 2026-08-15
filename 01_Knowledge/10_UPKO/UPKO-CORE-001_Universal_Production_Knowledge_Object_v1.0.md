# Universal Production Knowledge Object (UPKO)

## Canonical Normalized Master

This document is the canonical normalized master for the UPKO inventory and related normalization decisions.

It records the canonical production-knowledge inventory, normalized mappings, repository placement, and lock boundaries used by the UPKO system.

---

## Normative Taxonomy Authority

The canonical Object Type taxonomy is governed separately by:

```text
UPKO_Object_Type_Taxonomy_Canonical_v1.0.md
```

This master does **not** redefine or independently govern the Object Type taxonomy.

The taxonomy authority defines:

- Object Type values;
- Object Type definitions;
- Object Type assignment rules;
- Object Type governance and future-extension rules.

This document consumes that taxonomy for the normalized UPKO inventory.

---

## Canonical Classification Domain

```text
Classification
└── Domain
    ├── Foundation
    ├── Brand
    ├── Audience
    ├── Strategic
    ├── Content
    ├── Editorial
    └── Visual
```

Classification Domain identifies the production-knowledge area to which a UPKO belongs.

Classification Domain and Object Type are orthogonal dimensions and shall not be collapsed.

---

## Canonical 23-UPKO Mapping

| # | UPKO | Domain | Object Type |
|---:|---|---|---|
| 01 | Production Philosophy | Foundation | Philosophy |
| 02 | AI-First Production Knowledge | Foundation | Philosophy |
| 03 | Brand Identity | Brand | Model |
| 04 | Brand Positioning | Brand | Model |
| 05 | Brand Principles | Brand | Principle |
| 06 | Audience Model | Audience | Model |
| 07 | Audience Classification | Audience | Classification |
| 08 | Strategic Objective | Strategic | Objective |
| 09 | Strategic Alignment | Strategic | Model |
| 10 | Content Type | Content | Classification |
| 11 | Editorial Voice | Editorial | Model |
| 12 | Editorial Tone | Editorial | Model |
| 13 | Writing Standards | Editorial | Standard |
| 14 | Inclusive Language Standards | Editorial | Standard |
| 15 | Call-to-Action Standards | Editorial | Standard |
| 16 | Health & Educational Writing Standards | Editorial | Standard |
| 17 | Canvas System | Visual | System |
| 18 | Layout System | Visual | System |
| 19 | Surface System | Visual | System |
| 20 | Typography System | Visual | System |
| 21 | Color System | Visual | System |
| 22 | Graphic Elements System | Visual | System |
| 23 | Imagery System | Visual | System |

---

## Normalization Rules

- Domain identifies the production-knowledge area.
- Object Type is assigned according to the normative UPKO Object Type Taxonomy.
- Applicability Information is not converted into Classification values.
- `Foundation` is a sibling Domain value, not a parent of the other Domains.
- Identity, Positioning, Voice, Tone, and Alignment remain conceptual distinctions within the normalized inventory and are not treated as Object Types.
- Future taxonomy additions are governed by the separate Object Type Taxonomy authority.

---

## Canonical Status

**Classification.Domain — CANONICAL / LOCKED**

**Coverage — 23/23 UPKOs**

**Object Type assignments — conformant to the canonical UPKO Object Type Taxonomy**

---

## Repository Placement

Canonical repository placement:

```text
01_Knowledge/10_UPKO/
```

---

## Lock Boundary

This master establishes the normalized UPKO inventory and its recorded mappings.

It does not independently alter or redefine:

- Object Type taxonomy;
- Object Type definitions;
- Object Type governance;
- Applicability Information;
- Canonical Location;
- Lifecycle/Status;
- Version;
- Traceability;
- PKR mapping.

Changes to Object Type semantics shall be made in the canonical taxonomy authority and then reflected here through controlled normalization and re-audit.
