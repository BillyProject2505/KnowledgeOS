---
document_id: UAICP-CED-001
document_type: Concept & Entity Discovery Model
title: Universal Project Concept & Entity Discovery Model
version: 1.0
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
supersedes: none
parent_context: UAICP-POM-001
research_dependencies:
  - UAICP-RCC-001
  - UAICP-REF-001
  - UAICP-RQU-001
  - UAICP-POM-001
---

# Universal Project Concept & Entity Discovery Model

## 1. Purpose

This document establishes the research model for discovering the concepts and
entities that may be required by the new Universal AI-Native Production System.

Its purpose is to determine:

- what things or abstractions the system may need to understand;
- which of them are genuinely distinct;
- which are merely different representations, states, roles, or views of the
  same underlying thing;
- what properties appear essential;
- what distinctions are necessary;
- and what questions remain unresolved.

This document does **not** establish the final system architecture.

In particular, it does not decide:

- system layers;
- registry architecture;
- document taxonomy;
- identifier syntax;
- governance ownership;
- implementation mechanisms;
- or whether every discovered concept requires a separate document.

---

# 2. Relationship to Previous Research

The current methodological chain is:

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
UAICP-CED-001
Concept & Entity Discovery Model
        ↓
Boundary & Responsibility Discovery
        ↓
Relationship Discovery
        ↓
Dependency Analysis
        ↓
Architecture Discovery
```

Step 6 therefore converts validated problem/objective discoveries into a
**candidate conceptual landscape**.

It does not yet convert that landscape into architecture.

---

# 3. Discovery Principle

The project shall discover concepts and entities before assigning them system
roles.

The preferred direction is:

```text
Problem / Objective
        ↓
Candidate Concept / Entity
        ↓
Definition Candidate
        ↓
Distinction Analysis
        ↓
Evidence
        ↓
Validation
        ↓
Boundary Discovery
        ↓
Relationship Discovery
        ↓
Architecture
```

Not:

```text
Architecture Layer
        ↓
Invent Concepts That Fit the Layer
```

---

# 4. Concept vs Entity

For this discovery phase, the terms are intentionally provisional.

## Concept

A **Concept** is an abstraction used to reason about a meaningful aspect of the
system.

Examples might include:

- authority;
- provenance;
- canonicality;
- scope;
- production;
- knowledge.

A concept does not automatically imply that a separate object, document,
registry, or module must exist.

## Entity

An **Entity** is a candidate identifiable subject or thing that may require
persistent distinction because it can participate independently in relationships,
state, lifecycle, provenance, or governance.

An entity may eventually require stable identity, but this Framework does not
assume that identity is necessary for every candidate entity.

---

# 5. Distinction From Earlier Documents

This document must not duplicate the responsibilities of earlier research
artifacts.

## North Star

`UAICP-FC-001` defines the intended end-state.

It does not discover the actual conceptual inventory.

## Research & Construction Charter

`UAICP-RCC-001` defines how the project is constructed safely.

It does not define substantive system concepts.

## Research & Evidence Framework

`UAICP-REF-001` defines how evidence is evaluated.

It does not decide the final concept model.

## Research Questions & Unknowns Framework

`UAICP-RQU-001` records uncertainty.

It does not itself resolve the concepts under investigation.

## Problem & Objective Discovery Model

`UAICP-POM-001` identifies candidate problems and desired outcomes.

This document asks:

> **What concepts and entities are required to represent and solve those
> problems?**

---

# 6. Discovery Contract

Each material candidate should be evaluated through:

```text
Concept / Entity ID
Name
Candidate Definition
Candidate Type
Why It May Be Needed
Related Problem(s)
Related Objective(s)
Evidence
Source Lineage
Distinctions
Possible Properties
Possible States
Possible Relationships
Scope
Potential Identity Need
Potential Lifecycle Need
Potential Authority Relevance
Open Questions
Research Status
Confidence
```

These fields describe the discovery state.

They do not define final architecture.

---

# 7. Candidate Classification

A candidate may initially be classified as:

```text
CONCEPT
ENTITY
ROLE
PROPERTY
ATTRIBUTE
STATE
EVENT
RELATIONSHIP
VALUE / VOCABULARY
REPRESENTATION
PROCESS
BOUNDARY
UNRESOLVED
```

These classifications are **research categories**, not final Universal
taxonomy.

A candidate may move between categories as understanding improves.

For example, something initially believed to be an entity may later prove to be:

- a state of another entity;
- a representation;
- a role;
- a relationship;
- or a derived view.

---

# 8. Anti-Reification Rule

The project shall not create an independent entity merely because a word is
important.

For each candidate, ask:

> Does this require independent identity?

> Does it have its own lifecycle?

> Can it exist independently?

> Can it participate in relationships independently?

> Does governance need to address it independently?

> Would merging it with another concept destroy material meaning?

If the answer is no, the candidate may remain a concept rather than becoming an
entity.

---

# 9. Representation Rule

A representation is not automatically a distinct semantic entity.

Conceptually:

```text
Underlying Concept / Entity
        ↓
