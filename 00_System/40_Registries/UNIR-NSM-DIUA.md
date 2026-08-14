# DIUA Namespace Registration State

**Namespace:** DIUA  
**Canonical Name:** Document Identifier Universal Architecture  
**Registry Domain:** UNIR-NSM  
**Registration Governance:** UNIR-GRP  
**Governing Standard:** UNIS-CORE-001 v1.7  
**Namespace Status:** REGISTERED — ACTIVE  
**Registry Object:** NONE  

## Purpose

This record materializes the operational Namespace state for **DIUA (Document Identifier Universal Architecture)** within the Universal Naming & Identification Registry (UNIR).

DIUA is an architectural construct within the Universal Identifier Architecture (UIA). It is not a UNIR Core, Identifier Class, Document Identifier Grammar itself, individual Document Identifier, or separate UNIR Registry Object by default.

## Namespace Definition

**Namespace Literal:** `DIUA`

**Meaning:** Document Identifier Universal Architecture

**Scope:** Universal Document Identifier Architecture

**Governing Architecture:** Universal Identifier Architecture (UIA) under UNIS

## Applicable Identifier Class

**Identifier Class:** Document

**Class Marker:** `DIC`

## Applicable Identifier Grammar

```text
DIUA-DIC-<6DigitSequence>
```

The Namespace allocation does not itself allocate any individual Document Identifier.

## Registry Boundary

This record is a Namespace registration/state record under **UNIR-NSM** and is authorized through **UNIR-GRP**.

It does **not** create a separate UNIR Registry Object identity for DIUA.

## Status and Integrity

- Namespace selection: APPROVED
- Collision / uniqueness audit: PASS
- Scope audit: PASS
- Authority audit: PASS
- Identifier Class binding: DIC
- Grammar binding: `DIUA-DIC-<6DigitSequence>`
- Registry Object for DIUA: DEFERRED / NONE
- Namespace state: REGISTERED — ACTIVE

## Canonical Boundary

```text
UNIS / UIA
    ↓
DIUA
    ├── governs → DIC
    └── governs → Document Identifier Grammar
                         ↓
                       UNIR
                         ↓
              DIUA Namespace State
```

## Governing References

- **UNIS-CORE-001 v1.7** — Universal Naming and Identification Standard
- **UNIR-CORE-001 v1.1** — Universal Naming & Identification Registry
- **UNIR-NSM** — Namespace semantics ownership
- **UNIR-GRP** — Registration governance ownership

## Canonicality

This record is the operational Namespace state for `DIUA` under the canonical UNIR architecture. Changes to the Namespace state require the applicable UNIR governance and change-control process.
