# BAKU Edit Tugas — Production System

Folder ini berisi sistem operasional produksi pekerjaan klien BAKU Edit Tugas.

## Tujuan

Menstandarkan proses pengerjaan layanan akademik berbantuan AI agar setiap pekerjaan dapat dikerjakan secara konsisten, dapat diperiksa, dan dapat ditingkatkan dari waktu ke waktu.

## Prinsip Utama

> AI assists the work; human owns the academic responsibility.

AI digunakan sebagai alat bantu untuk mempercepat dan meningkatkan kualitas pekerjaan. Human review tetap wajib untuk judgment akademik, factual accuracy, citation verification, dan keputusan final.

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

## Batasan Data

Folder ini **tidak digunakan sebagai penyimpanan utama dokumen klien atau data pribadi klien**. Informasi sensitif dan file pekerjaan klien harus ditempatkan pada workspace produksi yang sesuai dan tidak dikomit ke repository kecuali ada alasan operasional yang jelas dan telah dipastikan aman.

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

Master Workflow adalah sumber rujukan proses. SOP, AI workflow, QC, dan template diturunkan dari workflow ini.
