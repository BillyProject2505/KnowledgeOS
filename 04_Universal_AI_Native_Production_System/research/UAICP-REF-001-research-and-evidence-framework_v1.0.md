---
document_id: UAICP-REF-001
document_type: Research & Evidence Framework
title: Universal Project Research & Evidence Framework
version: 1.0
status: ACTIVE
canonicality: REFERENCE
scope: Universal AI-Native Production System — New Research & Construction Trajectory
authority: Project Research Framework
audience:
  - human
  - AI
purpose: >
  Establish the methodological rules for identifying, classifying, evaluating,
  comparing, recording, and adopting research evidence before substantive
  architectural or normative decisions are made.
canonical_home: UAICP-REF-001
supersedes: none
parent_context: UAICP-RCC-001
---

# Universal Project Research & Evidence Framework

## 1. Purpose

This Framework establishes how the new project determines what information is
usable as research evidence before that information is allowed to influence
architecture, governance, specifications, or other normative decisions.

Its purpose is to prevent:

- assumption becoming evidence;
- reference material becoming authority;
- historical material becoming current truth;
- implementation convenience becoming semantic justification;
- repeated statements being mistaken for independent evidence;
- hypotheses becoming architecture without validation;
- and unresolved uncertainty being hidden by premature decisions.

This Framework governs **evidence handling**, not the final architecture of the
system.

---

# 2. Relationship to the Research & Construction Charter

`UAICP-RCC-001 — Universal Project Research & Construction Charter` defines the
overall construction method and anti-loop / anti-bootstrap safeguards.

This Framework defines the evidence discipline used inside that method.

The relationship is:

```text
North Star
    ↓
Research & Construction Charter
    ↓
Research & Evidence Framework
    ↓
Evidence / Sources
    ↓
Research Findings
    ↓
Concept Discovery
    ↓
Architecture Discovery
```

Neither the Framework nor any source used by it automatically becomes
architectural authority.

---

# 3. Core Research Principles

## 3.1 Evidence Before Authority

A source may provide evidence without possessing authority over the new system.

## 3.2 Source Existence Does Not Equal Truth

The existence of a document, repository artifact, implementation, or prior
decision does not establish that its assertions are correct for the new project.

## 3.3 Historical Is Not Current

Historical decisions remain evidence of what happened, not automatic evidence of
what should be true now.

## 3.4 Repetition Is Not Independence

Multiple documents repeating the same statement do not automatically constitute
multiple independent evidence sources.

## 3.5 Similarity Is Not Equivalence

A concept that looks similar to an existing concept is not automatically the
same concept.

## 3.6 Absence of Evidence Is Not Evidence of Absence

Failure to find a concept in the current corpus does not by itself establish
that the concept is unnecessary.

## 3.7 Uncertainty Must Remain Visible

Where evidence is insufficient, uncertainty shall remain explicit.

> **Unknown is an acceptable research state.**

## 3.8 Research Does Not Require Immediate Closure

The objective of research is not to eliminate every open question immediately.
The objective is to reduce uncertainty sufficiently and honestly for the next
authorized stage.

---

# 4. Research Source Classes

Sources shall be classified before their substantive claims are used.

Initial source classes are:

```text
S1 — Direct Evidence
S2 — Authoritative External Source
S3 — Project Artifact
S4 — Legacy Reference
S5 — Implementation Evidence
S6 — Derived Analysis
S7 — Hypothesis / Proposal
S8 — Unverified Material
```

These classes describe **research role**, not automatic authority.

## S1 — Direct Evidence

Primary material that directly establishes a fact, event, requirement, behavior,
or observed condition relevant to the research question.

## S2 — Authoritative External Source

External standards, official technical documentation, regulations, specifications,
or other authoritative sources applicable to the research question.

## S3 — Project Artifact

A document or artifact produced within the current project trajectory.

Its status depends on its own maturity and does not automatically make its claims
true.

## S4 — Legacy Reference

Material inherited from previous Universal / KnowledgeOS / OBK / KDS /
Coz We Care or related work.

It is useful for historical understanding, pattern discovery, and lessons learned.

It does not automatically transfer authority.

## S5 — Implementation Evidence

Observed behavior or consequences from an actual implementation.

Implementation evidence may reveal constraints or defects but does not
automatically determine semantic architecture.

