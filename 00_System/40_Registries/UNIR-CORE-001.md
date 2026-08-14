# Universal Naming & Identification Registry (UNIR)

**Document ID:** UNIR-CORE-001  
**Document Type:** Universal Registry Architecture  
**Version:** 1.0  
**Status:** LOCKED — CANONICAL  
**Canonical Scope:** Universal Naming & Identification Registry (UNIR)  
**Normative Relationship:** Operates within the normative authority established by UNIS

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

Accordingly:

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

## 4. Registered Construct Boundary

The following are governed/registered constructs and are not additional UNIR Core specifications merely by being represented in the registry:

- Universal Knowledge Object Identification (UKOI)
- Document Identity Class (DIC)
- Decision Identity Class (DEC)
- applicable identifier grammars
- registration events
- decision records
- audit and reconciliation records

Their semantics remain subject to their applicable normative ownership.

## 5. Core Ownership Boundaries

The following distinctions are canonical:

```text
SCH  → Registry Object structure
OCM  → Registry Object classification
IDM  → Registry Object identity
NSM  → Namespace semantics
LSM  → Registry lifecycle/state
GRP  → Governance and registration
```

The consolidated document does not merge these ownership domains semantically.

## 6. Canonicality and Change Control

The six Core domains below are canonically locked for UNIR v1.0.

The historical decision, review, reconciliation, and materialization artifacts used to construct this release remain provenance records. They are not individually promoted to normative status merely because they exist in the construction history.

Any substantive change to UNIR Core semantics requires controlled revision, impact assessment, traceability, review, and a new explicit canonical lock.

## 7. Consolidated Core Specifications



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

UNIR-IDM determines how the resulting registry object receives persistent registry identity.

Object classification does not determine identifier syntax.

## 14. Relationship to UNIR-NSM

A candidate object may have namespace implications, but namespace membership does not automatically determine object class.

```text
Namespace
    ≠ automatically
Namespace Object
```

## 15. Relationship to UNIR-LSM

Object classes may have lifecycle behavior, but lifecycle state does not determine object class.

```text
Registered
    ≠ Object Class
```

## 16. Relationship to UNIR-GRP

UNIR-GRP authorizes registration of eligible objects.

It shall not create object classes independently of UNIR-OCM and applicable higher authority.

```text
OCM
 ↓
What may be registered?

GRP
 ↓
May this candidate be authorized?
```

## 17. Legacy Object Protection

Legacy object classes shall not be adopted automatically.

For every legacy-derived class, determine:

1. whether its source remains authoritative;
2. whether its semantics survive in current UNIS;
3. whether it has been accommodated or migrated;
4. whether the class remains necessary;
5. whether a new registry representation is required.

Historical existence does not establish current authority.

## 18. Object-Class Evidence

Every eventual canonical object class shall retain evidence for:

- semantic basis;
- authority basis;
- scope;
- object boundary;
- registry necessity;
- identity requirement;
- lifecycle requirement;
- governance requirement.

## 19. Provisional Taxonomy

The current taxonomy is intentionally open:

```text
UNIR Registry Object
        │
        ├── Namespace-related construct       [PROVISIONAL]
        ├── Identifier Class-related construct [CANDIDATE]
        ├── Identifier Grammar/Scheme construct [PROVISIONAL]
        ├── Naming-related construct          [CANDIDATE]
        └── Other authorized construct        [OPEN]
```

This is a candidate space, not a canonical taxonomy.

## 20. Canonicalization Gate

An object class may become canonical only when:

- authoritative basis is established;
- semantic boundary is established;
- registry necessity is demonstrated;
- identity implications are established;
- lifecycle implications are established;
- governance authority is established;
- duplication and overlap are resolved;
- UNIS reconciliation is complete.

## 21. Current Reconciliation Decision

UNIR-OCM v0.2 records the following architectural decision:

> UNIR shall retain an Object Class Model as a Core specification, but no individual object class is canonically established by the current UNIR Core Set. Candidate classes remain subject to authoritative UNIS reconciliation and registry-necessity assessment.

## 22. Status

**Historical Revision Status:** Draft Core — Reconciled Provisional Revision

This revision supersedes UNIR-OCM v0.1.

The Core Set remains six specifications. No additional Core specification is created by this revision.

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

> **UNIR shall not infer a registry object taxonomy from UNIS terminology alone. Object classes must be established through semantic authority, independent object identity, registry necessity, and explicit reconciliation with the applicable Universal Architecture and UNIS authority.**

---


# UNIR-IDM v1.0

# Universal Naming & Identification Registry Object Identifier Model

**Document ID:** UNIR-IDM  
**Version:** 1.0
**Status:** CANONICALLY LOCKED — UNIR CORE v1.0
**Role:** Registry Object Identification  
**Canonical Lineage:** Reconciled Draft v0.x → UNIR Core v1.0

