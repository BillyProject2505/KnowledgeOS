# UPKO Object Type Taxonomy — Canonical v1.0

## Status

**CANONICAL — LOCKED**

## Canonical Taxonomy

```text
Object Type
├── Philosophy
├── Principle
├── Model
├── Classification
├── Objective
├── Standard
└── System
```

## Canonical Definition

Object Type identifies the **fundamental form of the knowledge object**.

Object Type is distinct from:

- Classification Domain
- Applicability Information
- Canonical Location
- Status
- Version

## Canonical Rules

1. Every UPKO receives one primary Object Type.
2. Object Type is determined by the substantive/fundamental form of the knowledge object, not by keyword matching in its name.
3. Object Type does not encode Domain.
4. Object Type does not encode applicability or project context.
5. `Model` is not a fallback type.
6. `Relationship` is not an Object Type.
7. `Identity`, `Positioning`, `Voice`, `Tone`, and `Alignment` remain conceptual distinctions, not Object Types.
8. Any future Object Type addition requires controlled taxonomy review and explicit canonical approval.

## Object Type Definitions

### Philosophy
Knowledge establishing fundamental production orientation or production-knowledge consumption philosophy.

Current UPKOs:
- Production Philosophy
- AI-First Production Knowledge

### Principle
Knowledge establishing guiding principles for production decisions.

Current UPKO:
- Brand Principles

### Model
Canonical reusable representation of a conceptual knowledge structure that can guide or inform downstream production.

Current UPKOs:
- Brand Identity
- Brand Positioning
- Audience Model
- Strategic Alignment
- Editorial Voice
- Editorial Tone

### Classification
Knowledge defining or organizing categorical/taxonomic distinctions within a production knowledge area.

Current UPKOs:
- Audience Classification
- Content Type

### Objective
Knowledge defining an intended production or strategic outcome.

Current UPKO:
- Strategic Objective

### Standard
Knowledge establishing explicit production requirements, rules, or constraints.

Current UPKOs:
- Writing Standards
- Inclusive Language Standards
- Call-to-Action Standards
- Health & Educational Writing Standards

### System
Knowledge organizing a coherent production subsystem with its own components, rules, and relationships.

Current UPKOs:
- Canvas System
- Layout System
- Surface System
- Typography System
- Color System
- Graphic Elements System
- Imagery System

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

## Distribution

```text
Philosophy      = 2
Principle       = 1
Model           = 6
Classification  = 2
Objective       = 1
Standard        = 4
System          = 7
Total           = 23
```

## Orthogonality

```text
Classification.Domain
    ↓
Where the knowledge belongs

Object Type
    ↓
What fundamental kind of knowledge object it is
```

The two dimensions are orthogonal and must not be collapsed.

## Lock Boundary

This lock establishes the Object Type taxonomy only.

It does not alter:

- Classification Domain taxonomy;
- Applicability Information;
- Canonical Location;
- Lifecycle/Status;
- Version;
- Traceability;
- PKR mapping.

## Governance

Future changes require:

```text
New / disputed UPKO
    ↓
Object Type Fit Test
    ↓
Existing type sufficient?
    ├── YES → use existing type
    └── NO  → Object Type Taxonomy Review
                  ↓
              Revision Proposal
                  ↓
              Explicit Canonical Approval
```

**Status: CANONICAL — LOCKED**
