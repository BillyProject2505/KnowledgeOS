# 10_Registries

## Purpose

This directory contains system-level registry artifacts for KnowledgeOS's Content OS layer — repository-side materializations of registries whose canonical authority is recorded elsewhere (currently: Linear).

## Scope

A registry artifact here is a machine-readable and/or navigable representation of a registry's current state. It supports mechanical validation (format, uniqueness, sequencing, required fields) of the canonical registry it materializes.

Repository presence does not make a registry artifact canonical. Canonical authority is declared explicitly by each registry's own documentation and its stated canonical source.

## Authority Boundary

This directory is subordinate to the repository-level framework defined in `../../README.md` and to `../README.md`.

Each registry subdirectory declares its own canonical source (the document or system that governs its actual state) and its own authority boundary. This directory does not itself grant or imply canonical authority to anything it contains.

## Navigation

### Parent

- [`../README.md`](../README.md) — 01_System orientation and authority boundary.

### Local Contents

- [`DIUA_DIC`](./DIUA_DIC/) — Content OS Universal Identifier Registry (`DIUA-DIC-*` namespace).

## Maintenance Rules

- Preserve one canonical source per registry; do not fork or duplicate canonical registry prose into this directory.
- Keep machine-readable registry state synchronized with its declared canonical source — do not let them silently drift.
- Do not fabricate, guess, or backfill allocation records; only represent allocations the canonical source actually declares.
- Distinguish reference/illustrative material (see `99_Archive/`) from live registry state.
- Do not create duplicate substantive authority in this README.
- Keep this README focused on navigation, scope, and registry boundaries.
