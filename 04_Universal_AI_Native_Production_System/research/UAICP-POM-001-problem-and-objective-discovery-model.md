---
document_id: UAICP-POM-001
document_type: Problem & Objective Discovery Model
title: Universal Project Problem & Objective Discovery Model
version: 1.0
status: ACTIVE
canonicality: REFERENCE
scope: Universal AI-Native Production System — New Research & Construction Trajectory
authority: Project Research Framework
audience:
  - human
  - AI
purpose: >
  Establish the research model for discovering the actual problems the project
  must solve and the outcomes the eventual system must achieve, without
  presupposing the final architecture or implementation.
canonical_home: UAICP-POM-001
supersedes: none
parent_context: UAICP-RQU-001
---

# Universal Project Problem & Objective Discovery Model

## 1. Purpose

This document establishes the working research model for discovering:

1. what problems the new system actually needs to solve;
2. what causes those problems;
3. what consequences they produce;
4. who and what they affect;
5. what outcomes would constitute meaningful resolution;
6. and what success conditions an eventual system must satisfy.

This is a **discovery artifact**, not a final problem statement and not an
architecture specification.

The model shall remain open to revision as research produces stronger evidence.

---

# 2. Relationship to the Project Methodology

The construction sequence is:

```text
UAICP-FC-001
Foundational Concept & North Star
        ↓
UAICP-RCC-001
Research & Construction Charter
        ↓
UAICP-REF-001
Research & Evidence Framework
        ↓
UAICP-RQU-001
Research Questions & Unknowns Framework
        ↓
UAICP-POM-001
Problem & Objective Discovery Model
        ↓
Concept / Entity Discovery
        ↓
Boundary Discovery
        ↓
Relationship Discovery
        ↓
Architecture Discovery
```

The purpose of this document is to provide the **problem and outcome layer**
between research control and system design.

---

# 3. Discovery Principle

The project shall not begin with a preferred solution.

The preferred direction is:

```text
Problem
    ↓
Evidence
    ↓
Root Cause
    ↓
Consequence
    ↓
Desired Outcome
    ↓
Success Condition
    ↓
System Requirement Candidate
    ↓
Architecture
```

Not:

```text
Existing Architecture
    ↓
Find a Problem That Justifies It
```

---

# 4. Problem Candidate Model

A material problem candidate should be recorded with:

```text
Problem ID
Problem Statement
Why It Matters
Evidence
Affected Actors
Affected Processes
Affected Outputs
Scope
Context
Root Causes
Consequences
Related Questions
Confidence
Research Status
```

A problem candidate is not a confirmed problem merely because it appears
plausible.

---

# 5. Preliminary Problem Landscape

The following are **research hypotheses / candidate problem areas**, not
confirmed findings.

## P-001 — AI Cannot Reliably Resolve the Applicable Knowledge

Possible symptom:

AI may require extensive user prompting to determine which project knowledge,
rules, standards, or specifications should apply to a request.

Potential consequences:

- inconsistent output;
- excessive prompt complexity;
- higher human supervision;
- unreliable reuse of existing knowledge;
- difficulty scaling production.

Research requirement:

Determine whether this is a genuine systemic problem, its scope, and its root
causes.

---

## P-002 — Authority May Be Implicit Rather Than Explicit

Potential symptom:

AI or human users may have to infer which document, rule, or source should be
trusted from filenames, locations, recency, or context.

Potential consequences:

- conflicting interpretations;
- incorrect rule application;
- use of superseded material;
- unreliable automation.

Research requirement:

Determine what authority signals are actually required and whether the problem is
universal or project-specific.

---

## P-003 — Knowledge May Be Distributed Without Sufficient Semantic Connection

Potential symptom:

Relevant information exists across multiple documents or repositories but the
relationships among the concepts are not always explicit.

Potential consequences:

- incomplete context retrieval;
- duplicate rules;
- inconsistent interpretation;
- missed dependencies.

Research requirement:

Determine whether the underlying issue is documentary organization,
semantic modeling, retrieval, governance, or some combination.

---

## P-004 — Production Rules May Be Difficult to Reuse Consistently

Potential symptom:

Project-specific rules may exist but require repeated human explanation or
manual interpretation.

Potential consequences:

- repeated prompt engineering;
- inconsistent output;
- duplicated instructions;
- reduced scalability.

