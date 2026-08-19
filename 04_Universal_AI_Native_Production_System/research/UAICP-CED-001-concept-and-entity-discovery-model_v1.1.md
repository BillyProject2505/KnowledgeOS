---
document_id: UAICP-CED-001
document_type: Concept & Entity Discovery Model
title: Universal Project Concept & Entity Discovery Model
version: 1.1
status: ACTIVE
canonicality: REFERENCE
scope: Universal AI-Native Production System — New Research & Construction Trajectory
authority: Project Research Framework
audience:
  - human
  - AI
purpose: >
  Establish the controlled discovery model for identifying, distinguishing,
  and validating candidate concepts and entities that may be materially
  relevant to the eventual Universal AI-Native Production System, without
  prematurely assigning architecture, governance, registry, or implementation
  roles.
canonical_home: UAICP-CED-001
supersedes: UAICP-CED-001 v1.0
parent_context: UAICP-POM-001
methodological_dependencies:
  - UAICP-FC-001
  - UAICP-RCC-001
  - UAICP-REF-001
  - UAICP-RQU-001
  - UAICP-POM-001
---

# Universal Project Concept & Entity Discovery Model

## 1. Purpose

This document defines the Step 6 discovery model for determining what concepts
and entities may actually be required by the new Universal AI-Native Production
System.

It is a **research-stage artifact**.

It does not define the final architecture.

Its purpose is to discover and distinguish candidate conceptual building blocks
before later steps decide:

- boundaries;
- responsibilities;
- relationships;
- dependencies;
- architecture;
- governance;
- registries;
- document decomposition;
- or implementation.

---

# 2. Methodological Lineage

Step 6 is governed by the methodological documents already established in
Steps 1–5.

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

The purpose of Step 6 is to answer:

> **What concepts and entities may be necessary to represent the problems and
> objectives discovered in Step 5?**

It does not answer:

> **What architecture should we build?**

---

# 3. Alignment Rules With Steps 1–5

This document shall remain subordinate to the methodological intent already
established in Steps 1–5.

## 3.1 North Star Alignment

`UAICP-FC-001` establishes the desired end-state: a governed, AI-native
production foundation that can resolve knowledge, authority, context, rules,
production requirements, validation, provenance, and publication.

Step 6 may investigate concepts needed to support those capabilities.

It shall not assume that every capability named in the North Star requires a
separate entity.

## 3.2 Construction Charter Alignment

`UAICP-RCC-001` requires:

- research before architecture;
- discovery before construction;
- semantic before representational reasoning;
- explicit dependencies;
- historical separation;
- modularity over file minimization;
- architectural restraint;
- and anti-loop / anti-bootstrap discipline.

Therefore Step 6 shall remain a discovery model, not a hidden architecture model.

## 3.3 Evidence Framework Alignment

`UAICP-REF-001` requires that material findings remain distinguishable from:

- source material;
- inference;
- hypothesis;
- and decision.

Therefore every material candidate concept/entity must retain evidence and research
status.

## 3.4 Questions & Unknowns Alignment

`UAICP-RQU-001` establishes that unknown is an explicit state.

Therefore a candidate concept may remain unresolved.

The absence of a final definition is not a defect.

## 3.5 Problem & Objective Alignment

`UAICP-POM-001` identifies problems, causes, objectives, and desired outcomes.

Step 6 should therefore trace candidate concepts/entities backward to the
problem or objective that makes them potentially necessary.

---

# 4. Concept and Entity Discovery Principle

The project shall discover **what must be conceptually distinct** before deciding
**what must be structurally built**.

The preferred direction is:

```text
Problem / Objective
        ↓
Candidate Concept / Entity
        ↓
Evidence
        ↓
Definition Candidate
        ↓
Distinction Analysis
        ↓
Validation / Open Questions
        ↓
Boundary Discovery
        ↓
Relationship Discovery
        ↓
Architecture
```

The prohibited direction is:

```text
Existing Architecture
        ↓
Create Concepts to Fit Its Structure
```

---

# 5. What Is a Concept?

For Step 6, a **Concept** is an abstraction that is materially useful for
reasoning about the system.

A concept may describe:

- a meaningful domain idea;
- a rule or condition;
- a relationship;
- a state;
- a process;
- a property;
- a role;
- or another abstraction required to reason about the system.

A concept does not automatically require:

- independent identity;
- a registry entry;
- a document;
- a database object;
- a system module;
- or an architecture layer.

---

# 6. What Is a Candidate Entity?

A **Candidate Entity** is a thing or subject that may need to be treated as
independently distinguishable because it may:

- persist over time;
- participate independently in relationships;
- have independently meaningful properties;
- require provenance;
- have lifecycle;
- be governed independently;
- or require stable identity.

The word **candidate** is essential.

Step 6 does not assume that every important thing is an entity.

---

