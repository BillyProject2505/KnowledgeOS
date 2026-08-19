---
document_id: UAICP-RQU-001
document_type: Research Questions & Unknowns Framework
title: Universal Project Research Questions & Unknowns Framework
version: 1.0
status: ACTIVE
canonicality: REFERENCE
scope: Universal AI-Native Production System — New Research & Construction Trajectory
authority: Project Research Framework
audience:
  - human
  - AI
purpose: >
  Establish the structure for identifying, classifying, prioritizing, tracking,
  and resolving material research questions and unknowns before they are allowed
  to become architectural, governance, or implementation assumptions.
canonical_home: UAICP-RQU-001
supersedes: none
parent_context: UAICP-REF-001
---

# Universal Project Research Questions & Unknowns Framework

## 1. Purpose

This Framework establishes how the project records what it does not yet know.

Its purpose is to prevent:

- unanswered questions being hidden;
- assumptions being mistaken for findings;
- open issues being silently resolved through document drafting;
- architecture being used to answer questions that research has not answered;
- decisions being made merely because progress appears blocked;
- and unresolved foundational uncertainty being carried invisibly into later
  system layers.

The central rule is:

> **Unknown is an explicit state, not a failure condition.**

---

# 2. Relationship to Prior Methodology

The methodological chain is:

```text
UAICP-FC-001
North Star
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
Research
    ↓
Findings
    ↓
Discovery
    ↓
Architecture
```

This Framework does not answer the research questions it records.

It establishes the discipline for handling them.

---

# 3. What Counts as a Material Unknown

An unknown is material when resolving it could materially affect one or more of:

- system scope;
- system boundaries;
- concept definitions;
- relationships;
- authority;
- identity;
- document architecture;
- lifecycle;
- registry requirements;
- AI consumption;
- production architecture;
- automation;
- or major implementation assumptions.

Minor uncertainties that do not affect architecture, governance, or material
research may remain as ordinary working notes.

---

# 4. Research Question Contract

Each material research question should have, where applicable:

```text
Question ID
Question
Purpose
Why It Matters
Affected Domain
Affected Concepts
Known Evidence
Current Hypotheses
Unknowns
Decision Dependency
Blocking Status
Priority
Confidence
Research Owner
Resolution Criteria
Resolution Status
Resolution Evidence
Decision Impact
Date Opened
Date Resolved
```

The minimum required fields may be reduced for exploratory questions, but
material architectural questions should retain sufficient traceability.

---

# 5. Question Classes

Research questions should be classified by what they seek to establish.

Initial classes:

```text
RQ-C — Concept Question
RQ-B — Boundary Question
RQ-R — Relationship Question
RQ-A — Authority Question
RQ-I — Identity Question
RQ-S — Scope Question
RQ-L — Lifecycle Question
RQ-D — Documentary Question
RQ-K — Knowledge / Semantic Question
RQ-T — Technical / Implementation Question
RQ-P — Production Question
RQ-AI — AI Consumption Question
RQ-AU — Automation Question
```

A question may have more than one classification where necessary.

---

# 6. Question Maturity

Each question has a maturity state.

```text
OPEN
↓
UNDER INVESTIGATION
↓
EVIDENCE SUFFICIENT
↓
ANSWERED
↓
VALIDATED
↓
DECISION-READY
↓
CLOSED
```

Possible alternate outcomes:

```text
DEFERRED
NO LONGER RELEVANT
MERGED
SPLIT
INVALID QUESTION
```

Closing a question does not automatically create a normative decision.

---

# 7. Priority

Priority should be assessed according to impact, not curiosity.

Initial priority levels:

```text
P0 — Foundational Blocker
P1 — Major Architectural Impact
P2 — Significant System Impact
P3 — Local / Limited Impact
P4 — Exploratory / Non-blocking
```

A P0 or P1 question should not be silently bypassed when its unresolved state
creates material architectural risk.

---

# 8. Blocking Status

Each question should indicate whether unresolved status blocks progression.

```text
BLOCKING
CONDITIONALLY BLOCKING
NON-BLOCKING
DEFERRED
```

A non-blocking question may remain open while work proceeds elsewhere.

A blocking question requires explicit treatment before the affected phase can
pass its gate.

---

# 9. Question Dependency

Questions may depend on other questions.