Research requirement:

Determine which production knowledge can be made reusable and under what
conditions.

---

## P-005 — Document Change May Produce Uncontrolled Dependency Effects

Potential symptom:

A modification to one rule or document may require changes in multiple dependent
documents or outputs.

Potential consequences:

- large revision workload;
- inconsistent versions;
- accidental contradictions;
- high maintenance cost.

Research requirement:

Determine the nature of these dependencies and what level of impact management
is actually required.

---

## P-006 — Historical and Current Material May Be Difficult to Distinguish

Potential symptom:

Legacy documents may remain accessible alongside current documents.

Potential consequences:

- accidental reuse of superseded rules;
- ambiguity for AI;
- loss of historical context if legacy material is deleted;
- incorrect reconstruction of past decisions.

Research requirement:

Determine what historical integrity and current-state resolution capabilities
are needed.

---

## P-007 — Production Automation May Be Unsafe Without Stronger Foundations

Potential symptom:

Automation can amplify knowledge or governance errors.

Potential consequences:

- repeated incorrect content;
- uncontrolled publication;
- loss of review control;
- difficult auditability.

Research requirement:

Determine the actual prerequisites for safe automation and which decisions must
remain governed.

---

# 6. Problem Root Cause Model

A problem shall not be treated as sufficiently understood merely because its
symptom is visible.

The project should distinguish:

```text
Observed Symptom
      ↓
Immediate Cause
      ↓
Contributing Causes
      ↓
Structural Cause
      ↓
Systemic Cause
```

For example:

```text
AI produces inconsistent content
        ↓
Different rules are retrieved
        ↓
Applicable authority is unclear
        ↓
Document relationships are not sufficiently explicit
        ↓
Knowledge / document governance infrastructure may be incomplete
```

This is only an illustrative hypothesis.

It is not a confirmed causal chain.

---

# 7. Consequence Model

For each confirmed problem, assess consequences across:

```text
User Impact
AI Impact
Production Impact
Governance Impact
Quality Impact
Operational Impact
Scalability Impact
Auditability Impact
Automation Impact
Historical Impact
```

A problem with no meaningful consequence may not require systemic treatment.

---

# 8. Problem Scope

Every material problem should be evaluated for scope:

```text
Universal
Cross-Project
Project-Specific
Domain-Specific
Implementation-Specific
```

A problem observed in one production system must not automatically be elevated to
a Universal problem.

Likewise, a Universal problem should not be weakened merely because the current
evidence was first observed in one project.

---

# 9. Non-Problem Classification

Research should also record things that may initially appear to be problems but
are intentionally accepted.

Examples:

- a project-specific difference that is not harmful;
- human judgment that is intentionally retained;
- a platform-specific limitation that does not need Universal treatment;
- legitimate complexity that cannot be removed without reducing capability.

The system should not "solve" complexity merely because it exists.

---

# 10. Objective Discovery

An objective describes the **desired capability or outcome**, not the mechanism
used to achieve it.

Prefer:

> "AI can reliably determine which knowledge and rules apply to a production
> request."

over:

> "Create a Universal Knowledge Registry."

Prefer:

> "A governed document can be identified independently of its physical
> representation."

over:

> "Use a specific identifier grammar."

The first statements describe outcomes.

The second statements presuppose implementations.

---

# 11. Objective Candidate Model

Each objective candidate should record:

```text
Objective ID
Objective Statement
Related Problem(s)
Desired Outcome
Who Benefits
Success Condition
Evidence Basis
Constraints
Priority
Confidence
Open Questions
```

---

# 12. Preliminary Objective Landscape

The following are **candidate objectives**, not final requirements.

## O-001 — Reliable Knowledge Resolution

The eventual system should enable an AI consumer to identify and retrieve the
knowledge applicable to a user intent with sufficient reliability.

## O-002 — Explicit Authority Resolution

The eventual system should enable AI and humans to determine which source or rule
has authority for a particular context.

## O-003 — Stable Semantic Identity

The eventual system should support stable identification of governed entities
independently of their representation or storage location, where such identity
is actually required.

## O-004 — Explicit Relationship Resolution

The eventual system should allow relevant relationships among knowledge,
documents, rules, and production artifacts to be represented and resolved when
those relationships materially affect interpretation.

