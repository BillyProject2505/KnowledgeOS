# Registries

## Purpose

This directory contains the canonical registry architecture and registry specifications for the Knowledge Operating System (KOS).

Registries provide controlled operational representations of governed objects, identities, namespaces, relationships, lifecycle/state, and registration metadata. Registry documents do not replace the normative standards that define the semantics they operationalize.

---

## Canonical Registry Architecture

The active registry layer is organized by distinct registry authorities and document roles. Registry architecture, current registry state, and registration-record representation are kept separate so that normative semantics are not conflated with operational registry state or evidence.

```text
00_System/40_Registries/
│
├── 10_UNIR/
│   ├── UNIR-CORE-001
│   │     ↓
│   │   UNIR architecture and Six-Core boundary
│   ├── UNIR-REGISTRY-001
│   │     ↓
│   │   current UNIR registry state
│   ├── UNIR-REGISTRATION-RECORD-001
│   │     ↓
│   │   registration-record representation & traceability
│   └── UNIR-ALLOCATION-ACT-005 / ACT-006 / ACT-007
│         ↓
│       concrete Document Identifier allocation evidence
│
└── 20_UPKR/
    ├── UPKR-CORE-001
    │     ↓
    │   UPKR architecture and governance
    ├── UPKR-REGISTRATION-RECORD-001
    │     ↓
    │   UPKR registration evidence, decisions, events & traceability
    └── UPKR-REGISTRY-001
          ↓
        current UPKR registered state
```

The registry families above have distinct semantic scope and shall not be treated as interchangeable.

---

## 1. Universal Naming & Identification Registry (UNIR)

The UNIR architecture is materialized as a canonical document set with distinct responsibilities.

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

UNIR-ALLOCATION-ACT-005 / ACT-006 / ACT-007
    ↓
Concrete Document Identifier Allocation Evidence
```

### 1.1 UNIR Core Document

**Document ID:** `UNIR-CORE-001`  
**Current Version:** `1.3`  
**Status:** `LOCKED — CANONICAL`  
**Canonicality:** `CANONICAL`

`UNIR-CORE-001` is the canonical architectural home of the UNIR Six Core domains:

- **UNIR-SCH** — Registry Object structure
- **UNIR-OCM** — Registry Object classification
- **UNIR-IDM** — Registry Object identity
- **UNIR-NSM** — Namespace semantics
- **UNIR-LSM** — Registry lifecycle and state
- **UNIR-GRP** — Governance and registration

The Core document defines the architectural and semantic ownership boundaries of the six Core domains. It is not the current registry inventory and is not a registration-record repository.

[Open UNIR-CORE-001 v1.3](./10_UNIR/UNIR-CORE-001_Universal_Naming_Identification_Registry_v1.3.md)

### 1.2 UNIR Registry State

**Document ID:** `UNIR-REGISTRY-001`  
**Current Version:** `1.5`  
**Status:** `LOCKED — CANONICAL`  
**Canonicality:** `CANONICAL`  
**Publication Status:** `PUBLISHED`

`UNIR-REGISTRY-001` represents the current registered state of UNIR, including current Registry Object representations, current registry state, applicable provenance, and bounded concrete Document Identifier allocations.

The current active allocation set represented by v1.5 includes `DIUA-DIC-000001` through `DIUA-DIC-000007`, including `DIUA-DIC-000005` for the Universal Production Knowledge Registry, `DIUA-DIC-000006` for `UPKR-REGISTRATION-RECORD-001`, and `DIUA-DIC-000007` for `UPKR-REGISTRY-001`.

It does not redefine the Six Core semantics and does not replace the underlying registration or allocation records.

[Open UNIR-REGISTRY-001 v1.5](./10_UNIR/UNIR-REGISTRY-001_v1.5.md)

### 1.3 UNIR Registration Record Representation

**Document ID:** `UNIR-REGISTRATION-RECORD-001`  
**Current Version:** `1.5`  
**Status:** `LOCKED — CANONICAL`  
**Canonicality:** `CANONICAL`  
**Publication Status:** `PUBLISHED`

`UNIR-REGISTRATION-RECORD-001` provides the canonical representation and traceability layer for validated UNIR registration records associated with current Registry Objects and explicitly represented concrete Document Identifier allocations.

The v1.5 revision incorporates `UNIR-ALLOCATION-ACT-005`, `UNIR-ALLOCATION-ACT-006`, and `UNIR-ALLOCATION-ACT-007` as verified allocation evidence for their respective targets.

[Open UNIR-REGISTRATION-RECORD-001 v1.5](./10_UNIR/UNIR-REGISTRATION-RECORD-001_v1.5.md)

### 1.4 UNIR Allocation Acts

Concrete Document Identifier allocation acts provide explicit allocation evidence for individual identifiers. They are distinct from Registry Objects, the current registry-state document, and the registration-record representation.

The currently materialized UNIR allocation evidence includes:

- `UNIR-ALLOCATION-ACT-005` → `DIUA-DIC-000005` → Universal Production Knowledge Registry
- `UNIR-ALLOCATION-ACT-006` → `DIUA-DIC-000006` → `UPKR-REGISTRATION-RECORD-001`
- `UNIR-ALLOCATION-ACT-007` → `DIUA-DIC-000007` → `UPKR-REGISTRY-001`

The detailed navigation and orientation page for the `10_UNIR` directory is maintained separately at [10_UNIR/README.md](./10_UNIR/README.md).

---

## 2. Universal Production Knowledge Registry (UPKR)

The UPKR is the active registry layer for the Universal Production Knowledge architecture. It governs the registration representation and current registered-state representation of Universal Production Knowledge Objects (UPKOs). It does not own or redefine the substantive semantics of UPKOs.

The active UPKR document set is organized as:

```text
UPKR-CORE-001
    ↓