## 1. Purpose

UNIR-IDM defines the identification mechanism for objects registered in the Universal Naming & Identification Registry (UNIR).

Its scope is limited to the identity and identifier requirements of the **UNIR registry object itself**.

## 2. Authority Boundary

The Universal Naming & Identification Standard (UNIS) establishes normative universal Naming & Identification semantics.

UNIR-IDM shall implement a registry-object identification mechanism without redefining:

- Universal Identity;
- universal identifier classes;
- universal identifier grammar;
- universal namespace hierarchy;
- domain-specific identifiers.

## 3. Registry Object Identifier

A **Registry Object ID** is the canonical identifier assigned to a UNIR registry object for persistent registry reference.

```text
Registry Object
      │
      └── Registry Object ID
```

The Registry Object ID identifies the registry object; it does not automatically identify the subject represented or governed by that object.

## 4. Identity vs Identifier

UNIR shall preserve the distinction:

```text
Identity
    ≠
Identifier
    ≠
Reference
    ≠
Name
    ≠
Representation
```

The Registry Object ID is an identifier used to represent and refer to the identity of the registry object.

It shall not be described as being the identity itself.

## 5. Persistent Registry Identity

A Registry Object ID shall remain associated with the same registry object across applicable:

- name changes;
- definition changes;
- metadata corrections;
- version changes;
- lifecycle transitions;
- supersession history.

A change in presentation or state does not by itself create a new registry object.

## 6. Non-Reuse

A Registry Object ID shall not be silently reassigned to another registry object.

When a registry object reaches a terminal lifecycle state, its identifier remains historically associated with that object.

Identifier reuse is prohibited unless an explicit higher-authority rule establishes otherwise.

## 7. Identity Change

A new Registry Object ID is required when a proposed change creates a semantically distinct registry object rather than merely revising the existing object.

The distinction shall be determined through applicable semantic and governance assessment.

```text
Same Object
    → retain Registry Object ID

New Semantic Object
    → assign new Registry Object ID
```

## 8. Name and Identifier

A Registry Object ID is distinct from the canonical name of the registry object.

```text
Canonical Name
    ≠
Registry Object ID
```

Changing the canonical name does not automatically change the Registry Object ID.

## 9. Reference and Identifier

A Registry Object ID may be used as a stable reference token.

However:

```text
Identifier
    ≠
Reference
```

Identifier semantics and reference semantics shall remain distinct even when the same Registry Object ID is used in a reference context.

## 10. External Identifiers

A UNIR registry object may contain references to external identifiers where authorized.

External identifiers remain subject to their own:

- identifier authority;
- namespace;
- grammar;
- allocation rules;
- lifecycle.

```text
UNIR Registry Object
    ├── Registry Object ID
    └── External Identifier Reference(s)
```

Recording an external identifier does not transfer its authority to UNIR.

## 11. Identifier Class

UNIR-IDM does not currently assign a final universal Identifier Class to the Registry Object ID.

Any identifier-class assignment shall be established through reconciliation with applicable UNIS and higher-level architecture.

```text
Identifier Class
    ≠ automatically
UNIR Object Class
```

## 12. Identifier Grammar

The exact grammar of Registry Object IDs remains provisional.

UNIR shall not invent a canonical grammar merely for implementation convenience.

The final grammar shall be established only after confirming compatibility with:

- applicable UNIS provisions;
- namespace requirements;
- uniqueness requirements;
- persistence requirements;
- implementation constraints.

## 13. Namespace Dependency

Namespace semantics are outside the primary ownership of UNIR-IDM.

Where Registry Object IDs use or require a namespace:

```text
UNIR-IDM
    → defines identifier role

UNIR-NSM
    → defines namespace semantics
```

UNIR-IDM shall not independently define a universal namespace hierarchy.

## 14. Uniqueness

Registry Object IDs shall be unique within their authorized identification context.

The exact uniqueness boundary shall be determined together with applicable namespace and governance rules.

Uniqueness shall not be assumed to mean universal uniqueness across every external system.

## 15. Persistence

Registry Object IDs shall support stable reference across the lifecycle of the registry object.

Persistence includes preservation of historical association through:

- supersession;
- withdrawal;
- retirement;
- correction;
- version changes.

## 16. Supersession

When one registry object supersedes another:

```text
Registry Object A
       │
       └── SUPERSEDED BY
                  ↓
            Registry Object B
```

A and B have distinct Registry Object IDs.

Supersession does not transfer the identifier of A to B.

## 17. Lifecycle Independence

Registry Object ID remains independent of lifecycle state.

```text
Registry Object ID
       │
       ├── PROPOSED
       ├── REGISTERED
       ├── SUPERSEDED
       ├── WITHDRAWN
       └── RETIRED
```

Lifecycle semantics are governed by UNIR-LSM.

