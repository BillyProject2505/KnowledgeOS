# Universal Naming & Identification Registry (UNIR)

> Canonical navigation and orientation page for the UNIR document set.
>
> **This README is navigational documentation. It is not a normative replacement for any UNIR canonical document.**

## 1. Overview

The `10_UNIR` directory contains the canonical UNIR document set currently materialized for the Universal Naming & Identification architecture.

The documents have distinct roles and shall not be treated as interchangeable:

```text
UNIR-CORE-001
    ↓
Core Architecture

UNIR-REGISTRY-001
    ↓
Current Registry State

UNIR-REGISTRATION-RECORD-001
    ↓
Registration Record Representation & Traceability

UNIR-ALLOCATION-ACT-005
    ↓
Concrete Document Identifier Allocation Evidence
```

The separation exists to prevent UNIR Core semantics, current Registry Object state, registration-record material, and concrete identifier-allocation evidence from being collapsed into one representation.

## 2. Canonical Document Set

### 2.1 UNIR-CORE-001 v1.3

**Role:** Core Document / Canonical Six-Core Architecture  
**Status:** `LOCKED — CANONICAL`  
**Canonicality:** `CANONICAL`  
**Lock Status:** `LOCKED`

This document is the canonical architectural home of the UNIR Six Core domains. It defines the architectural boundary and does not serve as the current registry-state inventory or registration-record repository.

[Open UNIR-CORE-001 v1.3](./UNIR-CORE-001_Universal_Naming_Identification_Registry_v1.3.md)

### 2.2 UNIR-REGISTRY-001 v1.2

**Role:** Canonical Current Registry State  
**Status:** `LOCKED — CANONICAL`  
**Canonicality:** `CANONICAL`  
**Lock Status:** `LOCKED`  
**Publication Status:** `PUBLISHED`

This document represents the current registered state of UNIR, including current Registry Object representations, current registry state, applicable provenance, and bounded concrete Document Identifier allocations. The current active allocation set includes `DIUA-DIC-000001` through `DIUA-DIC-000005`, with `DIUA-DIC-000005` allocated to Universal Production Knowledge Registry.

[Open UNIR-REGISTRY-001 v1.2](./UNIR-REGISTRY-001_Universal_Naming_Identification_Registry_v1.2.md)

### 2.3 UNIR-REGISTRATION-RECORD-001 v1.2

**Role:** Canonical Registration Record Representation  
**Status:** `LOCKED — CANONICAL`  
**Canonicality:** `CANONICAL`  
**Lock Status:** `LOCKED`  
**Publication Status:** `PUBLISHED`

This document provides the canonical representation and traceability layer for validated registration records associated with current UNIR Registry Objects and the explicitly represented concrete Document Identifier allocation `DIUA-DIC-000005`.

The v1.2 revision records `UNIR-ALLOCATION-ACT-005` as verified allocation evidence for the Universal Production Knowledge Registry target.

[Open UNIR-REGISTRATION-RECORD-001 v1.2](./UNIR-REGISTRATION-RECORD-001_Universal_Naming_Identification_Registration_Record_v1.2.md)

### 2.4 UNIR-ALLOCATION-ACT-005

**Role:** Concrete Document Identifier Allocation Evidence  
**Status:** `VERIFIED — ACTIVE EVIDENCE`  
**Allocation:** `DIUA-DIC-000005`  
**Target:** Universal Production Knowledge Registry  
**Allocation State:** `ALLOCATED — ACTIVE`

This artifact establishes the allocation evidence for `DIUA-DIC-000005`. It does not create a UNIR Registry Object, redefine DIC, create a DIUA namespace, or replace the Registration Record or Registry State representations.

[Open UNIR-ALLOCATION-ACT-005](./UNIR-ALLOCATION-ACT-005_Universal_Production_Knowledge_Registry_Concrete_Document_Identifier_Allocation_Act.md)

## 3. Architectural Reading Order

For understanding the UNIR corpus, use the following order:

1. **UNIR-CORE-001** — understand the canonical Core architecture and boundaries.
2. **UNIR-REGISTRY-001** — inspect the current registered Registry state.
3. **UNIR-REGISTRATION-RECORD-001** — inspect validated registration-record relationships and traceability.
4. **UNIR-ALLOCATION-ACT-005** — inspect the explicit allocation evidence for `DIUA-DIC-000005`.

