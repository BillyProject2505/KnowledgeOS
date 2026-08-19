# AI-Native Production System

## Purpose

This directory is the dedicated home for the new AI-Native Production System research and construction trajectory.

It is intentionally separated from the existing `00_System` architecture and governance corpus so that the new project can be researched and constructed from a clean methodological baseline while preserving the historical repository corpus unchanged.

## Boundary

The artifacts in this directory do not automatically inherit architectural or normative authority from legacy documents elsewhere in the repository.

Existing repository documents may be used as reference, evidence, historical material, or lessons learned only according to the new project's research and adoption process.

## Initial Reference

### Foundation

- `foundation/UAICP-FC-001-foundational-concept-and-north-star_v1.0.md` — foundational concept and project North Star.

### Construction Governance

- `governance/UAICP-RCC-001-project-research-and-construction-charter_v1.0.md` — governs how the new trajectory is researched and constructed, including anti-loop and anti-bootstrap safeguards.
- `governance/UAICP-ADM-001-architecture-decision-model-v1.0.md` — governs the controlled transition from Architecture Decision Basis to Architecture Decision; it is not a final system governance artifact and is not a numbered Step 11.

### Research Sequence

The root-level research and construction methodology currently contains the following sequence:

1. `UAICP-FC-001` — Foundational Concept & North Star
2. `UAICP-RCC-001` — Project Research & Construction Charter
3. `UAICP-REF-001` — Research & Evidence Framework
4. `UAICP-RQU-001` — Research Questions & Unknowns Framework
5. `UAICP-POM-001` — Problem & Objective Discovery Model
6. `UAICP-CED-001` — Concept & Entity Discovery Model
7. `UAICP-BRD-001` — Boundary & Responsibility Discovery Model
8. `UAICP-RDD-001` — Relationship & Dependency Discovery Model
9. `UAICP-DCA-001` — Dependency Analysis & Circularity Assessment Model
10. `UAICP-ARD-001` — Architecture Discovery Model

### Current Filenames

The repository currently uses explicit version suffixes in the filenames of the published methodology artifacts:

```text
UAICP-FC-001-foundational-concept-and-north-star_v1.0.md
UAICP-RCC-001-project-research-and-construction-charter_v1.0.md
UAICP-REF-001-research-and-evidence-framework_v1.0.md
UAICP-RQU-001-research-questions-and-unknowns-framework_v1.0.md
UAICP-POM-001-problem-and-objective-discovery-model_v1.0.md
UAICP-CED-001-concept-and-entity-discovery-model_v1.1.md
UAICP-BRD-001-boundary-and-responsibility-discovery-model_v1.0.md
UAICP-RDD-001-relationship-and-dependency-discovery-model_v1.0.md
UAICP-DCA-001-dependency-analysis-and-circularity-assessment-model_v1.2.md
UAICP-ARD-001-architecture-discovery-model_v1.1.md
UAICP-ADM-001-architecture-decision-model-v1.0.md
```

### Publication Status

Steps 1–10 are currently published in the repository.

`UAICP-ADM-001` is also published as a root-level architecture decision transition mechanism.

Publication does not automatically establish canonicality. Each document remains subject to its own stated status, authority, lifecycle, and later decision process.

## Construction Sequence

The current research-and-construction sequence is:

```text
North Star
    ↓
Research & Construction Charter
    ↓
Research & Evidence
    ↓
Research Questions & Unknowns
    ↓
Problem & Objective Discovery
    ↓
Concept & Entity Discovery
    ↓
Boundary & Responsibility Discovery
    ↓
Relationship Discovery
    ↓
Dependency & Circularity Analysis
    ↓
Architecture Discovery
    ↓
Architecture Decision Basis
    ↓
Architecture Decision Model
    ↓
Architecture Decision / Formalization when justified
    ↓
Governance / Document / Operational Architecture as determined by discovery
    ↓
Implementation
    ↓
AI Production / Automation
```

This sequence is a working methodological map. It does not by itself make any later artifact canonical or determine that every step must become a separate final document.

The numbered research sequence ends at Step 10. `UAICP-ADM-001` is a transition mechanism, not a new numbered discovery step.

## Outcome-Driven Principle After Architecture Discovery

After Architecture Discovery, the workflow becomes outcome-driven rather than document-count-driven.

```text
Architecture Discovery
        ↓
Architecture Decision Basis
        ↓
Architecture Decision Model
        ↓
Decision Eligibility
        ├── Evidence insufficient
        │       ↓
        │   Further research / discovery
        │
        └── Evidence sufficient
                ↓
        Architecture Decision
                ↓
        Approved / Rejected / Deferred / Return-to-Research / Return-to-Architecture-Discovery
```

No numbered Step 11 is predetermined merely to continue the numbering. Any subsequent artifact must be justified by the resulting decision and applicable discovery.

## Anti-Loop / Anti-Bootstrap Principle

The project shall establish its own research, boundary, architecture, governance, and implementation decisions through a controlled sequence.

The project shall not:

- derive semantic architecture from repository structure;
- inherit legacy architecture merely because it already exists;
- create documents only to reduce or increase file count;
- convert unresolved questions into architecture by assumption;
- force a predetermined Universal-level document set before architecture discovery justifies it;
- or allow implementation constraints to silently define unresolved semantics.

Legacy repository content is not automatically canonical for the new trajectory.

## Scope Principle

Steps 1–10 are root-level methodology artifacts. `UAICP-ADM-001` is a root-level architecture decision transition artifact. These artifacts are not automatically part of the Universal architectural layer.

The term `Universal` is reserved for artifacts whose architectural or knowledge scope is actually determined to be Universal through the research, discovery, and decision process.

Therefore, root-level methodology and transition artifacts do not use `Universal` merely because the overall initiative may later produce Universal-scope artifacts.
