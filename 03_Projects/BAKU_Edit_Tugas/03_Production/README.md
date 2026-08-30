# BAKU Edit Tugas — Production System

Folder ini berisi sistem operasional produksi pekerjaan klien BAKU Edit Tugas.

## Tujuan

Menstandarkan proses pengerjaan layanan akademik berbantuan AI agar setiap pekerjaan dapat dikerjakan secara konsisten, dapat diperiksa, dan dapat ditingkatkan dari waktu ke waktu.

## Ruang Lingkup

Production System digunakan untuk pekerjaan klien seperti:

- editing tugas;
- pengerjaan tugas;
- konsultasi dan bantuan akademik;
- dokumen akademik dan kebutuhan terkait yang masuk melalui workflow produksi.

Dokumentasi ini adalah sistem operasional produksi. Konteks brand, content strategy, dan keputusan sosial-media tingkat project tetap dikelola di `../00_Context/`, `../01_Content/`, dan `../02_Assets/` sesuai kewenangannya.

## Prinsip Utama

> AI assists the work; human owns the academic responsibility.

AI digunakan sebagai alat bantu untuk mempercepat dan meningkatkan kualitas pekerjaan. Human review tetap wajib untuk judgment akademik, factual accuracy, citation verification, dan keputusan final.

Jangan menganggap output AI sebagai sumber kebenaran tanpa pemeriksaan.

## Struktur

```text
03_Production/
├── 01_Workflows/
├── 02_SOP/
├── 03_AI/
├── 04_Standards/
├── 05_QC/
├── 06_Templates/
├── 07_Knowledge/
└── 08_Governance/
```

### `01_Workflows/`

Alur kerja produksi yang menjelaskan urutan aktivitas dan handoff antar tahap.

### `02_SOP/`

Prosedur operasional standar untuk aktivitas yang berulang.

### `03_AI/`

Pedoman penggunaan AI, prompt/workflow assistance, dan batasan penggunaan AI dalam pekerjaan.

### `04_Standards/`

Standar kualitas, format, penulisan, dokumentasi, dan kriteria kerja yang harus dipenuhi.

### `05_QC/`

Checklist, pemeriksaan kualitas, dan mekanisme review sebelum delivery.

### `06_Templates/`

Template yang digunakan untuk mempercepat pekerjaan tanpa mengorbankan consistency atau judgment.

### `07_Knowledge/`

Knowledge base produksi yang reusable dan relevan untuk penyelesaian pekerjaan.

### `08_Governance/`

Aturan perubahan, ownership, status, provenance, dan pengelolaan sistem produksi.

## Batasan Data

Folder ini **tidak digunakan sebagai penyimpanan utama dokumen klien atau data pribadi klien**.

Informasi sensitif dan file pekerjaan klien harus ditempatkan pada workspace produksi yang sesuai dan tidak dikomit ke repository kecuali ada alasan operasional yang jelas dan telah dipastikan aman.

Repository berfungsi sebagai durable operational knowledge dan production system, bukan sebagai default client-file storage.

## Master Workflow

Alur produksi utama BAKU:

```text
Client Request
    ↓
Intake
    ↓
Requirement Analysis
    ↓
Document Diagnosis
    ↓
Editing Plan
    ↓
AI-Assisted Editing
    ↓
Human Review
    ↓
Fact & Citation Verification
    ↓
Formatting
    ↓
Final QC
    ↓
Delivery
```

Master Workflow adalah sumber rujukan proses. SOP, AI workflow, QC, dan template harus konsisten dengan workflow ini.

## Production Quality Gate

Tidak ada pekerjaan yang dianggap final hanya karena AI telah menghasilkan output.

Sebelum delivery, output harus melewati human review dan pemeriksaan yang relevan, termasuk:

- kesesuaian terhadap requirement klien;
- academic judgment;
- factual accuracy;
- citation/reference verification;
- formatting;
- final QC.

Tahap yang tidak relevan untuk jenis pekerjaan tertentu dapat diadaptasi berdasarkan requirement, tetapi tidak boleh dihilangkan tanpa alasan yang jelas.

## Relationship to Project Context

Project-level decisions tetap berada di:

`../00_Context/`

Canonical content state berada di:

`../01_Content/`

Canonical brand assets berada di:

`../02_Assets/`

Production System mengeksekusi pekerjaan berdasarkan keputusan dan batasan yang berlaku pada project context. Jika terjadi konflik, jangan mengubah keputusan secara diam-diam; gunakan decision register sebagai rujukan dan catat perubahan yang disetujui.

## Current Integration with BAKU Project

Social-content production dan client-work production adalah dua konteks yang berbeda namun menggunakan prinsip operasional yang sama: clear requirements, reusable standards, human review, traceability, dan final QC.

Untuk current social-content state, lihat root project README dan `../00_Context/PROJECT_CONTEXT.md`.

FAQ Highlight yang sedang diproduksi merupakan content-production workstream, sedangkan folder ini menyediakan production operating system untuk pekerjaan klien.

## Status Vocabulary

Gunakan status berikut secara konsisten ketika status produksi perlu dicatat:

- `APPROVED` — final dan disetujui.
- `WORKING` — sedang dikembangkan.
- `DRAFT` — draft belum disetujui.
- `SUPERSEDED` — digantikan keputusan atau versi yang lebih baru.
- `OPEN` — membutuhkan keputusan.
- `BLOCKED` — tidak dapat dilanjutkan tanpa informasi atau keputusan yang diperlukan.

## Maintenance Rule

Perubahan pada workflow, SOP, standards, QC, templates, knowledge, atau governance harus tetap konsisten dengan project authority.

Jangan membuat struktur atau abstraksi baru hanya untuk menambah dokumentasi. Tambahkan aturan, template, atau layer baru hanya ketika terdapat kebutuhan operasional yang nyata dan dapat dipelihara.

Perubahan penting yang menjadi keputusan project harus direkam pada `../00_Context/DECISIONS.md` dan, bila relevan, dicatat di `../00_Context/CHANGELOG.md`.
