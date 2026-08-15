# 30_Bibles

## Purpose

This directory contains canonical **Production Bible** documents within the KnowledgeOS knowledge layer.

Production Bibles define governed production knowledge architectures, principles, boundaries, responsibilities, and related canonical production rules.

## Canonical Document

The current canonical Production Bible in this directory is:

| Document | Role | Status |
|---|---|---|
| [UPB-CORE-001 — Universal Production Bible v2.1](./UPB-CORE-001_Universal_Production_Bible_v2.1.md) | Universal Production Knowledge authority | **CANONICALLY LOCKED** |

## Universal Production Bible

**Document ID:** `UPB-001`  
**Title:** Universal Production Bible  
**Current Version:** `v2.1`  
**Canonical Form:** Single-file Markdown document  
**Document System:** UDS  
**Naming & Identification:** UNIS  
**Canonical Materialized Boundary:** Chapters 01–09  
**Architectural Baseline:** 20-chapter V2 baseline

The current UPB materializes Chapters 01–09. Chapters 10–20 remain part of the broader architectural baseline but are **not materialized** because their canonical responsibilities have not been sufficiently recovered from available evidence.

## Reading Priority for AI

When this directory is used as a repository source, AI systems should:

1. identify the canonical document listed above;
2. retrieve the current version of that document;
3. use the document's own metadata and Document Contract as the primary documentary interpretation layer;
4. treat the UPB chapter responsibility index and canonical chapter content as authoritative for Universal Production Knowledge;
5. preserve explicit deferred, pending, unresolved, and controlled states;
6. never infer canonical responsibility from filename, repository position, or chapter numbering alone.

## Canonical Boundaries

```text
UDS
→ Documentary / Document-System Authority

UNIS
→ Naming & Identification Authority

UPB
→ Universal Production Knowledge Authority
```

The folder README is a **navigation and discovery document**. It does not redefine the substantive canonical production knowledge owned by UPB.

## File Naming

Canonical Production Bible representations in this directory follow the applicable repository naming rules governed by UNIS.

The current canonical UPB representation is:

```text
UPB-CORE-001_Universal_Production_Bible_v2.1.md
```

Filename is a representation-level naming artifact and is not, by itself, the persistent document identity.

## Superseded Documents

Superseded Production Bible versions should not remain alongside the current canonical version as competing active documents. They should be removed from the canonical folder or moved to an explicitly governed archive location when archival retention is required.
