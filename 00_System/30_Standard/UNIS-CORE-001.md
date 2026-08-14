# Universal Naming and Identification Standard

**Document ID:** UNIS-CORE-001  
**Document Type:** Universal Standard  
**Version:** 1.7  
**Status:** LOCKED — CANONICAL  
**Canonical Authority:** UNIS  
**Previous Version:** 1.6  

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

UNIS-CORE-001 v1.7 is the current canonical version. v1.6 is the previous canonical version and remains historical.

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

This document is the current canonical materialization of UNIS-CORE-001 v1.7.

```text
UNIS-CORE-001
Version: 1.7
Status: LOCKED — CANONICAL
Previous Version: 1.6
```

The Universal Naming and Identification Registry (UNIR) is a separate registry document and is not incorporated into this Standard.
