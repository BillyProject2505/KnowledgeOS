# Research

## Purpose

This directory contains the research-control and substantive discovery artifacts for the new project trajectory.

## Root-Level Methodology Sequence

The current root-level research and construction methodology is:

```text
Step 1 — Foundational Concept / North Star
        ↓
Step 2 — Research & Construction Charter
        ↓
Step 3 — Research & Evidence
        ↓
Step 4 — Research Questions & Unknowns
        ↓
Step 5 — Project Problem & Objective Discovery
        ↓
Step 6 — Project Concept & Entity Discovery
        ↓
Step 7 — Project Boundary & Responsibility Discovery
        ↓
Step 8 — Project Relationship & Dependency Discovery
        ↓
Step 9 — Dependency Analysis & Circularity Assessment
        ↓
Step 10 — Architecture Discovery
```

This is a **root-level discovery and construction workflow**, not a pre-declared list of final system documents.

## File Index

| Step | Document ID | File | Purpose |
|---|---|---|---|
| 1 | `UAICP-FC-001` | `foundation/UAICP-FC-001-foundational-concept-and-north-star.md` | Foundational concept and North Star |
| 2 | `UAICP-RCC-001` | `governance/UAICP-RCC-001-project-research-and-construction-charter.md` | Research and construction control |
| 3 | `UAICP-REF-001` | `UAICP-REF-001-research-and-evidence-framework.md` | Evidence and research discipline |
| 4 | `UAICP-RQU-001` | `UAICP-RQU-001-research-questions-and-unknowns-framework.md` | Research questions and unresolved unknowns |
| 5 | `UAICP-POM-001` | `UAICP-POM-001-project-problem-and-objective-discovery-model.md` | Problem and objective discovery |
| 6 | `UAICP-CED-001` | `UAICP-CED-001-project-concept-and-entity-discovery-model_v1.1.md` | Concept and entity discovery |
| 7 | `UAICP-BRD-001` | `UAICP-BRD-001-project-boundary-and-responsibility-discovery-model.md` | Boundary and responsibility discovery |
| 8 | `UAICP-RDD-001` | `UAICP-RDD-001-project-relationship-and-dependency-discovery-model.md` | Relationship and candidate-dependency discovery |
| 9 | `UAICP-DCA-001` | `UAICP-DCA-001-dependency-analysis-and-circularity-assessment-model.md` | Dependency and circularity assessment |
| 10 | `UAICP-ARD-001` | `UAICP-ARD-001-architecture-discovery-model.md` | Architecture discovery and Architecture Decision Basis |

## Publication State

Steps 1–10 are now published in the repository.

Publication does not automatically establish canonicality. Each document remains subject to its own stated status, authority, lifecycle, and later decision process.

## Workflow Principle

The sequence is a discovery workflow, not a list of final architecture or governance documents.

The workflow deliberately avoids deciding in advance that the project must contain documents such as Universal Architecture, Universal Governance, Universal Registry, or Universal Standards.

Those artifacts may emerge later only when sufficiently mature research and architecture discovery establish that they are required.

After Step 10, the workflow becomes outcome-driven:

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

No Step 11 is predetermined merely to continue the numbering.

## Scope Principle

Steps 1–10 are **root-level methodology artifacts**. They are not automatically part of the Universal architectural layer.

The word **Universal** is reserved for artifacts whose architectural or knowledge scope has actually been established as Universal through the research, discovery, and decision process.

## Boundary

Research artifacts are not automatically normative architecture.

Research outputs may contain:

- evidence;
- findings;
- hypotheses;
- candidate concepts;
- unresolved questions;
- provisional relationships;
- candidate dependencies;
- architectural hypotheses; and
- decision candidates.

Their maturity and authority must be resolved through the project methodology before they become architectural or normative inputs.

## Anti-Loop / Anti-Bootstrap Principle

Research should discover the system rather than justify a structure chosen in advance.

```text
Evidence
→ Finding
→ Problem / Objective
→ Concept / Boundary
→ Relationship / Dependency
→ Architecture Discovery
→ Architecture Decision Basis
→ Architecture Decision
```

not:

```text
Existing Architecture
→ Justification
→ Research
```

## Step 9 Boundary

`UAICP-DCA-001` assesses candidate dependencies, dependency direction, transitivity, circularity, foundational dependency risk, and bootstrap risk. It does not itself establish final architecture or normative dependency policy.

## Step 10 Boundary

`UAICP-ARD-001` discovers and assesses candidate architectures, alternatives, architectural drivers, concerns, capability requirements, constraints, assumptions, risks, sensitivities, trade-offs, and traceability. It produces an **Architecture Decision Basis** rather than an automatically approved architecture.

## Reading Rule

AI and human readers should use this README as the navigation and orientation layer for the root-level research methodology. The substantive and normative meaning of each artifact must be resolved from the artifact itself and its applicable authority and lifecycle state.
