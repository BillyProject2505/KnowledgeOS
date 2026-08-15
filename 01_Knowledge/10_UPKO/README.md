# Universal Production Knowledge Object (UPKO)

## Purpose

This folder contains the canonical Universal Production Knowledge Object (UPKO) corpus and its normative taxonomy authority.

UPKO represents **canonical Production Knowledge Objects** within the Universal Production Knowledge Architecture.

## Canonical Artifacts

### 1. UPKO Canonical Normalized Master

[`UPKO-CORE-001_Universal_Production_Knowledge_Object_v1.0.md`](./UPKO-CORE-001_Universal_Production_Knowledge_Object_v1.0.md)

The canonical normalized master for the UPKO inventory. It records the 23-UPKO canonical mapping, classification domain, normalization rules, repository placement, and lock boundaries. fileciteturn19file0

### 2. UPKO Object Type Taxonomy

[`UPKO_Object_Type_Taxonomy_Canonical_v1.0.md`](./UPKO_Object_Type_Taxonomy_Canonical_v1.0.md)

The separate normative authority for UPKO Object Type values, definitions, assignment rules, governance, and future-extension rules. The master consumes this taxonomy rather than redefining it. fileciteturn19file0

## Canonical Inventory

The current canonical inventory contains **23 UPKOs**:

| # | UPKO | Domain | Object Type |
|---:|---|---|---|
| 01 | Production Philosophy | Foundation | Philosophy |
| 02 | AI-First Production Knowledge | Foundation | Philosophy |
| 03 | Brand Identity | Brand | Model |
| 04 | Brand Positioning | Brand | Model |
| 05 | Brand Principles | Brand | Principle |
| 06 | Audience Model | Audience | Model |
| 07 | Audience Classification | Audience | Classification |
| 08 | Strategic Objective | Strategic | Objective |
| 09 | Strategic Alignment | Strategic | Model |
| 10 | Content Type | Content | Classification |
| 11 | Editorial Voice | Editorial | Model |
| 12 | Editorial Tone | Editorial | Model |
| 13 | Writing Standards | Editorial | Standard |
| 14 | Inclusive Language Standards | Editorial | Standard |
| 15 | Call-to-Action Standards | Editorial | Standard |
| 16 | Health & Educational Writing Standards | Editorial | Standard |
| 17 | Canvas System | Visual | System |
| 18 | Layout System | Visual | System |
| 19 | Surface System | Visual | System |
| 20 | Typography System | Visual | System |
| 21 | Color System | Visual | System |
| 22 | Graphic Elements System | Visual | System |
| 23 | Imagery System | Visual | System |

## Canonical Classification Domain

```text
Foundation
Brand
Audience
Strategic
Content
Editorial
Visual
```

Domain and Object Type are orthogonal dimensions.

## Current UPKO Boundaries

UPKO owns the semantic knowledge-object layer, including its canonical knowledge, classification, and applicability information.

The following are governed by applicable higher-level authorities and are not independently redefined by the UPKO master:

- naming and identification grammar;
- document and representation governance;
- lifecycle/status authority;
- version grammar;
- traceability/provenance architecture;
- relationship ontology;
- registry governance.

In particular, the **Knowledge Object Identification Grammar belongs to the Universal Naming & Identification Standard (UNIS)** and is consumed by UPKO; it is not a UPKO-owned naming grammar.

## UPKO vs UPKR

UPKO and UPKR are separate canonical workstreams:

```text
UPKO
= Canonical Production Knowledge Objects

UPKR
= Universal Production Knowledge Registry
```

UPKR is a separate registry/governance artifact set. UPKR does not become part of the UPKO corpus, and the UPKO corpus does not absorb UPKR architecture.

## Repository Placement

```text
01_Knowledge/10_UPKO/
```

This is the current canonical repository placement for the UPKO knowledge corpus. Repository location is not UPKO identity.

## Status

**UPKO Corpus — Canonical Workstream**

**Current canonical inventory — 23/23**

**Object Type Taxonomy — CANONICAL / LOCKED**

**UPKR — Separate workstream**

## Maintenance Rule

Changes to Object Type semantics shall be made in the separate canonical Object Type Taxonomy authority and then reflected in the normalized master through controlled reconciliation and re-audit. fileciteturn19file0
