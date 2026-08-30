# Instagram Story Highlight — FAQ

## Purpose

Folder ini berisi **canonical content state dan production handoff** untuk workstream Instagram Story Highlight — FAQ BAKU Edit Tugas.

README ini berfungsi sebagai **navigation and workstream guide**. Detail content, visual direction, dan production state tetap berada pada dokumen sumber masing-masing.

## Workstream Scope

FAQ Highlight digunakan sebagai persistent decision-support content untuk calon pelanggan yang telah mengunjungi profil BAKU Edit Tugas.

Primary funnel:

`Profile → FAQ Highlight → Trust → Inquiry → Conversion`

Tujuan utamanya:

- menjawab pertanyaan umum;
- mengurangi friction;
- membangun trust;
- membantu calon pelanggan memahami layanan;
- mendorong inquiry melalui CTA yang jelas.

## Structure

```text
Story_Highlight_FAQ/
├── CONTENT.md
├── PRODUCTION_HANDOFF.md
└── README.md
```

### `CONTENT.md`

Canonical content state untuk empat Story, termasuk copy, status, visual baseline, claim boundaries, dan production sequence.

### `PRODUCTION_HANDOFF.md`

Dokumen handoff untuk menerjemahkan canonical content state menjadi pekerjaan visual dan finalisasi produksi.

### `README.md`

Index dan orientation layer untuk workstream ini. README tidak menggantikan authority dokumen content atau project context.

## Current State

**ACTIVE**

- Format: static Instagram Story, 9:16, target 1080 × 1920 px.
- Total: 4 Stories.
- Story 1: **APPROVED** sebagai visual baseline.
- Stories 2–4: **APPROVED CONTENT / visual belum final**.
- Visual system: **flat editorial illustration**.
- Finalization: Canva digunakan untuk typography, logo, alignment, spacing, copy, CTA, dan final visual QC.
- Logo: gunakan canonical BAKU Edit Tugas logo dari `02_Assets/Brand/`.

## Canonical Content Map

| Story | Role | Status |
|---|---|---|
| Story 1 | Positioning | APPROVED visual baseline |
| Story 2 | Speed | APPROVED content / visual open |
| Story 3 | Privacy | APPROVED content / visual open |
| Story 4 | Accessibility + Conversion | APPROVED content / visual open |

Untuk copy dan detail visual per Story, gunakan `CONTENT.md` sebagai source of truth.

## Visual Authority

Story 1 yang telah disetujui merupakan baseline visual canonical untuk seri ini.

Pertahankan:

- struktur layout;
- typography hierarchy dan relative sizing;
- spacing rhythm;
- logo relationship;
- color relationships;
- safe-area treatment;
- flat editorial illustration language;
- overall composition logic.

Elemen yang dapat berubah antar-Story antara lain character, scene, objects, visual metaphor, dan supporting imagery.

Jangan mengembalikan workstream ini ke realistic/cinematic treatment yang telah disupersede.

## Production Flow

```text
Concept
  ↓
Master Frame
  ↓
Generation
  ↓
Visual QC
  ↓
Canva Finalization
  ↓
Final QC
  ↓
Export
```

Untuk current production handoff, gunakan `PRODUCTION_HANDOFF.md`.

## Authority & Boundaries

Workstream ini mengikuti project-level authority di:

`../../../00_Context/`

Hubungan layer:

```text
Project Context
      ↓
Content State
      ↓
Production Handoff
      ↓
Visual Production
      ↓
Final QC
```

Do not create a competing source of truth in this folder.

## Content & Claim Boundaries

Konten harus tetap:

- santai tetapi profesional;
- jelas dan mudah dipahami siswa/mahasiswa;
- tidak menggunakan klaim yang tidak dapat dipertanggungjawabkan;
- tidak menggunakan fabricated statistics/social proof;
- tidak membuat absolute-security/privacy claims tanpa dasar;
- tidak menjanjikan performa reach, recommendation, engagement, atau conversion.

Untuk evidence dan platform guidance, gunakan `00_Context/META_PLATFORM_GUIDELINES.md` dan dokumen project context yang relevan.

## Status Vocabulary

- `APPROVED` — final dan disetujui.
- `WORKING` — sedang dikembangkan.
- `DRAFT` — draft belum disetujui.
- `OPEN` — membutuhkan keputusan atau pekerjaan lanjutan.
- `SUPERSEDED` — digantikan versi/keputusan yang lebih baru.
- `BLOCKED` — tidak dapat dilanjutkan tanpa informasi atau keputusan yang diperlukan.

## Maintenance Rules

1. `CONTENT.md` tetap menjadi source of truth untuk canonical content state.
2. `PRODUCTION_HANDOFF.md` tetap menjadi source untuk handoff produksi.
3. Keputusan project-level yang material harus dicatat pada `00_Context/DECISIONS.md`.
4. Jangan mempertahankan copy, visual, atau direction lama tanpa penandaan `SUPERSEDED` bila sudah diganti.
5. Jangan menambahkan struktur baru tanpa kebutuhan produksi nyata.
6. README ini hanya menjelaskan orientasi workstream dan relationship antar-dokumen.

## Current Next Step

**Produce Story 2 using the approved Story 1 visual baseline and canonical Story 2 copy.**
