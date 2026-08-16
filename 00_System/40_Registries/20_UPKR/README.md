# Universal Production Knowledge Registry (UPKR)

`20_UPKR` is the active repository layer for the **Universal Production Knowledge Registry (UPKR)**.

## Purpose

UPKR governs the registration representation and current registered-state representation of Universal Production Knowledge Objects (UPKOs). It does not own or redefine the substantive semantics of UPKOs.

## Core Architecture

The active UPKR layer is organized around three distinct document layers:

```text
UPKR-CORE-001
    ↓
UPKR architecture and governance

UPKR-REGISTRATION-RECORD-001
    ↓
registration evidence, decisions, events, and traceability

UPKR-REGISTRY-001
    ↓
current registered state
```

## Active Documents

### 1. UPKR Core

`UPKR-CORE-001_Universal_Production_Knowledge_Registry_v1.0.md`

Canonical architecture and governance authority for UPKR.

### 2. UPKR Registration Record

`UPKR-REGISTRATION-RECORD-001_v1.1_23-UPKO-Initial-Registration-Batch.md`

Canonical materialization of the initial 23-UPKO registration records, including registration evidence, decisions, events, state, effective date, and traceability.

### 3. UPKR Current Registry State

`UPKR-REGISTRY-001_v1.1_23-UPKO-Initial-Registered-State.md`

Canonical current registry-state representation for the initial 23 registered UPKOs.

## Initial Registration State

The current initial batch contains:

```text
UPKO-001 … UPKO-023
Registration State = REGISTERED — 23/23
Effective Date    = 2026-08-16
```

The registration layer is supported by the applicable Registration Decisions and Registration Events and is governed by the canonical UPKR architecture.

## Authority Boundary

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

## Archive

Historical baselines, superseded working artifacts, materialization notices, and supporting governance artifacts that are no longer part of the active UPKR document set are preserved under:

`/99_Archive/UPKR`

The archive preserves version lineage and traceability; archived artifacts are not treated as the active current-state representation.

## Versioning and Canonicality

The active documents above are governed artifacts. The presence of historical versions in `99_Archive/UPKR` does not alter their historical identity or lineage.

Substantive changes to locked canonical documents shall proceed through the applicable controlled revision and governance process.

## Canonicalization

The initial 23-UPKO registration batch was canonicalized through the governed act:

`UPKR-CD-001 — APPROVE CANONICALIZATION`

with effective date:

`2026-08-16`

## Directory Boundary

`20_UPKR` contains the active UPKR registry-layer documents and this README. Historical or superseded artifacts belong in the archive layer and should not be used as current authoritative replacements without explicit governance.

---

**Repository:** `BillyProject2505/KnowledgeOS`  
**Path:** `00_System/40_Registries/20_UPKR/`
