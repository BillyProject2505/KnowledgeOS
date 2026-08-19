---
document_id: UAICP-BRD-001
document_type: Boundary & Responsibility Discovery Model
title: Universal Project Boundary & Responsibility Discovery Model
version: 1.0
status: ACTIVE
canonicality: REFERENCE
scope: Universal AI-Native Production System — New Research & Construction Trajectory
authority: Project Research Framework
audience:
  - human
  - AI
purpose: >
  Establish the discovery model for determining the semantic, functional,
  authority, scope, and responsibility boundaries among candidate concepts and
  entities identified during the preceding research stages, without prematurely
  converting those boundaries into architecture, governance, registry, or
  repository structures.
canonical_home: UAICP-BRD-001
supersedes: none
parent_context: UAICP-CED-001
methodological_dependencies:
  - UAICP-FC-001
  - UAICP-RCC-001
  - UAICP-REF-001
  - UAICP-RQU-001
  - UAICP-POM-001
  - UAICP-CED-001
---

# Universal Project Boundary & Responsibility Discovery Model

## 1. Purpose

This document defines the Step 7 research model for discovering where one
candidate concept, entity, activity, or responsibility ends and another begins.

Its purpose is to determine:

- what each candidate is responsible for;
- what it is not responsible for;
- where concepts overlap;
- where responsibilities should remain separate;
- where one candidate depends on another;
- which boundaries are semantic;
- which boundaries are contextual;
- and which boundaries may later justify distinct system components.

Step 7 is still a **discovery artifact**.

It does not define the final architecture.

---

# 2. Methodological Lineage

Step 7 depends on the research chain already established:

```text
STEP 1
UAICP-FC-001
Foundational Concept & North Star
        ↓
STEP 2
UAICP-RCC-001
Research & Construction Charter
        ↓
STEP 3
UAICP-REF-001
Research & Evidence Framework
        ↓
STEP 4
UAICP-RQU-001
Research Questions & Unknowns Framework
        ↓
STEP 5
UAICP-POM-001
Problem & Objective Discovery Model
        ↓
STEP 6
UAICP-CED-001
Concept & Entity Discovery Model
        ↓
STEP 7
UAICP-BRD-001
Boundary & Responsibility Discovery
        ↓
STEP 8
Relationship Discovery
        ↓
STEP 9
Dependency & Circularity Analysis
        ↓
Architecture Discovery
```

Step 6 asks:

> What concepts and entities may actually be required?

Step 7 asks:

> **What must each concept or entity be responsible for, and where must that
> responsibility stop?**

---

# 3. Boundary Discovery Principle

The project shall determine semantic and responsibility boundaries before
choosing architecture boundaries.

Preferred sequence:

```text
Concept / Entity
        ↓
Purpose
        ↓
Responsibility
        ↓
Scope
        ↓
Exclusions
        ↓
Boundary Conditions
        ↓
Overlap Analysis
        ↓
Relationship Discovery
        ↓
Architecture
```

Not:

```text
Architecture Layer
        ↓
Assign Responsibilities to It
```

---

# 4. What Is a Boundary?

A **Boundary** is a meaningful distinction that limits where a concept,
responsibility, authority, or applicability begins and ends.

A boundary may be:

- semantic;
- functional;
- scope-based;
- authority-based;
- lifecycle-based;
- contextual;
- temporal;
- documentary;
- operational;
- or implementation-related.

Not every boundary requires a separate component.

---

# 5. What Is Responsibility?

A **Responsibility** is a defined capability, duty, or semantic function that a
candidate concept or entity is expected to own, provide, or govern.

Responsibility is distinct from:

- implementation;
- workflow sequence;
- repository location;
- document placement;
- and individual ownership by a person.

A candidate may have a responsibility without needing a separate system module.

---

# 6. Boundary Types

Each material boundary should be classified where useful.

```text
B-S — Semantic Boundary
B-F — Functional Boundary
B-SC — Scope Boundary
B-A — Authority Boundary
B-L — Lifecycle Boundary
B-T — Temporal Boundary
B-C — Context Boundary
B-D — Documentary Boundary
B-O — Operational Boundary
B-I — Implementation Boundary
```

These are discovery categories, not final architecture layers.

---

# 7. Responsibility Contract

For each candidate, record:

```text
Candidate ID
Candidate Name
Purpose
Primary Responsibility
Secondary Responsibilities
Explicit Exclusions
Scope
Authority Context
Lifecycle Context
Inputs
Outputs
Consumers
Dependencies
Neighboring Candidates
Overlap Risks
Boundary Questions
Evidence
Research Status
Confidence
```

This contract is intended to expose responsibility overlap before it becomes
architectural duplication.

---

# 8. Responsibility Ownership Principle

Every material responsibility should eventually have a clear conceptual owner.

However:

> **One responsibility, one owner**

does not necessarily mean:

> **One responsibility, one document**

or:

> **One responsibility, one software module.**

The ownership decision is semantic first.

