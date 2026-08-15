# Registries

## Purpose

This directory contains the canonical registry architecture and registry specifications for the Knowledge Operating System (KOS).

Registries provide controlled operational representations of governed objects, identities, namespaces, relationships, lifecycle/state, and registration metadata. Registry documents do not replace the normative standards that define the semantics they operationalize.

---

## Canonical Registry Architecture

### Universal Naming & Identification Registry (UNIR)

The UNIR architecture is materialized as three separate canonical documents with distinct responsibilities. They shall not be treated as interchangeable.

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
```

### 1. UNIR Core Document

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

### 2. UNIR Registry State

**Document ID:** `UNIR-REGISTRY-001`  
**Current Version:** `1.1`  
**Status:** `LOCKED — CANONICAL`  
**Canonicality:** `CANONICAL`  
**Publication Status:** `PUBLISHED`

`UNIR-REGISTRY-001` represents the current registered state of UNIR, including current Registry Object representations, current registry state, applicable current-source provenance, and bounded registered/allocated identification content.

It does not redefine the Six Core semantics and does not replace the underlying registration records.

[Open UNIR-REGISTRY-001 v1.1](./10_UNIR/UNIR-REGISTRY-001_Universal_Naming_Identification_Registry_v1.1.md)

### 3. UNIR Registration Record Representation

**Document ID:** `UNIR-REGISTRATION-RECORD-001`  
**Current Version:** `1.1`  
**Status:** `LOCKED — CANONICAL`  
**Canonicality:** `CANONICAL`  
**Publication Status:** `PUBLISHED`

`UNIR-REGISTRATION-RECORD-001` provides the canonical representation and traceability layer for validated UNIR registration records associated with current Registry Objects.

Underlying readiness, authorization, allocation, decision, registration-event, reassessment, audit, review, and reconciliation artifacts remain authoritative for their own record content. This document does not become a parallel evidence repository.

[Open UNIR-REGISTRATION-RECORD-001 v1.1](./10_UNIR/UNIR-REGISTRATION-RECORD-001_Universal_Naming_Identification_Registration_Record_v1.1.md)

The more detailed navigation and orientation page for the `10_UNIR` directory is maintained separately at [10_UNIR/README.md](./10_UNIR/README.md).

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
```

Accordingly:

- **DIC** remains the Document Identifier Class.
- **Document Identifier Grammar** remains the identifier construction rule.
- **UNIR** provides the applicable operational registration, allocation, lifecycle, and registry mechanisms.
- DIUA shall not be assigned a separate UNIR Registry Object identity unless a future explicit registration-eligibility decision establishes that such registration is required.

---

## Registry Principles

- Registry specifications operate within the authority of applicable normative standards.
- Registry identifiers must be unique within their applicable identity scope.
- Registry object identity, classification, namespace, lifecycle/state, and governance concerns must remain within their defined ownership boundaries.
- Current registry state shall be represented only by the canonical current-state registry document.
- Registration records shall remain traceable to their underlying authoritative artifacts.
- Historical versions and superseded releases must remain traceable and must not be silently overwritten.
- New registry constructs require explicit registration and eligibility decisions; names appearing in normative standards do not automatically become separate Registry Objects.
- Locked canonical documents shall not be edited in place; substantive change requires the applicable revision, audit, canonicalization, and lock process.

---

## Legacy Registry Architecture Disposition

The former `00_System/Registries/` directory contained an earlier registry architecture generation, including `DocumentRegistry.md`, `KnowledgeObjectRegistry.md`, `RegistrySpecification.md`, `RelationshipRegistry.md`, and `VersionRegistry.md`.

These artifacts are no longer canonical. Their registry concepts and responsibilities are superseded, reconstituted, or absorbed by newer Universal architecture, governance, identification, lifecycle, relationship, and registry mechanisms.

The legacy directory has therefore been removed from the active repository structure. Historical repository history remains preserved by Git.

---

## Current Canonical Registry Set

| Document | Version | Status | Scope |
|---|---:|---|---|
| `UNIR-CORE-001_Universal_Naming_Identification_Registry_v1.3.md` | 1.3 | LOCKED — CANONICAL | UNIR Core Architecture |
| `UNIR-REGISTRY-001_Universal_Naming_Identification_Registry_v1.1.md` | 1.1 | LOCKED — CANONICAL / PUBLISHED | Current UNIR Registry State |
| `UNIR-REGISTRATION-RECORD-001_Universal_Naming_Identification_Registration_Record_v1.1.md` | 1.1 | LOCKED — CANONICAL / PUBLISHED | Registration Record Representation & Traceability |

The canonical UNIR document set is located in `00_System/40_Registries/10_UNIR/`.

The directory-level README at `10_UNIR/README.md` provides document-by-document navigation and orientation for this canonical set.

---

## Reading Order

For a first-time reading of the current UNIR architecture, use this order:

1. `UNIR-CORE-001` — understand the canonical Six Core architecture and boundaries.
2. `UNIR-REGISTRY-001` — inspect the current registered Registry state.
3. `UNIR-REGISTRATION-RECORD-001` — inspect validated registration-record relationships and traceability.
4. The underlying registration/allocation/reassessment artifacts — consult individual records when record-level evidence is required.

---

## Boundary of This README

This README is a **navigation and orientation document**. It is not:

- a replacement for `UNIR-CORE-001`;
- a current registry inventory;
- a registration record repository;
- a normative definition of UNIR semantics;
- an alternative canonical source of registry state;
- an authority to modify locked UNIR documents.

---

**Directory:** `00_System/40_Registries`  
**UNIR canonical document directory:** `00_System/40_Registries/10_UNIR`
