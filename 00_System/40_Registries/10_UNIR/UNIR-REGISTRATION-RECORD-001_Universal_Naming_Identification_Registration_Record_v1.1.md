---
document_id: UNIR-REGISTRATION-RECORD-001
document_type: Registration Record Representation
title: Universal Naming & Identification Registration Record
version: "1.1"
status: LOCKED — CANONICAL
canonicality: CANONICAL
scope: Validated registration-record representations and traceability associated with current UNIR Registry Objects and concrete Document Identifier allocations
purpose: Canonical documentary representation and traceability layer for validated UNIR registration records and concrete Document Identifier allocations
parent_document: UNIR-REGISTRY-001 v1.1
source_basis: Validated registration readiness, decision, authorization, allocation, registration-event, reassessment, and concrete Document Identifier allocation evidence, including the pre-existing UNIR-REGISTRY-001 v1.0 traceability state, the explicit UNIR-ALLOCATION-ACT-001 reference declared by Universal Architecture for DIUA-DIC-000002 (not independently asserted as a verified separate allocation-act artifact), and the verified UNIR-ALLOCATION-ACT-003 for DIUA-DIC-000003 and UNIR-ALLOCATION-ACT-002 for DIUA-DIC-000004
semantic_authority: UNIS
registry_authority: UNIR Registry Authority
---

# Universal Naming & Identification Registration Record

**Document ID:** UNIR-REGISTRATION-RECORD-001  
**Document Type:** Registration Record Representation  
**Title:** Universal Naming & Identification Registration Record  
**Version:** 1.1  
**Status:** LOCKED — CANONICAL  
**Canonicality:** CANONICAL  
**Lock Status:** LOCKED  
**Document Role:** Canonical Registration Record Representation  
**Document Responsibility:** UNIR Registry Authority  
**Semantic Authority:** UNIS for Universal Naming & Identification semantics  
**Registry Authority:** UNIR Registry Authority for registry-record representation  
**Parent Document:** `UNIR-REGISTRY-001 v1.1`  
**Architectural Relationship:** Supporting record/traceability layer; does not replace current registry state  
**Supersedes:** `UNIR-REGISTRATION-RECORD-001 v1.0`  
**Superseded By:** None  
**Publication Status:** PUBLISHED  
**Publication Event:** Canonical repository publication  
**Publication Commit:** `a885e539c6981c1bffe13d23d68713f1c6a8d22c`  
**Publication Timestamp:** `2026-08-15T08:27:02Z`  
**Primary Form:** Markdown  
**Machine-Readable Metadata:** YES  
**Canonical Repository Path:** `00_System/40_Registries/10_UNIR/UNIR-REGISTRATION-RECORD-001_Universal_Naming_Identification_Registration_Record_v1.1.md`

---

## Navigation

