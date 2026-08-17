# Universal Naming and Identification Standard

---
document_id: UNIS-CORE-001
concrete_document_identifier: DIUA-DIC-000001
document_type: Universal Standard
title: Universal Naming and Identification Standard
short_name: UNIS
version: 1.8
status: LOCKED — CANONICAL
canonicality: CANONICAL
lock_status: LOCKED
publication_status: PUBLISHED
semantic_authority: UNIS
documentary_conformance_authority: Universal Document System
allocation_authority: Universal Naming and Identification Registry
identifier_class: DIC
namespace: DIUA
scope: Foundational architecture and normative rules governing naming and identification across the Universal system
purpose: Establish common boundaries and normative rules for naming, identity, identifiers, namespaces, qualification, reference, resolution, allocation, uniqueness, persistence, and related identification concerns across the Universal system
responsibility: Universal naming and identification architecture and normative authority
previous_version: 1.7
source_basis:
  - UNIS-CORE-001 v1.7 — locked canonical source artifact
  - UNIR-REGISTRY-001 v1.5 — allocation state establishing DIUA-DIC-000001 for UNIS-CORE-001 v1.7
  - Controlled metadata-correction materialization for the v1.8 successor candidate
change_scope: Documentary metadata correction and concrete identifier materialization only; substantive normative content inherited unchanged from v1.7
---

# Document Contract

| Property | Value |
|---|---|
| Document ID | `UNIS-CORE-001` |
| Concrete Document Identifier | `DIUA-DIC-000001` |
| Document Type | Universal Standard |
| Title | Universal Naming and Identification Standard |
| Short Name | UNIS |
| Version | 1.8 |
| Status | LOCKED — CANONICAL |
| Canonicality | CANONICAL |
| Lock Status | LOCKED |
| Publication Status | PUBLISHED |
| Semantic Authority | UNIS |
| Documentary Conformance Authority | Universal Document System |
| Allocation Authority | Universal Naming and Identification Registry |
| Identifier Class | `DIC` |
| Namespace | `DIUA` |
| Scope | Foundational architecture and normative rules governing naming and identification across the Universal system |
| Purpose | Establish common boundaries and normative rules for naming, identity, identifiers, namespaces, qualification, reference, resolution, allocation, uniqueness, persistence, and related identification concerns across the Universal system |
| Responsibility | Universal naming and identification architecture and normative authority |
| Previous Version | `UNIS-CORE-001 v1.7` |
| Source Basis | `UNIS-CORE-001 v1.7`; validated UNIR allocation state; controlled metadata-correction materialization |
| Change Scope | Documentary metadata correction and concrete identifier materialization only |

### Interpretation Rule

This artifact is the canonical locked materialization of `UNIS-CORE-001 v1.8`. It preserves the substantive normative content of v1.7 and materializes the concrete Document Identifier `DIUA-DIC-000001`.

`UNIS-CORE-001` remains the document identity/designation. `DIUA-DIC-000001` is the concrete Document Identifier allocated to that document.

Canonicalization, lock, and publication have been explicitly authorized. This artifact is immutable canonical state.

### Authority Boundary

- UNIS owns the substantive naming and identification semantics defined by this Standard.
- UNIR owns operational registry and allocation machinery.
- UDS governs documentary-system conformance.
- The concrete Document Identifier does not transfer semantic authority to UNIR or UDS.

### Provenance Boundary

The v1.8 change is limited to documentary metadata and explicit materialization of the already-established concrete Document Identifier. It does not retroactively alter the substantive v1.7 rules or historical state.

## 1. Purpose

Universal Naming and Identification Standard (UNIS) establishes the foundational architecture and normative rules governing naming and identification across the Universal system. It defines the common boundaries for naming, identity, identifiers, namespaces, qualification, reference, resolution, allocation, uniqueness, persistence, and related identification concerns.

UNIS is a standard and normative authority. Operational registry state, reservation, registration, allocation records, and other registry implementation concerns are maintained separately by the Universal Naming and Identification Registry (UNIR).

