---
document_id: UAICP-ARD-001
document_type: Architecture Discovery Model
title: Architecture Discovery Model
version: 1.1
status: DRAFT
canonicality: REFERENCE
scope: Root-level project methodology
authority: Project Research Framework
audience:
  - human
  - AI
purpose: >
  Establish the controlled discovery and assessment model for deriving candidate
  architectures from sufficiently supported research findings, architectural
  drivers, concerns, capability requirements, constraints, dependencies, quality
  concerns, alternatives, risks, and trade-offs without prematurely establishing
  final architecture, governance, document architecture, or implementation.
canonical_home: UAICP-ARD-001
supersedes: UAICP-ARD-001 v1.0
parent_context: UAICP-DCA-001
methodological_dependencies:
  - UAICP-FC-001
  - UAICP-RCC-001
  - UAICP-REF-001
  - UAICP-RQU-001
  - UAICP-POM-001
  - UAICP-CED-001
  - UAICP-BRD-001
  - UAICP-RDD-001
  - UAICP-DCA-001
---

# Architecture Discovery Model

## 1. Purpose

This document defines Step 10 of the root-level research and construction
methodology.

Its purpose is to discover and assess candidate architectures based on the
research performed in Steps 1–9.

Step 10 may:

- identify architectural drivers;
- identify architecture concerns;
- derive architectural capability requirements;
- identify constraints and invariants;
- explore architectural form hypotheses;
- construct credible architectural alternatives;
- assess quality attributes, scenarios, risks, sensitivities, and trade-offs;
- maintain architectural traceability;
- expose assumptions and architecture-specific unknowns;
- and produce an Architecture Decision Basis.

Step 10 does **not** establish the final architecture.

---

# 2. Scope and Level

Steps 1–10 are root-level methodology artifacts.

The word **Universal** is not used in the title of this document because Step 10
does not assume the architectural scope that discovery will ultimately produce.

Architecture Discovery may later determine that an architectural artifact belongs
to:

```text
Universal level
Domain level
Project level
Production level
Other justified scope
```

Scope is therefore a discovery outcome, not a naming assumption.

---

# 3. Methodological Position

```text
Step 1
Foundational Concept / North Star
        ↓
Step 2
Research & Construction Charter
        ↓
Step 3
Research & Evidence
        ↓
Step 4
Research Questions & Unknowns
        ↓
Step 5
Problem & Objective
        ↓
Step 6
Concept & Entity
        ↓
Step 7
Boundary & Responsibility
        ↓
Step 8
Relationship & Candidate Dependency
        ↓
Step 9
Dependency Analysis & Circularity Assessment
        ↓
Step 10
Architecture Discovery
        ↓
Architecture Decision Basis
        ↓
Future Architecture Decision
```

The methodological boundary is:

```text
Step 8
DISCOVER RELATIONSHIPS

Step 9
ASSESS DEPENDENCIES

Step 10
DISCOVER ARCHITECTURAL OPTIONS

Later
DECIDE / FORMALIZE ARCHITECTURE
```

---

# 4. Inputs From Previous Steps

Architecture Discovery may use:

```text
Problems
Objectives
Concepts
Entities
Responsibilities
Boundaries
Relationship Findings
Dependency Assessments
Circularity Assessments
Evidence
Constraints
Unknowns
```

Input maturity must remain visible.

For example:

```text
Candidate Concept
    ≠
Assessed Concept

Candidate Dependency
    ≠
Assessed Dependency

Research Hypothesis
    ≠
Architectural Fact
```

Unresolved findings must not silently become architectural facts.

---

# 5. Architecture Discovery Principles

## 5.1 Evidence Before Structure

Architecture must be derived from sufficiently supported findings.

## 5.2 Driver Before Response

Identify why architecture must address something before prescribing a structural
response.

## 5.3 Concern Before Component

Determine what architectural concern must be addressed before assigning it to a
component, document, registry, service, or other structure.

## 5.4 Capability Before Component

Identify architectural capability requirements before assigning responsibility
to specific structures.

## 5.5 Responsibility Before Ownership

Determine what must be done before deciding which structure owns or controls it.

## 5.6 Boundary Before Integration

Understand boundaries before designing integrations between them.

## 5.7 Dependency Before Structure

Use Step 9 dependency findings before selecting structural arrangements.

## 5.8 Alternatives Before Commitment

Material architectural choices should be compared with credible alternatives.

## 5.9 Architecture Before Implementation

Repository structures, software choices, file formats, or tools must not silently
determine semantic architecture.

## 5.10 No Premature Canonicalization

A candidate architecture is not automatically canonical.

---

# 6. Architecture Drivers

