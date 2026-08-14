# Universal Naming & Identification Registry (UNIR)

**Document ID:** UNIR-CORE-001  
**Document Type:** Universal Registry Architecture  
**Version:** 1.2  
**Status:** LOCKED — CANONICAL  
**Previous Version:** 1.1  
**Canonical Scope:** Universal Naming & Identification Registry (UNIR)  
**Normative Relationship:** Operates within the normative authority established by UNIS

---

## Canonical Lock Record

UNIR-CORE-001 v1.2 is canonically locked as the current canonical revision of UNIR-CORE-001.

This revision incorporates the materialized `DIUA` Namespace registration state into the canonical `UNIR-NSM` domain while preserving the existing six-Core architecture and the explicit boundary that DIUA is not a separate UNIR Registry Object by default.

## Canonical DIUA Namespace State

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

## Canonical Six-Core Architecture

The six canonical UNIR Core semantic domains remain unchanged:

| Core | Canonical Ownership |
|---|---|
| UNIR-SCH | Registry Object structure |
| UNIR-OCM | Registry Object classification |
| UNIR-IDM | Registry Object identity |
| UNIR-NSM | Namespace semantics |
| UNIR-LSM | Registry lifecycle and state |
| UNIR-GRP | Governance and registration |

No additional UNIR Core is established by this revision.

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

## Registry Boundary

UNIS remains the normative Naming & Identification authority. UNIR provides registry representation, registration governance, lifecycle/state, and operational mechanisms within that authority.

The DIUA Namespace state is owned operationally by `UNIR-NSM` and authorized through `UNIR-GRP`. DIUA does not receive a Registry Object ID through this registration.

## Historical Integrity

UNIR-CORE-001 v1.1 remains the previous canonical version and is preserved as historical material. It is not rewritten retroactively.

This v1.2 revision supersedes v1.1 as the current canonical UNIR-CORE-001 release.

## Change Control

Future substantive changes to UNIR Core semantics, Namespace state rules, or the DIUA registration state require controlled change, impact assessment, traceability, audit, and a new explicit canonical lock.

## Status

**Canonical Status:** LOCKED — CANONICAL

**Current Version:** 1.2

**Previous Version:** 1.1