## S6 — Derived Analysis

A conclusion produced by reasoning across other sources.

Derived analysis must remain traceable to its source inputs.

## S7 — Hypothesis / Proposal

A proposed explanation, model, mechanism, or design idea that has not yet been
sufficiently validated.

## S8 — Unverified Material

Material whose provenance, reliability, applicability, or interpretation is not
yet sufficiently established.

It may support further investigation but should not silently become normative
basis.

---

# 5. Claim Classification

Research shall distinguish source material from individual claims.

A claim may be classified as:

```text
Observed
Documented
Supported
Inferred
Hypothesized
Contested
Unknown
```

A document can therefore contain multiple claim classes.

The project should avoid treating an entire document as uniformly authoritative
merely because some portions are reliable.

---

# 6. Evidence Strength

Evidence strength should be evaluated independently from source class.

A preliminary scale is:

```text
E0 — No meaningful support
E1 — Weak support
E2 — Limited support
E3 — Substantial support
E4 — Strong support
E5 — Direct / highly authoritative support
```

Evidence strength should consider:

- source reliability;
- directness;
- independence;
- consistency;
- applicability;
- recency where relevant;
- provenance;
- and the nature of the claim.

The scale is a research aid, not itself a normative authority system.

---

# 7. Applicability

Evidence must be evaluated for applicability to the new project.

For each material claim, consider:

```text
Domain
Scope
Time
Context
Assumptions
Purpose
```

A source may be highly credible but irrelevant to the specific question being
researched.

Likewise, a legacy project document may be highly applicable to understanding
historical implementation while being inappropriate as current architectural
authority.

---

# 8. Independence

Research should distinguish:

```text
Independent Evidence
        ≠
Repeated Evidence
        ≠
Derived Evidence
```

For example, if five project documents copied the same original rule, they should
not be treated as five independent confirmations.

Where possible, identify the underlying source lineage.

---

# 9. Provenance of Findings

Every material research finding should be traceable to its supporting evidence.

Conceptually:

```text
Source
   ↓
Claim
   ↓
Evaluation
   ↓
Finding
   ↓
Decision Candidate
```

A finding without traceable support should remain clearly marked as a hypothesis,
interpretation, or unresolved question.

---

# 10. Legacy Adoption Protocol

Legacy material shall move through the following conceptual path before it can
influence a new foundational decision:

```text
Legacy Artifact
      ↓
Identify
      ↓
Classify
      ↓
Extract Relevant Claim / Concept
      ↓
Assess Applicability
      ↓
Assess Evidence
      ↓
Compare With Other Evidence
      ↓
Adopt / Adapt / Retain as Reference / Reject
      ↓
Record Decision
```

Possible outcomes include:

```text
Reference Only
Historical
Candidate
Adopted
Adapted
Superseded
Rejected
Pending Validation
```

The adoption outcome must not erase the historical status of the original
artifact.

---

# 11. Hypothesis Discipline

A hypothesis shall be explicitly identified as a hypothesis.

Minimum information should include:

```text
Hypothesis
Why it is plausible
Evidence supporting it
Evidence against it
Assumptions
What would confirm it
What would falsify it
Current confidence
Affected decisions
```

A hypothesis shall not silently become an architectural invariant.

---

# 12. Contradictory Evidence

When credible sources conflict, the project shall not resolve the conflict by
simply choosing the most convenient source.

The process should be:

```text
Conflict Identified
        ↓
Check Scope
        ↓
Check Authority
        ↓
Check Time
        ↓
Check Context
        ↓
Check Source Independence
        ↓
Check Definitions
        ↓
Identify Genuine Conflict or Apparent Conflict
        ↓
Resolve / Preserve as Open Question
```

Where the conflict remains unresolved, it should remain visible.

---

# 13. Research Finding Categories

Material findings should be classified, for example, as:

```text
F1 — Confirmed Finding
F2 — Supported Finding
F3 — Preliminary Finding
F4 — Contradicted Finding
F5 — Open Finding
```

A finding becomes a decision candidate only when the applicable evidence and
reasoning are sufficiently mature.

---

# 14. Evidence-to-Decision Boundary

The project shall maintain a clear separation:

```text
Evidence
   ↓
Finding
   ↓
Interpretation
   ↓
Decision
```