---

# 9. Responsibility Overlap

When two candidates appear to perform the same responsibility, investigate:

```text
Same Purpose?
Same Scope?
Same Authority?
Same Consumer?
Same Lifecycle?
Same Inputs?
Same Outputs?
Same Decision Rights?
```

Possible outcomes:

```text
Same Responsibility
Distinct but Related
One Is a Sub-Responsibility
One Is Contextual
One Is a Representation
Unresolved
```

The project should not split responsibilities merely to create more components.

It should not merge responsibilities merely to reduce file count.

---

# 10. Semantic Boundary vs Repository Boundary

A repository folder or file location is not itself a semantic boundary.

Conceptually:

```text
Semantic Boundary
        ↓
Documentary Representation
        ↓
Repository Structure
```

Therefore the project shall not infer:

```text
Different Folder = Different Concept
```

or:

```text
Same Folder = Same Concept
```

Repository structure is an implementation aid discovered later.

---

# 11. Authority Boundary

Authority boundaries determine:

> **Which candidate is entitled to decide or govern a particular matter?**

For each material boundary, investigate:

```text
Who Defines?
Who Decides?
Who Interprets?
Who Validates?
Who Changes?
Who Consumes?
```

These questions must remain separate from implementation ownership.

For example:

```text
Authority
≠
Repository Maintainer
≠
Document Author
≠
Implementation Owner
```

unless later evidence shows that these roles legitimately coincide.

---

# 12. Scope Boundary

Scope determines where a concept or rule applies.

Possible dimensions:

```text
Universal
Cross-Project
Project
Domain
Workflow
Output
Representation
Implementation
```

Scope classification is provisional.

A concept must not be promoted to Universal merely because it is useful in one
project.

---

# 13. Lifecycle Boundary

Two candidates may have different lifecycle responsibilities even when they are
closely related.

Investigate:

```text
What Changes?
Who Changes It?
What Triggers Change?
What History Must Persist?
What Constitutes a New Version?
What Constitutes a New Identity?
```

If their lifecycle rules materially differ, this may indicate a genuine boundary.

---

# 14. Temporal Boundary

Some distinctions exist because the meaning or applicability differs across time.

Examples of questions:

- Is a rule historically valid but no longer active?
- Is a decision valid only for a period?
- Can an output have multiple publication states over time?
- Can an authority relationship expire?

Temporal difference does not automatically imply separate entities.

---

# 15. Context Boundary

A concept may behave differently under different contexts.

Possible contexts:

```text
Project
Domain
Task
Audience
Channel
Production Stage
Lifecycle State
```

The project must distinguish:

```text
Different Context
        ≠
Different Concept
```

A single concept may legitimately operate across multiple contexts.

---

# 16. Boundary Test

For any proposed boundary, ask:

```text
1. Is the distinction semantically meaningful?
2. Is it supported by evidence?
3. Does it affect responsibility?
4. Does it affect authority?
5. Does it affect lifecycle?
6. Does it affect consumers?
7. Does collapsing the boundary create ambiguity?
8. Does separating it create unnecessary complexity?
```

A boundary should be retained when its semantic benefit is material.

---

# 17. Candidate Boundary Inventory

The following are **research candidates**, not final boundaries.

## BR-001 — Knowledge vs Document

Question:

Is Knowledge distinct from its documentary representation?

Need to investigate:

- semantic meaning;
- representation independence;
- lifecycle;
- identity;
- AI consumption.

Possible outcomes:

```text
Distinct
Related
Document Is Representation
Document Is Semantic Unit
Unresolved
```

---

## BR-002 — Identity vs Identifier

Question:

Is identity conceptually distinct from the identifier used to reference it?

Need to investigate:

- persistence;
- allocation;
- reassignment;
- representation;
- scope.

---

## BR-003 — Authority vs Canonicality

Question:

Are authority and canonicality distinct concepts?

Need to investigate:

- decision rights;
- current authoritative status;
- approval;
- validity;
- scope;
- temporal behavior.

---

## BR-004 — Lifecycle vs State

Question:

Is lifecycle a model governing state transitions, while state is the condition of
a subject?

Need to investigate:

- transition;
- history;
- state semantics;
- event semantics.

---

## BR-005 — Evidence vs Knowledge

Question:

Is evidence materially distinct from the knowledge or decisions derived from it?

Need to investigate:

- support relationship;
- provenance;
- validation;
- epistemic status.

---

## BR-006 — Production vs Publication

Question:

Is creating an output distinct from making that output available to an
audience/channel?

Need to investigate:

- ownership;
- authority;
- timing;
- validation;
- publication state;
- historical record.

---

## BR-007 — Output vs Document

Question:

Is a production output necessarily a document, or can a document be only one
representation of an output?

Need to investigate:

- identity;
- representation;
- publication;
- lifecycle;
- reuse.

---

## BR-008 — Universal vs Project-Specific Knowledge

Question:

What distinguishes knowledge that belongs to the Universal foundation from
knowledge that belongs only to a project?

Need to investigate:

- applicability;
- reuse;
- scope;
- authority;
- change impact.

---

## BR-009 — AI Consumer vs Knowledge System

Question:

Which responsibility belongs to AI as a consumer and which belongs to the system
that resolves governed knowledge?

Need to investigate:

- retrieval;
- interpretation;
- inference;
- validation;
- generation.

---

## BR-010 — Governance Decision vs Rule

Question:

Is a decision that establishes a rule distinct from the rule itself?

Need to investigate:

- decision history;
- rule content;
- authority;
- effective status;
- provenance.

---

# 18. Boundary Matrix

The project should eventually be able to express candidate boundaries using a
matrix such as:

| Candidate A | Candidate B | Boundary Question | Evidence Status | Current Finding | Confidence |
|---|---|---|---|---|---|
| Knowledge | Document | Semantic vs representation? | OPEN | — | — |
| Identity | Identifier | Subject vs reference? | OPEN | — | — |
| Authority | Canonicality | Decision right vs authoritative status? | OPEN | — | — |
| Lifecycle | State | Process/history vs condition? | OPEN | — | — |
| Evidence | Knowledge | Support vs governed content? | OPEN | — | — |
| Production | Publication | Creation vs availability? | OPEN | — | — |
| Output | Document | Result vs representation? | OPEN | — | — |
| Universal Knowledge | Project Knowledge | Scope boundary? | OPEN | — | — |

This matrix is a research tool, not an architecture diagram.

---

# 19. Responsibility Matrix

For candidates that remain materially relevant, the project should eventually
record:

| Candidate | Primary Responsibility | Exclusions | Potential Consumer | Boundary Status |
|---|---|---|---|---|
| Knowledge | TBD | TBD | AI / Human / Production | OPEN |
| Document | TBD | TBD | Human / AI | OPEN |
| Authority | TBD | TBD | Governance / AI | OPEN |
| Identity | TBD | TBD | Registry / AI | OPEN |
| Production | TBD | TBD | User / AI | OPEN |
| Publication | TBD | TBD | Channel / Audience | OPEN |

The initial values are intentionally unresolved.

---

# 20. Boundary Failure Modes

The following are patterns the project should actively detect.

## Boundary Collapse

Two distinct responsibilities are treated as one.

## Boundary Fragmentation

One coherent responsibility is split into unnecessary pieces.

## Boundary Leakage

One candidate silently performs another candidate's responsibility.

## Authority Leakage

A candidate exercises decision rights outside its justified scope.

## Scope Leakage

A project-specific rule is silently applied universally.

## Lifecycle Leakage

One candidate changes another candidate's lifecycle without explicit authority.

## Representation Leakage

Repository or document structure changes semantic meaning.

---

# 21. Anti-Loop Implication

Poor boundaries are a major source of loops.

Illustrative pattern:

```text
A needs B to define itself
B needs C
C needs A
```

Boundary discovery should therefore ask:

> Is this actually one responsibility wrongly divided?

or:

> Are these truly distinct responsibilities with a legitimate dependency?

This question must be resolved before dependency architecture is finalized.

---

# 22. Anti-Bootstrap Rule

The project shall not infer a boundary from an inherited architecture.

The presence of:

- an existing document;
- registry;
- system layer;
- repository folder;
- identifier class;
- or legacy standard

does not prove that the same boundary belongs in the new architecture.

The boundary must be justified through:

```text
Problem
→ Objective
→ Concept
→ Evidence
→ Responsibility
→ Boundary
```

---

# 23. AI Interpretation Rule

AI consumers shall interpret this document as a **boundary discovery map**.

AI shall not treat candidate boundaries as:

- final system layers;
- final document boundaries;
- final authority domains;
- final registries;
- or final implementation components.

When a boundary is unresolved, AI should preserve that status.

---

# 24. Step 7 Exit Condition

Step 7 is sufficiently mature to proceed to relationship discovery when:

- principal candidate responsibilities are identified;
- major responsibility overlaps are visible;
- key semantic boundaries are documented;
- authority and scope questions are explicit;
- important boundary conflicts are recorded;
- representation is kept separate from semantics;
- unresolved boundaries are fed back into `UAICP-RQU-001`;
- and no boundary is being accepted solely because it existed in the legacy
  architecture.

This does not require every boundary to be final.

It requires the major responsibilities to be sufficiently explicit for
relationship research to proceed.

---

# 25. Core Boundary Principle

> **Discover where responsibilities end before deciding what components should
> exist.**

And:

> **A boundary is justified by semantic consequence, not by file count,
> repository structure, or inherited architecture.**

---

# 26. Framework Evolution

This discovery model may evolve as Step 8 and Step 9 reveal stronger evidence.

Any revision should preserve the central methodological rule:

> **Semantic and responsibility boundaries must be discovered and justified
> before they are converted into architecture, governance structures,
> registries, document boundaries, or implementation modules.**