UPKR architecture and governance

UPKR-REGISTRATION-RECORD-001
    ↓
registration evidence, decisions, events, state & traceability

UPKR-REGISTRY-001
    ↓
current registered state
```

### 2.1 UPKR Core

`UPKR-CORE-001_Universal_Production_Knowledge_Registry_v1.0.md`

**Role:** Canonical architecture and governance authority for UPKR.

### 2.2 UPKR Registration Record

`UPKR-REGISTRATION-RECORD-001_v1.1_23-UPKO-Initial-Registration-Batch.md`

**Role:** Canonical materialization of the initial 23-UPKO registration records, including registration evidence, decisions, events, state, effective date, and traceability.

### 2.3 UPKR Current Registry State

`UPKR-REGISTRY-001_v1.1_23-UPKO-Initial-Registered-State.md`

**Role:** Canonical current registry-state representation for the initial 23 registered UPKOs.

### 2.4 Initial UPKR Registration State

The current initial batch contains:

```text
UPKO-001 … UPKO-023
Registration State = REGISTERED — 23/23
Effective Date    = 2026-08-16
```

The registration layer is supported by the applicable Registration Decisions and Registration Events and is governed by `UPKR-CORE-001`.

The initial batch was canonicalized through the governed act:

`UPKR-CD-001 — APPROVE CANONICALIZATION`

with effective date:

`2026-08-16`

### 2.5 UPKR Authority Boundary

```text
UPKO
    = substantive Production Knowledge authority

UPKR-CORE-001
    = UPKR architecture / governance authority

UPKR-REGISTRATION-RECORD-001
    = registration evidence / decision / event / traceability

UPKR-REGISTRY-001
    = current registered state
```

UPKR documents shall not redefine substantive UPKO semantics.

The detailed navigation and orientation page for the `20_UPKR` directory is maintained at [20_UPKR/README.md](./20_UPKR/README.md).

---

## Universal Identifier Architecture Boundary

UNIR operationalizes identifier-related constructs governed by the applicable Universal Identifier Architecture. It does not redefine the normative semantics established by UNIS.

**DIUA (Document Identifier Universal Architecture)** is an architectural construct within the Universal Identifier Architecture (UIA). It is **not** a UNIR Core and is **not** a separate UNIR Registry Object by default.

The canonical relationship is:

```text
UNIS / UIA
    ↓
DIUA
    ├── governs → DIC
    └── governs → Document Identifier Grammar
                         ↓
                       UNIR
                         ↓
                operational registration
                allocation & registry state