Representation
        ↓
Markdown / JSON / YAML / PDF / API / UI
```

Different representations may express the same semantic subject.

The project shall therefore avoid creating duplicate entities simply because the
same thing appears in different formats or repositories.

---

# 10. State Rule

A state is not automatically a separate entity.

For example:

```text
Draft
Approved
Published
Archived
```

may represent states of another entity rather than four independent entities.

Whether a state should become independently modeled must be discovered from
evidence and lifecycle requirements.

---

# 11. Role Rule

A role is not automatically an entity.

For example:

```text
Owner
Consumer
Reviewer
Publisher
Authority
```

may describe how an actor or object participates in a relationship.

The project should determine whether a role requires independent identity or is
simply contextual participation.

---

# 12. Relationship Rule

A relationship is not automatically a standalone entity.

However, if a relationship itself requires:

- identity;
- lifecycle;
- provenance;
- governance;
- temporal validity;
- or independent attributes,

then research may determine that it needs explicit representation.

That decision belongs to later discovery.

---

# 13. Candidate Concept Inventory — Initial Research Surface

The following candidates are derived from the project's current North Star and
previous research experience.

They are **not confirmed system concepts**.

## C-001 — Knowledge

Possible meaning:

The meaningful information, rules, principles, facts, instructions, or semantic
material that the system must preserve, govern, retrieve, and apply.

Key questions:

- What qualifies as knowledge?
- Is all governed content knowledge?
- How does knowledge differ from evidence?
- How does knowledge differ from a document?
- Can knowledge exist independently from its representation?

Status:

```text
CANDIDATE / OPEN
```

---

## C-002 — Document

Possible meaning:

A governed representation or documentary unit used to organize, express, or
reference semantic content.

Key questions:

- What makes something a document?
- Does every governed representation constitute a document?
- When is a document independently identifiable?
- Which document properties are semantic versus representational?

Status:

```text
CANDIDATE / OPEN
```

---

## C-003 — Project

Possible meaning:

A bounded context within which particular goals, knowledge, rules, outputs, and
production requirements apply.

Key questions:

- What establishes a project boundary?
- Can a project contain other projects?
- Which knowledge is universal versus project-specific?
- Does a project require persistent identity?

Status:

```text
CANDIDATE / OPEN
```

---

## C-004 — Rule

Possible meaning:

A governed instruction, constraint, or condition that influences interpretation,
decision-making, production, or system behavior.

Key questions:

- What distinguishes a rule from a principle?
- What distinguishes a rule from policy or standard?
- Does a rule have lifecycle?
- Can a rule be independently referenced?
- How is rule authority established?

Status:

```text
CANDIDATE / OPEN
```

---

## C-005 — Authority

Possible meaning:

The governed basis by which a source, decision, actor, or artifact is entitled
to determine what is valid or applicable within a defined scope.

Key questions:

- Is authority a property, relationship, role, or entity?
- What establishes authority?
- Can authority change over time?
- How does authority differ from canonicality?
- How does authority interact with governance?

Status:

```text
CANDIDATE / OPEN
```

---

## C-006 — Identity

Possible meaning:

The stable semantic distinction of a subject that allows it to be recognized as
the same subject across representations, contexts, or changes where applicable.

Key questions:

- Which subjects genuinely require identity?
- What is identity distinct from identifier?
- Which identities must remain representation-independent?
- Which identities are universal versus scoped?

Status:

```text
CANDIDATE / OPEN
```

---

## C-007 — Identifier

Possible meaning:

A representation used to distinguish or reference an identified subject.

Key questions:

- Which subjects require identifiers?
- Can multiple identifiers refer to one identity?
- Who or what assigns identifiers?
- Does identifier allocation create identity or merely represent it?

Status:

```text
CANDIDATE / OPEN
```

---

## C-008 — Scope

Possible meaning:

The governed contextual boundary within which a concept, rule, authority,
relationship, or other subject applies.

Key questions:

- Is scope a property or an entity?
- Can scope nest?
- Can scope change?
- How is cross-scope applicability handled?
- How does scope differ from namespace?

Status:

```text
CANDIDATE / OPEN
```

---

## C-009 — Provenance

Possible meaning:

The traceable history of origin, derivation, transformation, decision, or
publication associated with governed material.

Key questions:

- What must provenance attach to?
- Is provenance a property, graph, event sequence, or relationship?
- How much provenance is required for trustworthy AI use?
- How is historical uncertainty preserved?

Status:

```text
CANDIDATE / OPEN
```

---

## C-010 — Evidence

Possible meaning:

Material that supports, challenges, or contextualizes a claim, finding, or
decision.

Key questions:

- When does evidence become knowledge?
- Can evidence itself be canonical?
- How should evidence remain traceable to claims?
- What makes evidence sufficiently reliable?

Status:

```text
CANDIDATE / OPEN
```

---

## C-011 — Canonicality

Possible meaning:

A governed status indicating that a particular artifact, representation, or
semantic object is currently authoritative for a defined purpose or scope.

Key questions:

- Is canonicality a property or relationship?
- What can be canonical?
- Is canonicality temporal?
- How does canonicality differ from approval, validity, and authority?

Status:

```text
CANDIDATE / OPEN
```

---

## C-012 — Lifecycle

Possible meaning:

The governed progression of a subject through materially meaningful states or
events over time.

Key questions:

- Which subjects require lifecycle?
- Is lifecycle distinct from state?
- What triggers transitions?
- How should historical states be preserved?

Status:

```text
CANDIDATE / OPEN
```

---

## C-013 — State

Possible meaning:

A condition of a subject at a particular point in its lifecycle.

Key questions:

- Which states are intrinsic?
- Which are contextual?
- Can a subject have multiple simultaneous dimensions of state?
- What is the relationship between state and canonicality?

Status:

```text
CANDIDATE / OPEN
```

---

## C-014 — Production

Possible meaning:

The governed transformation of intent and applicable knowledge into a
communication or other output.

Key questions:

- What is the fundamental unit of production?
- What inputs are required?
- Which production decisions must be governed?
- Which decisions may remain implementation-dependent?

Status:

```text
CANDIDATE / OPEN
```

---

## C-015 — Output / Artefact

Possible meaning:

A produced result that may require identity, validation, lifecycle, provenance,
or publication tracking.

Key questions:

- What makes something a production artefact?
- Is every output independently identifiable?
- How does an output relate to source knowledge and production decisions?
- How does an output differ from a document?

Status:

```text
CANDIDATE / OPEN
```

---

## C-016 — Publication

Possible meaning:

The controlled act or resulting state through which an approved output is
made available to an intended audience or channel.

Key questions:

- Is publication an event, state, process, or entity?
- What distinguishes production from publication?
- What information must be preserved about publication?
- How does publication authority differ from production authority?

Status:

```text
CANDIDATE / OPEN
```

---

## C-017 — AI Consumer

Possible meaning:

An AI-based consumer that retrieves, interprets, reasons over, or applies
governed project knowledge.

Key questions:

- Is AI Consumer a role, actor, system, or implementation?
- Which responsibilities belong to the consumer versus the knowledge system?
- How should AI distinguish source content from inference?
- What trust signals must be machine-readable?

Status:

```text
CANDIDATE / OPEN
```

---

## C-018 — Intent

Possible meaning:

The user's desired outcome or requested objective that initiates a production
or knowledge interaction.

Key questions:

- How is user intent represented?
- Can intent be ambiguous?
- How is intent mapped to applicable project knowledge?
- Is intent an input artifact, event, or transient interaction state?

Status:

```text
CANDIDATE / OPEN
```

---

## C-019 — Governance Decision

Possible meaning:

A controlled decision that establishes, changes, resolves, approves, or
constrains something within the system.

Key questions:

- What makes a decision authoritative?
- Is a decision itself an entity?
- How is a decision linked to evidence?
- How is decision history preserved?

Status:

```text
CANDIDATE / OPEN
```

---

# 14. Candidate Relations Among Concepts

At this stage, only **possible relationships** should be recorded.

Examples:

```text
Intent
  ── requests / initiates ──>
