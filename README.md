# KnowledgeOS

Knowledge Operating System (KOS)

---

## Purpose

KnowledgeOS is a canonical repository designed to store, organize, govern, and maintain reusable Knowledge Objects and canonical knowledge artifacts for AI-assisted projects.

It serves as a primary repository-level knowledge reference across the KnowledgeOS ecosystem while preserving explicit authority boundaries between system, knowledge, project, resource, and archive layers.

---

## Repository Boundary

KnowledgeOS is organized into distinct repository layers. Repository location provides structural context but does not, by itself, establish canonical authority.

Each artifact remains authoritative only within its declared scope and governance boundary.

---

## Repository Structure

- `00_System` — system architecture, governance, standards, registries, specifications, releases, development, and planning.
- `01_Knowledge` — reusable canonical knowledge and knowledge-domain artifacts.
- `02_Projects` — project-specific canonical and operational knowledge.
- `03_Resources` — supporting resources and reference material.
- `99_Archive` — historical, superseded, retired, draft, legacy, and other non-active artifacts preserved for provenance and traceability.

---

## Project Layer

Project-specific knowledge and operational systems are maintained under `02_Projects/` and `03_Projects/` according to the repository structure currently in use.

The active `03_Projects/` layer includes project indexes and project-specific workspaces such as BAKU Edit Tugas. Project README files define local navigation, scope, and boundaries; they do not override repository or system authority.

Current project navigation:

- [`03_Projects`](./03_Projects/)
- [`BAKU Edit Tugas`](./03_Projects/BAKU_Edit_Tugas/)
- [`BAKU Edit Tugas — Context`](./03_Projects/BAKU_Edit_Tugas/00_Context/)
- [`BAKU Edit Tugas — Content`](./03_Projects/BAKU_Edit_Tugas/01_Content/)
- [`BAKU Edit Tugas — Assets`](./03_Projects/BAKU_Edit_Tugas/02_Assets/)
- [`BAKU Edit Tugas — Production`](./03_Projects/BAKU_Edit_Tugas/03_Production/)

---

## Canonical Interpretation Rule

AI and human contributors shall not infer canonicality from:

- filename alone;
- repository position alone;
- document recency alone;
- repeated usage;
- search ranking; or
- historical presence.

Canonical interpretation shall follow the artifact's own metadata, declared authority, applicable registries, governance decisions, and documented lineage.

---

## Documentation

- `README.md` — repository-level orientation and navigation.
- `INDEX.md` — repository index where maintained.
- `MAP.md` — structural repository map where maintained.

Folder-level `README.md` files provide local navigation, scope, authority, and maintenance guidance for their respective directories.

---

## Maintenance Principles

- Preserve explicit authority boundaries.
- Prefer one canonical home for each canonical concept.
- Preserve historical lineage and provenance.
- Do not silently overwrite canonical or historical artifacts.
- Use verified successor relationships when documenting supersession.
- Treat archived artifacts as historical/non-active unless explicit authority states otherwise.
- Keep README files navigational and boundary-oriented; they do not replace the substantive authority of canonical documents.
- Keep repository navigation synchronized with the actual directory structure.

---

## Navigation

### Primary Layers

- [`00_System`](./00_System/)
- [`01_Knowledge`](./01_Knowledge/)
- [`02_Projects`](./02_Projects/)
- [`03_Resources`](./03_Resources/)
- [`03_Projects`](./03_Projects/)
- [`99_Archive`](./99_Archive/)

### Repository Documents

- [`INDEX.md`](./INDEX.md)
- [`MAP.md`](./MAP.md)

---

## Status

**Current Phase:** Phase 2 — Navigation Layer

This README is the repository-level orientation layer. It does not redefine the substantive authority of documents contained within the repository.
