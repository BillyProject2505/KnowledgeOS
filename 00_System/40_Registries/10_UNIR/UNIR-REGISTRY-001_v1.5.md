---
document_id: UNIR-REGISTRY-001
document_type: Universal Registry State
title: Universal Naming & Identification Registry — Current Registry State
version: "1.5"
status: LOCKED — CANONICAL
canonicality: CANONICAL
scope: Current registered state of the Universal Naming & Identification Registry
purpose: Canonical documentary representation of current UNIR registry state, including validated active Concrete Document Identifier allocations
parent_document: UNIR-CORE-001 v1.3 (architectural boundary only; no semantic inheritance)
source_basis: Validated individual registration, authorization, allocation, reassessment, and concrete Document Identifier allocation evidence, including the explicit `UNIR-ALLOCATION-ACT-001` reference declared by Universal Architecture for DIUA-DIC-000002, the verified `UNIR-ALLOCATION-ACT-002` and `UNIR-ALLOCATION-ACT-003` allocation-act artifacts, and the verified `UNIR-ALLOCATION-ACT-005` allocation-act artifact establishing `DIUA-DIC-000005` for Universal Production Knowledge Registry, and the verified `UNIR-ALLOCATION-ACT-006` allocation-act artifact establishing `DIUA-DIC-000006` for `UPKR-REGISTRATION-RECORD-001`, and the verified `UNIR-ALLOCATION-ACT-007` allocation-act artifact establishing `DIUA-DIC-000007` for `UPKR-REGISTRY-001`.
---

# Universal Naming & Identification Registry — Current Registry State

**Document ID:** UNIR-REGISTRY-001  
**Document Type:** Universal Registry State  
**Title:** Universal Naming & Identification Registry — Current Registry State  
**Version:** 1.5  
**Status:** LOCKED — CANONICAL  
**Canonicality:** CANONICAL  
**Lock Status:** LOCKED  
**Document Role:** Canonical Current Registry State  
**Document Responsibility:** UNIR Registry Authority  
**Semantic Authority:** UNIS for Universal Naming & Identification semantics; UNIR Core governs registry representation within its defined boundary  
**Registry Authority:** UNIR Registry Authority  
**Normative Relationship:** Operates within the normative authority established by UNIS  
**Parent Document:** `UNIR-CORE-001 v1.3` — architectural boundary only; no semantic inheritance  
**Source Basis:** Validated individual registration, authorization, allocation, reassessment, and concrete identifier-allocation evidence established through R1–R5, including the explicit `UNIR-ALLOCATION-ACT-001` reference declared by Universal Architecture for `DIUA-DIC-000002`, the verified `UNIR-ALLOCATION-ACT-002` and `UNIR-ALLOCATION-ACT-003` allocation-act artifacts, and the verified `UNIR-ALLOCATION-ACT-005` allocation-act artifact establishing `DIUA-DIC-000005` for Universal Production Knowledge Registry, and the verified `UNIR-ALLOCATION-ACT-006` allocation-act artifact establishing `DIUA-DIC-000006` for `UPKR-REGISTRATION-RECORD-001`, and the verified `UNIR-ALLOCATION-ACT-007` allocation-act artifact establishing `DIUA-DIC-000007` for `UPKR-REGISTRY-001`.  
**Canonical Lineage:** UNIR Core architectural boundary → validated registration artifacts → R1–R5 validation → UNIR-REGISTRY-001  
**Supersedes:** `UNIR-REGISTRY-001 v1.3`  
**Superseded By:** None  
**Primary Form:** Markdown  
**Canonical Repository Path:** `00_System/40_Registries/10_UNIR/UNIR-REGISTRY-001_v1.5.md`  
**Publication Status:** PUBLISHED  
**Publication Event:** Canonical repository publication of successor revision  
**Publication Commit:** `PENDING — v1.5 publication evidence`  
**Publication Timestamp:** `PENDING — v1.5 publication evidence`

### Published v1.4 Provenance

The immediately preceding published canonical revision was `UNIR-REGISTRY-001 v1.4`.

