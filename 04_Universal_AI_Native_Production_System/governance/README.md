# Governance

## Purpose

This directory contains the root-level methodological governance and decision-control artifacts that control **how the new project is researched, discovered, assessed, decided, and constructed**.

## File Index

| Step / Function | Document ID | File | Role | State |
|---|---|---|---|---|
| 1 | `UAICP-FC-001` | `../foundation/UAICP-FC-001-foundational-concept-and-north-star_v1.0.md` | Foundational intent and North Star | Published |
| 2 | `UAICP-RCC-001` | `UAICP-RCC-001-project-research-and-construction-charter_v1.0.md` | Research and construction governance | Published |
| 3 | `UAICP-REF-001` | `../research/UAICP-REF-001-research-and-evidence-framework_v1.0.md` | Evidence and research control | Published |
| 4 | `UAICP-RQU-001` | `../research/UAICP-RQU-001-research-questions-and-unknowns-framework_v1.0.md` | Research questions and unknowns | Published |
| 5 | `UAICP-POM-001` | `../research/UAICP-POM-001-problem-and-objective-discovery-model_v1.0.md` | Problem and objective discovery | Published |
| 6 | `UAICP-CED-001` | `../research/UAICP-CED-001-concept-and-entity-discovery-model_v1.1.md` | Concept and entity discovery | Published |
| 7 | `UAICP-BRD-001` | `../research/UAICP-BRD-001-boundary-and-responsibility-discovery-model_v1.0.md` | Boundary and responsibility discovery | Published |
| 8 | `UAICP-RDD-001` | `../research/UAICP-RDD-001-relationship-and-dependency-discovery-model_v1.0.md` | Relationship and candidate-dependency discovery | Published |
| 9 | `UAICP-DCA-001` | `../research/UAICP-DCA-001-dependency-analysis-and-circularity-assessment-model_v1.2.md` | Dependency and circularity assessment | Published |
| 10 | `UAICP-ARD-001` | `../research/UAICP-ARD-001-architecture-discovery-model_v1.1.md` | Architecture discovery and Architecture Decision Basis | Published |
| Transition | `UAICP-ADM-001` | `UAICP-ADM-001-architecture-decision-model-v1.0.md` | Controlled transition from Architecture Decision Basis to Architecture Decision | Published |

Filenames in this index reflect the current repository naming convention, including explicit version suffixes. Root-level methodology filenames do not use a `Universal` prefix merely because the broader initiative may later contain Universal-scope artifacts.

## Primary Construction Governance

`UAICP-RCC-001-project-research-and-construction-charter_v1.0.md`

This document establishes the research and construction method, sequencing principles, anti-loop safeguards, anti-bootstrap controls, dependency discipline, legacy treatment, and phase/gate philosophy.

## Architecture Decision Transition

`UAICP-ADM-001` is a **root-level transition mechanism**, not a final system governance artifact.

It governs the controlled transition from an Architecture Decision Basis to an Architecture Decision. It does not define the architecture itself, create decision authority, or establish final Universal Governance.

```text
Architecture Discovery
        ↓
Architecture Decision Basis
        ↓
Decision Eligibility
        ↓
Architecture Decision
```

## Boundary

Governance artifacts in this directory govern the **construction and architecture-decision process** of the new trajectory. They do not automatically define the substantive governance model of the eventual Universal system.

## Scope Principle

Steps 1–10 are **root-level methodology artifacts**. `UAICP-ADM-001` is a root-level transition artifact associated with the architecture decision boundary. None of these artifacts is automatically part of the Universal architectural layer.

## Workflow Boundary After Step 10

Step 10 produces an **Architecture Decision Basis**, not an automatically approved architecture and not a predetermined Step 11. The workflow remains outcome-driven rather than document-count-driven.

## Reading Rule

AI and human readers should treat the files indexed here as methodological governance and decision-control artifacts. Normative rules for the eventual system must be resolved from the appropriate later authoritative artifacts.