## 18. Authority Separation

The following authority roles shall not be collapsed:

```text
Authority to define an identifier
        ≠
Authority to allocate an identifier
        ≠
Authority to register a registry object
        ≠
Authority over a namespace
```

UNIR-GRP governs registration authorization.

Applicable identifier and namespace authorities retain their respective authority unless explicitly delegated.

## 19. Registry Object ID Assignment

A Registry Object ID shall be assigned only through the authorized UNIR registration process.

A candidate identifier used during pre-registration is not a canonical Registry Object ID.

```text
Candidate ID
    ≠
Registry Object ID
```

## 20. Identifier Immutability

Once a Registry Object ID is canonically assigned, it shall not be changed merely because:

- the name changes;
- metadata changes;
- a definition is corrected;
- a version changes;
- the object changes lifecycle state.

A change to the Registry Object ID indicates a different identity and therefore requires a distinct registration object.

## 21. Relationship to UNIR-SCH

UNIR-SCH provides structural representation of the Registry Object ID.

UNIR-IDM owns the identity semantics and assignment rules.

```text
UNIR-IDM
    ↓
Registry Object ID semantics

UNIR-SCH
    ↓
Registry Object ID representation
```

## 22. Relationship to UNIR-OCM

UNIR-OCM determines which classes of registry object may exist.

UNIR-IDM determines how an authorized registry object receives persistent registry identity.

Object classification shall not determine identifier syntax automatically.

## 23. Relationship to UNIR-NSM

UNIR-NSM governs namespace semantics.

UNIR-IDM governs the identifier role and identity behavior of Registry Object IDs.

Neither specification shall silently absorb the other's authority.

## 24. Relationship to UNIR-LSM

UNIR-LSM governs lifecycle state and transitions.

UNIR-IDM ensures that lifecycle transitions do not silently alter registry object identity.

## 25. Relationship to UNIR-GRP

UNIR-GRP governs the authorization process through which Registry Object IDs are assigned.

UNIR-IDM defines the identity requirements that registration must satisfy.

## 26. Legacy Identifiers

Legacy identifiers shall not be adopted as canonical Registry Object IDs merely because they exist in historical systems.

For legacy identifiers, determine:

1. source authority;
2. semantic identity;
3. currentness;
4. namespace;
5. uniqueness;
6. persistence;
7. migration or supersession status.

Historical existence does not establish canonical UNIR identity.

## 27. External Identifier Mapping

Where a UNIR object maps to an external identifier, the mapping shall preserve distinction between:

- UNIR identity;
- UNIR Registry Object ID;
- external identity;
- external identifier;
- mapping/reference relationship.

A mapping shall not imply ownership transfer.

## 28. Conformance

A Registry Object ID conforms to UNIR-IDM when:

- it identifies exactly one canonical registry object within its authorized context;
- its assignment is authorized;
- it is unique within the applicable boundary;
- it is persistent;
- it is not silently reused;
- its namespace requirements are satisfied where applicable;
- its lifecycle behavior preserves identity.

## 29. Reconciliation Decision

UNIR-IDM v0.2 incorporates the first UNIS reconciliation.

The revision confirms:

- Registry Object ID remains a Core concern;
- identity and identifier are explicitly distinguished;
- identifier grammar remains provisional;
- identifier-class assignment remains unresolved;
- namespace semantics are delegated to UNIR-NSM;
- registration authority is delegated to UNIR-GRP;
- Registry Object ID is distinct from identifiers of governed subjects.

## 30. Status

**Historical Revision Status:** Draft Core — UNIS-Reconciled Revision

This revision supersedes UNIR-IDM v0.1.

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

> **UNIR-IDM shall provide persistent, unique, non-reusable identification for UNIR registry objects without redefining universal identity, identifier, namespace, or domain-specific identification authority.**

---


## UNIR-NSM v1.0

### Universal Naming & Identification Registry Namespace Model

**Document ID:** UNIR-NSM  
**Version:** 1.0
**Status:** CANONICALLY LOCKED — UNIR CORE v1.0
**Role:** Namespace Semantics and Registry Representation  
**Canonical Lineage:** Reconciled Draft v0.x → UNIR Core v1.0

## 1. Purpose

UNIR-NSM defines how namespace constructs relevant to the Universal Naming & Identification Registry (UNIR) are understood, represented, referenced, and governed within the registry architecture.

It does not establish a universal namespace ontology or hierarchy.

## 2. Authority Boundary

The Universal Naming & Identification Standard (UNIS) establishes normative universal Namespace semantics and boundaries.

UNIR-NSM provides registry architecture for applicable namespace constructs without transferring or redefining external namespace authority.

```text
UNIS
  ↓
Normative Namespace semantics

UNIR-NSM
  ↓
Namespace representation and registry boundary
```

## 3. Namespace as a Governed Construct