- **Published Commit:** `daa467df9c8e50ca475bb5dea66de9297638888f`
- **Published Timestamp:** `2026-08-16T06:23:02Z`
- **Published Blob SHA:** `13f4d30bfb9ff2c05ea0a4d4760f62aaad77cdee`

These values are historical publication evidence for v1.4 and are not publication metadata for v1.5.  
**Machine-Readable Metadata:** YES — explicit YAML front matter  
**AI Navigation:** See `## Navigation`

---

## 1. Document Contract

### 1.1 Purpose

This document provides the current documentary representation of the Universal Naming & Identification Registry (UNIR) registered state.

It represents current registered Registry Objects, current registered or allocated identification content, registration traceability, current normative-source provenance, historical provenance necessary to interpret current state, and explicitly deferred or excluded registry targets.

This document does not redefine the normative semantics of the represented constructs.

### 1.2 Scope

This document covers:

- current registered UNIR Registry Object representations;
- their Registry Object identities and current registration states;
- current normative-source provenance;
- registration, authorization, allocation, and reassessment traceability;
- current concrete Document Identifier allocation relevant to the registry state;
- DIUA as registered/operational namespace context, without creating a DIUA Registry Object;
- deferred registry targets and explicit non-registration boundaries;
- historical provenance required to interpret current state.

### 1.3 Non-Scope

This document does not:

- redefine or reproduce the Six-Core semantic specifications;
- modify or reopen `UNIR-CORE-001 v1.3`;
- establish a new UNIR Core;
- establish a new OCM taxonomy or infer class hierarchy;
- redefine UNIS-owned naming or identification semantics;
- replace individual readiness, authorization, allocation, reassessment, or registration records;
- rewrite historical registration events;
- convert a concrete Document Identifier into a Registry Object;
- convert DIUA into a separate UNIR Registry Object;
- convert a deferred candidate into a registered object.

### 1.4 Authority Boundary

UNIS remains the normative authority for Universal Naming & Identification semantics.

UNIR provides registry representation and operational governance within that normative architecture.

Registry representation does not transfer normative ownership of a represented construct to UNIR.

### 1.5 Source Basis

The substantive registry state in this document is materialized from validated individual registration, authorization, allocation, reassessment, and concrete identifier-allocation artifacts established through the Registry Materialization R1–R5 validation process.

The historical consolidated UNIR artifacts are not used as the normative source for the current Registry state. They may be retained only as historical or decomposition provenance.

`UNIR-CORE-001 v1.3` is used as the canonical architectural boundary for determining what belongs to Core and what may be represented as registry state; its Six-Core substantive content is not reconstructed here.

---

## 2. Registry Representation Model

### 2.1 Identity Planes

UNIR Registry Object identity is distinct from the identity of the construct represented by the object.

The following are distinct:

```text
UNIR Registry Object ID
        ≠
Represented-Construct Identifier
        ≠
Concrete Document Identifier
        ≠
Registration Event ID
        ≠
Allocation Record
```

A Registry Object ID identifies the UNIR registry representation.

A concrete Document Identifier identifies a document within its applicable identification architecture and is not thereby a UNIR Registry Object ID.

### 2.2 Current-State Principle

This document represents current registry state.

Historical registration facts remain historical facts. Current state is determined through validated registration evidence and explicit current-source reassessment rather than by copying an older registry inventory.

### 2.3 Registration vs Publication

Registration and publication are distinct states and processes.

A registered object is not treated as a published registry state solely because its registration evidence exists.

---

## 3. Current Registered Registry Objects

The current validated Registry Object set contains five registered representations.

### 3.1 UKOI — Knowledge Object Identification Space

**Registry Object ID:** `urn:unir:ro:ffc0bb08-912b-4153-b334-62777563159f`  
**Registered Construct:** UKOI — Knowledge Object Identification Space  
**Current State:** REGISTERED  
**Current Normative Source:** `UNIS-CORE-001 v1.7`  
**Historical Normative Source:** `UNIS-CORE-001 v1.6`  
**Registration Event:** `UNIR-REG-EVT-68C1B2E3CF07`  
**Current-Source Reassessment:** `UKOI-V1.7-REASSESSMENT-001`

