---
document_id: UNIR-REGISTRY-001
document_type: Universal Registry State
title: Universal Naming & Identification Registry — Current Registry State
version: "1.0"
status: LOCKED — CANONICAL
canonicality: CANONICAL
scope: Current registered state of the Universal Naming & Identification Registry
purpose: Canonical documentary representation of current UNIR registry state
parent_document: UNIR-CORE-001 v1.3 (architectural boundary only; no semantic inheritance)
source_basis: Validated individual registration, authorization, allocation, reassessment, and identifier-allocation artifacts
---

# Universal Naming & Identification Registry — Current Registry State

**Document ID:** UNIR-REGISTRY-001  
**Document Type:** Universal Registry State  
**Title:** Universal Naming & Identification Registry — Current Registry State  
**Version:** 1.0  
**Status:** LOCKED — CANONICAL  
**Canonicality:** CANONICAL  
**Lock Status:** LOCKED  
**Document Role:** Canonical Current Registry State  
**Document Responsibility:** UNIR Registry Authority  
**Semantic Authority:** UNIS for Universal Naming & Identification semantics; UNIR Core governs registry representation within its defined boundary  
**Registry Authority:** UNIR Registry Authority  
**Normative Relationship:** Operates within the normative authority established by UNIS  
**Parent Document:** `UNIR-CORE-001 v1.3` — architectural boundary only; no semantic inheritance  
**Source Basis:** Validated individual registration, authorization, allocation, reassessment, and concrete identifier-allocation artifacts established through R1–R5  
**Canonical Lineage:** UNIR Core architectural boundary → validated registration artifacts → R1–R5 validation → UNIR-REGISTRY-001  
**Supersedes:** None  
**Superseded By:** None  
**Primary Form:** Markdown  
**Canonical Repository Path:** NOT YET ASSIGNED — publication not yet performed  
**Machine-Readable Metadata:** YES — explicit YAML front matter  
**AI Navigation:** See `## Navigation`

---

## Navigation

