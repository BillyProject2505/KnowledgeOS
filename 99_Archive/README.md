# 99_Archive

## Purpose

`99_Archive` is the canonical archive boundary of KnowledgeOS.

It preserves deprecated, historical, superseded, retired, draft, legacy, migration, and other non-active artifacts for provenance, traceability, recovery, audit, and historical reference.

Archived artifacts are **not active Canonical Knowledge** unless an explicit canonical authority states otherwise.

---

## Archive Boundary

The presence of a file inside `99_Archive` establishes only that the artifact belongs to the repository's archive boundary.

Archive location does **not** by itself determine:

- whether an artifact is `SUPERSEDED`, `RETIRED`, `DRAFT`, or `HISTORICAL`;
- which successor replaced it;
- whether it was ever canonical;
- why it was archived.

Those meanings belong to the artifact's own archival metadata and, where applicable, its documented lifecycle lineage.

---

## Archive Status Model

Archived artifacts should use the following distinctions where they can be established reliably:

| Status | Meaning |
|---|---|
| `SUPERSEDED` | The historical version was replaced by an authorized successor. |
| `RETIRED` | The artifact was deliberately withdrawn without a direct successor serving as its replacement. |
| `DRAFT` | The artifact is a non-canonical development version that did not become the active canonical release. |
| `HISTORICAL` | The artifact is preserved for historical or provenance purposes without a verified direct successor being assigned. |
| `ARCHIVED` | Repository disposition indicating that the artifact is preserved inside this archive boundary. |

`ARCHIVED` is a repository disposition. It does **not** replace the artifact's historical or lifecycle status.

---

## Metadata Authority

Every archived artifact should carry explicit archival metadata whenever that metadata can be established reliably.

At minimum, the metadata should identify:

- document or artifact identity;
- version, where applicable;
- historical or lifecycle status;
- `canonicality` where applicable;
- `archive_status`;
- `archive_disposition`;
- `superseded_by` when a verified successor exists.

Example:

```yaml
---
document_id: EXAMPLE-001
version: "1.0"
status: SUPERSEDED
canonicality: HISTORICAL
archive_status: ARCHIVED
archive_disposition: SUPERSEDED
superseded_by: EXAMPLE-001_v2.0.md
---
```

The metadata belongs to the individual artifact. This README does **not** declare the lifecycle status of every file in the archive.

---

## Successor and Lineage Rule

When multiple historical versions exist, `superseded_by` should identify the **nearest verified successor in the document lineage**, not automatically the latest version in the chain.

For example:

```text
v1.0 → v2.0 → v3.0 → current
```

The correct archival lineage is:

```text
v1.0 → superseded_by: v2.0
v2.0 → superseded_by: v3.0
v3.0 → superseded_by: current successor
```

An archived successor may itself be archived. Archive location does not break lineage.

Do not invent `superseded_by` when the successor cannot be verified.

---

## Historical Content Rule

Archival metadata describes the **current status of the archived copy**. It does not rewrite the substantive historical content of that artifact.

Statements inside an archived artifact that describe a former `Canonical`, `Active`, or `Locked` state remain historical statements and do not override the current archival metadata.

Where an archival artifact is found to be truncated, corrupted, or otherwise unable to preserve its historical content, the artifact should be restored from a verified historical source or removed when reliable restoration is not possible.

---

## Archive Integrity Rules

- Do not place active Knowledge Objects in `99_Archive`.
- Do not treat archived artifacts as current canonical authority.
- Preserve substantive historical content.
- Do not silently overwrite historical versions.
- Do not classify every archived artifact as `SUPERSEDED` merely because it is archived.
- Do not assign a successor without verified lineage.
- Preserve version-to-version successor relationships when multiple historical versions exist.
- Use manual restoration or verified historical blobs when a large archived file cannot be safely mutated without risking truncation.
- Remove an archive artifact when its historical content is demonstrably corrupted and cannot be restored reliably, rather than preserving an invalid historical copy.

---

## Archive Index

The root of `99_Archive` is the primary archive index and navigation surface.

Historical artifacts should remain directly discoverable from this directory whenever practical. Subdirectories should only be used when there is an explicit structural reason and their contents remain navigable from this README.

The index is an orientation and navigation layer. It does **not** replace the metadata of individual archived artifacts.

---

## Current Archive Organization

The archive may contain, among others:

- Deprecated Documents
- Superseded Versions
- Retired Artifacts
- Historical Documents
- Drafts and Development Artifacts
- Legacy Structures
- Archived Project Artifacts
- Migration and Materialization Snapshots

Where a former archive subdirectory has been flattened into `99_Archive`, its artifacts should be treated as members of this same archive boundary.

---

## Navigation

### Parent

Repository Root

### Related KnowledgeOS Areas

- `00_System`
- `01_Knowledge`
- `02_Projects`
- `98_Operator_Manual`

---

## Canonical Archive Principle

> **Archive location preserves history; artifact metadata preserves meaning.**

`99_Archive/README.md` defines the archive boundary, orientation, and archival rules. The individual archived artifact remains authoritative for its own historical metadata and documented lineage.