The v1.7 reassessment updates current normative-source provenance while preserving the existing Registry Object identity where no material semantic displacement was established.

**Registry representation:** CURRENT / REGISTERED

### 3.2 Decision Identifier Grammar

**Registry Object ID:** `urn:unir:ro:90b1e3bc-5383-4c79-a259-35cc281f6961`  
**Registered Construct:** Decision Identifier Grammar — Universal Identifier Architecture  
**Current State:** REGISTERED  
**Current Normative Source:** `UNIS-CORE-001 v1.7`  
**Historical Normative Source:** `UNIS-CORE-001 v1.6`  
**Registration Event:** `UNIR-REG-EVT-47CCF590E63F`  
**Current-Source Reassessment:** `36-DECISION-IDENTIFIER-GRAMMAR-V1.7-REASSESSMENT-001`

The current-source reassessment preserves the existing Registry Object identity where semantic continuity was established.

**Registry representation:** CURRENT / REGISTERED

### 3.3 Document Identifier Grammar

**Registry Object ID:** `urn:unir:ro:a38fabe8-fe32-4e94-932a-df80c41c2fe4`  
**Registered Construct:** Document Identifier Grammar — Universal Identifier Architecture  
**Current State:** REGISTERED  
**Current Normative Source:** `UNIS-CORE-001 v1.7`  
**Registration Event:** `UNIR-REG-EVT-5C214B7869C7`

The registration event records the grammar as registered under the applicable current normative source.

**Registry representation:** CURRENT / REGISTERED

### 3.4 Decision Identifier Class — DEC

**Registry Object ID:** `urn:unir:ro:5fb50430-2d38-4aca-b04a-290d1cf4430f`  
**Registered Construct:** Decision Identifier Class — DEC  
**Current State:** REGISTERED  
**Current Normative Source:** `UNIS-CORE-001 v1.7`  
**Historical State:** DEFERRED under `UNIS-CORE-001 v1.6`  
**Current Assessment:** `42-DECISION-IDENTIFIER-CLASS-DEC-V1.7-REASSESSMENT-001`  
**Registration Event:** `UNIR-REG-EVT-E6F4CDF9DD74`

The v1.7 reassessment superseded the previous deferred assessment. The subsequent authorization, Registry Object ID allocation, and registration event established the current registered state.

**Registry representation:** CURRENT / REGISTERED

### 3.5 Document Identifier Class — DIC

**Registry Object ID:** `urn:unir:ro:b8c56dee-8a77-4247-9658-87fb7f0b6000`  
**Registered Construct:** Document Identifier Class — DIC  
**Current State:** REGISTERED  
**Current Normative Source:** `UNIS-CORE-001 v1.7`  
**Registration Event:** `UNIR-REG-EVT-7F1E039002A1`

This registration represents the Identifier Class only. It does not register a Document Namespace, individual Document Identifiers, Document Objects, or a Document Registry.

**Registry representation:** CURRENT / REGISTERED

---

## 4. Current Registry Object State Summary

| # | Registry Object ID | Registered Construct | Current Normative Source | Current State |
|---|---|---|---|---|
| 001 | `urn:unir:ro:ffc0bb08-912b-4153-b334-62777563159f` | UKOI — Knowledge Object Identification Space | UNIS-CORE-001 v1.7 | REGISTERED |
| 002 | `urn:unir:ro:90b1e3bc-5383-4c79-a259-35cc281f6961` | Decision Identifier Grammar | UNIS-CORE-001 v1.7 | REGISTERED |
| 003 | `urn:unir:ro:a38fabe8-fe32-4e94-932a-df80c41c2fe4` | Document Identifier Grammar | UNIS-CORE-001 v1.7 | REGISTERED |
| 004 | `urn:unir:ro:5fb50430-2d38-4aca-b04a-290d1cf4430f` | Decision Identifier Class — DEC | UNIS-CORE-001 v1.7 | REGISTERED |
| 005 | `urn:unir:ro:b8c56dee-8a77-4247-9658-87fb7f0b6000` | Document Identifier Class — DIC | UNIS-CORE-001 v1.7 | REGISTERED |

**Current Registered Registry Object Count: 5**

---

## 5. Registration Traceability