# 7. Concept vs Entity Is a Research Question

The project shall not force a candidate into "concept" or "entity" merely because
the terminology is convenient.

For every material candidate, ask:

```text
Is independent identity required?
Does it persist?
Does it have its own lifecycle?
Can it participate independently in relationships?
Does it require independent provenance?
Does governance address it separately?
Would collapsing it destroy material meaning?
```

Possible outcomes:

```text
Concept
Candidate Entity
Property / Attribute
State
Role
Relationship
Event
Representation
Process
Unresolved
```

These are **discovery classifications only**.

They are not a final Universal ontology.

---

# 8. Anti-Reification Rule

A word does not become an entity merely because it appears important.

The project shall not create a new object, registry, document, or module simply to
give a name a place in the system.

A candidate should earn structural distinctness through:

- evidence;
- semantic necessity;
- independent behavior;
- lifecycle;
- identity need;
- relationship need;
- governance consequence;
- or another material system requirement.

---

# 9. Representation Independence

A representation is not automatically a new semantic entity.

Conceptually:

```text
Semantic Subject
      ↓
Representation
      ├── Markdown
      ├── JSON
      ├── YAML
      ├── PDF
      ├── API
      └── UI
```

Different representations may express the same underlying subject.

Therefore:

> **Different representations do not automatically imply different entities.**

This prevents repository format, serialization, or platform constraints from
creating false semantic multiplicity.

---

# 10. State Independence

A state is not automatically an entity.

For example:

```text
Draft
Approved
Published
Archived
```

may be states of one subject.

The project shall determine later whether:

- state is a property;
- state is part of lifecycle;
- state requires independent representation;
- or state becomes independently governable.

Step 6 only records the distinction as a research question.

---

# 11. Role Independence

A role is not automatically an entity.

Examples:

```text
Owner
Reviewer
Consumer
Publisher
Authority
```

may be contextual roles played by different actors or subjects.

The project shall determine whether a role requires:

- identity;
- persistence;
- lifecycle;
- independent governance;

or whether it is simply a relationship context.

---

# 12. Relationship Independence

A relationship is not automatically an entity.

However, a relationship may eventually require explicit modeling if it has its own:

- identity;
- attributes;
- lifecycle;
- provenance;
- temporal validity;
- governance;
- or decision significance.

This remains a later discovery question.

---

# 13. Candidate Discovery Contract

Each material candidate should record:

```text
Candidate ID
Candidate Name
Candidate Classification
Candidate Definition
Why It May Be Needed
Related Problem(s)
Related Objective(s)
Evidence
Evidence Lineage
Distinctions
Possible Properties
Possible Lifecycle
Possible Identity Need
Possible Authority Relevance
Possible Relationship Relevance
Scope
Open Questions
Research Status
Confidence
```

This is a discovery contract, not a final schema.

---

# 14. Initial Candidate Landscape

The following candidates are derived **only from the conceptual direction established
in Steps 1–5** and are therefore deliberately provisional.

## C-001 — Knowledge

Candidate meaning:

Meaningful information, rules, principles, facts, instructions, or semantic
material that the eventual system may need to preserve, govern, retrieve, and
apply.

Questions:

- What qualifies as knowledge?
- What is the smallest independently governable semantic unit?
- How does knowledge differ from evidence?
- How does knowledge differ from a document?
- Can knowledge exist independently of a representation?

Status:

```text
CANDIDATE / OPEN
```

---

## C-002 — Document

Candidate meaning:

A governed documentary unit or representation through which semantic material
may be organized, expressed, referenced, or consumed.

Questions:

- What makes something a document?
- When does a document require independent identity?
- Is every representation a document?
- Which document properties are semantic and which are representational?

Status:

```text
CANDIDATE / OPEN
```

---

## C-003 — Project

Candidate meaning:

A bounded context within which particular objectives, knowledge, production
requirements, rules, and outputs apply.

Questions:

- What establishes a project boundary?
- Can projects contain projects?
- Which knowledge is project-specific?
- Does a project require stable identity?

Status:

```text
CANDIDATE / OPEN
```

---

## C-004 — Rule

Candidate meaning:

A governed instruction, constraint, or condition that may influence
interpretation, decision-making, production, validation, or system behavior.

Questions:

- How does a rule differ from a principle?
- How does a rule differ from a standard or policy?
- Does a rule have independent lifecycle?
- What establishes rule authority?

Status:

```text
CANDIDATE / OPEN
```

---

## C-005 — Authority

Candidate meaning:

The governed basis by which a source, decision, actor, or artifact may determine
what is valid or applicable within a defined context.

Questions:

- Is authority a property, relationship, role, or entity?
- What establishes authority?
- Can authority change over time?
- How does authority differ from canonicality?

Status:

```text
CANDIDATE / OPEN
```

---

## C-006 — Identity