## 4. Authority and Boundary Rules

The documents in this directory have separate roles:

```text
UNIS
  ↓
Normative naming & identification authority

UNIR-CORE-001
  ↓
Canonical Core architecture

UNIR-REGISTRY-001
  ↓
Canonical current registry state

UNIR-REGISTRATION-RECORD-001
  ↓
Canonical registration-record representation / traceability

UNIR-ALLOCATION-ACT-005
  ↓
Concrete identifier allocation evidence

Underlying registration / authorization / allocation records
  ↓
Authoritative for their own record content
```

No document in this directory should be interpreted as silently redefining the authority of another layer.

## 5. Important Boundary Notes

### Six Core

The Six Core semantics belong to `UNIR-CORE-001`. Older consolidated UNIR documents are historical/decomposition references and shall not be used to reconstruct or modify the locked Core.

### Current Registry State

The canonical current registry state belongs to `UNIR-REGISTRY-001`. It is not replaced by a README, historical inventory, allocation act, or registration event record.

### Registration Records

`UNIR-REGISTRATION-RECORD-001` provides representation and traceability. It does not replace the underlying authoritative records.

### Allocation Evidence

`UNIR-ALLOCATION-ACT-005` is evidence for the concrete identifier allocation `DIUA-DIC-000005`. It is distinct from the Registration Record, Registry Object, and Current Registry State.

### DIUA

DIUA-related registered/allocated content is represented within the Registry layer according to the canonical boundaries established by the UNIR documents. DIUA is not to be inferred as a separate UNIR Registry Object merely because it participates in identifier allocation.

## 6. Publication and Lock State

The canonical UNIR documents listed in this README are maintained as locked artifacts. `UNIR-REGISTRY-001 v1.2` and `UNIR-REGISTRATION-RECORD-001 v1.2` are currently published on GitHub. `UNIR-ALLOCATION-ACT-005` is maintained as `VERIFIED — ACTIVE EVIDENCE`.

This README does not confer canonicality, alter document state, or authorize publication of any document.

## 7. Change Control

Do not edit locked canonical UNIR documents in place.

Any substantive change must proceed through the applicable revision, audit, canonicalization, and lock process, producing a new version or other explicitly authorized successor artifact.

Metadata-only maintenance to this README shall not be interpreted as a substantive revision of the canonical UNIR documents it describes.

## 8. Directory Contents

| Document | Role | Current State |
|---|---|---|
| `UNIR-CORE-001_Universal_Naming_Identification_Registry_v1.3.md` | Core Architecture | `LOCKED — CANONICAL` |
| `UNIR-REGISTRY-001_Universal_Naming_Identification_Registry_v1.2.md` | Current Registry State | `LOCKED — CANONICAL / PUBLISHED` |
| `UNIR-REGISTRATION-RECORD-001_Universal_Naming_Identification_Registration_Record_v1.2.md` | Registration Record Representation | `LOCKED — CANONICAL / PUBLISHED` |
| `UNIR-ALLOCATION-ACT-005_Universal_Production_Knowledge_Registry_Concrete_Document_Identifier_Allocation_Act.md` | Concrete Document Identifier Allocation Evidence | `VERIFIED — ACTIVE EVIDENCE` |

## 9. Evidence Chain for DIUA-DIC-000005

```text
UNIR-ALLOCATION-ACT-005
        ↓
DIUA-DIC-000005
        ↓
Universal Production Knowledge Registry
        ↓
UNIR-REGISTRATION-RECORD-001 v1.2
        ↓
UNIR-REGISTRY-001 v1.2
```

The relationship above is traceability only. The allocation act, registration record, and registry state remain distinct artifact classes and shall not be collapsed into a single identity.

## 10. README Boundary

This README exists for:

- repository navigation;
- document orientation;
- role clarification;
- high-level architectural boundaries;
- change-control orientation;
- high-level evidence-chain orientation.

It is **not**:

- a replacement for `UNIR-CORE-001`;
- a current registry inventory;
- a registration record repository;
- an allocation-act repository;
- a normative definition of UNIR semantics;
- an alternative canonical source of registry state.

---

**Directory:** `00_System/40_Registries/10_UNIR`  
**Purpose:** UNIR canonical document navigation and orientation