Registration traceability is represented as references to the underlying operational records. Those records remain independently authoritative for the events and decisions they document.

### 5.1 UKOI

```text
UKOI
  ↓
UKOI-READINESS-001
  ↓
UKOI-REG-AUTH-001
  ↓
Registry Object ID allocation
  ↓
UNIR-REG-EVT-68C1B2E3CF07
  ↓
REGISTERED
```

Current-source reassessment:

`UKOI-V1.7-REASSESSMENT-001`

### 5.2 Decision Identifier Grammar

```text
Decision Identifier Grammar
  ↓
Registration readiness
  ↓
DEC-GRAMMAR-REG-AUTH-001
  ↓
Registry Object ID allocation
  ↓
UNIR-REG-EVT-47CCF590E63F
  ↓
REGISTERED
```

Current-source reassessment:

`36-DECISION-IDENTIFIER-GRAMMAR-V1.7-REASSESSMENT-001`

### 5.3 Document Identifier Grammar

```text
Document Identifier Grammar
  ↓
Registration readiness
  ↓
DOCUMENT-GRAMMAR-REG-AUTH-001
  ↓
Registry Object ID allocation
  ↓
UNIR-REG-EVT-5C214B7869C7
  ↓
REGISTERED
```

### 5.4 DEC

```text
DEC
  ↓
42-DECISION-IDENTIFIER-CLASS-DEC-V1.7-REASSESSMENT-001
  ↓
DEC-CLASS-REG-AUTH-001
  ↓
Registry Object ID allocation
  ↓
UNIR-REG-EVT-E6F4CDF9DD74
  ↓
REGISTERED
```

The previous v1.6 deferred assessment is historical provenance and is not the current state.

### 5.5 DIC

```text
DIC
  ↓
DIC registration readiness
  ↓
DIC-CLASS-REG-AUTH-001
  ↓
Registry Object ID allocation
  ↓
UNIR-REG-EVT-7F1E039002A1
  ↓
REGISTERED
```

---

## 6. Current Registered / Allocated Identification Content

### 6.1 DIUA Context

DIUA (Document Identifier Universal Architecture) is an architectural construct within the Universal Identifier Architecture.

For the purpose of this registry state, DIUA is represented as an applicable namespace/context for concrete Document Identifier allocation.

DIUA is **not** represented as a separate UNIR Registry Object.

Its current representation shall not be interpreted as independent UNIR ownership of the UIA architecture.

### 6.2 Active Concrete Document Identifier Allocation Summary

The current validated active allocation set represented by this revision is:

| # | Document Identifier | Target Document | Current State | Allocation Evidence |
|---|---|---|---|---|
| 001 | `DIUA-DIC-000001` | `UNIS-CORE-001 v1.7` — Universal Naming and Identification Standard | ALLOCATED — ACTIVE | Existing prior allocation; `UNIR-REG-EVT-DIUA-DIC-000001` |
| 002 | `DIUA-DIC-000002` | `UA-CORE-001 v0.2` — Universal Architecture | ALLOCATED — ACTIVE | `UNIR-ALLOCATION-ACT-001` |
| 003 | `DIUA-DIC-000003` | `UG-CORE-001 v1.0` — Universal Governance | ALLOCATED — ACTIVE | `UNIR-ALLOCATION-ACT-003` |
| 004 | `DIUA-DIC-000004` | Universal Document System | ALLOCATED — ACTIVE | `UNIR-ALLOCATION-ACT-002` |
| 005 | `DIUA-DIC-000005` | Universal Production Knowledge Registry | ALLOCATED — ACTIVE | `UNIR-ALLOCATION-ACT-005` |
| 006 | `DIUA-DIC-000006` | `UPKR-REGISTRATION-RECORD-001` — Universal Production Knowledge Registry Registration Record | ALLOCATED — ACTIVE | `UNIR-ALLOCATION-ACT-006` |
| 007 | `DIUA-DIC-000007` | `UPKR-REGISTRY-001` — Universal Production Knowledge Registry Current Registry State | ALLOCATED — ACTIVE | `UNIR-ALLOCATION-ACT-007` |