## 2. Authority Boundary

UNIS is the foundational Universal Naming and Identification authority. It governs the universal identification architecture and establishes the rules within which domain-specific identity models and identifier grammars operate.

UNIS does not replace domain-specific ownership of domain identifier grammars. Domain authorities retain responsibility for their own domain-specific identifier systems, subject to conformance with the Universal identification architecture and applicable namespace boundaries.

## 3. Canonical Layer Architecture

UNIS is organized into fourteen canonical layers:

1. Core Architecture
2. Authority Boundary
3. Naming
4. Identification
5. Identity
6. Relationship
7. Reference
8. Namespace & Scope
9. Qualification
10. Status
11. Lifecycle
12. State
13. Transition
14. Universal Identifier Architecture (UIA)

UIA is the canonical identifier architecture layer of UNIS.

## 4. Core Naming and Identification Boundaries

UNIS maintains the following fundamental distinctions:

- Name ≠ Identifier
- Identifier ≠ Identity
- Identity ≠ Scope
- Namespace ≠ Scope
- Namespace ≠ Authority
- Reference ≠ Identity
- Qualification ≠ Identity
- Status ≠ Lifecycle
- Lifecycle ≠ State
- State ≠ Transition
- Registry ≠ Identifier Authority
- Registration ≠ Creation

These boundaries are normative and shall not be collapsed merely because implementations store or represent the corresponding information together.

## 5. Namespace Architecture

A Namespace is a governed identification context within which identifiers are interpreted and uniqueness is determined according to the applicable identification scope and Identifier Class.

Namespace authority shall be explicitly established by the applicable governance architecture. A Namespace shall not be inferred solely from filenames, repository paths, folder structures, project labels, storage locations, or historical identifier usage.

UNIS permits shared, nested, related, and domain-specific namespaces where explicitly governed. Distinct namespaces shall provide sufficient separation to prevent unintended cross-domain or cross-class ambiguity.

## 6. Universal Identifier Architecture

Universal Identifier Architecture (UIA) defines the common requirements for identifiers across applicable Identifier Classes.

UIA governs:

- Identifier Classes
- identifier grammar requirements
- Namespace relationships
- allocation authority principles
- uniqueness
- identification scope
- collision prevention
- non-reuse
- persistence
- resolution
- registry boundaries
- historical traceability
- correction and replacement principles

UIA does not replace the semantic Identity Model of the entity being identified.

## 7. Identifier Architecture Principles

### 7.1 Identifier Class

An Identifier Class identifies the class of entity for which an identifier is constructed. The Identifier Class shall remain distinct from semantic type, lifecycle state, version, repository, representation, or other mutable attributes unless an applicable architecture explicitly governs otherwise.

### 7.2 Namespace

An identifier shall be interpreted within an explicit Namespace and Identification Scope. Namespace and Scope are distinct concepts and shall not be conflated.

### 7.3 Lexical and Structural Grammar

A class-specific Identifier Grammar shall conform to the Universal Identifier Architecture. Identifier components shall have stable lexical and structural rules and shall not encode semantics that are not part of the applicable identification architecture.

### 7.4 Allocation

Identifier allocation shall occur under an authority authorized for the applicable Namespace and Identifier Class. Allocation shall be controlled so that the same identifier is not allocated to more than one governed identity within the applicable uniqueness boundary.

### 7.5 Collision Prevention

Identifier allocation shall include mechanisms sufficient to prevent collisions within the applicable Namespace, Identifier Class, and Identification Scope. Repository search, filename comparison, or physical storage location alone shall not constitute authoritative collision control.

### 7.6 Non-Reuse

An allocated identifier shall not be reassigned to a different governed identity within the applicable identification scope. Retirement, withdrawal, supersession, or archival of the identified entity shall not by itself release the identifier for reuse.

### 7.7 Persistence

