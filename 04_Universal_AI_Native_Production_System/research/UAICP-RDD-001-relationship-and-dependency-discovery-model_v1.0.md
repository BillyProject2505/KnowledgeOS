---
document_id: UAICP-RDD-001
document_type: Relationship & Dependency Discovery Model
title: Universal Project Relationship & Dependency Discovery Model
version: 1.0
status: ACTIVE
canonicality: REFERENCE
scope: Universal AI-Native Production System — New Research & Construction Trajectory
authority: Project Research Framework
audience:
  - human
  - AI
purpose: >
  Establish the controlled discovery model for identifying, distinguishing, and
  validating relationships and candidate dependencies among concepts, entities,
  responsibilities, boundaries, and other subjects discovered in the preceding
  research stages, without prematurely converting those findings into
  architecture or implementation.
canonical_home: UAICP-RDD-001
supersedes: none
parent_context: UAICP-BRD-001
methodological_dependencies:
  - UAICP-FC-001
  - UAICP-RCC-001
  - UAICP-REF-001
  - UAICP-RQU-001
  - UAICP-POM-001
  - UAICP-CED-001
  - UAICP-BRD-001
---

# Universal Project Relationship & Dependency Discovery Model

## 1. Purpose

This document defines Step 8 of the Universal AI-Native Production System
research trajectory.

Its purpose is to discover:

- how candidate concepts and entities relate;
- what kinds of relationships exist;
- which relationships are merely associative;
- which relationships carry authority, lifecycle, provenance, scope, or other
  semantic consequences;
- which relationships create a genuine dependency;
- what direction a candidate dependency appears to have;
- and which questions must remain unresolved for later dependency and circularity
  analysis.

Step 8 is a **discovery artifact**.

It does not define the final relationship graph, dependency graph, architecture,
registry model, document structure, or implementation.

---

# 2. Methodological Position

The project currently follows this discovery sequence:

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
UAICP-RDD-001
Relationship & Dependency Discovery
        ↓
STEP 9
Dependency Direction & Circularity Analysis
        ↓
ARCHITECTURE DISCOVERY
```

The distinction is intentional:

```text
Step 6
What may exist?

Step 7
What is each thing responsible for and where does that responsibility stop?

Step 8
How do those things relate, and which relationships may constitute dependency?

Step 9
What is the dependency direction, strength, transitivity, and circularity risk?

Architecture
What structure should ultimately exist?
```

---

# 3. Alignment With Previous Steps

## 3.1 North Star Alignment

The North Star establishes the intended direction toward an AI-native production
foundation capable of resolving knowledge, authority, context, rules, production
requirements, validation, provenance, and publication.

Step 8 investigates relationships needed to support those capabilities.

It shall not assume that every capability requires an independent relationship
object or architecture component.

## 3.2 Construction Charter Alignment

The Construction Charter requires:

- research before architecture;
- discovery before construction;
- semantic before representational reasoning;
- explicit dependencies;
- anti-loop safeguards;
- anti-bootstrap safeguards;
- modularity without unnecessary fragmentation;
- and architectural restraint.

Step 8 operationalizes the relationship/dependency portion of those principles
without becoming architecture itself.

## 3.3 Evidence Alignment

Relationship findings remain subject to the evidence discipline established by
`UAICP-REF-001`.

A relationship is not confirmed merely because it appears intuitive.

The project should distinguish:

```text
Observed
Hypothesized
Supported
Validated
Contested
Rejected
```

## 3.4 Unknowns Alignment

Relationship questions are explicitly allowed to remain unresolved.

Step 8 shall feed material unresolved questions back to `UAICP-RQU-001` rather
than forcing premature relationship decisions.

## 3.5 Problem / Objective Alignment

A relationship should have a reason for being relevant to the system.

Where practical:

```text
Problem
  ↓
Objective
  ↓
Concept / Entity
  ↓
Relationship
  ↓
Candidate Dependency
```

## 3.6 Concept / Entity Alignment

Step 8 must use the candidate concepts/entities from `UAICP-CED-001` without
treating them as final ontology.

## 3.7 Boundary / Responsibility Alignment

Step 8 must respect the boundaries discovered in `UAICP-BRD-001`.

A relationship must not silently transfer responsibility from one candidate to
another.

---

# 4. Relationship Principle

A relationship means:

> **Two or more subjects have a meaningful semantic, functional, contextual,
> temporal, governance, or representational connection.**

A relationship does not automatically mean:

- dependency;
- ownership;
- authority;
- lifecycle control;
- inheritance;
- containment;
- or implementation coupling.

The project shall determine the relationship type before drawing architectural
conclusions from it.

---

# 5. Relationship vs Dependency

This distinction is fundamental.

## Relationship

```text
A is related to B.
```

This establishes a meaningful connection.

## Dependency

```text
A requires B in order to perform, remain valid, or satisfy a material
responsibility.
```

This establishes a directional requirement.

Therefore:

```text
Relationship
    ≠
