# Universal Naming & Identification Registry (UNIR)

**Document ID:** UNIR-CORE-001  
**Document Type:** Universal Registry Architecture  
**Version:** 1.2  
**Status:** LOCKED — CANONICAL  
**Previous Version:** 1.1  
**Canonical Scope:** Universal Naming & Identification Registry (UNIR)  
**Normative Relationship:** Operates within the normative authority established by UNIS

---

## Canonical Lock Record

UNIR-CORE-001 v1.2 is the current canonical revision of the Universal Naming & Identification Registry (UNIR).

This revision incorporates the materialized `DIUA` Namespace registration state into the canonical `UNIR-NSM` domain while preserving the six-Core architecture and the explicit boundary that DIUA is not a separate UNIR Registry Object by default.

## Canonical DIUA Namespace State

**Namespace Literal:** `DIUA`  
**Canonical Name:** Document Identifier Universal Architecture  
**Namespace Scope:** Universal Document Identifier Architecture  
**Governing Architecture:** Universal Identifier Architecture (UIA) under UNIS  
**Applicable Identifier Class:** Document  
**Identifier Class Marker:** `DIC`  
**Applicable Identifier Grammar:** `DIUA-DIC-<6DigitSequence>`  
**Namespace State:** REGISTERED — ACTIVE  
**Registry Object:** NONE

### Authority

**Normative Authority:** UNIS  
**Namespace Semantics Authority:** UNIR-NSM  
**Registration Governance:** UNIR-GRP

### Integrity

- Namespace selection: APPROVED
- Collision / uniqueness audit: PASS
- Scope audit: PASS
- Authority audit: PASS
- Identifier Class binding: DIC
- Grammar binding: `DIUA-DIC-<6DigitSequence>`
- Separate Registry Object eligibility: DEFERRED / NONE

### Allocation Boundary

The allocation of Namespace `DIUA` does not allocate any individual Document Identifier.

```text
DIUA
  = Namespace

DIC
  = Document Identifier Class Marker

DIUA-DIC-<6DigitSequence>
  = Identifier Grammar

DIUA-DIC-000001
  = future individual Document Identifier allocation
```

No individual Document Identifier is allocated by this revision.

---

## 1. Purpose

UNIR-CORE-001 is the consolidated canonical specification of the Universal Naming & Identification Registry (UNIR).

UNIR provides the bounded registry architecture, registry object machinery, namespace and identity registry semantics, lifecycle/state machinery, and governance/registration operations required to operationalize the Universal Naming & Identification architecture established by UNIS.

UNIR does not replace or supersede UNIS. UNIS remains the normative authority for Universal Naming & Identification semantics.

This document is a **single publication container** for the six canonical UNIR Core semantic domains. The six domains retain distinct ownership boundaries even though they are published in one document.

## 2. Canonical Six-Core Architecture

| Core | Canonical Ownership |
|---|---|
| UNIR-SCH | Registry Object structure |
| UNIR-OCM | Registry Object classification |
| UNIR-IDM | Registry Object identity |
| UNIR-NSM | Namespace semantics |
| UNIR-LSM | Registry lifecycle and state |
| UNIR-GRP | Governance and registration |

No additional UNIR Core is established by this document.

## 3. Authority Boundary

UNIS remains the normative naming and identification authority.

UNIR provides registry representation and operational governance machinery within that normative architecture.

```text
UNIS
  ↓
Normative Naming & Identification Authority
  ↓
UNIR
  ↓
Registry Architecture, Registration & Governance
```

UNIR shall not silently redefine semantics owned by UNIS or by another UNIR Core.

---

## 4. DIUA Boundary

**DIUA (Document Identifier Universal Architecture)** is an architectural construct within the Universal Identifier Architecture (UIA).

DIUA is not a UNIR Core specification, an Identifier Class, the Document Identifier Grammar itself, an individual Document Identifier, or a separate UNIR Registry Object by default.

The canonical relationship is:

```text
UNIS / UIA
    ↓
DIUA
    ├── governs → DIC
    └── governs → Document Identifier Grammar
                         ↓
                       UNIR
                         ↓
                operational registration
```

DIC remains the Document Identifier Class. The Document Identifier Grammar remains the identifier construction rule governed by the applicable Universal Identifier Architecture. UNIR operationalizes these governed constructs through registration, allocation, lifecycle, and related registry mechanisms.

DIUA shall not receive a separate UNIR Registry Object identity unless a future explicit registration-eligibility decision establishes that such registration is required.

---

## 5. Registered Construct Boundary

The following are governed/registered constructs and are not additional UNIR Core specifications merely by being represented in the registry:

- Universal Knowledge Object Identification (UKOI)
- Document Identifier Class (DIC)
- Decision Identifier Class (DEC)
- applicable identifier grammars
- registration events
- decision records
- audit and reconciliation records

Their semantics remain subject to their applicable normative ownership.

---

## 6. Core Ownership Boundaries

```text
SCH  → Registry Object structure
OCM  → Registry Object classification
IDM  → Registry Object identity
NSM  → Namespace semantics
LSM  → Registry lifecycle/state
GRP  → Governance and registration
```

The consolidated document does not merge these ownership domains semantically.

---

## 7. Canonicality and Change Control

The six Core domains are canonically locked for UNIR v1.2.

The historical decision, review, reconciliation, and materialization artifacts used to construct this release remain provenance records. They are not individually promoted to normative status merely because they exist in the construction history.

Any substantive change to UNIR Core semantics requires controlled revision, impact assessment, traceability, review, and a new explicit canonical lock.

---

## 8. Consolidated Core Specifications

## UNIR-SCH v1.0

### Universal Naming & Identification Registry Schema

**Document ID:** UNIR-SCH  
**Version:** 1.0  
**Status:** CANONICALLY LOCKED — UNIR CORE v1.0  
**Role:** Registry Schema  
**Canonical Lineage:** Reconciled Draft v0.x → UNIR Core v1.0

## 1. Purpose

UNIR-SCH defines the structural representation of an authorized registry object in the Universal Naming & Identification Registry (UNIR).

UNIR-SCH is a structural specification. It does not establish universal semantic authority, ontology, relationship taxonomy, reference syntax, or domain-specific subject semantics.

## 2. Authority Boundary

The Universal Naming & Identification Standard (UNIS) is the normative authority for universal Naming & Identification semantics and boundaries.

UNIR-SCH represents authorized registry information without silently redefining that authority.

```text
UNIS
  ↓
Normative semantic authority

UNIR-SCH
  ↓
Registry representation
```

## 3. Core Registry Record

A UNIR registry object may contain, as applicable:

- Registry Object ID
- Object Class
- Canonical Name
- Definition / Description
- Authority References
- Namespace Information
- Lifecycle / State Information
- Version Information
- Relationship References
- Provenance
- Effective Information
- Registration Metadata

The presence of a field does not imply that UNIR owns the semantics represented by that field.

## 4. Registry Object ID

Registry Object ID identifies the UNIR registry object.

```text
Registry Object ID
    ≠
Subject Identifier
    ≠
Name
    ≠
Reference
```

The identity mechanism is governed by UNIR-IDM.

## 5. Object Class

Object Class records the classification assigned under UNIR-OCM.

It identifies the class of the **registry object**, not a universal ontological class of the underlying subject.

```text
Registry Object
    ↓
UNIR Object Class
```

UNIR-SCH shall not create or expand object classes independently of UNIR-OCM.

## 6. Canonical Name

Canonical Name represents the controlled name assigned to the registry object.

It is distinct from identity.

```text
Canonical Name
    ≠
Registry Object ID
```

A change of name does not automatically create a new registry object.

Naming semantics remain subject to applicable authority.

## 7. Definition / Description

A registry object may contain a definition or description sufficient to identify the governed construct.