Conceptually:

```text
RQ-001
  ↓
RQ-002
  ↓
RQ-003
```

The project must distinguish:

```text
Question Dependency
        ≠
Artifact Dependency
```

A question may depend on another question being resolved without making the
corresponding future documents dependent in the same way.

---

# 10. No Assumption Closure

The project shall not close a question merely because:

- a document needs to be written;
- a phase is approaching a deadline;
- an implementation is easier with a particular answer;
- a previous project used a particular model;
- a filename suggests an answer;
- or AI has produced a plausible response.

An answer must be supported according to the applicable Research & Evidence
Framework.

---

# 11. Hypothesis Handling

A research question may have one or more hypotheses.

```text
Question
   ↓
Hypothesis A
Hypothesis B
Hypothesis C
   ↓
Evidence
   ↓
Comparison
   ↓
Finding
```

Multiple competing hypotheses should remain visible when they are materially
plausible.

The project should not silently collapse alternatives merely to simplify
documentation.

---

# 12. Unknown Types

Unknowns should be classified where useful.

```text
UNKNOWN-CONCEPT
UNKNOWN-BOUNDARY
UNKNOWN-RELATIONSHIP
UNKNOWN-AUTHORITY
UNKNOWN-SCOPE
UNKNOWN-IDENTITY
UNKNOWN-LIFECYCLE
UNKNOWN-DOCUMENT
UNKNOWN-KNOWLEDGE
UNKNOWN-IMPLEMENTATION
UNKNOWN-AI
UNKNOWN-AUTOMATION
```

This makes it easier to determine which research method should be used.

---

# 13. Resolution Criteria

A question should have explicit criteria for what would constitute a sufficient
answer.

Examples:

### Concept Question

Sufficient resolution may require:

- a stable definition;
- scope;
- distinction from neighboring concepts;
- supporting evidence;
- known implications.

### Boundary Question

Sufficient resolution may require:

- responsibility boundary;
- excluded responsibility;
- authority boundary;
- interaction boundary;
- known edge cases.

### Architecture Question

Sufficient resolution may require:

- relevant alternatives;
- dependencies;
- constraints;
- impacts;
- rationale;
- and sufficient evidence.

The exact criteria vary by question type.

---

# 14. Research Before Decision

The intended progression is:

```text
Question
   ↓
Research
   ↓
Evidence
   ↓
Finding
   ↓
Interpretation
   ↓
Decision Candidate
   ↓
Decision
```

Skipping directly from Question to Decision requires explicit justification.

---

# 15. Unknowns and Architecture

An open unknown may be:

1. safe to defer;
2. non-blocking;
3. conditionally blocking;
4. foundationally blocking.

The project should not hide unknowns by embedding an assumption into architecture.

If an architecture must temporarily use an assumption, the assumption must be
explicitly recorded.

Conceptually:

```text
Unknown
   ↓
Temporary Assumption
   ↓
Architecture
```

must never become:

```text
Unknown
   ↓
Architecture
```

without the assumption being visible.

---

# 16. Temporary Assumptions

Temporary assumptions are allowed only when necessary to continue non-blocking
work.

Each temporary assumption should record:

```text
Assumption ID
Underlying Unknown
Why Temporary Assumption Is Needed
Affected Work
Risk
Expiry / Reassessment Condition
Owner
Validation Required
```

Temporary assumptions must not silently become permanent architecture.

---

# 17. Question Splitting

A research question should be split when one question contains materially
different uncertainties.

For example:

```text
"How should identity work?"
```

may need to become:

```text
What is the identity entity?
What is the identity boundary?
What establishes identity?
What persists identity?
How is identity represented?
How is identity referenced?
```

Question splitting is preferred over vague umbrella questions.

---

# 18. Question Merging

Questions may be merged only when they are genuinely the same uncertainty with
the same evidence and decision dependency.

Merging questions merely to reduce the count is discouraged.

The goal is:

> **clear uncertainty, not fewer question records.**

---

# 19. Open Question Review

Open questions should be periodically reviewed for:

- new evidence;
- changed project context;
- changed dependencies;
- reduced or increased impact;
- changed priority;
- changed blocking status;
- possibility of splitting;
- possibility of closure;
- possibility of deferral.

Review should not be interpreted as a requirement to close questions artificially.

