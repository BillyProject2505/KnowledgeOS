# Universal Naming & Identification Registry — Namespace Registry

**Registry Document ID:** UNIR-NSM-REGISTRY  
**Registry Domain:** UNIR-NSM  
**Governing Registry Architecture:** UNIR-CORE-001 v1.1  
**Governing Standard:** UNIS-CORE-001 v1.7  
**Status:** ACTIVE — CANONICAL REGISTRY STATE  

## 1. Purpose

This document materializes the operational Namespace registration state governed by UNIR-NSM and authorized through UNIR-GRP.

It is an instance registry-state artifact. It does not redefine Namespace semantics established by UNIS or UNIR-NSM and does not create Registry Object identities for namespaces unless applicable registration-eligibility rules explicitly require them.

## 2. Namespace Record: DIUA

**Namespace Literal:** `DIUA`  
**Canonical Name:** Document Identifier Universal Architecture  
**Namespace Scope:** Universal Document Identifier Architecture  
**Governing Architecture:** Universal Identifier Architecture (UIA) under UNIS  
**Applicable Identifier Class:** Document  
**Identifier Class Marker:** `DIC`  
**Applicable Identifier Grammar:** `DIUA-DIC-<6DigitSequence>`  
**Namespace State:** REGISTERED — ACTIVE  
**Registry Object:** NONE  

### 2.1 Authority

**Normative Authority:** UNIS  
**Namespace Semantics Authority:** UNIR-NSM  
**Registration Governance:** UNIR-GRP  

### 2.2 Integrity

- Namespace selection: APPROVED
- Collision / uniqueness audit: PASS
- Scope audit: PASS
- Authority audit: PASS
- Identifier Class binding: DIC
- Grammar binding: `DIUA-DIC-<6DigitSequence>`
- Separate Registry Object eligibility: DEFERRED / NONE

### 2.3 Allocation Boundary

The allocation of Namespace `DIUA` does not allocate any individual Document Identifier.

Accordingly:

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

No individual Document Identifier is allocated by this registry record.

## 3. Registry Object Boundary

DIUA is an architectural construct within UIA and is not assigned a separate UNIR Registry Object identity by this record.

This preserves the canonical UNIR boundary under which a governed construct does not automatically become a Registry Object merely because it is represented operationally in a registry.

## 4. Canonical Relationship

```text
UNIS / UIA
    ↓
DIUA
    ├── governs → DIC
    └── governs → Document Identifier Grammar
                         ↓
                       UNIR
                         ↓
                 Namespace Registry State
```

## 5. Change Control

Any change to the DIUA Namespace state requires the applicable UNIR-NSM and UNIR-GRP governance and change-control process. Historical states shall remain traceable and shall not be silently overwritten.

## 6. Governing References

- `UNIS-CORE-001 v1.7` — Universal Naming and Identification Standard
- `UNIR-CORE-001 v1.1` — Universal Naming & Identification Registry
- `UNIR-NSM` — Namespace semantics ownership
- `UNIR-GRP` — Registration governance ownership

## 7. Canonicality

This document is the operational Namespace Registry State for `DIUA` under the canonical UNIR architecture. It does not amend or supersede `UNIR-CORE-001` or `UNIS-CORE-001`.