1. [Document Contract](#1-document-contract)
2. [Registry Representation Model](#2-registry-representation-model)
3. [Current Registered Registry Objects](#3-current-registered-registry-objects)
4. [Current Registry Object State Summary](#4-current-registry-object-state-summary)
5. [Registration Traceability](#5-registration-traceability)
6. [Current Registered / Allocated Identification Content](#6-current-registered--allocated-identification-content)
7. [Historical Provenance](#7-historical-provenance)
8. [Deferred and Excluded Registry Targets](#8-deferred-and-excluded-registry-targets)
9. [Current Registry State Boundaries](#9-current-registry-state-boundaries)
10. [Change and Source-Control Principle](#10-change-and-source-control-principle)
11. [Materialization Boundary](#11-materialization-boundary)
12. [Canonical Closure](#12-canonical-closure)

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
- historical provenance required to explain current state.

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

### 6.2 DIUA-DIC-000001

**Record Type:** Document Identifier Allocation Record  
**Identifier Class:** DIC  
**Namespace:** DIUA  
**Document Identifier:** `DIUA-DIC-000001`  
**Current State:** ALLOCATED — ACTIVE  
**Registry:** UNIR

The applicable construction is:

```text
DIUA Namespace
    ↓
DIC Identifier Class
    ↓
Document Identifier Grammar
    ↓
DIUA-DIC-000001
```

The allocation does not create:

- a new UNIR Core;
- a separate DIUA Registry Object;
- a new DIC definition;
- a new Document Identifier Grammar;
- a new DIUA namespace.

### 6.3 DIUA Allocation Registration Event

**Event ID:** `UNIR-REG-EVT-DIUA-DIC-000001`  
**Event Type:** Document Identifier Allocation  
**Identifier:** `DIUA-DIC-000001`  
**State:** RECORDED

The event provides operational registration evidence for the concrete Document Identifier allocation.

The event does not create a new namespace, a new UNIR Core, or a DIUA Registry Object.

---

## 7. Historical Provenance

Historical information is retained only where necessary to explain the current registry state.

### 7.1 UKOI and Decision Identifier Grammar

`UNIS-CORE-001 v1.6` remains historical provenance for registrations subsequently reassessed against `UNIS-CORE-001 v1.7`.

Current-source changes do not overwrite the historical registration basis.

### 7.2 DEC

The prior `DEC` assessment under `UNIS-CORE-001 v1.6` was:

```text
NOT READY — DEFERRED
```

That assessment was explicitly superseded by the v1.7 reassessment, after which DEC proceeded through authorization, allocation, and registration.

The historical deferred state is preserved as provenance and shall not be interpreted as current.

### 7.3 Historical Registry Inventory

Historical inventory artifacts are preserved as historical snapshots.

They are not authoritative sources for the current registry state represented by this document.

---

## 8. Deferred and Excluded Registry Targets

### 8.1 UIA

Universal Identifier Architecture (UIA) remains canonical in UNIS but is:

```text
Status: NOT REGISTERED
Outcome: NOT READY — DEFERRED
```

The current UNIR registration-readiness evidence does not establish independent registry eligibility for a normative architecture layer.

UIA therefore remains a normative reference and deferred registration candidate, not a current UNIR Registry Object.

### 8.2 Other Explicitly Unregistered Targets

The following are not represented as current Registry Objects by this document unless independently validated by current registration evidence:

- Decision Namespace;
- Document Namespace;
- individual Decision Identifiers;
- individual Document Identifiers other than the explicitly validated `DIUA-DIC-000001` allocation;
- unapproved registry targets.

This exclusion does not prohibit future registration where explicit eligibility, authorization, allocation, and registration evidence are subsequently established.

---

## 9. Current Registry State Boundaries

The following distinctions are normative for interpretation of this registry state:

```text
Registry Object
    ≠
Registry Object ID

Registry Object
    ≠
Represented Construct

Registry Object ID
    ≠
Concrete Document Identifier

Registration Event
    ≠
Registered Object

Allocation Record
    ≠
Registry Object

Historical State
    ≠
Current State

Registration
    ≠
Publication
```

No category above shall be collapsed merely because artifacts are operationally related.

---

## 10. Change and Source-Control Principle

When a normative UNIS source changes, UNIR shall distinguish:

```text
Previous Normative Source
        ↓
Historical Provenance

Current Normative Source
        ↓
Current Assessment / Reassessment
```

A source-version change does not automatically create a new Registry Object.

A new Registry Object is required only when the registered construct's semantic identity, registry identity, scope, validity, or authority relationship materially changes according to applicable governance.

Historical provenance shall not be overwritten.

---

## 11. Materialization Boundary

This document is a current-state representation.

It does not embed the full content of:

- readiness records;
- authorization records;
- allocation records;
- registration events;
- reassessment records;
- historical inventories;
- normative source specifications.

Those artifacts remain independently identifiable and authoritative for their own record types.

This document references their role in the current registry state and preserves the traceability required to reconstruct the registration chain.

---

## 12. Canonical Closure

### Current State

```text
Registry Object Representations: 5
Current Registered Objects:       5
Current Active Document Identifier Allocations represented: 1
Deferred Registry Candidates:     UIA
Document Status:                  LOCKED — CANONICAL
Canonicality:                     CANONICAL
Lock Status:                      LOCKED
Publication Status:               NOT PUBLISHED
```

### Canonical Lock

The document has completed the required materialization, artifact-level audit, UDS conformance review, and post-remediation final integrity check.

The resulting document state is:

```text
Canonicality: CANONICAL
Lock Status: LOCKED
Publication Status: NOT PUBLISHED
```

This lock applies to `UNIR-REGISTRY-001 v1.0` as the canonical registry-state artifact. It does not alter, supersede, or reopen `UNIR-CORE-001 v1.3`, nor does it alter any underlying registration, allocation, authorization, reassessment, or historical record.

Any future substantive change shall be governed through the applicable document revision and change-control process and shall not mutate this locked artifact in place.

---

## Governing Principle

> **UNIR-REGISTRY-001 represents the current state of the UNIR Registry without redefining the normative semantics of the constructs represented, without reconstructing the Six-Core architecture from historical consolidated artifacts, and without collapsing Registry Objects, identifiers, registration events, allocation records, historical states, or deferred candidates into a single identity or state category.**