A namespace is a governed naming or identification context within which applicable names, identifiers, or related constructs may be interpreted, allocated, or constrained.

Namespace is distinct from:

```text
Namespace
    ≠
Name
    ≠
Identifier
    ≠
Identity
    ≠
Reference
    ≠
Registry Object ID
```

## 4. Namespace Is Not Automatically a Registry Object

The existence of a namespace does not automatically establish that the namespace must be represented as a canonical UNIR registry object.

Two representations remain architecturally possible:

```text
Namespace
    ↓
Registry Object
```

or:

```text
Namespace
    ↓
Contextual information associated with
a Registry Object
```

The applicable representation shall be determined through UNIR-OCM, registry necessity, and governing authority.

## 5. Namespace Object Status

“Namespace Object” remains **PROVISIONAL**.

It is not a canonical UNIR Object Class at this stage.

A namespace may become a canonical registry object only when:

- independent object identity is established;
- registry representation is justified;
- applicable authority permits or requires it;
- lifecycle and governance are established;
- classification is authorized through UNIR-OCM.

## 6. Namespace Authority

Namespace authority shall remain distinct from other authority roles.

```text
Namespace Authority
    ≠
Registration Authority
    ≠
Identifier Allocation Authority
    ≠
Semantic Authority
```

Registration of a namespace representation in UNIR does not by itself transfer namespace authority to UNIR.

## 7. Namespace Administration and Delegation

Where applicable, UNIR may represent:

- namespace administrator;
- delegated authority;
- allocation authority;
- delegation period;
- authority references.

Delegation shall not be interpreted as ownership transfer unless an authoritative source explicitly establishes that meaning.

## 8. Namespace Scope

A namespace record or reference may include applicable scope, such as:

- naming scope;
- identification scope;
- organizational scope;
- domain scope;
- temporal scope;
- externally governed scope.

Scope shall be represented as applicable information rather than converted into an assumed universal hierarchy.

## 9. Namespace Uniqueness Context

A namespace may establish a uniqueness boundary for names or identifiers.

Uniqueness shall always be interpreted within its authorized context.

```text
Uniqueness
    ↓
within applicable namespace / context
```

UNIR-NSM shall not assume universal global uniqueness merely because a construct is registered.

## 10. Universal Namespace Hierarchy Prohibition

UNIR shall not create a universal namespace hierarchy unless explicitly authorized by higher-level architecture.

The following shall not be treated as canonical merely by convention:

```text
Universal Namespace
    ↓
Global Namespace
    ↓
Domain Namespace
    ↓
Local Namespace
```

Any hierarchy must be supported by applicable authority.

## 11. Namespace Identifier

A namespace may have an identifier, but:

```text
Namespace
    ≠
Namespace Identifier
```

Whether a namespace identifier is required, and what identifier mechanism applies, remains subject to applicable identification authority.

UNIR-NSM shall not independently assign a universal identifier class or grammar to namespace identifiers.

## 12. Registry Object ID

If a namespace is represented as a UNIR registry object, its Registry Object ID is governed by UNIR-IDM.

```text
Namespace
    ↓
UNIR Registry Object
    ↓
Registry Object ID
```

The Registry Object ID does not become the namespace identifier merely because the namespace is registered.

## 13. Identifier Grammar Boundary

Namespace semantics shall not be conflated with identifier grammar.

```text
Namespace
    ≠
Identifier Grammar
```

Namespace may constrain or contextualize identifier allocation, but grammar remains subject to applicable identifier authority and UNIR-IDM where Registry Object IDs are concerned.

## 14. External Namespaces

UNIR may represent or reference an externally governed namespace.

Such representation shall preserve:

- external authority;
- external namespace identity;
- external scope;
- external identifier where applicable;
- provenance;
- relationship to UNIR representation.

Representation does not imply ownership or authority transfer.

## 15. Namespace Collisions

Where two namespace constructs use identical or similar names but arise from different authorities or contexts, UNIR shall not silently merge them.

Assessment shall preserve:

- authority;
- scope;
- provenance;
- context;
- distinct identities where applicable.

```text
Same Namespace Name
    ≠
Same Namespace
```

## 16. Namespace Mapping

UNIR may represent mappings or relationships between namespaces where authorized.

A mapping does not automatically mean equivalence.

The semantic relationship must be explicit, such as:

- mapped;
- referenced;
- related;
- delegated;
- aligned;
- equivalent,

only where the applicable authority supports the relationship.

UNIR-NSM does not create a Universal Relationship Ontology.

## 17. Namespace Lifecycle Boundary

Namespace constructs may have their own external lifecycle.

UNIR-NSM does not independently define a universal namespace lifecycle.

Where a namespace is represented as a UNIR registry object, its **registry lifecycle** is governed by UNIR-LSM.

```text
Namespace semantics
    → UNIR-NSM

Registry lifecycle
    → UNIR-LSM
```

