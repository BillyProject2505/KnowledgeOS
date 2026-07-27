# AIFDS-003 — Information Model

> **Identifier:** AIFDS-003
>
> **Title:** Information Model
>
> **Version:** 1.0
>
> **Status:** Canonical (LOCK)
>
> **Type:** Core Specification
>
> **Parent Standard:** AI-First Documentation Standard (AIFDS)

---

# 1. Purpose

This specification defines the canonical Information Model of the AI-First Documentation Standard (AIFDS).

The Information Model establishes the shared vocabulary, object model, and relationship model used consistently throughout all AIFDS specifications.

It serves as the semantic foundation for all documentation governed by AIFDS.

---

# 2. Scope

This specification defines:

- Information Objects
- Object Categories
- Object Identity
- Object Relationships
- Object Lifecycle
- Object Ownership

This specification does not define repository implementation or document formatting.

---

# 3. Design Principles

The Information Model shall:

- define every concept exactly once;
- eliminate ambiguity;
- establish a shared vocabulary;
- support AI reasoning and retrieval;
- support human understanding;
- remain repository agnostic.

---

# 4. Object Categories

AIFDS organizes Information Objects into canonical categories.

## 4.1 Structural Objects

Structural Objects define the building blocks of documentation.

Objects:

- Document
- Section
- Metadata
- Identifier

---

## 4.2 Normative Objects

Normative Objects define rules, requirements, and governing knowledge.

Objects:

- Specification
- Standard
- Principle
- Framework
- Policy

---

## 4.3 Governance Objects

Governance Objects define authority, accountability, and governance records.

Objects:

- Decision
- Registry

---

## 4.4 Reusable Objects

Reusable Objects support consistent documentation creation.

Objects:

- Template

---

## 4.5 Informational Objects

Informational Objects provide supporting information without defining normative requirements.

Objects:

- Reference

---

# 5. Information Objects

## Document

A self-contained information asset with a defined purpose, identifier, version, status, and lifecycle.

---

## Section

A logical subdivision of a document containing information related to a single responsibility.

---

## Metadata

Structured descriptive information about an information object.

Metadata describes an object without forming part of its primary content.

---

## Identifier

A permanent unique identifier assigned to an information object.

Identifiers shall remain stable throughout the object's lifecycle.

---

## Specification

A normative document defining architecture, requirements, or rules.

---

## Standard

A normative set of requirements intended for repeated application.

---

## Principle

A fundamental rule guiding decisions and behaviour.

---

## Framework

A structured model organizing concepts or processes.

---

## Policy

A governing statement defining organizational intent or constraints.

---

## Registry

A canonical catalogue of uniquely identified information objects.

---

## Decision

A documented governance or architectural decision together with its rationale.

---

## Template

A reusable document structure supporting consistent authoring.

---

## Reference

A non-normative source intended to support understanding.

---

# 6. Object Identity

Every Information Object shall possess the following minimum identity.

- Identifier
- Title
- Type
- Version
- Status

Additional metadata may be defined by other specifications.

---

# 7. Relationships

Information Objects may be connected through explicit relationships.

Relationship semantics are defined by AIFDS-007.

Examples include:

- Depends On
- Implements
- References
- Supersedes
- Replaces
- Related To
- Derived From

---

# 8. Lifecycle

Information Objects progress through lifecycle states defined by AIFDS-008.

Lifecycle rules are not defined by this specification.

---

# 9. Ownership

Every normative Information Object shall have an identified owner or governing authority responsible for its maintenance.

---

# 10. Conformance

All AIFDS specifications shall use the terminology established by this Information Model.

No specification shall redefine concepts already defined herein.

---

# 11. Change History

| Version | Status | Description |
|----------|--------|-------------|
| 1.0 | Canonical | Initial Information Model specification with Object Categories. |