An **architecture driver** is a sufficiently supported factor that materially
influences architectural structure.

Examples may include:

```text
System Purpose
Material Problem
Material Objective
Required Quality
Governance Requirement
Knowledge Resolution Need
Authority Resolution Need
Identity Requirement
Context Requirement
Provenance Requirement
Validation Requirement
Lifecycle Requirement
Publication Requirement
AI Consumption Requirement
Automation Requirement
Scalability Requirement
Extensibility Requirement
Interoperability Requirement
Traceability Requirement
```

These are discovery categories, not a predetermined driver list.

Every material driver should be traceable to prior research.

---

# 7. Architecture Concerns

An **architecture concern** is an aspect of the architecture that must be
addressed because of one or more drivers, requirements, constraints, risks, or
stakeholder needs.

The distinction is:

```text
Driver
"What makes this matter?"

Concern
"What architectural question must be addressed?"
```

Example:

```text
Driver:
Reliable knowledge resolution is required.

Concern:
How should knowledge resolution be structured so that authority,
context, provenance, and applicability remain reliable?
```

Concerns should be connected to:

```text
Driver
Evidence
Scenario
Requirement
Risk
Architectural Response
```

---

# 8. Architectural Capability Requirements

An **architectural capability requirement** describes something the architecture
must enable, support, or expose.

It does not prescribe a component.

For example:

```text
Knowledge Resolution
```

does not automatically imply:

```text
Knowledge Registry
```

Likewise:

```text
Identity Resolution
```

does not automatically imply:

```text
Identity Service
```

A capability becomes architecturally material when its realization affects
boundaries, responsibilities, dependencies, quality attributes, governance,
lifecycle, or other structural concerns.

---

# 9. Capability Analysis

For each material architectural capability requirement, investigate:

```text
Capability
    ↓
Purpose
    ↓
Inputs
    ↓
Outputs
    ↓
Responsibilities
    ↓
Constraints
    ↓
Dependencies
    ↓
Consumers
    ↓
Providers
    ↓
Quality Concerns
```

The decomposition must stop before it becomes premature implementation design.

---

# 10. Architectural Constraints

Architecture must respect constraints discovered earlier.

Potential constraint categories include:

```text
Foundational Dependency Constraints
Authority Constraints
Boundary Constraints
Identity Constraints
Lifecycle Constraints
Provenance Constraints
Repository / Representation Constraints
Governance Constraints
Quality Constraints
Publication Constraints
```

A constraint must be traceable to evidence, a prior finding, an established
requirement, or an explicit higher-level principle.

---

# 11. Architectural Invariants

An **architectural invariant** is a condition that must remain true across valid
architecture alternatives.

Examples may include:

```text
Authority remains explicit.
Semantic identity remains distinguishable from representation.
Provenance remains traceable.
Foundational construction dependencies remain non-circular.
Canonical meaning does not depend solely on file location.
```

These are examples only.

An invariant must not be created merely because it sounds architecturally
desirable.

Every material invariant must be traceable to:

```text
Validated Problem
Requirement
Constraint
Dependency Finding
Governance Principle
or other sufficiently supported basis
```

---

# 12. Architectural Form Hypotheses

Architecture Discovery may explore possible structural forms.

Examples:

```text
Layered
Domain-Oriented
Capability-Oriented
Knowledge-Centered
Registry-Centered
Pipeline-Oriented
Hybrid
Other
```

These are **form hypotheses**, not an architecture taxonomy.

They are search-space aids only.

The project must not assume that a candidate architecture must conform to one of
these forms.

---

# 13. Candidate Architectures

A candidate architecture is a sufficiently concrete structural hypothesis that
can be assessed against the discovered requirements and concerns.

A candidate should identify, as appropriate:

```text
Major Structures
Responsibilities
Boundaries
Relationships
Dependencies
Information / Knowledge Flows
Authority Flows
Lifecycle Implications
Quality Implications
Operational Implications
```

A candidate architecture remains non-canonical during Step 10.

---

# 14. Architectural Alternatives

Where a material architectural choice exists, credible alternatives should be
considered.

For each alternative:

```text
Architecture Form
Strengths
Weaknesses
Dependencies
Constraints
Quality Impact
Risks
Trade-offs
Change Propagation
Governance Implications
Implementation Implications
```

The project need not create artificial alternatives when evidence clearly
indicates that a choice is immaterial or constrained.

---

# 15. Quality Attributes and Scenarios

Architecture candidates should be assessed against material quality concerns.

Potential attributes include:

```text
Correctness
Consistency
Traceability
Reliability
Maintainability
Extensibility
Interoperability
Scalability
Performance
Security
Recoverability
Auditability
AI Interpretability
```

