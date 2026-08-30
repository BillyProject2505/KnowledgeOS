# BAKU Edit Tugas — Project Context

## Purpose

Folder ini berisi **durable project context** untuk BAKU Edit Tugas: keputusan yang telah disetujui, konteks produksi, platform references, changelog, dan dokumen lain yang menjadi dasar lintas sesi dan lintas tahap produksi.

Folder ini adalah **context and decision layer**, bukan tempat menyimpan seluruh output kerja atau file klien.

## Authority Role

Dokumen di folder ini menjadi sumber rujukan untuk **project-level decisions and context** dalam batas kewenangannya.

Authority tetap mengikuti hirarki project:

`Repository / System Authority → Project Context → Production Documentation → Working Content → Exploratory Output`

Project Context tidak mengoverride repository-level, system-level, atau Universal authority.

Exploratory output, mockup, dan keputusan sementara tidak dianggap canonical sampai disetujui dan dicatat pada decision register.

## Files

### `PROJECT_CONTEXT.md`

Ringkasan kondisi project saat ini, workstream aktif, production state, format, visual system, content structure, claim boundaries, dan open items.

### `DECISIONS.md`

Decision register untuk keputusan project yang telah disetujui, termasuk perubahan yang supersede keputusan sebelumnya.

### `CHANGELOG.md`

Riwayat perubahan penting pada project memory, content state, brand assets, platform references, dan production state.

### `CONTENT_PRODUCTION_BRIEF.md`

Brief strategis dan produksi yang menjadi input untuk pekerjaan content-production yang relevan.

### `META_PLATFORM_GUIDELINES.md`

Living reference untuk guidance platform Meta yang relevan dengan produksi Instagram/Facebook. Dokumen ini harus dibedakan dari project strategy dan tidak boleh diperlakukan sebagai jaminan performa platform.

## Current Project State

Current active workstream:

**Instagram Story Highlight — FAQ**

Current visual baseline:

**Story 1 approved** dengan **flat editorial illustration** sebagai visual system canonical untuk seri FAQ.

Current next production items:

**Stories 2–4**.

Untuk status operasional paling mutakhir, gunakan `PROJECT_CONTEXT.md`. Untuk keputusan yang bersifat canonical, gunakan `DECISIONS.md`.

## Context Maintenance Rules

1. Keputusan yang telah approved harus dicatat di `DECISIONS.md` sebelum diperlakukan sebagai canonical.
2. Perubahan project state yang material harus dicatat di `CHANGELOG.md` bila relevan.
3. Jangan menyimpan duplicate source of truth ketika dokumen yang lebih tepat sudah tersedia.
4. Jangan mengubah keputusan yang telah locked/superseded secara diam-diam.
5. Bedakan dengan jelas antara `APPROVED`, `WORKING`, `DRAFT`, `SUPERSEDED`, `OPEN`, dan `BLOCKED`.
6. Platform guidance harus memiliki evidence boundary yang jelas dan diverifikasi ulang ketika guidance/policy berubah.
7. README ini tetap sebagai **navigation and context guide**; detail normative atau substantive authority berada pada dokumen masing-masing.

## Relationship to Other Project Layers

- `../README.md` — project entry point dan high-level project index.
- `../01_Content/` — canonical content state.
- `../02_Assets/` — canonical project assets.
- `../03_Production/` — production operating system untuk pekerjaan klien.

## Current Status

**ACTIVE** — project context terpelihara dan digunakan sebagai dasar keputusan serta koordinasi produksi BAKU Edit Tugas.