Candidate meaning:

The stable semantic distinction of a subject that permits it to be recognized as
the same subject across applicable representations, contexts, or changes.

Questions:

- Which subjects truly require identity?
- What is identity distinct from identifier?
- Which identities are universal or scoped?
- What persistence guarantees are actually needed?

Status:

```text
CANDIDATE / OPEN
```

---

## C-007 — Identifier

Candidate meaning:

A value, symbol, code, or other reference mechanism used to distinguish or
refer to an identified subject.

Questions:

- Which subjects need identifiers?
- Does allocation establish identity?
- Who may allocate identifiers?
- Can multiple identifiers refer to one identity?

Status:

```text
CANDIDATE / OPEN
```

---

## C-008 — Scope

Candidate meaning:

The contextual boundary within which a rule, authority, concept, relationship,
or other subject applies.

Questions:

- Is scope a property or an independently modeled subject?
- Can scope nest?
- Can scope change?
- How is cross-scope applicability handled?

Status:

```text
CANDIDATE / OPEN
```

---

## C-009 — Evidence

Candidate meaning:

Material that supports, challenges, or contextualizes a claim, finding, or
decision.

Questions:

- When does evidence become part of governed knowledge?
- Can evidence itself be governed independently?
- What provenance must evidence retain?
- What makes evidence sufficiently reliable?

Status:

```text
CANDIDATE / OPEN
```

---

## C-010 — Provenance

Candidate meaning:

Traceable information describing origin, derivation, transformation, decision,
revision, or publication history.

Questions:

- What subjects require provenance?
- Is provenance a property, relationship set, or event history?
- What minimum provenance is needed for trustworthy AI use?
- How is historical uncertainty preserved?

Status:

```text
CANDIDATE / OPEN
```

---

## C-011 — Canonicality

Candidate meaning:

A governed condition or status indicating that a particular subject or
representation is the authoritative reference for a defined purpose and scope.

Questions:

- Is canonicality a property or relationship?
- What can become canonical?
- Is canonicality temporal?
- How does canonicality differ from authority, validity, and approval?

Status:

```text
CANDIDATE / OPEN
```

---

## C-012 — Lifecycle

Candidate meaning:

The governed progression of a subject through materially meaningful states or
events over time.

Questions:

- Which candidates genuinely require lifecycle?
- Is lifecycle a model, process, or property?
- What triggers transitions?
- How is history preserved?

Status:

```text
CANDIDATE / OPEN
```

---

## C-013 — State

Candidate meaning:

A condition of a subject at a point or interval in its lifecycle.

Questions:

- Which states are intrinsic?
- Which are contextual?
- Can multiple state dimensions coexist?
- How does state differ from canonicality?

Status:

```text
CANDIDATE / OPEN
```

---

## C-014 — Intent

Candidate meaning:

The user's desired outcome or requested objective that initiates a system
interaction or production task.

Questions:

- How is intent represented?
- How is ambiguous intent handled?
- How is intent mapped to applicable context and knowledge?
- Is intent persistent or transient?

Status:

```text
CANDIDATE / OPEN
```

---

## C-015 — Production

Candidate meaning:

The governed transformation of user intent and applicable knowledge into an
output or other desired result.

Questions:

- What is the fundamental unit of production?
- What inputs does production require?
- Which production decisions require governance?
- Which production choices may remain implementation-dependent?

Status:

```text
CANDIDATE / OPEN
```

---

## C-016 — Output / Production Artefact

Candidate meaning:

A result produced by a governed production activity that may itself require
identity, validation, provenance, lifecycle, or publication tracking.

Questions:

- What makes an output independently governable?
- Is every output independently identifiable?
- How does an output relate to source knowledge and decisions?
- How does an output differ from a document?

Status:

```text
CANDIDATE / OPEN
```

---

## C-017 — Publication

Candidate meaning:

The controlled act or resulting availability through which a produced output is
released to an intended audience or channel.

Questions:

- Is publication an event, activity, state, or relationship?
- What distinguishes production from publication?
- What authority applies to publication?
- What publication history must be preserved?

Status:

```text
CANDIDATE / OPEN
```

---

## C-018 — AI Consumer

Candidate meaning:

An AI-based consumer that retrieves, interprets, reasons over, or applies
governed knowledge for a task.

Questions:

- Is AI Consumer an actor, role, system, or implementation concept?
- What belongs to the AI consumer versus the knowledge system?
- How should source content be distinguished from AI inference?
- What trust signals must be machine-readable?

Status:

```text
CANDIDATE / OPEN
```

---

## C-019 — Governance Decision

Candidate meaning:

A controlled decision that establishes, changes, resolves, approves, or
constrains something within the system.

Questions:

- What makes a decision authoritative?
- Does a decision require independent identity?
- How is a decision linked to evidence?
- How is decision history preserved?