Dependency
```

A relationship may exist without dependency.

A dependency is a special case of relationship only when the requiredness and
direction are sufficiently justified.

---

# 6. Dependency Candidate

A **Candidate Dependency** exists when there is evidence that a subject cannot
perform a material responsibility, remain valid, or satisfy a material
constraint without another subject.

For every candidate dependency, ask:

```text
What does A require from B?
Why is B required?
Is the requirement semantic or merely implementation-specific?
Is it mandatory or optional?
Can A remain valid without B?
Can the dependency be reversed?
Is the dependency temporal?
Is it transitive?
```

The answer may remain unresolved.

---

# 7. Relationship Contract

Each material candidate relationship should record:

```text
Relationship ID
Subject
Object
Relationship Type
Direction
Purpose
Semantic Meaning
Scope
Temporal Behavior
Cardinality / Multiplicity
Authority Relevance
Lifecycle Relevance
Provenance Relevance
Dependency Candidate
Dependency Reason
Implementation Dependence
Evidence
Open Questions
Research Status
Confidence
```

This is a discovery record, not a final schema.

---

# 8. Relationship Type Discovery

The following are initial research categories.

They are not a final taxonomy.

```text
Semantic
Reference
Representation
Containment
Derivation
Composition
Context
Scope
Authority
Governance
Lifecycle
Provenance
Consumption
Production
Publication
Validation
Dependency
```

A candidate relationship may ultimately prove to be:

- one of these;
- a combination;
- a more specific type;
- a property rather than a relationship;
- or not materially distinct.

---

# 9. Directionality

Relationships must not automatically be treated as bidirectional.

Consider:

```text
A → relates to → B
```

This does not prove:

```text
B → depends on → A
```

or:

```text
B → governs → A
```

For each candidate relationship, investigate:

```text
A → B
B → A
A ↔ B
Context-dependent
Temporal
Unknown
```

Direction must be based on semantic meaning, not diagram convenience.

---

# 10. Relationship vs Ownership

The fact that:

```text
A → has relationship with → B
```

does not imply:

```text
A owns B
```

Ownership requires separate justification.

Potential distinctions include:

```text
Association
Reference
Responsibility
Control
Authority
Ownership
Custody
Consumption
```

These must not be collapsed.

---

# 11. Relationship vs Authority

Authority is especially sensitive.

For example:

```text
A references B
```

does not imply:

```text
A has authority over B
```

Similarly:

```text
A publishes B
```

does not automatically imply:

```text
A defines B
```

Authority relationships require explicit evidence of decision rights or
governing legitimacy.

---

# 12. Relationship vs Representation

A representation relationship describes how one subject expresses another.

For example:

```text
Representation
      ↓
expresses
      ↓
Semantic Subject
```

This must remain distinct from:

```text
Semantic dependency
Governance dependency
Operational dependency
```

A Markdown file may represent a governed subject without becoming the source of
that subject's semantic identity.

---

# 13. Relationship vs Lifecycle

A lifecycle relationship describes how subjects participate in or affect
lifecycle progression.

It does not automatically mean:

```text
A owns B's lifecycle.
```

Investigate separately:

- lifecycle participation;
- lifecycle control;
- lifecycle dependency;
- lifecycle observation;
- lifecycle history.

---

# 14. Relationship vs Provenance

Provenance may connect:

```text
Output
  ← derived from ←
Production
  ← consumed ←
Knowledge
  ← supported by ←