**Current Active Concrete Document Identifier Allocation Count: 7**

These allocations do not constitute additional UNIR Registry Objects.

### 6.3 DIUA-DIC-000001 — Universal Naming and Identification Standard

**Record Type:** Document Identifier Allocation Record  
**Identifier Class:** DIC  
**Namespace:** DIUA  
**Document Identifier:** `DIUA-DIC-000001`  
**Target Document:** `UNIS-CORE-001 v1.7` — Universal Naming and Identification Standard  
**Current State:** ALLOCATED — ACTIVE  
**Registration Event:** `UNIR-REG-EVT-DIUA-DIC-000001`

### 6.4 DIUA-DIC-000002 — Universal Architecture

**Record Type:** Document Identifier Allocation Record  
**Identifier Class:** DIC  
**Namespace:** DIUA  
**Document Identifier:** `DIUA-DIC-000002`  
**Target Document:** `UA-CORE-001 v0.2` — Universal Architecture  
**Current State:** ALLOCATED — ACTIVE  
**Allocation Act Reference:** `UNIR-ALLOCATION-ACT-001`

### 6.5 DIUA-DIC-000003 — Universal Governance

**Record Type:** Document Identifier Allocation Record  
**Identifier Class:** DIC  
**Namespace:** DIUA  
**Document Identifier:** `DIUA-DIC-000003`  
**Target Document:** `UG-CORE-001 v1.0` — Universal Governance  
**Current State:** ALLOCATED — ACTIVE  
**Allocation Act:** `UNIR-ALLOCATION-ACT-003`

### 6.6 DIUA-DIC-000004 — Universal Document System

**Record Type:** Document Identifier Allocation Record  
**Identifier Class:** DIC  
**Namespace:** DIUA  
**Document Identifier:** `DIUA-DIC-000004`  
**Target Document:** Universal Document System  
**Current State:** ALLOCATED — ACTIVE  
**Allocation Act:** `UNIR-ALLOCATION-ACT-002`

### 6.7 DIUA-DIC-000005 — Universal Production Knowledge Registry

**Record Type:** Document Identifier Allocation Record  
**Identifier Class:** DIC  
**Namespace:** DIUA  
**Document Identifier:** `DIUA-DIC-000005`  
**Target Document:** Universal Production Knowledge Registry  
**Current State:** ALLOCATED — ACTIVE  
**Allocation Act:** `UNIR-ALLOCATION-ACT-005`

`UNIR-ALLOCATION-ACT-005` is the verified dedicated allocation evidence establishing this assignment.


### 6.8 DIUA-DIC-000006 — UPKR Registration Record

**Record Type:** Document Identifier Allocation Record  
**Identifier Class:** DIC  
**Namespace:** DIUA  
**Document Identifier:** `DIUA-DIC-000006`  
**Target Document:** `UPKR-REGISTRATION-RECORD-001` — Universal Production Knowledge Registry Registration Record  
**Current State:** ALLOCATED — ACTIVE  
**Allocation Act:** `UNIR-ALLOCATION-ACT-006` — VERIFIED — ACTIVE EVIDENCE

`UNIR-ALLOCATION-ACT-006` is the verified dedicated allocation evidence establishing this assignment.


### 6.10 DIUA-DIC-000007 — UPKR Registry

**Record Type:** Document Identifier Allocation Record  
**Identifier Class:** DIC  
**Namespace:** DIUA  
**Document Identifier:** `DIUA-DIC-000007`  
**Target Document:** `UPKR-REGISTRY-001` — Universal Production Knowledge Registry Current Registry State  
**Title:** Universal Production Knowledge Registry Current Registry State  
**Document Type:** Registry State  
**Short Name:** UPKR Registry  
**Current State:** ALLOCATED — ACTIVE  
**Allocation Act:** `UNIR-ALLOCATION-ACT-007` — VERIFIED — ACTIVE EVIDENCE

`UNIR-ALLOCATION-ACT-007` is the verified dedicated allocation evidence establishing this assignment.

### Current Materialization Relationship — ACT-007

```text
UNIR-ALLOCATION-ACT-007
        ↓
DIUA-DIC-000007
        ↓
UPKR-REGISTRY-001
        ↓
UNIR-REGISTRY-001 v1.5
```