Evidence does not automatically become a decision.

Likewise, a decision must not be presented as though it were directly observed
evidence when it is actually a design choice.

---

# 15. Research Artifact Minimum Contract

A material research artifact should identify, where applicable:

```text
Research Artifact ID
Research Question
Source(s)
Claim(s)
Source Class
Claim Class
Applicability
Evidence Strength
Independence
Finding
Confidence
Open Questions
Decision Impact
Provenance
```

This does not require every note or exploratory thought to become a formal
artifact.

The contract applies to material research outputs that may influence later
architecture or governance.

---

# 16. Research Question Boundary

A research question should identify:

- what needs to be known;
- why it matters;
- what decisions may depend on it;
- what evidence could answer it;
- what remains unknown;
- and what would constitute sufficient resolution.

A research question should not be written in a way that presupposes its desired
answer.

Prefer:

> "What identity mechanisms are actually required by the system?"

over:

> "Which identity registry should we build?"

The second question assumes a solution before the problem has been sufficiently
researched.

---

# 17. Research Sequence

The initial research sequence is:

```text
Research Question
    ↓
Source Discovery
    ↓
Source Classification
    ↓
Claim Extraction
    ↓
Evidence Evaluation
    ↓
Applicability Assessment
    ↓
Cross-Source Comparison
    ↓
Finding
    ↓
Open Questions / Hypotheses
    ↓
Decision Candidate
```

Architecture should occur only after the relevant discovery and evidence maturity
is sufficient.

---

# 18. AI Research Consumption

AI may assist with:

- source discovery;
- extraction;
- comparison;
- summarization;
- classification;
- contradiction detection;
- relationship discovery;
- hypothesis generation.

AI shall not silently promote its own generated interpretation into evidence or
authority.

AI-generated analysis should remain distinguishable from source material.

Conceptually:

```text
Human / External Source
        ↓
Source Evidence
        ↓
AI Analysis
        ↓
Research Finding
        ↓
Human / Governed Validation
```

---

# 19. Research Completeness Does Not Mean Exhaustiveness

Research completion does not require finding every document in existence.

A research stage may be considered sufficiently mature when:

- relevant source classes have been considered;
- material evidence has been evaluated;
- important contradictions are visible;
- important uncertainties are recorded;
- the applicable decision question can be answered with justified confidence;
- and no known unresolved issue creates an unacceptable architectural risk.

The maturity threshold should be proportional to the decision being made.

---

# 20. Evidence Change and Reassessment

When new evidence materially changes an earlier finding, the project should
record:

```text
New Evidence
      ↓
Affected Finding
      ↓
Affected Decision
      ↓
Affected Dependency
      ↓
Required Reassessment
```

A new source should not silently invalidate prior work without tracing the impact.

---

# 21. Research Stop Conditions

Research may stop for a specific question when one of the following is true:

```text
Resolved
Resolved with explicit uncertainty
Decision is sufficiently supported
Question is intentionally deferred
Question is no longer relevant
```

"Unable to find more information" is not by itself a sufficient stop condition
for a high-impact unresolved question.

---

# 22. Non-Goals

This Framework does not:

- define the final Universal Architecture;
- determine final governance;
- establish final canonicality;
- prescribe a final document hierarchy;
- determine the final registry model;
- define production automation;
- or guarantee that every research question has a single objective answer.

It provides the discipline through which such decisions may later be made.

---

# 23. Research Integrity Rule

> **Do not make the evidence fit the architecture. Make the architecture answer to the evidence.**

When evidence contradicts a preferred model, the correct response is to:

- inspect the evidence;
- inspect the assumptions;
- inspect the model;
- and revise the model where justified.

The project shall not selectively retain evidence merely because it supports a
desired architecture.

---

# 24. Final Evidence Principle

> **Evidence informs decisions.  
> Findings organize evidence.  
> Decisions define the system.  
> Authority governs decisions.  
> Canonicality records approved system truth.**

These are distinct stages and should not be collapsed into one.

---

# 25. Framework Evolution

This Framework may evolve as the project gains experience.

Any revision should preserve its core objective:

> **to ensure that foundational decisions are traceable, evidence-aware,
> uncertainty-aware, and protected from circular reasoning or inherited
> assumptions.**
