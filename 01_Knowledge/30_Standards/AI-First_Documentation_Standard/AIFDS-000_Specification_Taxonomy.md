# AIFDS-000 — Specification Taxonomy

> **Identifier:** AIFDS-000
>
> **Title:** Specification Taxonomy
>
> **Version:** 1.0
>
> **Status:** Canonical (LOCK)
>
> **Type:** Constitutional Specification
>
> **Parent Standard:** AI-First Documentation Standard (AIFDS)

---

# 1. Purpose

This specification defines the taxonomy of specification types used within the AI-First Documentation Standard (AIFDS).

The taxonomy establishes the authority level and intended purpose of each specification category.

---

# 2. Specification Types

## Constitutional Specification

Defines the constitutional foundation of AIFDS.

Characteristics:

- Highest normative authority.
- Establishes philosophy.
- Establishes architecture.
- Establishes governing principles.
- Takes precedence over all other AIFDS specifications.

Example:

- AIFDS-001 — Foundation

---

## Core Specification

Defines the normative rules that collectively implement AIFDS.

Characteristics:

- Normative.
- Required for AIFDS conformance.
- Must comply with Constitutional Specifications.

Examples:

- Documentation Classification
- Information Model
- Document Structure
- Writing Rules
- Document Templates
- Cross Reference
- Versioning
- Governance
- Registry

---

## Supporting Specification

Defines implementation guidance, operational guidance, or supporting recommendations.

Characteristics:

- Supports implementation.
- Does not redefine constitutional principles.
- Does not override Core Specifications.

Example:

- GitHub Implementation

---

# 3. Authority Hierarchy

Authority shall be interpreted in the following order:

1. Constitutional Specification
2. Core Specification
3. Supporting Specification

Lower-level specifications shall not contradict higher-level specifications.

---

# 4. Conflict Resolution

When conflicting requirements exist:

- Constitutional Specifications take precedence.
- Core Specifications take precedence over Supporting Specifications.
- Supporting Specifications shall be updated to restore consistency.

---

# 5. Change Management

Changes to this taxonomy constitute architectural changes.

Such changes shall follow the governance process defined by AIFDS.

---

# 6. Change History

| Version | Status | Description |
|----------|--------|-------------|
| 1.0 | Canonical | Initial specification taxonomy. |