Production

Production
  ── consumes ──>
Knowledge

Document
  ── represents / organizes / references ──>
Knowledge

Rule
  ── constrains ──>
Production

Authority
  ── applies to / governs ──>
Rule / Decision / Document / Knowledge

Evidence
  ── supports ──>
Claim / Finding / Decision

Provenance
  ── traces ──>
Knowledge / Document / Decision / Output

Lifecycle
  ── governs progression of ──>
Entity / Document / Output

Publication
  ── makes available ──>
Output
```

These are discovery hypotheses only.

The authoritative relationship model belongs to a later step.

---

# 15. Identity Screening

For every candidate entity, ask:

```text
Does it require stable identity?
Does it persist across representations?
Does it have independent lifecycle?
Can it be referenced independently?
Can it participate independently in relationships?
Can governance address it independently?
```

Possible results:

```text
Identity Required
Identity Possibly Required
Identity Not Yet Justified
Identity Not Applicable
Unknown
```

This prevents identifier architecture from being created before the underlying
identity requirements are understood.

---

# 16. Canonical Home Screening

For each candidate concept, ask:

> Where should this concept live semantically?

Possible research outcomes:

```text
Universal
Project
Domain
Documentary
Operational
Implementation
Unknown
```

This is deliberately **not** a repository-folder decision.

A semantic home must be discovered before a repository home is assigned.

---

# 17. Independence Screening

A candidate may be independently modeled when there is sufficient evidence that
it has its own:

- meaning;
- scope;
- identity need;
- lifecycle;
- authority;
- relationships;
- or governance implications.

Otherwise it may remain a property, attribute, role, state, relationship, or
concept.

---

# 18. Duplicate and Synonym Detection

The project shall actively test whether apparently different terms actually
refer to the same underlying concept.

For each suspected overlap:

```text
Term A
Term B
Shared Meaning?
Different Scope?
Different Lifecycle?
Different Authority?
Different Consumer?
Different Semantic Consequence?
```

Possible outcomes:

```text
Same Concept
Related Concepts
Distinct Concepts
One Is a Property / Role / State
Unresolved
```

The goal is not to eliminate vocabulary but to eliminate accidental duplication.

---

# 19. Legacy Comparison Rule

When a candidate concept resembles a legacy concept, the project should compare:

```text
Legacy Definition
New Candidate Definition
Purpose
Scope
Authority
Semantics
Dependencies
Historical Context
Evidence
```

Possible result:

```text
Equivalent
Partially Equivalent
Conceptually Related
Different
Historical Only
Requires Re-Research
```

Similarity in naming is never sufficient.

---

# 20. Concept Maturity

Each candidate should carry a research status such as:

```text
Candidate
Under Investigation
Supported
Validated
Contested
Deferred
Rejected
Superseded
```

A candidate becomes **Validated** only when the evidence and distinctions are
sufficient for the relevant discovery stage.

Validation does not automatically make the concept architectural.

---

# 21. Concept-to-Problem Traceability

Every material candidate concept should be traceable to one or more:

- problems;
- objectives;
- research questions;
- evidence sources.

Conceptually:

```text
Problem
  ↓