## O-005 — Controlled Evolution

The eventual system should allow changes to knowledge, rules, documents, and
production systems while preserving traceability and minimizing uncontrolled
dependency effects.

## O-006 — Safe AI Production

The eventual system should provide sufficient governed context for AI to
generate consistent production output without requiring the user to repeatedly
restate established project rules.

## O-007 — Controlled Automation

The eventual system should support automation only to the degree that its
knowledge, authority, validation, approval, and publication foundations are
sufficiently governed.

---

# 13. Objective vs Requirement

The project must distinguish:

```text
Objective
    ↓
Desired Capability / Outcome

Requirement
    ↓
Condition the System Must Satisfy

Architecture
    ↓
Structure Chosen to Satisfy Requirements
```

A candidate objective must not be converted directly into an architecture
component.

---

# 14. Success Condition Model

A success condition should be observable or assessable.

Examples:

```text
AI can resolve the current applicable rule without relying on filename recency.
```

```text
A user can request project content without restating project-specific production
rules already governed by the system.
```

```text
A change to one governed rule can be traced to affected downstream artifacts.
```

These are illustrative outcomes, not yet acceptance criteria.

---

# 15. Problem-to-Objective Traceability

The project should maintain relationships such as:

```text
Problem
   ↓
Root Cause
   ↓
Objective
   ↓
Success Condition
```

Example:

```text
Problem:
AI cannot reliably determine applicable production rules.

Root Cause Candidate:
Authority is insufficiently explicit.

Objective:
Enable explicit authority resolution.

Success Condition:
AI can identify the applicable active authority for a request without relying
on filename or recency alone.
```

The causal relationship remains subject to research validation.

---

# 16. Priority Model

Problem and objective priority should be based on impact.

Initial scale:

```text
P0 — Foundational
P1 — Major
P2 — Significant
P3 — Limited
P4 — Exploratory
```

Priority is not a statement of truth.

A high-priority hypothesis remains a hypothesis until validated.

---

# 17. Research Status

Each problem or objective candidate may have:

```text
Candidate
Under Research
Supported
Confirmed
Contested
Deferred
Rejected
Superseded
```

A confirmed problem does not automatically imply a particular solution.

---

# 18. Architecture Entry Rule

No problem or objective shall be used as justification for a major architectural
component unless:

1. the problem is sufficiently evidenced;
2. its scope is understood;
3. its root cause is sufficiently understood;
4. the objective is clearly defined;
5. relevant open questions are visible;
6. and reasonable alternatives have been considered where material.

This is the primary guardrail against solution-first architecture.

---

# 19. Known Constraint vs Problem

A constraint is not necessarily a problem.

For example:

```text
GitHub has a particular repository behavior.
```

is a constraint.

It becomes a system problem only when:

```text
Constraint
    ↓
causes a material failure against
    ↓
an objective
```

The project must not elevate every implementation limitation into a Universal
semantic requirement.

---

# 20. Research Backlog

The following questions should be explored before the first major architecture
commitment:

### Problem Discovery

- Which current workflows genuinely fail or become unreliable?
- Which failures recur across multiple projects?
- Which problems are caused by knowledge ambiguity?
- Which are caused by document ambiguity?
- Which are caused by governance?
- Which are caused by retrieval or AI limitations?
- Which are caused only by implementation constraints?

### Objective Discovery

- What capabilities must the final system reliably provide?
- Which capabilities must be Universal?
- Which capabilities may remain project-specific?
- Which capabilities require human control?
- Which capabilities can eventually be automated?

These questions should feed back into `UAICP-RQU-001`.

---

# 21. Non-Goals

This document does not:

- define final architecture;
- define the final system layers;
- name mandatory registries;
- establish final identifiers;
- define final document counts;
- decide the final AI implementation;
- or declare the preliminary problem/objective candidates as confirmed.

---

# 22. Core Discovery Principle

> **Do not start by asking what system we should build. Start by proving what
> problem exists and what outcome is genuinely required.**

---

# 23. Final Problem-to-Architecture Rule

> **Problem → Evidence → Cause → Objective → Success Condition → Requirement →
> Architecture**

The project should avoid the reverse path:

> **Architecture → justification → problem statement**

This ordering is a core anti-loop and anti-bootstrap safeguard.
