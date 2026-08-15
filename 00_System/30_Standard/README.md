# Universal Standards

## Purpose

This directory contains canonical Universal Standards that define normative rules, boundaries, and reusable requirements for the Universal system.

It is a **standards layer**, not a registry, operational workspace, project-specific documentation area, or general archive.

## Authority Boundary

Documents stored here are normative Standard artifacts within their stated scope.

A Standard may define:

- universal principles and requirements;
- authority and scope boundaries;
- semantic and structural rules;
- conformance requirements;
- interfaces and dependencies with other Universal layers.

A Standard does not acquire authority over matters explicitly owned by another canonical layer merely because it references or constrains them.

Operational registry state, allocation records, registration records, and other implementation state belong to the applicable Registry rather than to the Standard itself.

## Canonical Standards

### UNIS-CORE-001 — Universal Naming and Identification Standard

**Version:** 1.7  
**Status:** LOCKED — CANONICAL  
**Authority:** Universal Naming and Identification Standard (UNIS)

Defines the foundational Universal architecture and normative rules for naming and identification, including identity, identifiers, namespaces, qualification, reference, resolution, allocation, uniqueness, persistence, and related identification concerns.

The current canonical Document Identifier Grammar is:

```text
<Namespace>-DIC-<6DigitSequence>
```

The `DIC` marker is reserved for Document identifiers. Namespace allocation remains governed separately under the applicable identification architecture.

### UDS-CORE-001 — Universal Document System

**Document ID:** `UDS-CORE-MASTER-001`  
**Version:** 1.5  
**Status:** CURRENT CANONICAL MASTER — LOCKED  
**Concrete Document Identifier:** `DIUA-DIC-000004`

Defines the Universal Document System architecture and governance for authoritative documents and their associated knowledge, metadata, relationships, provenance, lifecycle, authority, canonicality, representation, and machine consumption.

UDS operates within the foundational naming and identification authority of UNIS. The concrete Document Identifier `DIUA-DIC-000004` is allocated through the applicable Universal Identifier Architecture and represented in UNIR; this identifier allocation does not transfer UDS semantic authority to UNIS or UNIR.

The canonical UDS document is:

```text
UDS-CORE-001_Universal_Document_System_v1.5.md
```

## Document Governance

Documents in this directory shall:

1. use the applicable Universal Document System requirements;
2. maintain explicit identity, version, status, scope, and authority boundaries;
3. preserve distinction between document identity, title, representation, filename, and storage location;
4. use UNIS-governed identification where applicable;
5. preserve canonical and historical versions without silently rewriting historical artifacts;
6. keep normative Standard content separate from operational Registry state.

## Navigation

- [`UNIS-CORE-001_Universal_Naming_Identification_Standard_v1.7.md`](./UNIS-CORE-001_Universal_Naming_Identification_Standard_v1.7.md) — current canonical Universal Naming and Identification Standard.
- [`UDS-CORE-001_Universal_Document_System_v1.5.md`](./UDS-CORE-001_Universal_Document_System_v1.5.md) — current canonical Universal Document System.

## Directory Boundary

This README is a **folder-level navigation and orientation artifact**. It does not itself constitute a Universal Standard and does not override the authority of any canonical Standard document stored in this directory.

The directory may contain additional canonical Standards as they are formally materialized and published. Each such document remains authoritative only within its declared scope and status.