Evidence
```

These relationships may contribute to provenance but must not automatically be
collapsed into a single "provenance relationship."

Provenance may ultimately require temporal events, transformations, or other
structures discovered later.

---

# 15. Candidate Relationship Surface

The following relationships are intentionally provisional.

## R-001 — Document ↔ Knowledge

Questions:

- Does a document represent knowledge?
- Does it organize knowledge?
- Can knowledge exist without a document?
- Can multiple documents represent the same semantic subject?
- Does the document depend on the knowledge or merely represent it?

Possible result:

```text
Representation
Reference
Organization
Dependency
Multiple Relationships
Unresolved
```

---

## R-002 — Production → Knowledge

Questions:

- Does production consume applicable knowledge?
- Is the dependency mandatory?
- Does production depend on a resolved context rather than raw knowledge?
- Can production proceed with incomplete knowledge?

---

## R-003 — Rule → Production

Questions:

- Does a rule constrain production?
- Does production depend on the rule?
- Does the rule govern the production process or only its output?
- Is the relationship contextual?

---

## R-004 — Authority → Rule / Decision / Subject

Questions:

- Does authority govern the subject?
- Is authority a relationship or property?
- What establishes the relationship?
- Can authority expire or change?

---

## R-005 — Evidence → Finding / Decision / Knowledge

Questions:

- Does evidence support a claim?
- Does it establish a decision?
- Does it become knowledge?
- Is the relationship temporal?

---

## R-006 — Provenance → Subject

Questions:

- What does provenance trace?
- Is provenance attached to a subject, event, transformation, or relationship?
- Does provenance itself create dependencies?

---

## R-007 — Lifecycle → Subject

Questions:

- Does lifecycle describe state progression?
- Who or what triggers transitions?
- Does the lifecycle depend on another subject?

---

## R-008 — Intent → Production

Questions:

- Does intent initiate production?
- Is intent a persistent subject or interaction event?
- Is production dependent on resolved intent?

---

## R-009 — Production → Output

Questions:

- Is output derived from production?
- Does the output have independent identity?
- Does production remain part of output provenance?

---

## R-010 — Output → Publication

Questions:

- Does publication act on an output?
- Is publication a lifecycle transition, event, activity, or relationship?
- Can an output exist without publication?

---

## R-011 — Project ↔ Knowledge

Questions:

- Is knowledge scoped to a project?
- Can knowledge be shared across projects?
- Does project scope determine applicability?
- Does project ownership imply authority?

---

## R-012 — AI Consumer → Governed Context

Questions:

- Does AI consume a resolved context rather than individual documents?
- Is this a consumption relationship or dependency?
- Which responsibilities remain with AI versus the governed knowledge system?

---

# 16. Relationship Cardinality

Cardinality should be discovered only when materially relevant.

Possible forms:

```text
One-to-One
One-to-Many
Many-to-One
Many-to-Many
Conditional
Temporal
Unknown
```

Cardinality should not be invented merely to complete a diagram.

---

# 17. Temporal Relationships

A relationship may exist only:

```text
before
after
during
until
from
within a validity interval
```

For each material temporal relationship, investigate:

- start condition;
- end condition;
- effective time;
- historical validity;
- current validity;
- and whether the relationship changes without changing subject identity.

Temporal validity is not the same as lifecycle.

---

# 18. Conditional Relationships

Some relationships exist only when conditions are satisfied.

Conceptually:

```text
A
 ── relates to B when condition X is true
```

The project should distinguish:

```text
Always
Conditional
Contextual
Temporal
Derived
Unknown
```

This prevents conditional relationships from being mistaken for universal
architecture dependencies.

---

# 19. Dependency Classification

Candidate dependencies should initially be classified as:

```text
Mandatory
Optional
Conditional
Temporal
Derived
Informational
Operational
Semantic
Governance
Implementation-Specific
Unknown
```

This classification is provisional.

In particular:

> **Implementation-specific dependency must not be promoted into semantic
> architecture merely because it exists in the current toolchain.**

---

# 20. Semantic vs Implementation Dependency

This distinction is mandatory.

## Semantic Dependency

A dependency exists because the meaning or validity of A materially requires B.

Example form:

```text
A cannot be correctly interpreted without B.
```

## Implementation Dependency

A dependency exists because the current implementation happens to use B.

Example form:

```text
A currently reads B because the software was implemented that way.
```

The second does not prove the first.

This distinction protects the architecture from becoming a reflection of current
repository or software constraints.

---

# 21. Dependency Evidence Test

Before treating a relationship as a dependency, ask:

```text
1. What responsibility of A is affected?
2. What does B provide?
3. Is B necessary?
4. What happens if B is unavailable?
5. Is the failure semantic, operational, or merely implementation-specific?
6. Can another subject provide the same requirement?
7. Is the dependency reversible?
8. Is the dependency temporary?
```

Only sufficiently supported dependencies should proceed as candidates for Step 9.

---

# 22. Relationship Matrix

The project should eventually be able to record relationships in a matrix such
as:

| Subject | Relationship | Object | Dependency Candidate | Direction | Evidence Status |
|---|---|---|---|---|---|
| Document | represents | Knowledge | Possible | Document → Knowledge | OPEN |
| Production | consumes | Knowledge | Possible | Production → Knowledge | OPEN |
| Rule | constrains | Production | Possible | Rule → Production | OPEN |
| Evidence | supports | Decision | Possible | Evidence → Decision | OPEN |
| Production | produces | Output | Possible | Production → Output | OPEN |
| Output | published through | Publication | Possible | Output → Publication | OPEN |
| AI Consumer | consumes | Governed Context | Possible | AI → Context | OPEN |

This matrix is a research instrument, not a final architecture graph.

---

# 23. Dependency Chain Discovery

Where multiple candidate dependencies exist, record the chain without yet
deciding whether it is acceptable:

```text
A
 ↓
