# 60_Releases

## Purpose

Contains the controlled release records and publication history of KnowledgeOS.

---

## Scope

`60_Releases` records official releases, release notes, changelog information, version history, migration notes, and other publication-traceability artifacts associated with released system states.

This directory records release history; it does not define normative architecture, governance, standards, or registry semantics.

---

## Canonical Function

Release artifacts provide temporal and publication traceability for approved system states and released changes.

A release record shall not silently replace the canonical artifact that established the underlying architecture, governance rule, standard, registry definition, or specification. Release records document the publication event and its resulting state.

---

## Contents

- Release Records
- Release Notes
- Changelog
- Version History
- Migration Notes
- Withdrawal or Correction Records, where applicable

---

## Rules

- Official releases shall be traceable to the applicable approved source artifacts.
- Published release records shall preserve historical integrity and shall not be silently overwritten.
- Superseded releases remain historically traceable.
- Release records do not redefine the normative authority of Architecture, Governance, Standards, Registries, or Specifications.
- Changes to release-control semantics shall follow the applicable governance process.

---

## Relationship to Other System Layers

```text
10_Architecture
        ↓
20_Governance
        ↓
30_Standard / 40_Registries / 50_Specifications
        ↓
     Release
        ↓
60_Releases
```

`60_Releases` records the resulting published state and its traceability; it is not the source of the underlying normative semantics.

---

## Navigation

### Parent

`00_System`

### Related

- `../10_Architecture`
- `../20_Governance`
- `../30_Standard`
- `../40_Registries`
- `../50_Specifications`
- `../70_Development`
- `../80_Planning`
- `../../01_Knowledge`

---

## Canonical Boundary Principle

`60_Releases` is the historical and publication-traceability layer of the System. It records what was officially released and when, without acquiring ownership of the substantive authority contained in the released artifacts.