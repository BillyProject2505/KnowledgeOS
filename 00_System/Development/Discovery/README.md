# Discovery Workspace

Version: 1.0

Status: Active

---

# Purpose

The Discovery Workspace is dedicated to the exploration of architectural ideas before formal design begins.

It provides a structured environment for collecting knowledge, analysing problems, identifying concepts, and evaluating alternatives prior to creating an Architecture Blueprint.

---

# Scope

The Discovery Workspace contains Discovery Notes for architectural initiatives across the Knowledge Operating System.

Typical contents include:

- Background information
- Problem exploration
- Initial concepts
- Existing standards
- Alternative approaches
- Assumptions
- Risks
- Questions
- Preliminary conclusions

Discovery artifacts are exploratory and are expected to evolve during the Architecture Discovery phase.

---

# Relationship to ADL

The Discovery Workspace supports **Phase 1 – Architecture Discovery** of the Architecture Development Lifecycle (ADL).

The output of Discovery is an Architecture Blueprint.

```text
Idea
    ↓
Discovery Notes
    ↓
Architecture Blueprint
```

---

# Directory Structure

```text
Discovery/
├── KOS-AS/
├── PRS/
├── IP/
└── ...
```

Each subdirectory contains Discovery Notes for a specific specification.

---

# Discovery Principles

Discovery follows these principles:

- Explore before deciding.
- Record ideas before evaluating them.
- Preserve alternative approaches.
- Separate exploration from architectural decisions.
- Focus on understanding the problem before proposing solutions.

---

# Relationship to Blueprints

Discovery Notes are the primary input for Architecture Blueprints.

Architecture Blueprints summarise validated discoveries and should not introduce new concepts that were not explored during Discovery.

---

# Expected Outputs

Each Discovery effort should produce:

- a clear understanding of the problem,
- identified core concepts,
- documented assumptions,
- evaluated alternatives,
- preliminary conclusions suitable for Blueprint development.

---

# Status

This workspace supports active exploration.

Discovery Notes are working artifacts and are not Canonical Specifications.