This field is a registry representation and shall not be treated as an independent normative authority that overrides UNIS or applicable domain authority.

## 8. Authority References

Authority information shall identify applicable authorities rather than collapsing distinct authority roles into a single undifferentiated concept.

Where applicable, records may distinguish:

- semantic authority;
- registration authority;
- namespace authority;
- identification authority;
- other explicitly applicable authority.

UNIR-GRP governs registration authorization. UNIR-SCH records the relevant authority information.

## 9. Namespace Information

Namespace information may be represented where applicable.

Namespace semantics, scope, uniqueness context, and authority are governed by UNIR-NSM and applicable higher authority.

```text
Namespace
    ≠
Registry Object ID
    ≠
Name
```

UNIR-SCH shall not independently define a universal namespace taxonomy.

## 10. Lifecycle / State Information

Registry records may contain lifecycle or state information.

UNIR-LSM defines the canonical lifecycle semantics and permitted transitions.

UNIR-SCH only represents the resulting state information.

```text
UNIR-LSM
    ↓
State / lifecycle semantics

UNIR-SCH
    ↓
State / lifecycle representation
```

## 11. Version Information

Version information may be represented independently of registry object identity.

```text
Stable Registry Object ID
        +
Changing Version
```

A version change does not automatically constitute a new registry object.

## 12. Relationship References

Registry records may contain references to relationships with other registry objects.

UNIR-SCH does not establish a Universal Relationship Ontology.

Relationship semantics and allowed relationship types must come from applicable authoritative architecture.

```text
Relationship Representation
    ≠
Universal Relationship Authority
```

## 13. Provenance

Provenance records the evidence and history supporting registry representation.

It may include:

- source;
- source version;
- authority basis;
- registration decision;
- materialization history;
- relevant change history.

```text
Provenance
    ≠
Authority
```

Provenance demonstrates traceability; it does not itself create authority.

## 14. Effective Information

Effective information may record when a registry state, definition, or authorized change becomes applicable.

It is distinct from:

- authorization;
- lifecycle state;
- transition;
- version.

These semantics belong to their respective Core specifications.

## 15. Registration Metadata

Registration metadata supports:

- registration;
- audit;
- publication;
- traceability;
- controlled maintenance.

It shall not become an ungoverned semantic layer.

## 16. Schema Ownership Boundaries

| Concern | Owning Specification |
|---|---|
| Object classification | UNIR-OCM |
| Registry Object identity | UNIR-IDM |
| Namespace semantics | UNIR-NSM |
| Lifecycle and state | UNIR-LSM |
| Registration governance | UNIR-GRP |
| Normative Naming & Identification semantics | UNIS |
| Structural representation | UNIR-SCH |

## 17. What UNIR-SCH Does Not Define

UNIR-SCH shall not independently define:

- Universal Ontology;
- Universal subject taxonomy;
- Universal Relationship Ontology;
- Universal Reference Syntax;
- identifier grammar;
- namespace hierarchy;
- lifecycle authority;
- registration authority.

These are outside its structural role unless explicitly delegated by higher authority and the applicable Core specification.

## 18. Registry Object vs Governed Subject

A registry object may represent or govern a Naming & Identification construct without becoming the subject itself.

```text
UNIR Registry Object
        │
        └── represents / governs
                    │
                    ▼
        Naming & Identification Construct
```

The registry object therefore has its own identity and lifecycle.

## 19. Schema Conformance

A registry record conforms to UNIR-SCH when:

- its structural fields are valid;
- its object class is recognized by UNIR-OCM;
- its Registry Object ID conforms to UNIR-IDM;
- namespace information conforms to UNIR-NSM where applicable;
- lifecycle/state information conforms to UNIR-LSM;
- registration metadata is authorized under UNIR-GRP.

## 20. Reconciliation Decision

UNIR-SCH v0.2 incorporates the first UNIS reconciliation.

The revision confirms that the schema remains a Core specification while explicitly separating:

```text
Structural Representation
        ≠
Semantic Authority
        ≠
Governance Authority
```

## 21. Status

**Historical Revision Status:** Draft Core — UNIS-Reconciled Revision

This revision supersedes UNIR-SCH v0.1.

The six-Core UNIR architecture remains unchanged.

## Canonical Lock

**Canonical Status:** LOCKED

This specification is canonically locked as part of **UNIR Core v1.0**.

The lock confirms:

- the defined concern boundary is authoritative within UNIR Core;
- cross-specification ownership is authoritative;
- UNIS reconciliation and final pre-canonicalization audit have been completed;
- controlled provisional/open matters remain explicitly bounded;
- no implementation may silently expand this specification's authority.

Changes to this specification after lock require an authorized revision and must preserve the canonical change-control and cross-specification validation process.

## Governing Principle

> **UNIR-SCH shall represent authorized registry information without becoming an independent source of universal semantic, ontological, relational, identifier, namespace, lifecycle, or governance authority.**

---

## UNIR-OCM v1.0

### Universal Naming & Identification Registry Object Class Model

**Document ID:** UNIR-OCM  
**Version:** 1.0  
**Status:** CANONICALLY LOCKED — UNIR CORE v1.0  
**Role:** Registry Object Classification  
**Canonical Lineage:** Reconciled Draft v0.x → UNIR Core v1.0

## 1. Purpose

UNIR-OCM defines the model used to determine which independently governed Naming & Identification constructs may be represented as canonical objects in the Universal Naming & Identification Registry (UNIR).

UNIR-OCM does **not** establish a universal ontology.

## 2. Authority Boundary

The Universal Naming & Identification Standard (UNIS) establishes normative Naming & Identification semantics and boundaries.

UNIR derives its registry representation from that authority but shall not automatically convert every UNIS concept into a registry object class.

Therefore:

```text
UNIS Concept
    ≠ automatically
UNIR Object Class
```

## 3. Fundamental Principle

An object class shall exist in UNIR only when:

- the semantic construct is sufficiently distinct;
- applicable authority permits or requires registry representation;
- independent identity is meaningful;
- lifecycle and governance are meaningful;
- canonical registry representation provides a legitimate governance or interoperability function.

## 4. Registry Object Boundary

A UNIR Registry Object is the canonical registry representation of an authorized Naming & Identification construct.

It shall be distinguished from:

- the semantic concept itself;
- the subject governed by that concept;
- an operational identifier;
- a document;
- a rule;
- a property;
- a relationship;
- implementation metadata.

```text
UNIR Registry Object
        │
        └── represents / governs
                    │
                    ▼
        Naming & Identification Construct
```

## 5. Universal Ontology Boundary

UNIR shall not become a Universal Ontology Registry.

The existence of concepts such as:

- Name;
- Identifier;
- Identity;
- Namespace;
- Reference;
- Identifier Class;
- Identifier Grammar;

within UNIS does not, by itself, establish each as a UNIR Object Class.

Object classification is a registry architecture decision constrained by UNIS authority.

## 6. Current Object-Class Status

The following classes previously proposed in UNIR-OCM v0.1 are **not canonically established**:

- Naming Object;
- Identification Object;
- Namespace Object;
- Identifier Scheme Object.

Their status is now:

| Candidate Class | Current Status | Reason |
|---|---|---|
| Naming Object | UNRESOLVED | Not established by UNIS as a registry class |
| Identification Object | UNRESOLVED | Identification architecture does not automatically imply a registry object class |
| Namespace Object | PROVISIONAL | Namespace is authoritative UNIS concept; registry-object status remains to be established |
| Identifier Scheme Object | PROVISIONAL | Identifier classes/grammars are governed constructs; registry-object status remains to be established |

## 7. Candidate Object Classes

The following are retained only as candidates for further reconciliation:

### 7.1 Namespace-related Object

A potential registry representation of a governed namespace or namespace construct.

Its final object status, scope, identity, and authority remain unresolved.