An external namespace lifecycle remains subject to its external authority.

## 18. Namespace Relationships

Namespace relationships may be represented where authorized.

However, UNIR-NSM shall not assume universal relationship types or hierarchy.

Relationship representation is subject to applicable relationship authority.

## 19. Canonical Naming Context

A canonical name recorded in UNIR may have an associated namespace context.

However:

```text
Canonical Name
    ≠
Namespace
    ≠
Naming Authority
```

Each remains independently identifiable where required.

## 20. Namespace Provenance

Namespace information shall preserve provenance sufficient to establish:

- source;
- authority;
- scope;
- allocation or delegation basis;
- relevant version;
- registration decision.

Provenance demonstrates traceability and does not itself create namespace authority.

## 21. Relationship to UNIR-OCM

UNIR-OCM determines whether a namespace construct may be represented as a distinct UNIR Object Class.

UNIR-NSM defines namespace-specific semantics and representation once applicable registry representation is authorized.

```text
UNIR-OCM
    ↓
Can this namespace construct be a registry object?

UNIR-NSM
    ↓
How is the namespace represented and governed?
```

## 22. Relationship to UNIR-SCH

UNIR-SCH provides the structural fields used to represent namespace information.

UNIR-NSM owns namespace semantics.

Schema representation shall not expand namespace authority.

## 23. Relationship to UNIR-IDM

UNIR-IDM governs Registry Object IDs.

UNIR-NSM governs namespace context.

Neither specification shall silently absorb the other's authority.

## 24. Relationship to UNIR-LSM

UNIR-LSM governs lifecycle of a namespace when it is represented as a UNIR registry object.

UNIR-NSM does not define the canonical registry lifecycle.

## 25. Relationship to UNIR-GRP

UNIR-GRP governs authorization for registration.

Registration authorization does not by itself confer namespace ownership or namespace authority.

## 26. Legacy Namespace Protection

Legacy namespace structures shall not be adopted automatically.

For legacy-derived namespace information, determine:

1. whether the source remains authoritative;
2. whether the namespace remains active;
3. whether it has been superseded or migrated;
4. whether its authority remains valid;
5. whether a current representation is required.

Historical existence does not establish current namespace authority.

## 27. Conformance

A namespace representation conforms to UNIR-NSM when:

- its authority is identifiable;
- its scope is sufficiently defined;
- its uniqueness context is understood where applicable;
- external authority is preserved where applicable;
- namespace and identifier concepts remain distinct;
- any registry-object representation is authorized;
- relationships and mappings are supported by evidence.

## 28. Reconciliation Decision

UNIR-NSM v0.2 incorporates the first UNIS reconciliation.

The revision confirms:

- Namespace is a governed UNIS construct;
- Namespace is distinct from Name, Identifier, Identity, Reference, and Registry Object ID;
- no universal namespace hierarchy is created;
- namespace authority is distinct from registration authority;
- Namespace Object remains provisional;
- namespace identifier status remains unresolved;
- external namespace representation does not transfer authority;
- registry lifecycle is delegated to UNIR-LSM.

## 29. Status

**Historical Revision Status:** Draft Core — UNIS-Reconciled Revision

This revision supersedes UNIR-NSM v0.1.

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

> **UNIR-NSM shall represent and govern applicable namespace information without creating a universal namespace hierarchy, transferring external authority, or collapsing Namespace into Name, Identifier, Identity, Reference, or Registry Object identity.**

---


## UNIR-LSM v1.0

### Universal Naming & Identification Registry Lifecycle & State Model

**Document ID:** UNIR-LSM  
**Version:** 1.0
**Status:** CANONICALLY LOCKED — UNIR CORE v1.0
**Role:** UNIR Registry Object Lifecycle and State  
**Canonical Lineage:** Reconciled Draft v0.x → UNIR Core v1.0

## 1. Purpose

UNIR-LSM defines the lifecycle and state model applicable to objects registered in the Universal Naming & Identification Registry (UNIR).

Its scope is limited to the lifecycle of the **UNIR registry object**.

It does not establish a Universal Lifecycle Model for subjects represented, governed, named, or identified by UNIR.

## 2. Authority Boundary

The Universal Naming & Identification Standard (UNIS) establishes universal conceptual boundaries among Lifecycle, State, Status, Transition, Version, Identity, Event, Decision, Evidence, Condition, and Time.

UNIR-LSM defines the lifecycle architecture of UNIR registry objects within those boundaries.

```text
UNIS
  ↓
Universal conceptual boundaries

UNIR-LSM
  ↓
UNIR Registry Object Lifecycle
```

## 3. Registry Lifecycle ≠ Universal Lifecycle

The UNIR registry lifecycle is an architecture-specific lifecycle.

```text
UNIR Registry Lifecycle
    ≠
Universal Lifecycle
    ≠
External Subject Lifecycle
```

