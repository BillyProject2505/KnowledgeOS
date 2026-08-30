# BAKU Edit Tugas — Production System

Folder ini berisi sistem operasional produksi pekerjaan klien BAKU Edit Tugas.

## Tujuan

Menstandarkan proses pengerjaan layanan akademik berbantuan AI agar setiap pekerjaan dapat dikerjakan secara konsisten, dapat diperiksa, dapat ditelusuri, dan dapat ditingkatkan dari waktu ke waktu.

## Ruang Lingkup

Production System digunakan untuk pekerjaan klien seperti:

- editing tugas;
- pengerjaan tugas;
- konsultasi dan bantuan akademik;
- dokumen akademik dan kebutuhan terkait yang masuk melalui workflow produksi.

Dokumentasi ini adalah sistem operasional produksi. Konteks brand, content strategy, dan keputusan sosial-media tingkat project tetap dikelola di `../00_Context/`, `../01_Content/`, dan `../02_Assets/` sesuai kewenangannya.

## Operating Model

Arsitektur proses produksi ditetapkan pada:

`01_Workflows/Operating_Model.md`

**Version:** 2.1

Operating Model adalah source of truth arsitektural untuk lifecycle, mandatory controls, decision gates, evidence, resolution state, dan Definition of Done.

`01_Workflows/Master_Workflow.md` adalah implementasi workflow operasional yang diturunkan dari Operating Model dan tidak boleh menyimpang secara diam-diam.

## Prinsip Utama

> AI assists the work; human owns the academic responsibility.

AI digunakan sebagai alat bantu untuk mempercepat dan meningkatkan kualitas pekerjaan. Human review tetap wajib untuk judgment akademik, factual accuracy, citation verification, dan keputusan final yang relevan dengan scope/risk pekerjaan.

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

Operating Model dan workflow produksi yang menjelaskan lifecycle, control, urutan aktivitas, dan handoff antar tahap.

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

## Master Production Lifecycle

```text
Client Request
    ↓
01 Intake
    ↓
02 Diagnose + Risk
    ↓
03 Authorize
    ↓
04 Produce
    ↓
05 Review
    ↓
06 Academic QC
    ↓
07 Originality / AI Review [conditional]
    ↓
08 Final QC
    ↓
09 Delivery
    ↓
10 Archive
```

Detail lifecycle dan controls berada di `01_Workflows/Operating_Model.md` dan implementasinya di `01_Workflows/Master_Workflow.md`.

## Production Quality Gate

Tidak ada pekerjaan yang dianggap final hanya karena AI telah menghasilkan output.

Sebelum delivery, output harus memenuhi Definition of Done pada Operating Model dan melewati review/QC yang relevan terhadap scope dan risk, termasuk bila applicable:

- kesesuaian terhadap requirement klien;
- institutional/assignment compliance;
- academic judgment;
- factual accuracy;
- source/citation verification;
- originality/similarity review;
- AI-assistance screening;
- formatting;
- final QC.

Tahap conditional hanya dijalankan ketika applicable, tetapi tidak boleh dilewati tanpa alasan yang jelas dan tercatat.

## Resolution State

Finding production menggunakan status:

- `RESOLVED`
- `OPEN`
- `WAITING_AUTHOR`
- `WAITING_SOURCE`
- `ESCALATED`

Only `RESOLVED` findings satisfy completion requirements.

## Risk Model

Gunakan risk level:

- `LOW`
- `MEDIUM`
- `HIGH`

Risk level menentukan kedalaman evidence, review, dan QC yang diperlukan. Jangan menambah status untuk setiap aktivitas kecil.

## Relationship to Project Context

Project-level decisions tetap berada di:

`../00_Context/`

Canonical content state berada di:

`../01_Content/`

Canonical brand assets berada di:

`../02_Assets/`

Production System mengeksekusi pekerjaan berdasarkan keputusan dan batasan yang berlaku pada project context. Jika terjadi konflik, jangan mengubah keputusan secara diam-diam; gunakan decision register sebagai rujukan dan catat perubahan yang disetujui.

## Repository Boundary

GitHub adalah durable source of truth untuk approved operating knowledge, standards, SOPs, templates, governance, dan dokumentasi project yang memang perlu dipelihara.

Working drafts, client files, personal data, dan production evidence tidak otomatis masuk repository. Simpan di workspace produksi yang sesuai kecuali ada alasan operasional yang jelas dan aman.

Exploratory conversation output adalah working knowledge sampai secara eksplisit disetujui dan direkam.

## Maintenance Rule

Perubahan pada workflow, SOP, standards, QC, templates, knowledge, atau governance harus tetap konsisten dengan Operating Model.

Jangan membuat struktur atau abstraksi baru hanya untuk menambah dokumentasi. Tambahkan aturan, template, atau layer baru hanya ketika terdapat kebutuhan operasional yang nyata dan dapat dipelihara.

Perubahan penting yang menjadi keputusan project harus direkam pada `../00_Context/DECISIONS.md` dan, bila relevan, dicatat di `../00_Context/CHANGELOG.md`.
