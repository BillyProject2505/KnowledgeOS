# BAKU Edit Tugas — QC System

**Status:** Active  
**Version:** 2.1  
**Authority:** Derived from `01_Workflows/Operating_Model.md` v2.1, `01_Workflows/Control_Matrix.md` v2.1, and `01_Workflows/Master_Workflow.md` v2.1

## Purpose

Folder ini berisi quality-control artifacts untuk memverifikasi apakah hasil produksi memenuhi scope, applicable requirements, mandatory controls, dan Final QC gate sebelum delivery.

QC memverifikasi hasil eksekusi. QC tidak menggantikan atau mendefinisikan ulang normative controls yang ditetapkan pada workflow, control matrix, dan SOP.

## QC Principles

- QC verifies outcomes; it does not redefine normative controls.
- Gunakan control IDs yang ditetapkan di `01_Workflows/Control_Matrix.md`.
- Record evidence secara proporsional terhadap risk dan scope.
- Jangan mengubah missing evidence langsung menjadi `FAIL`; terapkan aturan evidence sufficiency yang berlaku.
- Pertahankan status `OPEN`, `WAITING_AUTHOR`, `WAITING_SOURCE`, dan `ESCALATED` sampai finding diselesaikan atau di-escalate sesuai prosedur.
- Critical unresolved findings block delivery.

## QC Layer

```text
Operating_Model.md
        ↓
Control_Matrix.md
        ↓
Master_Workflow.md
        ↓
SOPs
        ↓
QC Artifacts
        ↓
Final QC / Delivery Gate
```

QC artifacts digunakan untuk memverifikasi eksekusi control dan SOP. Mereka tidak boleh menjadi competing source of normative rules.

## Current QC Artifact Set

QC artifact set sudah tersedia dan digunakan sebagai layer pemeriksaan produksi:

| Artifact | Fungsi |
|---|---|
| `QC-01_Intake_QC.md` | Memverifikasi intake, Work Brief, requirement inventory, dan guideline gate bila applicable. |
| `QC-02_Production_and_Human_Review_QC.md` | Memverifikasi production execution dan human review. |
| `QC-03_Academic_Compliance_QC.md` | Memverifikasi academic compliance dan applicable requirements. |
| `QC-04_Originality_and_AI_Review_QC.md` | Memverifikasi originality/AI-related review sesuai scope dan control yang berlaku. |
| `QC-05_Final_QC.md` | Memverifikasi final production state sebelum delivery. |
| `Final_QC_Checklist.md` | Checklist final delivery gate yang berorientasi pada requirement, content, language, coherence, citation/evidence, AI output, formatting, dan delivery. |
| `E2E-01_Production_Workflow_Integration_Test.md` | Verifikasi integrasi end-to-end production workflow. |
| `E2E-01_Synthetic_Execution_Packet.md` | Paket eksekusi sintetis untuk pengujian workflow dan QC. |

Artifacts harus mereferensikan applicable control IDs dan prosedur terkait daripada menduplikasi definisi control secara penuh.

## Final QC Gate

Final delivery tidak ditentukan hanya berdasarkan keberadaan output atau penyelesaian langkah produksi.

`READY FOR DELIVERY` hanya dapat diberikan ketika requirement utama terpenuhi, critical findings telah diselesaikan, human review telah dilakukan, fakta dan citation yang relevan telah diverifikasi, serta file final telah diperiksa setelah ekspor.

Untuk detail gate, gunakan:

- `QC-05_Final_QC.md`
- `Final_QC_Checklist.md`

## Issue Handling

Gunakan klasifikasi project yang berlaku ketika mendokumentasikan finding:

- `Critical Issue` — harus diperbaiki dan dapat memblok delivery.
- `Improvement` — sebaiknya diperbaiki tetapi tidak otomatis memblok delivery.
- `Preference` — opsional dan tidak memengaruhi minimum quality gate.

Gunakan status finding secara konsisten. Jangan menutup issue hanya karena tidak ada solusi langsung; escalate atau pertahankan statusnya sesuai evidence dan control yang berlaku.

## Relationship to Production System

QC adalah salah satu layer dalam `03_Production/` dan harus tetap konsisten dengan:

- `01_Workflows/` — normative workflow dan control model;
- `02_SOP/` — procedures;
- `03_AI/` — AI usage and workflow boundaries;
- `04_Standards/` — quality and formatting standards;
- `08_Governance/` — change control and authority.

QC tidak boleh memperkenalkan requirement baru yang tidak berasal dari applicable project requirements, controls, standards, atau governance.

## Evidence & Traceability

Evidence yang dicatat harus cukup untuk menunjukkan dasar dari hasil QC tanpa membuat dokumentasi yang tidak perlu.

Untuk setiap finding yang material, pertahankan traceability ke:

`Requirement → Control → Procedure → Evidence → Finding → Decision`

Jika sumber atau evidence belum cukup, gunakan status yang sesuai seperti `REVIEW`, `WAITING_SOURCE`, atau `ESCALATED` daripada mengarang keputusan.

## Current Status

**ACTIVE — QC artifact set tersedia dan menjadi bagian dari production gate.**

README ini menjelaskan fungsi dan hubungan antar-QC artifacts. Detail normative controls tetap berada pada workflow dan control matrix, bukan di README ini.

## Maintenance Rule

Perubahan pada QC yang mengubah gate behavior, required evidence, status semantics, atau control applicability harus ditinjau terhadap `01_Workflows/Operating_Model.md` dan `01_Workflows/Control_Matrix.md` sebelum disetujui.

Jangan menambah checklist atau layer baru hanya untuk menambah dokumentasi. Tambahkan artifact baru hanya ketika terdapat kebutuhan operasional yang nyata, dapat dipelihara, dan memiliki authority yang jelas.