A lifecycle state of a UNIR registry object shall not automatically be interpreted as a lifecycle state of the subject represented or governed by that object.

## 4. Lifecycle, State, and Status

UNIR-LSM shall preserve the distinctions:

```text
Lifecycle
    ≠
State
    ≠
Status
```

Lifecycle describes the structured temporal evolution of the registry object.

State represents a condition or position at a point in that lifecycle.

Status is a separately governed assertion and shall not automatically be treated as a lifecycle stage.

## 5. Transition

A lifecycle transition is a governed change between applicable registry lifecycle states.

```text
State A
   │
   │ authorized transition
   ▼
State B
```

Transition shall remain distinct from:

- event;
- decision;
- evidence;
- time;
- lifecycle itself;
- state.

UNIR-LSM defines registry lifecycle transitions only where required by UNIR architecture.

## 6. Provisional Registry States

The following states are retained as **provisional UNIR registry states** pending final governance approval:

```text
PROPOSED
REGISTERED
SUPERSEDED
WITHDRAWN
RETIRED
```

They are not universal lifecycle states.

Their exact semantics and permitted transitions remain subject to UNIR-GRP and final canonical governance.

## 7. Proposed

`PROPOSED` provisionally represents a registry object candidate that has entered the controlled registration process but has not yet achieved canonical registered status.

It does not imply:

- canonicality;
- validity;
- publication;
- approval by every external authority.

## 8. Registered

`REGISTERED` provisionally represents a registry object that has completed the applicable UNIR registration authorization process.

Registered status means authorized registry status within UNIR.

It does not automatically mean:

```text
Universal validity
    or
External subject validity
    or
External authority approval
```

## 9. Superseded

`SUPERSEDED` provisionally represents a registry object that remains historically identifiable but is no longer the current operative registry representation for its applicable purpose because another authorized object has superseded it.

Supersession does not transfer identity.

```text
Object A
  │
  └── SUPERSEDED BY
             ↓
          Object B
```

A and B retain distinct Registry Object IDs.

## 10. Withdrawn

`WITHDRAWN` provisionally represents a registry object removed from the applicable active registration pathway by an authorized decision.

Withdrawal semantics are limited to UNIR registry status and shall not automatically be interpreted as withdrawal of an external subject, identifier, namespace, or authority.

## 11. Retired

`RETIRED` provisionally represents a registry object that is no longer intended for active registry operation but remains historically preserved.

Retirement does not:

- delete identity;
- authorize identifier reuse;
- erase provenance;
- erase historical lifecycle information.

## 12. State Transition Authority

UNIR-LSM defines lifecycle transition semantics.

UNIR-GRP defines the governance and authorization process under which transitions may be approved.

```text
UNIR-LSM
    → what registry transitions mean

UNIR-GRP
    → how transitions are authorized
```

Neither specification shall silently absorb the other's authority.

## 13. Registration and Lifecycle

Registration is a governance process.

It shall not be treated as a universal lifecycle initiation event.

Within UNIR, registration may establish the transition into `REGISTERED` when the applicable governance rules explicitly authorize that transition.

```text
Registration Decision
        │
        └── may authorize
                    ↓
              Lifecycle Transition
```

Decision and transition remain distinct.

## 14. Identity Continuity

Lifecycle transitions shall preserve Registry Object identity unless the transition explicitly concerns creation of a semantically distinct object.

```text
Lifecycle Change
    ≠
Identity Change
```

Registry Object ID semantics remain governed by UNIR-IDM.

## 15. Version Independence

Version changes do not automatically constitute lifecycle transitions.

```text
Version Change
    ≠
Lifecycle Transition
```

A registry object may change version while retaining its identity and lifecycle state.

## 16. Temporal Information

UNIR-LSM may represent temporal information relevant to lifecycle, including:

- effective time;
- transition time;
- registration time;
- supersession time;
- withdrawal time;
- retirement time.

Temporal information is not itself lifecycle semantics.

```text
Time
    ≠
Lifecycle
```

## 17. Decision and Transition

A governance decision may authorize a lifecycle transition.

However:

```text
Decision
    ≠
Transition
```

The decision is the governance act; the transition is the resulting lifecycle change.

Both may require separate traceability.

## 18. Event and Transition

An event may provide the trigger or evidence associated with a lifecycle transition.

However:

```text
Event
    ≠
Transition
```

UNIR-LSM shall not infer lifecycle transitions solely from event occurrence unless an applicable governance rule establishes that relationship.

## 19. Evidence and Lifecycle

Evidence may support a lifecycle decision or transition.

However:

```text
Evidence
    ≠
Lifecycle State
```

Evidence shall not create lifecycle state without applicable governance authority.

## 20. Historical Lifecycle

UNIR shall preserve sufficient lifecycle history to reconstruct:

