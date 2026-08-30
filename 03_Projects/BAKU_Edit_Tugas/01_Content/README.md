# BAKU Edit Tugas — Content System

## Purpose

Folder ini berisi **canonical content state** untuk BAKU Edit Tugas, termasuk struktur konten, copy yang telah disetujui, production handoff, dan content references yang digunakan dalam proses produksi.

Folder ini adalah **content layer**. Project decisions dan strategic context berada di `../00_Context/`, sedangkan production operating system berada di `../03_Production/`.

## Authority Role

Content di folder ini harus mengikuti keputusan dan batasan yang berlaku pada project context.

Authority tetap mengikuti hirarki project:

`Repository / System Authority → Project Context → Production Documentation → Working Content → Exploratory Output`

Content yang masih berupa eksplorasi, mockup, atau draft tidak dianggap canonical sampai secara eksplisit disetujui dan dicatat pada project decision/context layer bila diperlukan.

## Current Content Structure

```text
01_Content/
└── Instagram/
    └── Story_Highlight_FAQ/
        ├── CONTENT.md
        └── PRODUCTION_HANDOFF.md
```

### `Instagram/`

Content yang ditujukan untuk Instagram. Struktur platform dapat berkembang sesuai kebutuhan produksi tanpa mengubah authority model project.

### `Instagram/Story_Highlight_FAQ/`

Workstream FAQ Highlight Instagram yang saat ini menjadi content-production workstream aktif.

## Current Workstream

**Instagram Story Highlight — FAQ**

Tujuan content asset:

`Profile → FAQ Highlight → Trust → Inquiry → Conversion`

FAQ Highlight berfungsi sebagai persistent decision-support content untuk calon pelanggan yang telah mengunjungi profil BAKU Edit Tugas.

## Canonical Content State

Four-story FAQ structure yang saat ini tercatat sebagai canonical:

### Story 1 — Positioning

Hook: `Ini joki skripsi ya?`

Answer:

`Bukang! Torang itu dampingi`

`Supaya ngana mangarti`

Supporting copy: `Konsultasi & revisi sesuai kebutuhan.`

### Story 2 — Speed

Hook: `Berapa lama?`

Answer: `1–3 hari`

Supporting copy: `Tergantung panjang & tingkat pengerjaan.`

### Story 3 — Privacy

Hook: `Privasi aman?`

Answer: `Aman. File tidak disebarkan.`

Supporting copy: `Bisa request hapus setelah selesai.`

### Story 4 — Accessibility + Conversion

Hook: `Bisa luar Manado?`

Answer: `Bisa. 100% online.`

CTA: `Butuh bantuan? Chat BAKU →`

Untuk detail lengkap purpose, visual direction, dan production state, gunakan `Instagram/Story_Highlight_FAQ/CONTENT.md` dan `PRODUCTION_HANDOFF.md`.

## Content Principles

Content BAKU Edit Tugas harus:

- jelas dan langsung dipahami;
- relevan dengan kebutuhan siswa dan mahasiswa;
- santai tetapi profesional;
- tidak menggunakan klaim yang tidak dapat dipertanggungjawabkan;
- menjaga distinction antara editing, pengerjaan, konsultasi, dan assistance;
- menggunakan CTA yang jelas ketika conversion atau inquiry menjadi tujuan;
- mempertahankan konsistensi dengan approved brand dan visual system.

Preferensi copy utama:

`Problem → Solution → Benefit → CTA`

Gunakan copy sesingkat mungkin tanpa menghilangkan konteks yang diperlukan.

## Production Relationship

Content layer bekerja bersama project dan production layer:

- `../00_Context/` — project decisions, context, evidence boundaries, dan current state.
- `../02_Assets/` — canonical brand assets.
- `../03_Production/` — production workflows, SOPs, standards, QC, templates, knowledge, dan governance.

Canva dapat digunakan sebagai finalization layer ketika diperlukan untuk typography, logo, alignment, spacing, CTA, dan final visual QC.

## Status Vocabulary

Gunakan status berikut secara konsisten:

- `APPROVED` — final dan disetujui.
- `WORKING` — sedang dikembangkan.
- `DRAFT` — draft belum disetujui.
- `SUPERSEDED` — digantikan oleh versi/keputusan yang lebih baru.
- `OPEN` — masih membutuhkan keputusan.
- `BLOCKED` — tidak dapat dilanjutkan tanpa informasi atau keputusan yang diperlukan.

## Maintenance Rules

1. Jangan membuat duplicate source of truth di dalam content folder.
2. Perubahan canonical content harus tercermin pada file content yang relevan dan, bila merupakan keputusan project, dicatat pada `../00_Context/DECISIONS.md`.
3. Jangan mempertahankan placeholder atau content lama yang telah superseded tanpa penandaan yang jelas.
4. Bedakan dengan jelas antara approved content, working drafts, dan exploratory output.
5. Jangan mengubah locked project decisions dari layer content secara diam-diam.
6. Tambahkan struktur content baru hanya ketika kebutuhan produksi nyata sudah ada.

## Current Status

**ACTIVE** — `Instagram/Story_Highlight_FAQ/` adalah workstream content aktif. Story 1 memiliki approved visual baseline; Stories 2–4 merupakan item produksi berikutnya.