These are examples, not mandatory universal requirements.

Only material quality concerns identified through research should be assessed.

Where useful, express a quality concern as a scenario:

```text
Stimulus
   ↓
Architectural Response
   ↓
Expected Quality
   ↓
Assessment / Measurement
```

---

# 16. Trade-off Analysis

Architecture may improve one concern while degrading another.

Therefore compare material alternatives through:

```text
Benefit
Cost
Risk
Complexity
Flexibility
Governance Burden
Change Propagation
Operational Consequence
Quality Impact
```

A candidate must not be preferred solely because it optimizes one attribute while
creating unacceptable consequences elsewhere.

---

# 17. Risk, Sensitivity, and Assumption Analysis

## 17.1 Risk

A condition that could cause failure or material degradation.

## 17.2 Sensitivity

An architectural decision whose change materially affects one or more quality
attributes or system properties.

## 17.3 Assumption

A proposition on which an architectural candidate relies but which is not yet
sufficiently established.

Assumptions must be tracked explicitly.

Example:

```text
A-001

Assumption:
Knowledge resolution can be structurally separated from production.

Status:
Unverified

Potential Impact:
High
```

An unverified high-impact assumption must not silently become an architectural
fact.

---

# 18. Architecture Unknowns

Architecture-specific unknowns must not create a second independent unknown
system.

When a question remains unresolved:

```text
Architecture Unknown
        ↓
UAICP-RQU-001
```

The question should be registered or linked through the existing Research
Questions & Unknowns framework.

Step 10 may add architectural context, impact, and priority to the existing
unknown.

This prevents duplicate unknown registries.

---

# 19. Dependency and Circularity Integration

Step 10 consumes Step 9.

It must consider:

```text
Foundational Dependencies
Dependency Chains
Construction / Definition Cycles
Authority Cycles
Implementation Dependencies
Change Propagation
```

A candidate architecture must not silently ignore an unresolved foundational
dependency or circularity finding.

Architecture Discovery may propose a structural response, but that response is a
**candidate architectural solution**, not a previously established fact.

---

# 20. Architecture Traceability

Every material architectural finding should be traceable backward.

A preferred chain is:

```text
Architecture Candidate
        ↓
Architectural Requirement / Concern
        ↓
Architecture Driver
        ↓
Problem / Objective / Constraint
        ↓
Research Finding
        ↓
Evidence
```

Where applicable, dependency and boundary findings should also be linked.

Traceability should answer:

> Why does this architectural structure exist?

The answer must not simply be:

> Because the architecture says so.

---

# 21. Legacy Architecture Treatment

Legacy architecture is evidence, not automatic authority.

For each significant legacy architectural element, assess:

```text
Retain
Adapt
Replace
Supersede
Ignore
Unknown
```

The classification must be evidence-based.

The required sequence is:

```text
Legacy Artifact
      ↓
Evidence
      ↓
Assessment
      ↓
Candidate Architectural Input
      ↓
Possible Retention / Adaptation / Replacement
```

Legacy architecture must not become the new architecture merely because it
already exists in a repository.

---

# 22. Repository and Representation Constraints

GitHub, Markdown, directory structures, naming conventions, file formats, and
other tools may impose representation or implementation constraints.

They must not silently determine semantic architecture.

The preferred relationship is:

```text
Semantic Architecture
        ↓
Representation
        ↓
Repository / Implementation
```

not:

```text
Repository
        ↓
Semantic Architecture
```

Repository constraints may influence later implementation and publication
decisions.

---

# 23. Architecture Assessment

Each candidate architecture should be assessed against material dimensions such
as:

```text
Research Alignment
Problem Coverage
Objective Coverage
Capability Coverage
Boundary Integrity
Dependency Integrity
Circularity Risk
Quality Attributes
Constraint Compliance
Invariant Compliance
Governance Implications
Change Propagation
Extensibility
Implementation Feasibility
Operational Complexity
```

Assessment results must remain traceable to their basis.

---

# 24. Rejected Alternatives

Material rejected alternatives should be retained when their rejection provides
useful architectural provenance.

For each:

```text
Alternative
Reason Considered
Reasons Rejected
Evidence
Risks
Trade-offs
```

This prevents repeated rediscovery of previously evaluated alternatives.

---

# 25. Architecture Decision Basis

The output of Step 10 is an **Architecture Decision Basis**, which may contain:

```text
Architecture Drivers
Architecture Concerns
Architectural Capability Requirements
Constraints
Invariants
Form Hypotheses
Candidate Architectures
Alternative Architectures
Quality Assessments
Trade-offs
Risks
Sensitivities
Assumptions
Dependency Findings
Rejected Alternatives
Traceability
Open Questions
Evidence
```

