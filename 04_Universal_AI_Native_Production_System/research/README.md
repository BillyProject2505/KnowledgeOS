# Research

## Purpose

This directory contains the research-control and substantive discovery artifacts for the new Universal AI-Native Production System trajectory.

## Current Research Sequence

```text
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
Relationship & Dependency Discovery
        ↓
Dependency Direction & Circularity Analysis
        ↓
Architecture Discovery
```

The sequence is a discovery workflow, not a pre-declared list of final system documents.

The eventual document architecture shall be discovered from sufficiently mature architecture, governance, and operational requirements.

## Current Artifacts

- `UAICP-REF-001-research-and-evidence-framework.md` — defines evidence handling, source treatment, research status, and validation discipline.
- `UAICP-RQU-001-research-questions-and-unknowns-framework.md` — controls material research questions and unresolved unknowns.
- `UAICP-POM-001-problem-and-objective-discovery-model.md` — discovers the actual problems and desired outcomes the system must address.
- `UAICP-CED-001-concept-and-entity-discovery-model_v1.1.md` — discovers and distinguishes candidate concepts and entities without prematurely turning them into architecture.
- `UAICP-BRD-001-boundary-and-responsibility-discovery-model.md` — discovers semantic boundaries and responsibilities without treating them as architecture layers.
- `UAICP-RDD-001-relationship-and-dependency-discovery-model.md` — discovers and differentiates relationships and candidate dependencies before formal circularity analysis.

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
- and decision candidates.

Their maturity and authority must be resolved through the project methodology before they become architectural or normative inputs.

## Anti-Loop Principle

Research should discover the system rather than justify a structure chosen in advance.

```text
Evidence
→ Finding
→ Problem / Objective
→ Concept / Boundary
→ Relationship / Dependency
→ Architecture
```

not:

```text
Existing Architecture
→ Justification
→ Research
```

## Step 8 Boundary

`UAICP-RDD-001` does not establish the final relationship graph or dependency graph. It distinguishes ordinary relationships from candidate dependencies, separates semantic dependencies from implementation dependencies, and records possible circularity for later Step 9 analysis.