### 7.2 Identifier Class-related Object

A potential registry representation of an authorized identifier class.

This must not be assumed merely because UNIS defines identifier classes.

### 7.3 Identifier Grammar / Scheme-related Object

A potential registry representation of an identifier grammar, scheme, or related governed construct.

The exact semantic boundary must be established before classification.

### 7.4 Naming-related Object

A potential registry representation of an explicitly governed naming construct.

Its distinction from a name, naming rule, naming scheme, or naming authority remains subject to reconciliation.

### 7.5 Other Authorized Construct

UNIR may require additional object classes if authoritative UNIS material and registry necessity establish them.

No additional class shall be invented merely to complete the taxonomy.

## 8. Object Classification Test

A candidate shall not become a UNIR Object Class solely because:

- the term appears in UNIS;
- the term is defined;
- the term is frequently used;
- a legacy registry contains it;
- an implementation requires it.

The candidate must pass:

```text
Semantic Identity
        ↓
Authority
        ↓
Independent Object Status
        ↓
Registry Necessity
        ↓
Identity Requirement
        ↓
Lifecycle / Governance Requirement
        ↓
Object-Class Validation
```

## 9. Concept vs Object

A normalized concept may ultimately be represented as:

- an object;
- a property;
- a rule;
- a relationship;
- metadata;
- another construct.

Therefore:

```text
Canonical Concept
       ↓
Classification Assessment
       ↓
Object Class only if justified
```

## 10. Registry Object vs Subject Identity

A Registry Object ID identifies the UNIR registry object.

It does not automatically identify the subject represented or governed by that object.

```text
Registry Object ID
        ≠
Subject Identifier
        ≠
Name
        ≠
Reference
```

This boundary shall be preserved across the UNIR Core.

## 11. Classification Independence

UNIR-OCM shall define object classes independently of:

- identifier syntax;
- namespace syntax;
- lifecycle state;
- registration workflow.

Those concerns are governed by the corresponding Core specifications.

## 12. Relationship to UNIR-SCH

UNIR-OCM defines **what kinds of registry objects may exist**.

UNIR-SCH defines **how an authorized registry object is structurally represented**.

```text
OCM
 ↓
Object Type
 ↓
SCH
 ↓
Object Representation
```

## 13. Relationship to UNIR-IDM

UNIR-OCM determines whether an object is eligible for registry representation.

UNIR-IDM determines how the registry object is uniquely identified.

```text
OCM
 ↓
Object Class
 ↓
IDM
 ↓
Registry Object Identity
```

## 14. Relationship to UNIR-NSM

UNIR-OCM does not establish Namespace semantics.

Namespace authority, scope, and uniqueness boundaries are governed by UNIR-NSM.

## 15. Relationship to UNIR-LSM

Object classification does not establish lifecycle semantics.

UNIR-LSM defines registry lifecycle and state behavior.

## 16. Relationship to UNIR-GRP

The existence of an Object Class does not authorize registration by itself.

Registration authority and governance are defined by UNIR-GRP.

## 17. Cross-Core Boundary

```text
Object Classification
        ≠
Object Identity
        ≠
Namespace
        ≠
Lifecycle
        ≠
Governance
```

## 18. Classification Freeze

No new Object Class shall be canonically introduced solely during implementation.

New classes require:

- semantic definition;
- authority validation;
- cross-Core impact assessment;
- registration necessity determination;
- explicit canonical decision.

## 19. Reconciliation Record

UNIR-OCM v0.2 incorporated UNIS reconciliation and preserved the distinction:

```text
UNIS semantic concept
        ≠
UNIR Registry Object Class
```

## 20. Canonical Lock

**Canonical Status:** LOCKED

UNIR-OCM is canonically locked as part of **UNIR Core v1.0**.

Changes require controlled revision and cross-Core validation.

## Governing Principle

> **UNIR-OCM shall classify registry objects without becoming a universal ontology, semantic taxonomy, or independent Naming & Identification authority.**