This current-state relationship is distinct from any historical publication-context relationship embedded in the ACT-007 evidence artifact.

### 6.11 Allocation Boundary

The current concrete Document Identifier allocations above do not constitute additional UNIR Registry Objects, do not redefine DIC, and do not create a separate DIUA Registry Object.

---

## 7. Historical Provenance

The v1.2 registry state is the direct predecessor of this v1.3 successor revision.

---

## 8. Deferred and Excluded Registry Targets

### 8.1 UIA

Universal Identifier Architecture (UIA) remains canonical in UNIS but is not independently registered as a UNIR Registry Object by this document.

### 8.2 Other Explicitly Unregistered Targets

No additional Registry Objects are created by the concrete identifier allocations represented in Section 6.

---

## 9. Current Registry State Boundaries

The following distinctions remain normative for interpretation:

```text
Registry Object

    ≠
Concrete Document Identifier

Concrete Document Identifier
    ≠
Allocation Act

Allocation Act
    ≠
Registration Event

Historical State
    ≠
Current State

Registration
    ≠
Publication
```

---

## 10. Change and Source-Control Principle

A source-version or allocation-state change does not automatically create a new Registry Object.

Concrete Document Identifier allocations are represented separately from Registry Object identity.

Historical provenance shall not be overwritten.

---

## 11. Materialization Boundary

This document is a current-state representation. It does not embed the full contents of the underlying allocation, authorization, registration, reassessment, or normative artifacts.

---

## 12. Canonical Closure

```text
Document Status:                  LOCKED — CANONICAL
Canonicality:                     CANONICAL
Lock Status:                      LOCKED
Publication Status:               PUBLISHED
Publication Commit:    PENDING — populated from actual GitHub publication commit
Publication Timestamp: PENDING — populated from actual GitHub publication timestamp
Registry Object Representations:  5
Current Active Document Identifier Allocations represented: 6
```

`UNIR-REGISTRY-001 v1.4` is the successor revision to `UNIR-REGISTRY-001 v1.2` and incorporates the verified `DIUA-DIC-000006` allocation for `UPKR-REGISTRATION-RECORD-001` while preserving the existing `DIUA-DIC-000005` allocation.

---

## Governing Principle

> **UNIR-REGISTRY-001 represents the current state of the UNIR Registry without redefining the normative semantics of the constructs represented, without collapsing Registry Objects and concrete identifiers into one identity, and with each concrete identifier allocation traceable to its applicable allocation evidence.**

---

## Appendix A — Verified Allocation Evidence

The following allocation act is incorporated as the documentary evidence basis for the `DIUA-DIC-000005` allocation represented in Section 6.7.

### UNIR-ALLOCATION-ACT-005

# Universal Production Knowledge Registry Concrete Document Identifier Allocation Act

**Allocation Act ID:** UNIR-ALLOCATION-ACT-005  
**Document Type:** Concrete Document Identifier Allocation Act  
**Version:** 1.0  
**Status:** VERIFIED — ACTIVE EVIDENCE  
**Authority:** UNIR Registry Authority  
**Target:** Universal Production Knowledge Registry  
**Allocated Identifier:** `DIUA-DIC-000005`  
**Identifier Class:** DIC  
**Namespace:** DIUA  
**Allocation State:** ALLOCATED — ACTIVE  
**Grammar:** `DIUA-DIC-<6DigitSequence>`  
**Allocation Sequence:** `000005`

## 1. Allocation Determination

This Allocation Act establishes the concrete Document Identifier allocation:

```text
DIUA-DIC-000005
        ↓
Universal Production Knowledge Registry
```

The allocation is made under the applicable DIUA/DIC identification architecture and does not establish a new naming or identification grammar.

## 2. Allocation Scope

The allocated identifier applies specifically to the concrete document:

**Universal Production Knowledge Registry**

This Allocation Act does not create a UNIR Registry Object, does not redefine the DIC Identifier Class, does not create a new DIUA namespace, and does not alter UNIS normative naming or identification semantics.

## 3. Allocation State

```text
Allocation State: ALLOCATED — ACTIVE
```

