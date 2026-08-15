---
document_id: UNIR-REGISTRATION-RECORD-001
document_type: Registration Record Representation
title: Universal Naming & Identification Registration Record
version: "1.2"
status: LOCKED — CANONICAL
canonicality: CANONICAL
scope: Validated registration-record representations and traceability associated with current UNIR Registry Objects and concrete Document Identifier allocations
purpose: Canonical documentary representation and traceability layer for validated UNIR registration records and concrete Document Identifier allocations
parent_document: UNIR-REGISTRY-001 v1.2
source_basis: Validated registration readiness, decision, authorization, allocation, registration-event, reassessment, and concrete Document Identifier allocation evidence, including the current UNIR-REGISTRY-001 v1.1 traceability state and subsequent allocation materialization for DIUA-DIC-000003 through UNIR-ALLOCATION-ACT-003
semantic_authority: UNIS
registry_authority: UNIR Registry Authority
---

# Universal Naming & Identification Registration Record

**Document ID:** UNIR-REGISTRATION-RECORD-001  
**Document Type:** Registration Record Representation  
**Title:** Universal Naming & Identification Registration Record  
**Version:** 1.2  
**Status:** LOCKED — CANONICAL  
**Canonicality:** CANONICAL  
**Lock Status:** LOCKED  
**Document Role:** Canonical Registration Record Representation  
**Document Responsibility:** UNIR Registry Authority  
**Semantic Authority:** UNIS for Universal Naming & Identification semantics  
**Registry Authority:** UNIR Registry Authority for registry-record representation  
**Parent Document:** `UNIR-REGISTRY-001 v1.2`  
**Architectural Relationship:** Supporting record/traceability layer; does not replace current registry state  
**Supersedes:** `UNIR-REGISTRATION-RECORD-001 v1.1`  
**Superseded By:** None  
**Publication Status:** READY FOR PUBLICATION  
**Primary Form:** Markdown  
**Machine-Readable Metadata:** YES  
**Canonical Repository Path:** `00_System/40_Registries/10_UNIR/UNIR-REGISTRATION-RECORD-001_Universal_Naming_Identification_Registration_Record_v1.2.md`

---

## Identifier Allocation Traceability — Current Active Coverage

The current validated active Concrete Document Identifier allocation set is:

| # | Concrete Document Identifier | Target Document | Allocation State | Allocation Evidence |
|---|---|---|---|---|
| 001 | `DIUA-DIC-000001` | `UNIS-CORE-001 v1.7` — Universal Naming and Identification Standard | ALLOCATED — ACTIVE | Existing prior allocation; `UNIR-REG-EVT-DIUA-DIC-000001` |
| 002 | `DIUA-DIC-000002` | `UA-CORE-001 v0.2` — Universal Architecture | ALLOCATED — ACTIVE | `UNIR-ALLOCATION-ACT-001` |
| 003 | `DIUA-DIC-000003` | `UG-CORE-001 v1.0` — Universal Governance | ALLOCATED — ACTIVE | `UNIR-ALLOCATION-ACT-003` |
| 004 | `DIUA-DIC-000004` | Universal Document System | ALLOCATED — ACTIVE | `UNIR-ALLOCATION-ACT-002` |

These are Concrete Document Identifier allocations, not UNIR Registry Objects.

### DIUA-DIC-000003 — Universal Governance

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

`UNIR-ALLOCATION-ACT-003` provides the explicit allocation authority for the assignment.

### Allocation Boundary

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

The four allocation entries do not create new UNIR Registry Objects. They represent concrete document identities within the applicable DIUA/DIC identification architecture.

---

## Canonical Closure

```text
Document Status:       LOCKED — CANONICAL
Canonicality:          CANONICAL
Lock Status:           LOCKED
Publication Status:    READY FOR PUBLICATION
Concrete ID allocations represented: 4 / 4 known active allocations
```

`UNIR-REGISTRATION-RECORD-001 v1.2` supersedes v1.1 as the current materialized registration-record representation.