It does not itself establish final architecture.

---

# 26. Architecture Decision Boundary

Step 10 ends at:

```text
Architecture Discovery
        ↓
Architecture Assessment
        ↓
Architecture Decision Basis
```

A later process may establish:

```text
Architecture Decision
        ↓
Approved Architecture
```

The later decision must not be retroactively represented as if it had already
been established during Step 10.

---

# 27. No Automatic Document Creation

Step 10 shall not infer:

```text
Capability
    ↓
Document
```

or:

```text
Capability
    ↓
Registry
```

or:

```text
Architecture
    ↓
One File
```

The eventual document architecture must be discovered after the architecture is
sufficiently understood.

Therefore Step 10 must not prematurely create or mandate:

```text
Universal Architecture
Universal Governance
Universal Registry
Universal Standard
or any other core artifact
```

unless later discovery establishes that such artifacts are required.

---

# 28. No Forced Consolidation

A smaller document count is not automatically a better architecture.

Two concepts may require separate artifacts when their semantic responsibilities,
boundaries, lifecycle, authority, or consumers differ.

Conversely, multiple concepts may legitimately share an artifact when their
boundaries and responsibilities support that arrangement.

Document count must not be optimized independently of semantic and architectural
needs.

---

# 29. Architecture Scope Discovery

Architecture Discovery must determine whether an architectural structure belongs
to:

```text
Universal Level
Domain Level
Project Level
Production Level
Other justified scope
```

Scope must be derived from responsibility, applicability, authority, dependency,
and intended consumers.

The word "Universal" must not be applied merely because the project itself has a
Universal initiative.

---

# 30. AI Interpretation Rule

AI consumers must interpret this document as:

> **A controlled architecture discovery and assessment model.**

AI must not interpret:

- example capabilities;
- example drivers;
- example constraints;
- example invariants;
- example architectural forms;
- candidate architectures;
- or alternative architectures

as approved architecture.

Only later approved architectural artifacts may establish normative
architecture.

---

# 31. Outputs of Step 10

Step 10 may produce:

```text
Architecture Driver Set
Architecture Concern Set
Architectural Capability Requirements
Constraint Set
Invariant Set
Architectural Form Hypotheses
Candidate Architecture Set
Alternative Architecture Set
Quality Attribute Assessments
Trade-off Analysis
Risk Findings
Sensitivity Findings
Assumption Register
Architecture Traceability
Architecture Unknowns linked to RQU-001
Rejected Alternatives
Architecture Decision Basis
```

These outputs may become inputs to later architecture decision and documentation
work.

---

# 32. Step 10 Exit Condition

Step 10 is sufficiently mature to proceed toward architecture decision when:

- major architectural drivers are identified;
- material architecture concerns are explicit;
- architectural capability requirements are sufficiently understood;
- boundaries and responsibilities remain coherent;
- material dependencies are understood;
- unresolved foundational circularity is visible;
- architectural constraints are explicit;
- material invariants are justified;
- credible architectural alternatives have been considered where material;
- material quality concerns and scenarios have been assessed where relevant;
- material risks, sensitivities, and assumptions are documented;
- architectural traceability is sufficiently established;
- architecture-specific unknowns are linked to RQU-001;
- important rejected alternatives are traceable;
- and a defensible Architecture Decision Basis exists.

The objective is not to eliminate every unknown.

The objective is to ensure that architecture decisions can be made consciously,
with evidence, alternatives, risks, assumptions, and trade-offs visible.

---

# 33. Non-Goals

Step 10 does not:

- establish final architecture;
- establish governance;
- define canonical document structures;
- define registries;
- define lifecycle systems;
- specify implementation technology;
- establish repository structure as semantic architecture;
- automatically resolve every dependency;
- determine the final set of core project documents;
- or force all architectural capabilities into separate components or documents.

---

# 34. Core Principle

> **Discover architecture from sufficiently supported needs, capabilities,
boundaries, dependencies, constraints, quality concerns, alternatives,
assumptions, risks, and evidence—not from a predetermined component or
document list.**

More specifically:

> **Architecture is a reasoned response to discovered system needs and
constraints; it is not the starting assumption of the research.**

---

# 35. Framework Evolution

This model may evolve when architecture research reveals new evidence.

Any evolution must preserve:

```text
Research
    ↓
Discovery
    ↓
Assessment
    ↓
Architecture Decision Basis
    ↓
Architecture Decision
```

Later architectural decisions must not be retroactively represented as if they
had already been established during Step 10.
