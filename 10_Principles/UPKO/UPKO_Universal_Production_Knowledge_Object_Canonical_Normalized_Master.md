# Universal Production Knowledge Object (UPKO)

## Canonical Normalized Master — Reconciled and Locked Baseline

> This file is the canonical normalized master for the UPKO reconstruction work. It contains the Phase 1 audit, Phase 2 CPB extraction, Phase 3 cross-project normalization, Phase 4 canonical inventory, Phase 5 specification work, and the current locked taxonomy, metadata, lifecycle, version, relationship, and representation decisions.

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

## Canonical Object Type

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

## Canonical Metadata Boundary

```text
UPKO
├── Identity
├── Classification.Domain
├── Object Type
├── Applicability Information
├── Canonical Location
├── Lifecycle / Status
├── Version
├── Relationships
├── Provenance / Traceability
└── Representation
```

## Reconciliation Rule

Legacy Phase 1–5 statements that previously marked Object Type taxonomy or Classification taxonomy as deferred are historical process states and are not current canonical metadata.

Current state:

- Classification.Domain = **CANONICAL / LOCKED**
- Object Type = **CANONICAL / LOCKED**
- Applicability Information = contextual information, not a Classification taxonomy value
- Relationship mechanism = structural metadata
- Final UPKO ID grammar = **CANONICAL / LOCKED**
- Lifecycle / Status vocabulary = **CANONICAL / LOCKED**
- Version grammar = **CANONICAL / LOCKED**
- Relationship vocabulary/schema = **CANONICAL / LOCKED**
- Canonical Representation Contract = **CANONICAL / LOCKED**, subject to future UDS reconciliation

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

## Canonical Metadata Normalization & Controlled Vocabulary Resolution

### 1. Identity

- `UPKO ID` identifies the canonical knowledge object and is permanent, unique, and non-reusable.
- `UPKO Name` is the canonical concept name.
- Identity is independent of document, repository file, project, version, status, and representation format.

### 2. Classification Domain — Locked Vocabulary

```text
Foundation
Brand
Audience
Strategic
Content
Editorial
Visual
```

Each UPKO has one primary `Classification.Domain`.

### 3. Object Type — Locked Vocabulary

```text
Philosophy
Principle
Model
Classification
Objective
Standard
System
```

Object Type identifies the fundamental form of the knowledge object. It does not encode subject, applicability, project, location, lifecycle, or representation format.

### 4. Applicability Information

Applicability is contextual information and is not a Classification or Object Type vocabulary.

Example:

```text
Health & Educational Writing Standards
Domain        = Editorial
Object Type   = Standard
Applicability = Health / Educational
```

### 5. Canonical Location

Current canonical repository placement:

```text
10_Principles/UPKO/
```

Repository placement is distinct from Classification.Domain and Object Type.

### 6. Lifecycle / Status Vocabulary — Locked

```text
IDENTIFIED
DRAFT
CANDIDATE
VALIDATED
CANONICAL
SUPERSEDED
DEPRECATED
ARCHIVED
```

Lifecycle State is distinct from Version, Revision, PKR Registration Status, and Publication Status.

Canonical transition baseline:

```text
IDENTIFIED
    ↓
DRAFT
    ↓
CANDIDATE
    ↓
VALIDATED
    ↓
CANONICAL
   ├──────────────┐
   ↓              ↓
SUPERSEDED    DEPRECATED
   ↓              ↓
ARCHIVED      ARCHIVED
```

No lifecycle transition is implicit.

### 7. Version Grammar — Locked

Format:

```text
MAJOR.MINOR.PATCH
```

Grammar:

```text
^[0-9]+\.[0-9]+\.[0-9]+$
```

Semantics:

- `PATCH` = non-substantive correction, clarification, or representation/metadata correction that does not change canonical meaning.
- `MINOR` = additive or refining knowledge that remains backward-compatible.
- `MAJOR` = material change to canonical meaning or incompatible interpretation while retaining the same fundamental production concept.
- A fundamentally different production concept becomes a **new UPKO** with a supersession relationship rather than merely a major version.

