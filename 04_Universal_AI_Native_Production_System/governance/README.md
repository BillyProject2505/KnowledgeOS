# Governance

## Purpose

This directory contains the root-level methodological governance artifacts that control **how the new project is researched, discovered, assessed, and constructed**.

## File Index

The following files are the current root-level methodology artifacts associated with this construction trajectory:

| Step | Document ID | File | Role |
|---|---|---|---|
| 1 | `UAICP-FC-001` | [Foundational Concept & North Star](../foundation/UAICP-FC-001-foundational-concept-and-north-star.md) | Foundational intent and North Star |
| 2 | `UAICP-RCC-001` | `UAICP-RCC-001-project-research-and-construction-charter.md` | Research and construction governance |
| 3 | `UAICP-REF-001` | `UAICP-REF-001-research-and-evidence-framework.md` | Evidence and research control |
| 4 | `UAICP-RQU-001` | `UAICP-RQU-001-research-questions-and-unknowns.md` | Research questions and unknowns |
| 5 | `UAICP-POM-001` | `UAICP-POM-001-project-problem-and-objective-discovery-model.md` | Problem and objective discovery |
| 6 | `UAICP-CED-001` | `UAICP-CED-001-project-concept-and-entity-discovery-model.md` | Concept and entity discovery |
| 7 | `UAICP-BRD-001` | `UAICP-BRD-001-project-boundary-and-responsibility-discovery-model.md` | Boundary and responsibility discovery |
| 8 | `UAICP-RDD-001` | `UAICP-RDD-001-project-relationship-and-dependency-discovery-model.md` | Relationship and candidate-dependency discovery |
| 9 | `UAICP-DCA-001` | `UAICP-DCA-001-dependency-analysis-and-circularity-assessment-model.md` | Dependency and circularity assessment |
| 10 | `UAICP-ARD-001` | `UAICP-ARD-001-architecture-discovery-model.md` | Architecture discovery |

The file names in this index reflect the current root-level naming convention. Steps 5–8 use the normalized filenames without the `Universal` prefix.

## Primary Governance Document

`UAICP-RCC-001-project-research-and-construction-charter.md`

This document establishes the research and construction method, sequencing principles, anti-loop safeguards, anti-bootstrap controls, dependency discipline, legacy treatment, and phase/gate philosophy.

## Boundary

Governance artifacts in this directory govern the **construction process** of the new trajectory.

They do not automatically define the substantive governance model of the eventual Universal system.

## Construction Governance vs Final System Governance

```text
Construction Governance
    ≠
Final System Governance
```

Construction governance answers **how we build the system safely**.

Final system governance will be discovered and defined later, after the substantive architecture is sufficiently understood and an appropriate architecture decision has been made.

## Scope Principle

Steps 1–10 are **root-level methodology artifacts**. They are not automatically part of the Universal architectural layer.

The word **Universal** is reserved for artifacts whose architectural or knowledge scope has been established as Universal through the research, discovery, and decision process.

## Workflow Boundary After Step 10

Step 10 produces an **Architecture Decision Basis**, not an automatically approved architecture and not a predetermined Step 11.

```text
Architecture Discovery
        ↓
Architecture Decision Basis
        ↓
Decision Point
        ├── Evidence insufficient
        │       ↓
        │   Further research / discovery
        │
        └── Evidence sufficient
                ↓
        Architecture Decision
                ↓
        Approved Architecture / Architecture Description
```

The workflow therefore remains outcome-driven rather than document-count-driven.

## Reading Rule

AI and human readers should treat the files indexed here as methodological governance and research-control artifacts. Normative rules for the eventual system must be resolved from the appropriate later authoritative artifacts.

No file in this directory should be interpreted as establishing the final Universal architecture, final system governance, registry model, document architecture, or implementation merely because it appears in this index.
