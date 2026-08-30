# BAKU Edit Tugas — Master Production Workflow

**Status:** Active
**Version:** 1.0
**Purpose:** Menjadi sumber kebenaran utama alur produksi pekerjaan klien BAKU Edit Tugas.

## 1. Production Principle

BAKU menyediakan bantuan akademik berbasis AI dengan human oversight.

> AI assists the work; human owns the academic responsibility.

AI tidak dianggap sebagai sumber kebenaran tunggal. Output AI harus diperlakukan sebagai draft atau assistance sampai diverifikasi.

## 2. End-to-End Workflow

```text
01 Intake
    ↓
02 Requirement Analysis
    ↓
03 Document Diagnosis
    ↓
04 Editing Plan
    ↓
05 AI-Assisted Editing
    ↓
06 Human Review
    ↓
07 Fact & Citation Verification
    ↓
08 Formatting
    ↓
09 Final QC
    ↓
10 Delivery
```

## 3. Stage Definitions

### 01 — Intake

**Objective:** Mengumpulkan informasi minimum yang diperlukan untuk memahami pekerjaan.

**Input:** Permintaan klien, file, brief, deadline, dan persyaratan yang tersedia.

**Output:** Intake record yang lengkap dan pekerjaan yang dapat dianalisis.

**Gate:** Tidak ada pekerjaan dimulai sebelum scope, deadline, dan file utama cukup jelas.

### 02 — Requirement Analysis

**Objective:** Menerjemahkan permintaan klien menjadi requirement yang dapat dikerjakan.

Periksa:
- jenis dokumen;
- tujuan dokumen;
- instruksi dosen/institusi;
- bahasa;
- gaya penulisan;
- citation style;
- format;
- batasan dan prioritas;
- deadline.

**Output:** Requirement summary / editing brief.

### 03 — Document Diagnosis

**Objective:** Menentukan kondisi dokumen sebelum editing.

Periksa minimal:
- grammar dan spelling;
- clarity;
- coherence;
- struktur;
- konsistensi istilah;
- citation/reference;
- formatting;
- kemungkinan factual issues;
- bagian yang ambigu atau kurang informasi.

**Output:** Diagnosis dan daftar masalah yang diprioritaskan.

### 04 — Editing Plan

**Objective:** Menentukan apa yang akan diperbaiki, apa yang dipertahankan, dan bagaimana AI akan digunakan.

Prinsip:
- pertahankan makna dan intent penulis;
- jangan mengubah fakta tanpa dasar;
- bedakan editing dari content creation;
- gunakan AI hanya pada task yang sesuai;
- tandai area yang membutuhkan human judgment.

**Output:** Editing plan yang dapat dieksekusi.

### 05 — AI-Assisted Editing

**Objective:** Menggunakan AI untuk mempercepat dan meningkatkan pekerjaan editing.

Use case umum:
- grammar correction;
- spelling;
- sentence clarity;
- rephrasing;
- academic tone;
- paragraph coherence;
- redundancy detection;
- structure suggestions;
- checklist-based review.

AI **tidak otomatis memiliki otoritas** untuk:
- menetapkan fakta;
- mengarang sumber;
- memvalidasi citation tanpa pemeriksaan;
- membuat keputusan akademik final.

**Output:** Draft hasil editing berbantuan AI.

### 06 — Human Review

**Objective:** Memastikan perubahan AI sesuai konteks dan tidak merusak makna.

Reviewer memeriksa:
- apakah intent penulis tetap;
- apakah perubahan masuk akal;
- apakah ada perubahan makna;
- apakah gaya konsisten;
- apakah AI memperkenalkan klaim baru;
- apakah ada bagian yang perlu dikembalikan atau ditulis ulang.

**Output:** Human-reviewed draft.

### 07 — Fact & Citation Verification

**Objective:** Memastikan klaim dan referensi yang membutuhkan verifikasi memiliki dasar yang dapat dipertanggungjawabkan.

Prinsip:
- sumber primer diprioritaskan bila relevan;
- citation harus dapat dilacak;
- jangan menerima referensi AI tanpa verifikasi;
- pisahkan factual editing dari factual invention.

**Output:** Verified content dan citation status.

### 08 — Formatting

**Objective:** Menyesuaikan dokumen dengan requirement yang berlaku.

Periksa:
- heading;
- numbering;
- spacing;
- margins;
- typography;
- page layout;
- table/figure formatting;
- references;
- file naming.

**Output:** Formatted document.

### 09 — Final QC

**Objective:** Memastikan pekerjaan siap dikirim.

Minimal check:
- requirement terpenuhi;
- isi konsisten;
- grammar diperiksa;
- citation/reference diperiksa;
- formatting sesuai;
- tidak ada placeholder;
- tidak ada AI artifact yang mengganggu;
- file dapat dibuka;
- versi final benar.

**Output:** Approved final deliverable.

### 10 — Delivery

**Objective:** Menyerahkan hasil dengan jelas dan tanpa ambiguity.

Delivery harus menyertakan:
- file final;
- informasi revisi bila relevan;
- catatan keterbatasan bila ada;
- next action bila diperlukan.

## 4. Decision Rules

### Editing vs Writing

Jika klien menyediakan draft, default-nya adalah mempertahankan substansi dan memperbaiki kualitas dokumen.

Jika pekerjaan membutuhkan penambahan substansi, bagian tersebut harus dapat dibedakan secara internal dari pure editing dan memerlukan review yang lebih ketat.

### AI vs Human

Gunakan AI untuk pattern work, drafting assistance, restructuring suggestions, dan language assistance.

Gunakan human judgment untuk intent, factual reliability, academic appropriateness, source verification, dan final approval.

## 5. Quality Gate

Tidak ada tahap yang dianggap selesai hanya karena AI menghasilkan output.

Setiap stage harus menghasilkan output yang cukup jelas untuk menjadi input stage berikutnya.

## 6. Change Control

Perubahan terhadap Master Workflow harus disengaja dan didokumentasikan. SOP, prompt, template, dan QC tidak boleh diam-diam menyimpang dari workflow ini.