- previous states;
- transitions;
- effective times;
- authorization decisions;
- relevant evidence;
- supersession relationships;
- identity continuity.

Historical lifecycle information shall not be silently overwritten by current state.

## 21. Terminal States and Identity

A terminal registry lifecycle state does not erase the identity of the registry object.

```text
RETIRED
   ↓
Historical identity preserved
```

Registry Object ID remains non-reusable under UNIR-IDM.

## 22. External Lifecycle Boundary

An external namespace, identifier scheme, naming authority, or governed subject may have its own lifecycle.

UNIR shall not infer that external lifecycle from the lifecycle state of its registry representation.

```text
External Lifecycle
        ≠
UNIR Registry Lifecycle
```

Where external lifecycle is relevant, it shall be represented with explicit provenance and authority.

## 23. Lifecycle Continuity

Lifecycle continuity shall be established through authorized semantic and governance evidence.

The following alone do not establish continuity:

- same name;
- similar identifier;
- timestamp proximity;
- document similarity;
- numerical sequence;
- implementation reuse.

## 24. Object Creation and Lifecycle

A lifecycle state does not automatically create a separate registry object.

```text
REGISTERED
SUPERSEDED
RETIRED
```

are states of a registry object, not separate objects merely because they are distinct lifecycle states.

## 25. Lifecycle Authority

Authority to define registry lifecycle semantics is distinct from authority over:

- Naming;
- Identification;
- Identity;
- Namespace;
- Version;
- Status;
- Relationship;
- Decision;
- Evidence.

UNIR-LSM owns registry lifecycle semantics within its scope.

UNIR-GRP owns authorization governance.

## 26. Relationship to UNIR-OCM

UNIR-OCM determines which registry object classes may exist.

UNIR-LSM determines how an authorized registry object evolves through its registry lifecycle.

Lifecycle state shall not create or determine object class.

## 27. Relationship to UNIR-SCH

UNIR-SCH structurally represents lifecycle and state information.

UNIR-LSM defines the semantics of that information.

## 28. Relationship to UNIR-IDM

UNIR-IDM governs persistent Registry Object identity.

UNIR-LSM ensures that lifecycle transitions preserve that identity unless a genuinely distinct object is created.

## 29. Relationship to UNIR-NSM

UNIR-NSM governs namespace semantics.

UNIR-LSM governs lifecycle of a namespace only when the namespace is represented as a UNIR registry object.

External namespace lifecycle remains under external authority.

## 30. Relationship to UNIR-GRP

UNIR-GRP defines registration and lifecycle governance procedures and authorization.

UNIR-LSM defines the meaning and structure of registry lifecycle transitions.

## 31. Legacy Lifecycle Protection

Legacy lifecycle states shall not be adopted as canonical merely because they appear in historical systems.

For legacy lifecycle information, determine:

1. source authority;
2. semantic meaning;
3. current applicability;
4. supersession or migration status;
5. compatibility with current UNIR lifecycle semantics.

Historical state names shall not automatically become current UNIR states.

## 32. Conformance

A registry lifecycle implementation conforms to UNIR-LSM when:

- lifecycle scope is limited to UNIR registry objects;
- lifecycle, state, status, and transition remain distinct;
- transitions are authorized;
- Registry Object identity remains persistent;
- historical lifecycle information is preserved;
- external lifecycle is not silently conflated with registry lifecycle;
- temporal information is traceable;
- terminal states do not erase identity.

## 33. Reconciliation Decision

UNIR-LSM v0.2 incorporates the first UNIS reconciliation.

The revision confirms:

- UNIR requires a registry-object lifecycle model;
- no Universal Lifecycle Model is created;
- lifecycle, state, status, transition, time, decision, and evidence remain distinct;
- provisional states remain provisional;
- registration does not automatically imply universal lifecycle initiation;
- external lifecycle is explicitly separated;
- historical lifecycle is preserved;
- identity continuity is governed through UNIR-IDM.

## 34. Status

**Historical Revision Status:** Draft Core — UNIS-Reconciled Revision

This revision supersedes UNIR-LSM v0.1.

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

> **UNIR-LSM shall govern only the lifecycle of UNIR registry objects, preserving the distinctions established by UNIS and avoiding any claim to define universal or external subject lifecycle semantics.**

---


## UNIR-GRP v1.0

### UNIR-GRP — Integrated Specification

**Document ID:** UNIR-GRP  
**Version:** 1.0  
**Status:** INTEGRATED — REVIEW PENDING  
**Canonicality:** NOT YET CANONICAL  
**Lock Status:** UNLOCKED

## 1. Purpose

UNIR-GRP defines the governance and registration semantics required to authorize, perform, maintain, trace, and evolve UNIR Registry operations without absorbing normative authority belonging to UNIS or other UNIR Core specifications.

## 2. Scope