```

Accordingly:

- **DIC** remains the Document Identifier Class.
- **Document Identifier Grammar** remains the identifier construction rule.
- **UNIR** provides the applicable operational registration, allocation, lifecycle, and registry mechanisms.
- DIUA shall not be assigned a separate UNIR Registry Object identity unless a future explicit registration-eligibility decision establishes that such registration is required.
- A concrete Document Identifier allocation shall not be treated as a separate UNIR Registry Object solely because it is represented in the registry state.

---

## Registry Principles

- Registry specifications operate within the authority of applicable normative standards.
- Registry identifiers must be unique within their applicable identity scope.
- Registry object identity, classification, namespace, lifecycle/state, and governance concerns must remain within their defined ownership boundaries.
- Current registry state shall be represented only by the applicable canonical current-state registry document.
- Registration records shall remain traceable to their underlying authoritative artifacts.
- Historical versions and superseded releases must remain traceable and must not be silently overwritten.
- New registry constructs require explicit registration and eligibility decisions; names appearing in normative standards do not automatically become separate Registry Objects.
- Concrete identifier allocation does not by itself create a Registry Object.
- Registry families may represent different governed object classes; one registry's semantics must not be inferred from another registry without explicit authority.
- Locked canonical documents shall not be edited in place; substantive change requires the applicable revision, audit, canonicalization, and lock process.

---

## Legacy Registry Architecture Disposition

The former `00_System/Registries/` directory contained an earlier registry architecture generation, including `DocumentRegistry.md`, `KnowledgeObjectRegistry.md`, `RegistrySpecification.md`, `RelationshipRegistry.md`, and `VersionRegistry.md`.

These artifacts are no longer canonical. Their registry concepts and responsibilities are superseded, reconstituted, or absorbed by newer Universal architecture, governance, identification, lifecycle, relationship, and registry mechanisms.

The legacy directory has therefore been removed from the active repository structure. Historical repository history remains preserved by Git.

---

## Current Canonical Registry Set

| Registry Family | Document | Version / State | Scope |
|---|---|---|---|
| UNIR | `UNIR-CORE-001_Universal_Naming_Identification_Registry_v1.3.md` | 1.3 — LOCKED / CANONICAL | UNIR Core Architecture |
| UNIR | `UNIR-REGISTRY-001_v1.5.md` | 1.5 — LOCKED / CANONICAL / PUBLISHED | Current UNIR Registry State |
| UNIR | `UNIR-REGISTRATION-RECORD-001_v1.5.md` | 1.5 — LOCKED / CANONICAL / PUBLISHED | Registration Record Representation & Traceability |
| UPKR | `UPKR-CORE-001_Universal_Production_Knowledge_Registry_v1.0.md` | 1.0 — Active Canonical | UPKR Architecture & Governance |
| UPKR | `UPKR-REGISTRATION-RECORD-001_v1.1_23-UPKO-Initial-Registration-Batch.md` | v1.1 — Active Registration Record | Initial 23-UPKO Registration Records |
| UPKR | `UPKR-REGISTRY-001_v1.1_23-UPKO-Initial-Registered-State.md` | v1.1 — Active Current State | Initial 23 Registered UPKOs |

The canonical UNIR document set is located in `00_System/40_Registries/10_UNIR/`.

The active UPKR document set is located in `00_System/40_Registries/20_UPKR/`.

---

## Reading Order

For a first-time reading of the current registry architecture, use this order:

1. `UNIR-CORE-001` — understand the canonical UNIR Six-Core architecture and boundaries.
2. `UNIR-REGISTRY-001` — inspect the current UNIR registered state and active concrete Document Identifier allocations.
3. `UNIR-REGISTRATION-RECORD-001` — inspect validated UNIR registration-record relationships and traceability.
4. `10_UNIR/README.md` — use the UNIR directory-level navigation and evidence-chain orientation when tracing specific allocation acts.
5. `UPKR-CORE-001` — understand UPKR architecture and governance.
6. `UPKR-REGISTRATION-RECORD-001` — inspect the UPKR registration evidence for the registered UPKO set.
7. `UPKR-REGISTRY-001` — inspect the current registered state of UPKR.
8. `20_UPKR/README.md` — use the UPKR directory-level navigation and archive boundary orientation.

---

## Boundary of This README

This README is a **navigation and orientation document**. It is not:

- a replacement for any registry Core document;
- a current registry inventory;
- a registration record repository;
- an allocation-act repository;
- a normative definition of UNIR, UPKR, UNIS, UIA, or UPKO semantics;
- an alternative canonical source of registry state;
- an authority to modify locked canonical registry documents.

---

**Directory:** `00_System/40_Registries`  
**UNIR canonical document directory:** `00_System/40_Registries/10_UNIR`  
**UPKR active document directory:** `00_System/40_Registries/20_UPKR`
