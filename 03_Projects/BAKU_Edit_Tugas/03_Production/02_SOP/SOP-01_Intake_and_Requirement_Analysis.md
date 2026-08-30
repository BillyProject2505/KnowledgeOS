# BAKU Edit Tugas — SOP-01 Intake & Requirement Analysis

**Status:** Approved  
**Version:** 2.1  
**Type:** Standard Operating Procedure  
**Authority:** Derived from `Operating_Model.md` v2.1 and `Control_Matrix.md` v2.1  
**Primary Controls:** MC-01, MC-04

## 1. Purpose

Menstandarkan cara menerima pekerjaan, mengubah permintaan klien menjadi Work Brief yang dapat diproduksi, dan memastikan requirement eksternal yang relevan tersedia serta dapat diverifikasi sebelum diagnosis/production berjalan.

SOP ini menjawab **bagaimana operator menjalankan intake dan requirement analysis**. Aturan normatif tetap berada di `Operating_Model.md`.

## 2. Scope

Berlaku untuk semua pekerjaan klien BAKU Edit Tugas pada tahap intake.

MC-04 menjadi aktif ketika client, instructor, institution, assignment, journal, atau requirement eksternal lain menjadi bagian dari scope/compliance requirement.

## 3. Inputs

Gunakan input yang tersedia dan relevan:

- client request;
- client-provided files/drafts;
- service request/scope;
- academic level;
- institution/program;
- deadline;
- output format;
- instructor/client requirements;
- reference/source materials;
- institutional or assignment guideline;
- known constraints or dependencies.

## 4. Procedure

### Step 1 — Register the Request

Catat minimal:

- service type;
- document type;
- academic level;
- institution/program bila relevan;
- requested scope;
- deadline;
- expected output format;
- files received.

Jangan mengasumsikan detail yang belum diberikan.

### Step 2 — Normalize the Scope

Ubah permintaan bebas menjadi scope yang dapat dikerjakan.

Pisahkan:

- requested service;
- included work;
- excluded/unknown work;
- deadline;
- dependencies.

Jika scope masih ambigu, tandai `CLARIFICATION_REQUIRED` sebelum production.

### Step 3 — Capture Requirements

Kelompokkan requirement yang ditemukan menjadi:

- client requirements;
- instructor requirements;
- institutional requirements;
- document/format requirements;
- source/reference requirements;
- other explicit constraints.

Jangan mengubah preferensi operator menjadi requirement tanpa dasar.

### Step 4 — Identify Institutional Guideline Applicability

Tentukan apakah pekerjaan memiliki requirement institusional/assignment yang harus diikuti.

Jika **tidak ada**:

- catat bahwa institutional guideline tidak tersedia/tidak diperlukan untuk scope tersebut;
- jangan membuat klaim compliance terhadap guideline yang tidak ada.

Jika **ada**:

lanjutkan MC-04.

### Step 5 — Validate Guideline Source

Untuk guideline yang berlaku, catat:

- title;
- issuing institution/program;
- version/year bila tersedia;
- source URL atau file source;
- applicability metadata;
- access/readability status.

Pastikan guideline berasal dari authority yang relevan.

Jangan menggunakan guideline program/institusi lain hanya karena tampak serupa.

Jika source tidak dapat diidentifikasi, tidak dapat dibaca, atau applicability tidak dapat dipastikan:

`UNVERIFIED / REVIEW`

### Step 6 — Extract Applicable Requirements

Ekstrak hanya requirement yang relevan terhadap pekerjaan.

Untuk setiap requirement, catat minimal:

```text
Requirement ID
Requirement summary
Guideline section/page
Applicability
Evidence needed
```

Jangan mengarang requirement yang tidak ditemukan dalam source.

### Step 7 — Build the Work Brief

Work Brief minimal harus berisi:

- service;
- document;
- scope;
- audience/academic context when relevant;
- deadline;
- output requirements;
- requirement sources;
- guideline status;
- known dependencies;
- unresolved questions.

### Step 8 — Determine Intake Gate

Gunakan keputusan:

- `READY_FOR_DIAGNOSIS` — minimum information tersedia;
- `CLARIFICATION_REQUIRED` — requirement penting belum jelas;
- `REVIEW / UNVERIFIED` — guideline/source requirement belum cukup dapat diverifikasi.

Jangan meneruskan pekerjaan sebagai fully specified jika input kritis masih hilang.

## 5. Work Brief Minimum Fields

| Field | Required When |
|---|---|
| Service type | Always |
| Document type | Always |
| Scope | Always |
| Deadline | Always |
| Output format | When specified/needed |
| Academic level | Academic work |
| Institution/program | When institutional requirements may apply |
| Client/instructor requirements | When provided |
| Guideline source | When compliance is requested/required |
| Reference/source materials | When relevant |
| Open questions/dependencies | When applicable |

## 6. Guideline Gate Rules

### Guideline identified and readable

Proceed to requirement extraction and compliance planning.

### Guideline identified but inaccessible/unreadable

Status:

`UNVERIFIED`

Do not claim compliance.

### Guideline available but applicability uncertain

Status:

`REVIEW`

Do not force-fit the requirement.

### Multiple possible guidelines

Prefer the authoritative and applicable source based on institution/program, version, date, and explicit applicability. If unresolved, escalate before making a compliance claim.

## 7. Outputs

At the end of SOP-01, produce:

1. **Work Brief**
2. **Requirement Source Inventory**
3. **Guideline Record** when applicable
4. **Applicable Requirement List/Matrix** when MC-04 is active
5. **Open Questions / Dependencies**
6. Intake gate decision

## 8. Quality Checks

Before handoff to `02 Diagnose + Risk`, verify:

- scope is explicit enough to diagnose;
- critical files are present or missing items are recorded;
- institution/program captured when relevant;
- external requirements are identified;
- guideline source is recorded when applicable;
- no requirement was invented;
- unresolved ambiguity is visible;
- intake gate decision is recorded.

## 9. Escalation Rules

Escalate or stop intake when:

- client requests conflict materially with known institutional requirements and no resolution is available;
- guideline applicability cannot be established;
- required source/material is missing;
- scope would require substantive academic decisions outside the approved service;
- a request appears to require fabrication, concealment, or other prohibited activity.

Use the normative escalation/authorization rules in `Operating_Model.md` and record the applicable control outcome.

## 10. Handoff

Successful handoff to `02 Diagnose + Risk` requires:

```text
Work Brief
+
Requirement Source Inventory
+
Applicable Guideline Record (when required)
+
Open Questions / Dependencies
```

Do not treat an unresolved clarification as silently resolved during handoff.

## 11. Control Traceability

| Control | SOP Step | Evidence |
|---|---|---|
| MC-01 Client Requirement Capture | Steps 1–3, 7–8 | Work Brief + requirement/source inventory |
| MC-04 Institutional Guideline Gate | Steps 4–6 | Guideline Record + applicable requirement list/matrix |

Normative control definitions remain in:

`../01_Workflows/Operating_Model.md`

Control specification remains in:

`../01_Workflows/Control_Matrix.md`

## 12. Change Control

Changes to this SOP that alter control applicability, required evidence, decision gates, or scope must be reviewed against `Operating_Model.md` and `Control_Matrix.md` before approval.
