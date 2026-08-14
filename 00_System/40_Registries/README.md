# Registries

## Purpose

This directory contains the canonical registry architecture and registry specifications for the Knowledge Operating System (KOS).

Registries provide controlled operational representations of governed objects, identities, namespaces, relationships, lifecycle/state, and registration metadata. Registry documents do not replace the normative standards that define the semantics they operationalize.

---

## Canonical Registry Architecture

### Universal Naming & Identification Registry (UNIR)

**Document ID:** `UNIR-CORE-001`  
**Current Version:** `1.1`  
**Status:** `LOCKED — CANONICAL`

UNIR is the canonical registry architecture for Universal Naming & Identification. It operates within the normative authority established by UNIS and provides the registry machinery required for registration, identity, namespace, lifecycle/state, and governance operations.

UNIR Core v1.1 is consolidated into a single canonical publication containing six distinct semantic ownership domains:

- **UNIR-SCH** — Registry Object structure
- **UNIR-OCM** — Registry Object classification
- **UNIR-IDM** — Registry Object identity
- **UNIR-NSM** — Namespace semantics
- **UNIR-LSM** — Registry lifecycle and state
- **UNIR-GRP** — Governance and registration

The six Core domains retain separate semantic ownership even though they are published as one canonical document.

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
- Registries represent governed objects and operational state; they do not silently redefine normative semantics.
- Registry identifiers must be unique within their applicable identity scope.
- Registry object identity, classification, namespace, lifecycle/state, and governance concerns must remain within their defined ownership boundaries.
- Historical versions and superseded releases must remain traceable and must not be silently overwritten.
- New registry constructs require explicit registration and eligibility decisions; names appearing in normative standards do not automatically become separate Registry Objects.

---

## Current Canonical Registry

| Document | Version | Status | Scope |
|---|---:|---|---|
| `UNIR-CORE-001.md` | 1.1 | LOCKED — CANONICAL | Universal Naming & Identification Registry |

Additional registry specifications may be introduced only through the applicable architecture, governance, and registration processes.