Objective
  ↓
Concept / Entity Candidate
  ↓
Evidence
  ↓
Validation
```

A concept with no meaningful problem, objective, or research justification should
be treated cautiously.

---

# 22. Initial Research Questions for Concept Discovery

The following questions should remain open during Step 6:

### Knowledge

- Is Knowledge an entity, a conceptual category, or both?
- What is the smallest independently governable semantic unit?
- What distinguishes knowledge from evidence, rule, document, and output?

### Document

- Is Document a semantic object, a representation, or a documentary abstraction?
- When does a document deserve independent identity?
- Can one semantic object have multiple documentary representations?

### Rule and Authority

- Is Rule an independent entity?
- Is Authority an entity, relationship, role, or property?
- What distinguishes authority from canonicality?

### Identity

- Which candidates genuinely require stable identity?
- Which only need identifiers as references?
- What is the minimum identity model required?

### Lifecycle

- Which candidates genuinely change over time?
- Which changes are revisions versus state transitions versus new identity?

### Production

- What is the fundamental production object?
- Is Production itself an entity, process, relationship, or lifecycle?

### Output and Publication

- What makes an output independently governable?
- Is Publication a process, event, state, or relationship?

### AI

- What is actually being consumed by AI?
- Does AI consume documents, knowledge objects, rules, relationships, or a
  resolved context assembled from them?

These questions should feed back into `UAICP-RQU-001`.

---

# 23. Non-Goals

This Model does not:

- establish final system layers;
- define final Universal taxonomy;
- establish final registries;
- define identifier syntax;
- establish governance ownership;
- prescribe document decomposition;
- or convert candidate concepts into canonical architecture.

---

# 24. Core Discovery Principle

> **Discover what must be distinct before deciding what must be built.**

A concept should become structurally important only when its distinction is
supported by evidence and has material consequences for the system.

---

# 25. Anti-Bootstrap Rule for Concept Discovery

The project shall not define a concept solely because a previous architecture
already contains a place for it.

Likewise, the project shall not reject a concept solely because the previous
architecture did not contain it.

The question is:

> **Does the new system genuinely require this distinction?**

---

# 26. Step 6 Exit Condition

Step 6 is sufficiently mature to proceed toward boundary discovery when:

- major candidate concepts and entities have been surfaced;
- important duplicates and overlaps have been investigated;
- entity versus concept distinctions are reasonably clear;
- major unresolved distinctions are visible;
- identity needs are not being assumed prematurely;
- candidate relationships have been identified without being treated as final;
- and the concept inventory can support the next stage of boundary discovery.

This is a **readiness condition**, not a claim that every concept has been fully
resolved.

---

# 27. Framework Evolution

This document may evolve as research produces stronger evidence.

Any revision should preserve its central function:

> **to identify and distinguish the conceptual building blocks of the system
> before those building blocks are prematurely turned into architecture.**
