# DIUA-DIC-000001 — Document Identifier Allocation Record

**Record Type:** Document Identifier Allocation Record  
**Identifier Class:** DIC  
**Namespace:** DIUA  
**Document Identifier:** DIUA-DIC-000001  
**Status:** ALLOCATED — ACTIVE  
**Governing Architecture:** DIUA / UIA  
**Registry:** UNIR  

## Allocation Basis

This record establishes the first concrete Document Identifier allocation within the active `DIUA` namespace for the canonical documented architecture reference represented by the DIUA construct.

## Allocation Boundary

This allocation:

- assigns `DIUA-DIC-000001` as a concrete Document Identifier;
- does not create a new UNIR Core;
- does not create a separate DIUA Registry Object;
- does not redefine DIC;
- does not redefine the Document Identifier Grammar;
- does not reallocate the DIUA namespace.

## Grammar Conformance

```text
Namespace               = DIUA
Identifier Class Marker = DIC
Sequence                = 000001

DIUA-DIC-000001
```

The identifier conforms to:

```text
DIUA-DIC-<6DigitSequence>
```

## Registry Relationship

```text
DIUA Namespace
    ↓
DIC Identifier Class
    ↓
Document Identifier Grammar
    ↓
DIUA-DIC-000001
```

## Lifecycle

`DIUA-DIC-000001` is allocated and active within its applicable identification scope.

A later document version, filename change, repository migration, or representation change does not by itself reallocate this identifier.

## Traceability

This record closes the gap between the already active `DIUA` namespace and the existence of a concrete Document Identifier allocation.
