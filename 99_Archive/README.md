# 99_Archive

## Purpose

Stores deprecated, historical, superseded, retired, draft, and other archived materials within KnowledgeOS.

---

## Scope

This directory preserves repository history while ensuring that archived materials remain available for reference, provenance, recovery, and historical traceability.

Archived materials are **not** considered active Canonical Knowledge.

The presence of an artifact in this directory establishes its **archive boundary**, but does not by itself determine the artifact's individual lifecycle disposition. Each archived artifact should therefore carry explicit archival metadata identifying its status and disposition where practical.

---

## Archive Status Model

Archived artifacts should use the following distinctions where applicable:

- `SUPERSEDED` — an active or canonical predecessor replaced by an authorized successor.
- `RETIRED` — deliberately withdrawn from active use without a direct successor serving as its replacement.
- `DRAFT` — a non-canonical development artifact that did not become the active canonical version.
- `HISTORICAL` — preserved for historical or provenance purposes without implying that it was superseded by a specific successor.
- `ARCHIVED` — the repository disposition indicating that the artifact is preserved within this archive boundary.

`ARCHIVED` describes repository disposition. It does not, by itself, replace the artifact's lifecycle or historical status.

---

## Metadata Rule

Each archived artifact should, where metadata is available or can be established reliably, identify at minimum:

- document or artifact identity;
- version, where applicable;
- current archival status;
- archive disposition;
- superseding successor, where one exists;
- historical or archival reason, where useful for traceability.

Archived metadata is documentary metadata only. It does not rewrite the substantive historical content of the archived artifact.

Statements inside an archived artifact that describe a former `Canonical`, `Active`, or `Locked` state remain part of that artifact's historical content and do not override its current archival metadata.

---

## Rules

- Do not place active Knowledge Objects in this directory.
- Do not treat archived artifacts as current canonical authority.
- Preserve archived substantive content unless an explicit archival correction is required for traceability or governance.
- Do not silently overwrite historical versions.
- Do not classify every archived artifact as `SUPERSEDED`; use the disposition that matches its actual historical lifecycle.
- Every archived item should include, or be accompanied by, sufficient information to understand why it was archived.
- The `README.md` is the canonical navigation and orientation document for this archive boundary.

---

## Contents

- Deprecated Documents
- Superseded Versions
- Retired Artifacts
- Historical Documents
- Drafts and Development Artifacts
- Legacy Structures
- Archived Projects
- Migration and Materialization Snapshots

---

## Navigation

### Parent

Repository Root

### Related

- 00_System
- 01_Knowledge
- 02_Projects
- 98_Operator_Manual
