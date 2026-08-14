# Universal Naming & Identification Registry (UNIR)

**Document ID:** UNIR-CORE-001  
**Document Type:** Universal Registry Architecture  
**Version:** 1.2 (Controlled Revision)  
**Status:** CONTROLLED REVISION — NOT YET CANONICAL  
**Previous Version:** 1.1  
**Canonical Scope:** Universal Naming & Identification Registry (UNIR)  
**Normative Relationship:** Operates within the normative authority established by UNIS

---

## Revision Purpose

This controlled revision incorporates the materialized `DIUA` Namespace registration state into the canonical `UNIR-NSM` domain while preserving the existing six-Core architecture and the explicit boundary that DIUA is not a separate UNIR Registry Object by default.

This revision does not alter the authority of UNIS, does not create an additional UNIR Core, and does not allocate any individual Document Identifier.

---

## DIUA Namespace Registration State

The following Namespace state is proposed for incorporation into `UNIR-NSM`:

**Namespace Literal:** `DIUA`  
**Canonical Name:** Document Identifier Universal Architecture  
**Namespace Scope:** Universal Document Identifier Architecture  
**Governing Architecture:** Universal Identifier Architecture (UIA) under UNIS  
**Applicable Identifier Class:** Document  
**Identifier Class Marker:** `DIC`  
**Applicable Identifier Grammar:** `DIUA-DIC-<6DigitSequence>`  
**Namespace State:** REGISTERED — ACTIVE  
**Registry Object:** NONE

### Authority

**Normative Authority:** UNIS  
**Namespace Semantics Authority:** UNIR-NSM  
**Registration Governance:** UNIR-GRP

### Integrity

- Namespace selection: APPROVED
- Collision / uniqueness audit: PASS
- Scope audit: PASS
- Authority audit: PASS
- Identifier Class binding: DIC
- Grammar binding: `DIUA-DIC-<6DigitSequence>`
- Separate Registry Object eligibility: DEFERRED / NONE

### Allocation Boundary

The allocation of Namespace `DIUA` does not allocate any individual Document Identifier.

```text
DIUA
  = Namespace

DIC
  = Document Identifier Class Marker

DIUA-DIC-<6DigitSequence>
  = Identifier Grammar

DIUA-DIC-000001
  = future individual Document Identifier allocation
```

No individual Document Identifier is allocated by this revision.

---

## DIUA Boundary

DIUA remains an architectural construct within the Universal Identifier Architecture (UIA).

It is not a UNIR Core, an Identifier Class, the Document Identifier Grammar itself, an individual Document Identifier, or a separate UNIR Registry Object by default.

```text
UNIS / UIA
    ↓
DIUA
    ├── governs → DIC
    └── governs → Document Identifier Grammar
                         ↓
                       UNIR
                         ↓
                Namespace state
```

---

## Change Control

This document is a controlled revision of `UNIR-CORE-001 v1.1`. The existing v1.1 artifact remains immutable and canonical until this revision completes review, impact assessment, audit, and an explicit canonical lock.

No current canonical authority is transferred by this revision.

---

## Lock Readiness

The following gates are required before canonicalization:

- Six-Core architecture preserved
- UNIS authority boundary preserved
- UNIR-NSM ownership preserved
- UNIR-GRP registration governance preserved
- DIUA Registry Object eligibility remains deferred
- No individual Document Identifier allocated
- Historical traceability preserved

**Current Status:** LOCK-READINESS PENDING