1. [Document Contract](#1-document-contract)
2. [Registration Record Model](#2-registration-record-model)
3. [Record Type Vocabulary](#3-record-type-vocabulary)
4. [Record State Model](#4-record-state-model)
5. [Current Registration Record Coverage](#5-current-registration-record-coverage)
6. [UKOI Registration Record Chain](#6-ukoi-registration-record-chain)
7. [Decision Identifier Grammar Chain](#7-decision-identifier-grammar-chain)
8. [Document Identifier Grammar Chain](#8-document-identifier-grammar-chain)
9. [DEC Registration Record Chain](#9-dec-registration-record-chain)
10. [DIC Registration Record Chain](#10-dic-registration-record-chain)
11. [Identifier Allocation Traceability](#11-identifier-allocation-traceability)
12. [Historical Registration Provenance](#12-historical-registration-provenance)
13. [Conditional Evidence Families](#13-conditional-evidence-families)
14. [Evidence & Authority Rules](#14-evidence--authority-rules)
15. [Completeness & Claim Boundary](#15-completeness--claim-boundary)
16. [Materialization Boundary](#16-materialization-boundary)
17. [Canonical Closure](#17-canonical-closure)

---

## 1. Document Contract

### 1.1 Purpose

This document provides a canonical documentary representation and traceability layer for validated UNIR registration records associated with current registered Registry Objects.

It preserves the independent authority of underlying registration, authorization, allocation, decision, reassessment, and related evidence artifacts.

### 1.2 Scope

In scope:

- validated registration readiness records;
- registration decision/outcome references;
- registration authorization records;
- Registry Object ID allocation records;
- registration events;
- applicable reassessment records;
- registration-related audit, review, and reconciliation references where individually validated;
- historical registration provenance;
- record relationships;
- evidence and provenance references;
- temporal traceability.

### 1.3 Non-Scope

This document does not:

- redefine the Six-Core semantics;
- replace or modify `UNIR-CORE-001 v1.3`;
- represent current registry state in place of `UNIR-REGISTRY-001`;
- redefine Registry Objects;
- create a separate DIUA Registry Object;
- replace authoritative underlying registration records;
- become a repository for full copies of operational records;
- define UDS semantics;
- define document construction or canonicalization methodology;
- act as a general publication or release registry.

### 1.4 Authority Boundary

UNIS remains the normative authority for Universal Naming & Identification semantics.

`UNIR-CORE-001` remains the canonical architectural boundary.

`UNIR-REGISTRY-001` represents current registry state.

Underlying registration, authorization, allocation, decision, reassessment, and related record artifacts remain authoritative for their own record content.

This document provides canonical representation and traceability only.

### 1.5 Source Basis

The materialized record chains in this document are limited to validated evidence established through the preceding D3-R1 through D3-R10 process and the current `UNIR-REGISTRY-001` traceability state.

Historical consolidated UNIR artifacts are not treated as the normative source for current registry state.

### 1.6 Interpretation Rule

This document shall be interpreted as a canonical representation and traceability layer for the registration records explicitly validated and represented herein.

It shall not be interpreted as:

- the current registry-state authority;
- a replacement for an underlying authoritative record artifact;
- an exhaustive archive of all UNIR registration, audit, reconciliation, or review records;
- a source for redefining UNIR Core semantics.

Where a record is marked `NOT ESTABLISHED`, the document records an evidence boundary rather than an assertion of non-existence.

---

## 2. Registration Record Model

A Registration Record Representation identifies and relates an authoritative record artifact without replacing it.

The representation model is:

```text
Registration Record Representation
│
├── Record ID
├── Record Type
├── Subject Reference
├── Related Registry Object
├── Record State
├── Event / Effective Time
├── Normative Source Reference
├── Authority Reference
├── Related Record References
├── Evidence Artifact Reference
└── Provenance
```

### 2.1 Identity Separation

The following identities remain distinct:

```text
Record ID
    ≠
Registry Object ID
    ≠
Represented Construct Identifier
    ≠
Concrete Document Identifier
    ≠
Registration Event
    ≠
Allocation Record
```

### 2.2 Representation Rule

A representation in this document shall not supersede, overwrite, or alter the authority of the underlying record artifact.

Where an underlying record is unavailable or not individually validated, the representation shall not invent its contents.

---

## 3. Record Type Vocabulary

### 3.1 Core Registration Record Types

```text
REGISTRATION_READINESS
REGISTRATION_DECISION
REGISTRATION_AUTHORIZATION
OBJECT_ID_ALLOCATION
REGISTRATION_EVENT
REASSESSMENT
```

### 3.2 Conditional Supporting Types

```text
AUDIT
RECONCILIATION
REVIEW
```

These types are represented only where an individual authoritative record has been validated for inclusion.

### 3.3 Historical Representation

```text
HISTORICAL_REGISTRATION
```

Historical records are provenance and shall not be interpreted as current registration state.

---

## 4. Record State Model

Record state is distinct from Registry Object state.

The representation vocabulary is:

```text
VALID
HISTORICAL
SUPERSEDED
CONDITIONAL
NOT ESTABLISHED
```

`NOT ESTABLISHED` means that the available evidence does not establish the existence or applicability of a record for this representation. It does not assert that the record never existed.

---

## 5. Current Registration Record Coverage

The current registry contains five validated Registry Objects:

| # | Registry Object | Registration-Record Coverage |
|---|---|---|
| 001 | UKOI | VALIDATED — FULL MINIMUM CHAIN |
| 002 | Decision Identifier Grammar | VALIDATED — FULL MINIMUM CHAIN |
| 003 | Document Identifier Grammar | VALIDATED — MINIMUM CHAIN |
| 004 | Decision Identifier Class — DEC | VALIDATED — FULL TEMPORAL CHAIN |
| 005 | Document Identifier Class — DIC | VALIDATED — MINIMUM CHAIN |

**Validated minimum registration-chain coverage: 5 / 5 current Registry Objects.**

This is not a claim of exhaustive historical or operational record coverage.

---

## 6. UKOI Registration Record Chain

**Registry Object ID:**

`urn:unir:ro:ffc0bb08-912b-4153-b334-62777563159f`

**Registered Construct:** UKOI — Knowledge Object Identification Space

### 6.1 Validated Chain

```text
UKOI
  ↓
UKOI-READINESS-001
  ↓
UKOI-REG-AUTH-001
  ↓
Registry Object ID Allocation
  ↓
UNIR-REG-EVT-68C1B2E3CF07
  ↓
REGISTERED
```

### 6.2 Applicable Reassessment

`UKOI-V1.7-REASSESSMENT-001`

### 6.3 Representation Status

```text
Registration readiness: VALIDATED
Authorization:          VALIDATED
Allocation:             VALIDATED
Registration event:     VALIDATED
Reassessment:           VALIDATED
```

Underlying records remain independently authoritative.

---

## 7. Decision Identifier Grammar Chain

**Registry Object ID:**

`urn:unir:ro:90b1e3bc-5383-4c79-a259-35cc281f6961`

**Registered Construct:** Decision Identifier Grammar — Universal Identifier Architecture

### 7.1 Validated Chain

```text
Decision Identifier Grammar
  ↓
Registration Readiness
  ↓
DEC-GRAMMAR-REG-AUTH-001
  ↓
Registry Object ID Allocation
  ↓
UNIR-REG-EVT-47CCF590E63F
  ↓
REGISTERED
```

### 7.2 Applicable Reassessment

`36-DECISION-IDENTIFIER-GRAMMAR-V1.7-REASSESSMENT-001`

### 7.3 Representation Status

```text
Registration readiness: VALIDATED
Authorization:          VALIDATED
Allocation:             VALIDATED
Registration event:     VALIDATED
Reassessment:           VALIDATED
```

---

## 8. Document Identifier Grammar Chain

**Registry Object ID:**

`urn:unir:ro:a38fabe8-fe32-4e94-932a-df80c41c2fe4`

**Registered Construct:** Document Identifier Grammar — Universal Identifier Architecture

### 8.1 Validated Chain

```text
Document Identifier Grammar
  ↓
Registration Readiness
  ↓
DOCUMENT-GRAMMAR-REG-AUTH-001
  ↓
Registry Object ID Allocation
  ↓
UNIR-REG-EVT-5C214B7869C7
  ↓
REGISTERED
```

### 8.2 Reassessment Status

```text
Reassessment: NOT ESTABLISHED
```

This means no applicable reassessment record is established by the validated current traceability evidence used for this materialization. It does not assert that no such record exists historically.

### 8.3 Representation Status

```text
Registration readiness: VALIDATED
Authorization:          VALIDATED
Allocation:             VALIDATED
Registration event:     VALIDATED
Reassessment:           NOT ESTABLISHED
```

---

## 9. DEC Registration Record Chain

**Registry Object ID:**

`urn:unir:ro:5fb50430-2d38-4aca-b04a-290d1cf4430f`

**Registered Construct:** Decision Identifier Class — DEC

### 9.1 Historical State

```text
UNIS-CORE-001 v1.6
        ↓
DEC
        ↓
DEFERRED
```

### 9.2 Current Registration Chain

```text
42-DECISION-IDENTIFIER-CLASS-DEC-V1.7-REASSESSMENT-001
        ↓
DEC-CLASS-REG-AUTH-001
        ↓
Registry Object ID Allocation
        ↓
UNIR-REG-EVT-E6F4CDF9DD74
        ↓
REGISTERED
```

### 9.3 Representation Status

```text
Historical assessment: VALIDATED
Reassessment:          VALIDATED
Authorization:         VALIDATED
Allocation:            VALIDATED
Registration event:    VALIDATED
Current state:         REGISTERED
```

The historical deferred state is provenance and is not current state.

---

## 10. DIC Registration Record Chain

**Registry Object ID:**

`urn:unir:ro:b8c56dee-8a77-4247-9658-87fb7f0b6000`

**Registered Construct:** Document Identifier Class — DIC

### 10.1 Validated Chain

```text
DIC
  ↓
DIC Readiness
  ↓
DIC-CLASS-REG-AUTH-001
  ↓
Registry Object ID Allocation
  ↓
UNIR-REG-EVT-7F1E039002A1
  ↓
REGISTERED
```

### 10.2 Reassessment Status

```text
Reassessment: NOT ESTABLISHED
```

This does not assert that no historical reassessment exists.

### 10.3 Representation Status

```text
Registration readiness: VALIDATED
Authorization:          VALIDATED
Allocation:             VALIDATED
Registration event:     VALIDATED
Reassessment:           NOT ESTABLISHED
```

---

## 11. Identifier Allocation Traceability

### 11.1 DIUA Boundary

DIUA is represented here only as the applicable namespace/context for identifier-allocation traceability.

DIUA is not represented as a separate UNIR Registry Object.

### 11.2 Concrete Document Identifier Allocation Coverage

The current validated allocation set represented by this revision is:

| # | Concrete Document Identifier | Target Document | Allocation State | Allocation Evidence |
|---|---|---|---|---|
| 001 | `DIUA-DIC-000001` | `UNIS-CORE-001 v1.7` — Universal Naming and Identification Standard | ALLOCATED — ACTIVE | Existing prior allocation represented by prior UNIR registry state and event reference |
| 002 | `DIUA-DIC-000002` | `UA-CORE-001 v0.2` — Universal Architecture | ALLOCATED — ACTIVE | `UNIR-ALLOCATION-ACT-001` and target-document identity record |
| 003 | `DIUA-DIC-000003` | `UG-CORE-001 v1.0` — Universal Governance | ALLOCATED — ACTIVE | `UNIR-ALLOCATION-ACT-003` |
| 004 | `DIUA-DIC-000004` | Universal Document System | ALLOCATED — ACTIVE | `UNIR-ALLOCATION-ACT-002` |

These are Concrete Document Identifier allocations, not UNIR Registry Objects.

### 11.3 DIUA-DIC-000001 — Existing Prior Allocation

```text
DIUA
  ↓
DIC Identifier Class
  ↓
Document Identifier Grammar
  ↓
DIUA-DIC-000001
  ↓
UNIS-CORE-001 v1.7 — Universal Naming and Identification Standard
```

**Allocation State:** ALLOCATED — ACTIVE  
**Allocation Record:** Existing prior allocation  
**Registration Event:** `UNIR-REG-EVT-DIUA-DIC-000001`  
**Target Document:** `UNIS-CORE-001 v1.7`

The existing prior allocation remains historical/current provenance for the first concrete DIUA/DIC document identifier. No new allocation act is created by this revision.

### 11.4 DIUA-DIC-000002 — Universal Architecture

```text
DIUA
  ↓
DIC Identifier Class
  ↓
Document Identifier Grammar
  ↓
DIUA-DIC-000002
  ↓
UA-CORE-001 v0.2 — Universal Architecture
```

**Allocation State:** ALLOCATED — ACTIVE  
**Allocation Act Reference:** `UNIR-ALLOCATION-ACT-001`  
**Target Document:** `UA-CORE-001 v0.2`  
**Target Document Identity State:** `ALLOCATED_ACTIVE`

The Universal Architecture document explicitly identifies `DIUA-DIC-000002` as its allocated active Concrete Document Identifier and references `UNIR-ALLOCATION-ACT-001`.

### 11.5 DIUA-DIC-000003 — Universal Governance

```text
DIUA
  ↓
DIC Identifier Class
  ↓
Document Identifier Grammar
  ↓
DIUA-DIC-000003
  ↓
UG-CORE-001 v1.0 — Universal Governance
```

**Allocation State:** ALLOCATED — ACTIVE  
**Allocation Act:** `UNIR-ALLOCATION-ACT-003`  
**Target Document:** `UG-CORE-001 v1.0`  
**Target Document Identity State:** `ALLOCATED_ACTIVE`

`UNIR-ALLOCATION-ACT-003` is the verified dedicated allocation act establishing the allocation authority for `DIUA-DIC-000003`.

### 11.6 DIUA-DIC-000004 — Universal Document System

```text
DIUA
  ↓
DIC Identifier Class
  ↓
Document Identifier Grammar
  ↓
DIUA-DIC-000004
  ↓
Universal Document System
```

**Allocation State:** ALLOCATED — ACTIVE  
**Allocation Act:** `UNIR-ALLOCATION-ACT-002`  
**Target Document:** Universal Document System

The allocation was explicitly authorized through `UNIR-ALLOCATION-ACT-002`.

### 11.7 Allocation Boundary

The following identities remain distinct:

```text
Concrete Document Identifier
    ≠
Allocation Record
    ≠
Allocation Act
    ≠
Registration Event
    ≠
UNIR Registry Object
    ≠
Current Registry State
```

The allocation entries above do not create new UNIR Registry Objects. They represent concrete document identities within the applicable DIUA/DIC identification architecture.

## 12. Historical Registration Provenance

Historical material is represented only where necessary to explain current registration state.

### 12.1 DEC Historical Provenance

```text
UNIS-CORE-001 v1.6
        ↓
DEFERRED
        ↓
v1.7 Reassessment
        ↓
REGISTERED
```

### 12.2 Historical Inventory Boundary

Historical registry inventories may be retained as provenance references.

They are not current registry state and do not supersede `UNIR-REGISTRY-001`.

---

## 13. Conditional Evidence Families

The following record families are recognized as potentially relevant to registration traceability:

```text
AUDIT
RECONCILIATION
REVIEW
```

However, the current materialization does not claim exhaustive discovery of all historical or operational records in these families.

An individual record shall be represented here only after its authoritative artifact has been independently validated.

Therefore:

```text
Audit corpus:           CONDITIONAL
Reconciliation corpus:  CONDITIONAL
Review corpus:          CONDITIONAL
```

No unvalidated records are invented or inferred.

---

## 14. Evidence & Authority Rules

### 14.1 Underlying Record Authority

The underlying authoritative record remains authoritative for its own content.

### 14.2 Representation Authority

This document is authoritative only for the canonical representation and traceability relationships it explicitly establishes within its scope.

### 14.3 Current Registry Authority

`UNIR-REGISTRY-001` remains the current registry-state representation.

### 14.4 Core Authority

`UNIR-CORE-001 v1.3` remains the canonical Core architectural boundary.

### 14.5 No Semantic Transfer

Representation of a record in this document does not transfer normative ownership of the represented construct or record semantics to this document.

---

## 15. Completeness & Claim Boundary

### 15.1 Validated Current Coverage

```text
Current Registry Objects:                 5
Validated minimum registration chains:    5 / 5
Concrete Document Identifier allocations represented: 4 / 4 known active allocations
```

### 15.2 Non-Exhaustive Historical Coverage

This document does not claim to contain an exhaustive inventory of:

- all historical registration records;
- all historical audit records;
- all reconciliation records;
- all review records;
- all construction or document-governance artifacts.

### 15.3 Evidence Absence Rule

`NOT ESTABLISHED` shall not be interpreted as `ABSENT`.

An unvalidated record shall not be fabricated to complete a symmetrical chain.

---

## 16. Materialization Boundary

This document materializes validated record representations and traceability.

It does not reproduce the full substantive contents of underlying:

- readiness records;
- authorization records;
- allocation records;
- decision records;
- registration events;
- reassessment records;
- audit records;
- reconciliation records;
- review records.

Those remain independently identifiable artifacts.

UDS construction, document materialization, canonicalization, and general publication/release records remain outside the substantive registration-record scope of this document; only the Concrete Document Identifier allocation for Universal Document System is represented here.

---

## 17. Canonical Closure

### 17.1 Current State

```text
Document Status:       LOCKED — CANONICAL
Canonicality:          CANONICAL
Lock Status:           LOCKED
Publication Status:    PUBLISHED
Publication Commit:    a885e539c6981c1bffe13d23d68713f1c6a8d22c
Publication Timestamp: 2026-08-15T08:27:02Z
```

### 17.2 Canonical Lock Decision

The document has completed:

1. record representation completeness audit;
2. registration-chain evidence reconciliation;
3. identity and authority boundary re-audit;
4. UDS conformance audit and controlled remediation;
5. final integrity verification;
6. explicit canonical lock authorization.

Accordingly, `UNIR-REGISTRATION-RECORD-001 v1.1` is now **LOCKED — CANONICAL** and supersedes v1.0 as the current materialized registration-record representation.

The canonical lock applies to the substantive content and approved documentary contract of this artifact. Publication has been completed through the canonical repository publication event recorded above.

---

## Governing Principle

> **UNIR-REGISTRATION-RECORD-001 provides a canonical representation and traceability layer for validated UNIR registration records. It does not replace underlying authoritative records, redefine UNIR Core semantics, or become the current registry-state authority.**