---

# 20. Decision Impact

Each material question should indicate what future work may depend on its answer.

Possible impacts:

```text
No material impact
Concept impact
Boundary impact
Relationship impact
Architecture impact
Governance impact
Document architecture impact
Operational impact
AI consumption impact
Automation impact
```

This allows research effort to be proportional to consequence.

---

# 21. Reopening Closed Questions

A closed question may be reopened when:

- new evidence materially changes the answer;
- a contradiction is discovered;
- an assumption is shown to be invalid;
- downstream architecture reveals an unresolved dependency;
- or the resolution criteria are shown to have been insufficient.

Reopening a question does not erase its previous history.

---

# 22. Historical Integrity of Questions

The project should preserve:

```text
Question
→ Research
→ Finding
→ Resolution
→ Decision Impact
```

Historical questions must not be rewritten solely to make the present state appear
cleaner.

A later answer may supersede an earlier answer without pretending the earlier
uncertainty never existed.

---

# 23. AI Handling of Unknowns

AI must be instructed to distinguish:

```text
Known
Supported
Inferred
Hypothesized
Unknown
```

AI must not fill a material unknown with confident prose merely because the
prompt expects an answer.

When an unresolved question materially affects architecture, AI should surface
the uncertainty rather than silently inventing a solution.

---

# 24. Research-to-Architecture Gate

Before a material research result can influence architecture, verify:

```text
Question identified
    ↓
Evidence evaluated
    ↓
Finding recorded
    ↓
Uncertainty visible
    ↓
Impact understood
    ↓
Decision readiness established
```

Only then may the result enter architectural reasoning as an appropriate input.

---

# 25. Initial Research Question Backlog

At the beginning of the new project, the following questions should remain open
unless research has already answered them:

### Foundational

- What is the minimum problem the Universal system must solve?
- What is the system's fundamental unit of value?
- What must be universal versus project-specific?
- What must remain outside the Universal boundary?

### Knowledge

- What is "knowledge" in the system?
- What makes knowledge governable?
- What makes knowledge reusable?
- How does semantic knowledge differ from its representation?

### Document

- Why must documents exist as governed objects?
- What documentary functions genuinely require separate identities?
- What should remain in document content versus semantic objects?
- What makes a document suitable for reliable AI consumption?

### Identity

- What entities require stable identity?
- Which entities need identifiers?
- What is identity-independent from representation?
- What identity relationships are actually required?

### Authority

- What types of authority exist?
- Where does authority originate?
- How is authority attached to knowledge and documents?
- How are authority conflicts resolved?

### Lifecycle

- What actually changes over time?
- Which objects require lifecycle states?
- Which changes require new identity versus revision?
- How should historical integrity be preserved?

### Production

- What information is required for AI to produce correct project output?
- Which production rules are universal versus project-specific?
- What must be deterministic?
- What may remain an AI implementation choice?

### Automation

- What must be true before production can be automated?
- What activities require human approval?
- What activities may be autonomous?
- What safety boundaries are necessary?

This backlog is intentionally preliminary.

It is a **starting research surface**, not a predefined answer set.

---

# 26. Non-Goals

This Framework does not:

- answer the research questions it records;
- define final architecture;
- establish final governance;
- declare a final taxonomy;
- decide the final document hierarchy;
- select a final technology stack;
- or require every unknown to be resolved before any project activity can occur.

Its purpose is to make uncertainty visible and manageable.

---

# 27. Core Unknowns Principle

> **Do not hide uncertainty inside architecture.**

A visible unknown is manageable.

A hidden assumption embedded in architecture can become a dependency,
propagate into multiple documents, and create expensive reconstruction.

---

# 28. Final Research Question Principle

> **Ask the question that discovers the system, not the question that presupposes the solution.**

Prefer:

> "What identity capabilities are actually required?"

over:

> "Which identity registry should we implement?"

Prefer:

> "What documentary boundaries are required?"

over:

> "Which documents should we create?"

Prefer:

> "What must be true for safe autonomous production?"

over:

> "How should the automation engine work?"

---

# 29. Framework Evolution

This Framework may evolve as research reveals better ways to manage uncertainty.

Any revision should preserve its central function:

> **make important unknowns explicit, traceable, prioritized, and resistant to
> premature closure.**