The identifier is treated as actively allocated to the stated target document for UNIR registration and registry-state traceability purposes.

## 4. Allocation Boundary

```text
Concrete Document Identifier
    ≠
Allocation Act
    ≠
Registration Record
    ≠
UNIR Registry Object
    ≠
Current Registry State
```

This act is the allocation evidence for `DIUA-DIC-000005`. It is not itself the UNIR Registry Object representation and does not replace the Registration Record or Registry State representation.

## 5. Registry Traceability

The allocation established by this act may be represented in:

- `UNIR-REGISTRATION-RECORD-001 v1.2`; and
- `UNIR-REGISTRY-001 v1.2`.

The corresponding registry representations shall preserve the distinction between the concrete identifier, the allocation act, registration record representation, and current registry state.

## 6. Canonical Closure

```text
Allocation Act:       UNIR-ALLOCATION-ACT-005
Allocated ID:         DIUA-DIC-000005
Target:               Universal Production Knowledge Registry
Allocation State:     ALLOCATED — ACTIVE
Evidence State:       VERIFIED — ACTIVE EVIDENCE
```

### Evidence Relationship

```text
UNIR-ALLOCATION-ACT-005
        ↓
DIUA-DIC-000005
        ↓
Universal Production Knowledge Registry
        ↓
UNIR-REGISTRATION-RECORD-001 v1.4
        ↓
UNIR-REGISTRY-001 v1.3
```

The incorporated act remains a distinct evidence artifact. Its inclusion here does not collapse the Allocation Act into the Registry Object, Registration Record, or Registry State.

---

## Appendix B — Verified Allocation Evidence: UNIR-ALLOCATION-ACT-006

# Universal Production Knowledge Registry Registration Record Concrete Document Identifier Allocation Act

**Allocation Act ID:** UNIR-ALLOCATION-ACT-006  
**Document Type:** Concrete Document Identifier Allocation Act  
**Version:** 1.0  
**Status:** VERIFIED — ACTIVE EVIDENCE  
**Authority:** UNIR Registry Authority  
**Target:** `UPKR-REGISTRATION-RECORD-001` — Universal Production Knowledge Registry Registration Record  
**Allocated Identifier:** `DIUA-DIC-000006`  
**Identifier Class:** DIC  
**Namespace:** DIUA  
**Allocation State:** ALLOCATED — ACTIVE  
**Grammar:** `DIUA-DIC-<6DigitSequence>`  
**Allocation Sequence:** `000006`

## 1. Allocation Determination

This Allocation Act establishes the concrete Document Identifier allocation:

```text
DIUA-DIC-000006
        ↓
UPKR-REGISTRATION-RECORD-001
        ↓
Universal Production Knowledge Registry Registration Record
```

The allocation is made under the applicable DIUA/DIC identification architecture and does not establish a new naming or identification grammar.

## 2. Allocation Scope

The allocated identifier applies specifically to the concrete document:

**`UPKR-REGISTRATION-RECORD-001` — Universal Production Knowledge Registry Registration Record**

This Allocation Act does not create a UNIR Registry Object, does not redefine the DIC Identifier Class, does not create a new DIUA namespace, and does not alter UNIS normative naming or identification semantics.

## 3. Allocation State

```text
Allocation State: ALLOCATED — ACTIVE
```

The identifier is treated as actively allocated to the stated target document for UNIR registration and registry-state traceability purposes.

## 4. Allocation Boundary

```text
Concrete Document Identifier
    ≠
Allocation Act
    ≠
Registration Record
    ≠
UNIR Registry Object
    ≠
Current Registry State
```

This act is the allocation evidence for `DIUA-DIC-000006`. It is not itself the UNIR Registry Object representation and does not replace the Registration Record or Registry State representation.

## 5. Registry Traceability

The allocation established by this act may be represented in the applicable UNIR Registration Record and UNIR Registry successor revisions after validation and materialization.

The corresponding registry representations shall preserve the distinction between the concrete identifier, the allocation act, registration record representation, and current registry state.

## 6. Canonical Closure