Initial canonical baseline for the current 23-UPKO set:

```text
1.0.0
```

### 8. Relationship Vocabulary & Schema — Locked

Canonical relationship types:

```text
Dependency
Governance
Inheritance
Refinement
Constraint
Source
Supersession
Related Knowledge
```

Canonical relationship record:

```text
Relationship ID
Relationship Type
Source Object
Target Object
Direction
Scope / Applicability
Description
Source / Evidence
Effective State
```

Required fields:

```text
Relationship Type
Source Object
Target Object
```

Relationship is structural metadata and is not an Object Type.

Directional relationships must preserve semantic direction. Symmetric relationships may be represented without directional asymmetry where the relationship semantics permit it.

### 9. Canonical Representation Contract — Locked Baseline

The canonical UPKO representation baseline is a knowledge-object representation contract, not the Universal Document Standard itself.

Canonical field order:

```text
1. UPKO ID
2. UPKO Name
3. Object Type
4. Classification
5. Applicability
6. Canonical Location
7. Lifecycle State
8. Version
9. Canonical Purpose
10. Canonical Concept
11. Boundary
12. Canonical Knowledge
13. Relationships
14. Source / Traceability
15. Canonical Principle
16. Revision History
```

Current repository representation baseline:

```text
YAML Front Matter
        +
Markdown
```

Representation must not be confused with canonical knowledge identity. Future Universal Document Standard requirements may revise this representation contract through formal reconciliation.

### 10. Provenance / Traceability

Provenance points to authoritative source evidence and must remain distinguishable from copied source content.

Canonical knowledge objects must retain sufficient source/traceability references to support reconstruction, validation, and later governance review.

## Canonical Metadata Rules

1. Normalize only what has an established canonical semantic function.
2. Do not invent controlled vocabulary merely to complete a schema.
3. Controlled vocabulary values must use exact canonical forms.
4. Synonym proliferation is prohibited for canonical taxonomy values.
5. Object Type is determined by substantive/fundamental form, not keyword matching.
6. Applicability remains contextual unless explicitly canonicalized through a separate taxonomy decision.
7. Relationship semantics remain structurally separate from Object Type.
8. Identity remains separate from document and repository representation.
9. Lifecycle, Version, Revision, PKR Registration Status, and Publication Status remain separate dimensions.
10. Future taxonomy additions require controlled review and explicit canonical approval.

## Future Universal Standards Reconciliation

The current UPKO baseline is canonical and locked for the present architecture.

After completion of:

```text
Universal Production Bible (UPB)
        +
Universal Document Standard (UDS)
        ↓
UPKO Architecture Reconciliation
        ↓
Formal revision only if required
```

This is a planned future architectural reconciliation dependency, not an unresolved current specification.

## Canonical Status

**Classification.Domain — CANONICAL / LOCKED**  
**Object Type — CANONICAL / LOCKED**  
**Metadata Normalization & Controlled Vocabulary — CANONICAL / LOCKED**  
**UPKO ID Grammar — CANONICAL / LOCKED**  
**Lifecycle / Status Vocabulary — CANONICAL / LOCKED**  
**Version Grammar — CANONICAL / LOCKED**  
**Relationship Vocabulary & Schema — CANONICAL / LOCKED**  
**Canonical Representation Contract — CANONICAL / LOCKED BASELINE**  
**Coverage — 23/23 UPKOs**  
**Legacy Deferred Metadata Reconciliation — COMPLETE**

## Repository Placement

```text
10_Principles/UPKO/
```

## Lock Boundary

The current canonical baseline does not alter the substantive 23-UPKO inventory. It resolves the previously deferred metadata and controlled-vocabulary specifications while preserving a formal future reconciliation point with the Universal Production Bible and Universal Document Standard.
