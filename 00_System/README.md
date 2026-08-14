# 00_System

## Purpose

Contains the authoritative system architecture, governance, standards, registries, specifications, release controls, and controlled system workspaces of KnowledgeOS.

---

## Scope

`00_System` contains artifacts that define, govern, constrain, register, specify, release, or support the operation and evolution of KnowledgeOS as a system.

Repository placement is determined by the artifact's canonical function and authority.

---

## Canonical System Layers

- `10_Architecture` — architectural authority and system structure.
- `20_Governance` — governance, authority, decision, and change-control mechanisms.
- `30_Standard` — canonical normative standards.
- `40_Registries` — canonical registry architecture and operational registration mechanisms.
- `Specifications` — canonical system specifications and materialized technical definitions.
- `Releases` — release records, publication history, and versioned system release information.

## Controlled Workspaces

- `Development` — non-canonical architecture-development workspace governed by the Architecture Development Lifecycle.
- `Planning` — implementation-planning workspace; planning artifacts do not define architectural authority.

## System Boundary

Knowledge-bearing artifacts belong under `01_Knowledge` unless their canonical function is explicitly system-governing or system-operational.

A Knowledge Object does not become a System artifact merely because it describes a standard, system, classification, or governed concept.

---

## Canonical Authority Boundary

`00_System` is the system layer of KnowledgeOS. Its artifacts operate within the applicable higher-level architectural authority of the repository and shall not silently redefine authority owned by another canonical layer.

Normative Standards establish rules within their declared scope. Registries operationalize governed semantics and registration state. Specifications materialize approved system definitions. Development and Planning workspaces are non-canonical unless an artifact is formally promoted through the applicable lifecycle.

---

## Navigation

### Parent

Repository Root

### Children

- `10_Architecture`
- `20_Governance`
- `30_Standard`
- `40_Registries`
- `Specifications`
- `Releases`
- `Development`
- `Planning`

### Related Knowledge Layer

- `../01_Knowledge`

---

## Canonical Boundary Principle

`00_System` contains system-defining and system-operational artifacts. It does not serve as a general repository for knowledge content merely because that content is authoritative or canonical within its own subject domain.