```text
Allocation Act:       UNIR-ALLOCATION-ACT-006
Allocated ID:         DIUA-DIC-000006
Target:               UPKR-REGISTRATION-RECORD-001
Allocation State:     ALLOCATED — ACTIVE
Evidence State:       VERIFIED — ACTIVE EVIDENCE
```

### Evidence Relationship

```text
UNIR-ALLOCATION-ACT-006
        ↓
DIUA-DIC-000006
        ↓
UPKR-REGISTRATION-RECORD-001
        ↓
UNIR-REGISTRATION-RECORD-001 v1.4
        ↓
UNIR-REGISTRY-001 v1.3
```

The incorporated act remains a distinct evidence artifact. Its inclusion does not create a new Registry Object or alter DIC/DIUA semantics.

---

## Appendix C — Verified Allocation Evidence: UNIR-ALLOCATION-ACT-007

# Universal Production Knowledge Registry Current Registry State Concrete Document Identifier Allocation Act

**Allocation Act ID:** UNIR-ALLOCATION-ACT-007  
**Document Type:** Concrete Document Identifier Allocation Act  
**Version:** 1.0  
**Status:** VERIFIED — ACTIVE EVIDENCE  
**Authority:** UNIR Registry Authority  
**Target:** `UPKR-REGISTRY-001` — Universal Production Knowledge Registry Current Registry State  
**Allocated Identifier:** `DIUA-DIC-000007`  
**Identifier Class:** DIC  
**Namespace:** DIUA  
**Allocation State:** ALLOCATED — ACTIVE  
**Grammar:** `DIUA-DIC-<6DigitSequence>`  
**Allocation Sequence:** `000007`

## 1. Allocation Determination

This Allocation Act establishes the concrete Document Identifier allocation:

```text
DIUA-DIC-000007
        ↓
UPKR-REGISTRY-001
        ↓
Universal Production Knowledge Registry Current Registry State
```

The allocation is made under the applicable DIUA/DIC identification architecture and does not establish a new naming or identification grammar.

## 2. Allocation Scope

The allocated identifier applies specifically to the concrete document:

**`UPKR-REGISTRY-001` — Universal Production Knowledge Registry Current Registry State**

**Title:** Universal Production Knowledge Registry Current Registry State  
**Document Type:** Registry State  
**Short Name:** UPKR Registry

This Allocation Act does not create a UNIR Registry Object, does not redefine the DIC Identifier Class, does not create a new DIUA namespace, and does not alter UNIS normative naming or identification semantics.

## 3. Allocation State

```text
Allocation State: ALLOCATED — ACTIVE
```

The identifier is treated as actively allocated to the stated target document for UNIR registration and registry-state traceability purposes.

## 4. Allocation Boundary

```text
Concrete Document Identifier
    ≠
Allocation Act
    ≠
Registry State Document
    ≠
UNIR Registry Object
    ≠
Current UNIR Registry State
```

This act is the allocation evidence for `DIUA-DIC-000007`. It is not itself the UNIR Registry Object representation and does not replace the target Registry State document or the current UNIR Registry representation.

## 5. Registry Traceability

The allocation established by this act may be represented in the applicable UNIR Registration Record and UNIR Registry successor revisions after validation and materialization.

The corresponding registry representations shall preserve the distinction between the concrete identifier, the allocation act, the target Registry State document, the registration record representation, and the current UNIR registry state.

## 6. Canonical Closure

```text
Allocation Act:       UNIR-ALLOCATION-ACT-007
Allocated ID:         DIUA-DIC-000007
Target:               UPKR-REGISTRY-001
Allocation State:     ALLOCATED — ACTIVE
Evidence State:       VERIFIED — ACTIVE EVIDENCE
```

### Evidence Relationship

```text
UNIR-ALLOCATION-ACT-007
        ↓
DIUA-DIC-000007
        ↓
UPKR-REGISTRY-001
        ↓
Universal Production Knowledge Registry Current Registry State
        ↓
UNIR-REGISTRATION-RECORD-001 v1.4
        ↓
UNIR-REGISTRY-001 v1.4
```

The incorporated act remains a distinct evidence artifact. Its inclusion does not create a new Registry Object or alter DIC/DIUA semantics.
