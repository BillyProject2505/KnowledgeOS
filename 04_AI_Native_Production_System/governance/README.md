# Governance

## Purpose

This directory contains the root-level methodological governance artifacts that control **how the new project is researched, discovered, assessed, decided, and constructed**.

## File Index

The following files are the current root-level methodology and decision-control artifacts associated with this construction trajectory:

| Step / Function | Document ID | File | Role | State |
|---|---|---|---|---|
| 1 | `UAICP-FC-001` | [Foundational Concept & North Star](../foundation/UAICP-FC-001-foundational-concept-and-north-star.md) | Foundational intent and North Star | Published |
| 2 | `UAICP-RCC-001` | `UAICP-RCC-001-project-research-and-construction-charter.md` | Research and construction governance | Published |
| 3 | `UAICP-REF-001` | `../research/UAICP-REF-001-research-and-evidence-framework.md` | Evidence and research control | Published |
| 4 | `UAICP-RQU-001` | `../research/UAICP-RQU-001-research-questions-and-unknowns-framework.md` | Research questions and unknowns | Published |
| 5 | `UAICP-POM-001` | `../research/UAICP-POM-001-project-problem-and-objective-discovery-model.md` | Problem and objective discovery | Published |
| 6 | `UAICP-CED-001` | `../research/UAICP-CED-001-project-concept-and-entity-discovery-model_v1.1.md` | Concept and entity discovery | Published |
| 7 | `UAICP-BRD-001` | `../research/UAICP-BRD-001-project-boundary-and-responsibility-discovery-model.md` | Boundary and responsibility discovery | Published |
| 8 | `UAICP-RDD-001` | `../research/UAICP-RDD-001-project-relationship-and-dependency-discovery-model.md` | Relationship and candidate-dependency discovery | Published |
| 9 | `UAICP-DCA-001` | `../research/UAICP-DCA-001-dependency-analysis-and-circularity-assessment-model.md` | Dependency and circularity assessment | Published |
| 10 | `UAICP-ARD-001` | `../research/UAICP-ARD-001-architecture-discovery-model.md` | Architecture discovery and Architecture Decision Basis | Published |
| Transition | `UAICP-ADM-001` | `UAICP-ADM-001-architecture-decision-model-v1.0.md` | Controlled transition from Architecture Decision Basis to Architecture Decision | Publication-ready / Not yet published |

The file names in this index reflect the current root-level naming convention. Steps 5–8 use normalized filenames without the `Universal` prefix.

## Primary Construction Governance

`UAICP-RCC-001-project-research-and-construction-charter.md`

This document establishes the research and construction method, sequencing principles, anti-loop safeguards, anti-bootstrap controls, dependency discipline, legacy treatment, and phase/gate philosophy.

## Architecture Decision Transition

`UAICP-ADM-001` is a **root-level transition mechanism**, not a final system governance artifact.

It governs the controlled transition from an Architecture Decision Basis to an Architecture Decision. It does not define the architecture itself, create decision authority, or establish final Universal Governance.

The intended transition is:

```text
Architecture Discovery
        ↓
Architecture Decision Basis
        ↓
Architecture Decision Model
        ↓
Architecture Decision
```

If legitimate decision authority is unavailable, an architecture decision cannot become `APPROVED` or `EFFECTIVE` through implicit authority.

## Boundary

Governance artifacts in this directory govern the **construction and architecture-decision process** of the new trajectory.

They do not automatically define the substantive governance model of the eventual Universal system.

## Construction Governance vs Final System Governance

```text
Construction Governance
    ≠
Final System Governance
```

Construction governance answers **how we build and decide the system safely**.

Final system governance will be discovered and defined later, after the substantive architecture is sufficiently understood and the applicable architecture decision has been made.

## Scope Principle

Steps 1–10 are **root-level methodology artifacts**. `UAICP-ADM-001` is a root-level transition artifact associated with the architecture decision boundary. None of these artifacts is automatically part of the Universal architectural layer.

The word **Universal** is reserved for artifacts whose architectural or knowledge scope has been established as Universal through the research, discovery, and decision process.

## Workflow Boundary After Step 10

Step 10 produces an **Architecture Decision Basis**, not an automatically approved architecture and not a predetermined Step 11.

`UAICP-ADM-001` provides the decision transition mechanism:

```text
Architecture Discovery
        ↓
Architecture Decision Basis
        ↓
Decision Eligibility
        ↓
Architecture Decision
        ↓
Approved / Rejected / Deferred / Return-to-Research / Return-to-Architecture-Discovery
```

The workflow remains outcome-driven rather than document-count-driven.

## Reading Rule

AI and human readers should treat the files indexed here as methodological governance and decision-control artifacts. Normative rules for the eventual system must be resolved from the appropriate later authoritative artifacts.

No file in this directory should be interpreted as establishing the final Universal architecture, final system governance, registry model, document architecture, or implementation merely because it appears in this index.