B
 ↓
C
```

Then ask:

```text
Is A → B genuine?
Is B → C genuine?
Does A therefore transitively depend on C?
Is any link optional?
Is any link contextual?
```

This prepares the system for Step 9.

---

# 24. Circularity Is Not Resolved in Step 8

Step 8 may **detect a possible cycle**, but it shall not perform the final
circularity judgment.

For example:

```text
A → B
B → C
C → A
```

Step 8 records:

```text
Potential Circular Dependency: YES
```

Step 9 determines:

- whether the links are genuine dependencies;
- whether they are directional;
- whether the cycle is foundational;
- whether the cycle is contextual;
- whether it is resolvable;
- and what corrective options exist.

This prevents Step 8 from silently becoming architecture analysis.

---

# 25. Relationship Conflict Detection

The project should detect contradictory claims such as:

```text
A → governs → B

B → governs → A
```

or:

```text
A → depends on → B
B → independent of → A
```

or:

```text
A represents B
B represents A
```

Such conflicts should be recorded as research issues rather than resolved by
intuition.

---

# 26. Relationship Duplication Detection

Two relationship types should be compared when they appear to mean the same
thing.

Compare:

```text
Name
Meaning
Direction
Purpose
Scope
Authority
Lifecycle
Consumer
Dependency Consequence
```

Possible outcomes:

```text
Same Relationship
Distinct Relationships
One Is a Specialization
One Is Derived
One Is Implementation-Specific
Unresolved
```

This prevents relationship taxonomy from growing unnecessarily.

---

# 27. Legacy Relationship Treatment

Legacy documents may be consulted after the Step 1–7 conceptual baseline has
been established.

Legacy material may provide:

- examples;
- historical relationship patterns;
- known dependency failures;
- terminology;
- implementation evidence.

It shall not establish the new relationship model automatically.

The project must distinguish:

```text
Historical Relationship
Candidate Relationship
Current Validated Relationship
```

---

# 28. Anti-Bootstrap Safeguards

Step 8 shall not:

- inherit a legacy relationship graph;
- assume existing registry dependencies;
- infer semantic dependency from repository links;
- infer authority from authorship;
- infer ownership from containment;
- infer dependency from sequence alone;
- or create architecture to satisfy a relationship that has not been validated.

The guiding question is:

> **What relationship actually exists, and what consequence follows from it?**

---

# 29. AI Interpretation Rule

AI consumers shall interpret this document as a **relationship and candidate
dependency discovery map**.

AI shall not treat:

- candidate relationship types;
- candidate directions;
- dependency candidates;
- cardinalities;
- or example chains

as final architecture.

Unresolved relationships must remain unresolved.

---

# 30. Step 8 Exit Condition

Step 8 is sufficiently mature to proceed to Step 9 when:

- principal relationships among discovered candidates have been surfaced;
- relationship types are sufficiently differentiated;
- candidate dependencies are explicitly distinguished from ordinary
  relationships;
- directionality has been examined;
- semantic and implementation dependencies are separated;
- possible dependency chains are visible;
- possible circularities are recorded but not prematurely resolved;
- contradictory relationship claims are visible;
- material unknowns are fed back into `UAICP-RQU-001`;
- and no relationship has been accepted solely because it existed in legacy
  architecture or current implementation.

This does not require every relationship to be final.

It requires the relationship/dependency landscape to be sufficiently explicit for
formal dependency and circularity analysis.

---

# 31. Core Discovery Principle

> **Discover relationships before designing the graph, and discover dependencies
> before designing the architecture.**

More specifically:

> **Not every relationship is a dependency, and not every dependency belongs in
> architecture.**

---

# 32. Framework Evolution

This model may evolve as Step 9 reveals stronger evidence.

Any revision should preserve its central methodological rule:

> **Relationships and dependencies must be discovered, differentiated, and
> justified before they are converted into architecture, governance structures,
> registries, document boundaries, or implementation mechanisms.**