GRP owns:

- governance conceptual semantics;
- registration conceptual semantics;
- authority and authorization;
- registration decisions and outcomes;
- governance actions and controls;
- delegation and representation;
- traceability and temporal integrity;
- controlled extensibility and semantic closure.

## 3. Governance Model

Governance is the scoped authority framework through which rules, responsibilities, permissions, decisions, controls, and actions are established and applied.

Governance is not a Registry Object, identifier, namespace, lifecycle state, or registration record.

## 4. Registration Model

Registration is a governed act/process through which an eligible construct is formally admitted, recorded, recognized, or maintained within the UNIR Registry.

Registration establishes or maintains a UNIR Registry representation; it does not redefine the normative semantics of the registered construct.

## 5. Authority and Authorization

Authority is scoped governed capacity.

Authorization is an explicit permission or grant within that authority.

```text
Authority
    ↓
Authorization
    ↓
Specified Action / Decision
```

Registration authority does not automatically confer normative semantic authority.

## 6. Registration Decision and Outcome

```text
Registration Request
        ↓
Assessment
        ↓
Registration Decision
        ↓
Registration Outcome
        ↓
Registry Representation / State
```

Decision and outcome remain distinct.

Approval, rejection, deferral, and return/correction are governed outcomes where applicable.

## 7. Governance Actions and Controls

Governance Actions operationalize authorized decisions or rules.

Governance Controls constrain, verify, or safeguard governed activity.

```text
Rule / Decision
      ↓
Action
      ↓
Governed Effect

Control
      ↓
constrains / verifies
      ↓
Governed Activity
```

## 8. Delegation and Representation

Delegation grants specified authority within defined limits.

Representation permits an actor to act on behalf of another party under a governed mandate.

Neither changes identity or expands authority beyond the mandate.

## 9. Traceability and Temporal Integrity

Governance and registration history shall remain reconstructable through appropriate traceability.

Temporal dimensions shall remain distinct where applicable:

```text
event time
record time
decision time
effective time
registration time
state transition time
withdrawal time
supersession time
```

Historical facts shall not be silently overwritten.

## 10. Extensibility and Closure

GRP may evolve through controlled explicit decisions.

```text
Extension
    ≠
New Core
```

Unresolved matters are deferred to the applicable authority rather than assigned invented semantics.

## 11. Core Boundaries

```text
GRP → governance / registration semantics
SCH → Registry Object structure
OCM → Registry Object classification
IDM → Registry Object identity
NSM → namespace semantics
LSM → Registry Object lifecycle/state
UNIS → normative naming / identification authority
```

GRP shall not redefine semantics owned by another authority.

## 12. D01–D08 Conformance

```text
GRP-D01  Governance Conceptual Model       ✓
GRP-D02  Registration Conceptual Model     ✓
GRP-D03  Authority / Authorization         ✓
GRP-D04  Registration Decision / Outcome   ✓
GRP-D05  Governance Action / Control       ✓
GRP-D06  Delegation / Representation       ✓
GRP-D07  Traceability / Temporal Integrity ✓
GRP-D08  Extensibility / Closure           ✓
```

## 13. Canonicalization Record

The integrated GRP specification completed the required canonicalization gates:

1. Cross-Core Boundary Review — PASS;
2. UDS Conformance Review — PASS;
3. Semantic Integrity Review — PASS;
4. Final Traceability Check — PASS;
5. explicit canonical lock — RECORDED.

UNIR-GRP v1.0 is canonically locked as part of UNIR Core v1.0.

## Governing Principle

> UNIR-GRP provides the minimum bounded governance and registration semantics required to operate the UNIR Registry while preserving UNIS normative authority and the distinct ownership of UNIR-SCH, OCM, IDM, NSM, and LSM.

---


## 8. Canonical Release Integrity

UNIR Core v1.0 has completed:

```text
Six-Core canonicalization                 ✓
Cross-Core integrity reconciliation       ✓
UDS conformance review                    ✓
Semantic integrity review                 ✓
Final traceability check                  ✓
Package integrity verification            ✓
Release closure                           ✓
Publication authorization                 ✓
```

Actual repository publication remains a separate controlled act.

## 9. Provenance

The consolidated document is derived from the canonically locked six-Core specifications and their approved decision/review history.

The construction package contains additional provenance artifacts, including decision records, review records, reconciliation records, release records, and historical material. Those artifacts support traceability but do not override this canonical consolidated specification.

## 10. Final Status

```text
UNIR-CORE-001
Version: 1.0
Status: LOCKED — CANONICAL
Publication Status: AUTHORIZED — NOT YET PUBLISHED
```

> UNIR Core v1.0 is the single consolidated canonical publication of the bounded six-Core UNIR registry architecture. Its internal Core boundaries remain authoritative and distinct, while UNIS remains the normative authority for Universal Naming & Identification.