An identifier shall remain persistently associated with the identity to which it was allocated. Revision, version change, state transition, lifecycle change, name change, representation change, repository migration, storage migration, or registry migration shall not by themselves alter the identifier.

### 7.8 Resolution

A valid identifier shall be resolvable, within its applicable Namespace and Identification Scope, to the governed Identity or authoritative subject for which it was allocated. Resolution shall not depend solely on filename, repository path, storage location, or physical representation.

Ambiguous or conflicting identifiers shall not be silently resolved to an alternative subject.

## 8. Universal Sequence Model

Where a class-specific identifier grammar adopts the Universal Sequence Model, the canonical sequence representation is:

- decimal numeric
- fixed width
- six digits
- zero-padded
- non-repeating within the applicable allocation context

Canonical examples include:

```text
000001
000002
000003
```

The sequence is an identifier component and shall not, by itself, encode date, version, priority, quantity, lifecycle, or other semantic attributes.

## 9. Decision Identifier Grammar

The Decision Identifier Grammar is a fully materialized class-specific Identifier Grammar under the canonical Universal Identifier Architecture.

Canonical structural form:

```text
<Namespace>-DEC-<6DigitSequence>
```

Where:

- `DEC` is the canonical Decision Identifier Class Marker.
- `<6DigitSequence>` uses the canonical six-digit Universal Sequence Model.
- `<Namespace>` is governed by the applicable Decision Identification Namespace rules and is not fixed by this document unless separately allocated and materialized.

The `DEC` Identifier Class Marker is reserved for Decision identifiers and shall not be reused for Document identifiers.

The grammar is canonical; an illustrative or historical Namespace prefix shall not be promoted into the canonical Namespace without an explicit allocation decision.

## 10. Document Identifier Grammar

The Document Identifier Grammar is a class-specific Identifier Grammar under the canonical Universal Identifier Architecture.

Canonical structural form:

```text
<Namespace>-DIC-<6DigitSequence>
```

Where:

- `DIC` is the canonical Document Identifier Class Marker.
- `<6DigitSequence>` uses the canonical six-digit Universal Sequence Model.
- `<Namespace>` is governed by the applicable Document Identification Namespace rules and is not fixed by this document unless separately allocated and materialized.

The `DIC` Identifier Class Marker shall be used for Document identifiers within identification architectures that adopt the Universal Document Identifier Grammar. `DIC` shall remain distinct from Document Type, Namespace, Identity, lifecycle state, version, repository, and representation.

The Document Identifier Grammar is distinct from the Decision Identifier Grammar. `DEC` shall not be reused as the Document Identifier Class Marker.

## 11. Knowledge Object Identification Boundary

Universal Knowledge Objects are a governed Knowledge Object entity class within the Universal identification architecture. UDS establishes the semantic concept of the Universal Knowledge Object (UKO) and its stable identity model.

The Universal Knowledge Object Identification namespace and its operational registry state are governed by UNIS and, once allocated, administered through the Universal Naming and Identification Registry (UNIR).

UKOI-related registry records, reservation, registration, operational allocation, and resolution records are outside this Standard and belong to UNIR.

## 12. Registry Boundary

UNIS defines normative registry requirements and the distinction between registry functions and identifier authority.

A Registry may store, register, and resolve identifiers when designated by the applicable architecture, but a Registry does not acquire independent semantic authority over identifier construction merely by storing or resolving identifiers.

Registration of an identifier does not, by itself, constitute creation of the governed Identity.

The operational specification, record model, allocation workflow, reservation state, registration state, audit trail, and resolution records of the Universal Naming and Identification Registry are maintained in the separate UNIR document.

## 13. Domain Identifier Architecture

UNIS does not require domain-specific identifier systems to adopt the Universal Knowledge Object Identifier Grammar merely because they operate within the Universal environment.

Domain authorities retain ownership of their domain-specific identifier grammars and allocation mechanisms, provided those systems conform to applicable Universal identification boundaries and maintain clear Namespace and scope separation.

For example, an existing domain identifier such as:

```text
CWC-OBJ-000001
```

shall not be retroactively renamed solely because the Universal identification architecture is established. Domain-specific identity and identifier governance remain with the applicable domain authority.

## 14. Historical Integrity

Canonical and historical versions shall remain distinguishable. A newer canonical version supersedes the previous canonical version without retroactively rewriting the historical artifact.

UNIS-CORE-001 v1.7 is the previous locked canonical version. v1.6 is the historical predecessor to v1.7. This v1.8 artifact is a revision candidate and shall not be treated as canonical until separately authorized and locked.

The introduction of `DIC` does not retroactively rewrite historical identifiers or historical artifacts. Any historical or provisional use of `DEC` for Document identification shall be treated according to applicable supersession and historical-traceability rules.

## 15. Conformance

A class-specific Naming or Identification Architecture conforms to UNIS when it:

1. respects the authority boundaries established by UNIS;
2. maintains the distinction between Name, Identifier, and Identity;
3. uses explicitly governed Namespace and Identification Scope;
4. applies stable lexical and structural identifier rules;
5. prevents collisions within applicable uniqueness boundaries;
6. does not reassign allocated identifiers;
7. preserves identifier persistence across ordinary evolution;
8. supports authoritative resolution and traceability;
9. does not silently acquire authority belonging to another Universal or domain-specific layer; and
10. keeps operational registry implementation separate from normative Standard authority.

## 16. Canonical Lock Record

This revision was subjected to controlled revision and lock-readiness review. No blocking architectural, authority, semantic, collision, namespace, registry-boundary, or historical-integrity finding remains within the approved scope of the revision.

The canonical Identifier Class Marker allocation under this revision is:

```text
Decision  → DEC
Document  → DIC
```

The canonical class-specific grammars are:

```text
Decision:
<Namespace>-DEC-<6DigitSequence>

Document:
<Namespace>-DIC-<6DigitSequence>
```

No literal Namespace is allocated by this lock record.

## 17. Canonical Status

This artifact is the canonical locked materialization of `UNIS-CORE-001 v1.8`.

```text
Document ID:                 UNIS-CORE-001
Concrete Document ID:        DIUA-DIC-000001
Version:                     1.8
Status:                      LOCKED — CANONICAL
Canonicality:                CANONICAL
Lock Status:                 LOCKED
Publication Status:          PUBLISHED
Previous Canonical Version:  1.7
```

`UNIS-CORE-001 v1.7` remains the previous locked canonical version. This v1.8 canonical artifact supersedes v1.7 for current use while preserving v1.7 as the previous locked canonical historical version.

The Universal Naming and Identification Registry (UNIR) is a separate registry authority and is not incorporated into this Standard.

## UDS Conformance Record

The v1.8 canonical artifact conforms to the applicable UDS documentary requirements.

```text
Identity / Concrete Identifier          PASS
Document Type / Purpose / Scope         PASS
Responsibility / Authority Boundary     PASS
Source Basis / Provenance               PASS
Structure / Navigation                  PASS
Normative / Informative Distinction     PASS
Canonicality / Lifecycle State          PASS
Historical Integrity                    PASS
Machine-Readable Metadata               PASS
Presentation Independence               PASS
Closure / Lock / Publication Boundary   PASS
```

UDS conformance was established before canonicalization and does not replace the explicit canonicalization, lock, and publication decision recorded for this artifact.

## Metadata Clarification

The document identity `UNIS-CORE-001` remains unchanged across versions. The concrete Document Identifier allocated to this document is:

```text
DIUA-DIC-000001
```

The concrete identifier persists across version changes and therefore remains `DIUA-DIC-000001` for v1.8.

This metadata materialization does not replace `UNIS-CORE-001`, redefine the Document Identifier Grammar, or transfer allocation authority from UNIR. It records the concrete identifier allocated to this document.

The substantive normative content of v1.7 is preserved; the approved change scope was limited to documentary metadata and identifier materialization. This canonical artifact is now immutable.