Status:

```text
CANDIDATE / OPEN
```

---

# 15. Candidate Classification Must Remain Reversible

A candidate may move from:

```text
Concept
→ Entity
```

or:

```text
Entity
→ Relationship
```

or:

```text
Entity
→ State
```

or:

```text
Candidate
→ Rejected
```

without this being treated as failure.

The purpose of discovery is to improve the model.

---

# 16. Concept Overlap Analysis

When two candidates appear similar, compare:

```text
Name
Definition
Purpose
Scope
Identity Need
Lifecycle
Authority
Relationships
Consumer
Decision Impact
```

Possible outcomes:

```text
Same Concept
Related but Distinct
One Is a Property / Role / State
One Is a Representation
Historical Terminology Difference
Unresolved
```

The project should not merge concepts merely because the names are similar.

It should not split concepts merely because different words are being used.

---

# 17. Concept-to-Problem Traceability

Each material concept/entity candidate should trace to:

```text
Problem
    ↓
Objective
    ↓
Candidate Concept / Entity
    ↓
Evidence
    ↓
Research Question
```

A candidate with no meaningful connection to the problem/objective model should
be treated as exploratory until justified.

---

# 18. Identity Screening

For every candidate, assess:

```text
Identity Required
Identity Possibly Required
Identity Not Yet Justified
Identity Not Applicable
Unknown
```

This is a research output only.

It does not define a final identifier system.

---

# 19. Semantic Home Screening

For each candidate, ask where its meaning may ultimately belong:

```text
Universal
Project
Domain
Documentary
Operational
Implementation
Unknown
```

This is a **semantic classification**, not a repository folder assignment.

---

# 20. Legacy Comparison as a Secondary Check

Previous project documents may be consulted **after** the candidate landscape has
been derived from Steps 1–5.

Their role is to test:

- whether a historically observed concept has already been encountered;
- whether terminology differs;
- whether a known failure mode suggests a missing candidate;
- whether an apparent duplicate has historical reasons.

Legacy material must not be used to define the candidate inventory automatically.

Possible outcomes:

```text
Equivalent
Partially Equivalent
Related
Different
Historical Only
Requires New Research
```

---

# 21. Candidate Relationships — Preliminary Only

The following are possible relationships derived from the North Star and
Problem/Objectives, not from legacy architecture:

```text
Intent
  ── initiates / requests ──>
Production

Production
  ── uses / consumes ──>
Knowledge

Document
  ── represents / organizes / references ──>
Knowledge

Rule
  ── constrains ──>
Production

Evidence
  ── supports ──>
Finding / Decision Candidate

Authority
  ── governs / applies to ──>
Rule / Decision / Document / Knowledge

Provenance
  ── traces ──>
Knowledge / Document / Decision / Output

Lifecycle
  ── describes progression of ──>
Candidate Subject

Publication
  ── makes available ──>
Output
```

These relationships must **not** be treated as the final relationship model.
Step 8 will research them explicitly.

---

# 22. Anti-Bootstrap Safeguards

Step 6 must not:

- copy the previous Universal Architecture's layers;
- assume existing registry types;
- assume existing document taxonomy;
- assume existing identifier classes;
- assume that every candidate must become a document;
- assume that every concept must be registered;
- or use a repository folder to decide semantic identity.

The guiding question remains:

> **Does the new system genuinely require this distinction?**

---

# 23. AI Interpretation Rule for Step 6

AI consumers shall interpret this document as a **candidate discovery map**.

AI shall not treat:

- candidate names;
- candidate classifications;
- candidate relationships;
- or candidate definitions

as final normative architecture.

When a candidate is unresolved, AI should preserve that status.

---

# 24. Step 6 Exit Condition

Step 6 is sufficiently mature to proceed to Step 7 when:

- the principal candidate concepts/entities have been surfaced from Steps 1–5;
- major concept overlaps have been examined;
- concept-versus-entity uncertainty is visible;
- identity needs have not been assumed;
- candidate relationships are explicitly provisional;
- candidate-to-problem/objective traceability exists;
- material unknowns have been fed back to `UAICP-RQU-001`;
- and no major candidate is being accepted solely because it existed in the
  previous architecture.

This does **not** require every candidate to be validated.

It requires the conceptual landscape to be sufficiently explicit for boundary
research to begin.

---

# 25. Core Discovery Principle

> **Discover what must be distinct before deciding what must be built.**

And more specifically:

> **Do not inherit the old conceptual map. Reconstruct the conceptual map from
the new project's problems, objectives, evidence, and questions.**

---

# 26. Framework Evolution

This discovery model may evolve as Steps 7–9 expose stronger evidence.

Any revision should preserve the central methodological rule:

> **Conceptual distinctions must be discovered and justified before they are
turned into architecture, governance, registries, documents, or implementation
mechanisms.**
