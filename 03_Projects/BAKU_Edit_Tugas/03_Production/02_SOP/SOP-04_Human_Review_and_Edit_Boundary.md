# BAKU Edit Tugas — SOP-04 Human Review & Edit Boundary

**Status:** Approved  
**Version:** 2.1  
**Type:** Standard Operating Procedure  
**Authority:** Derived from `Operating_Model.md` v2.1 and `Control_Matrix.md` v2.1  
**Primary Controls:** MC-05, MC-06, MC-07, MC-08

## 1. Purpose

Menstandarkan review manusia setelah production untuk memastikan hasil tetap sesuai scope, mempertahankan makna penulis, menghormati edit authority, dan tidak meninggalkan finding yang belum ditangani secara diam-diam.

SOP ini menjawab **bagaimana reviewer memeriksa hasil production**. Aturan normatif tetap berada di `Operating_Model.md`, sedangkan control specification berada di `Control_Matrix.md`.

## 2. Scope

Berlaku setelah tahap production dan sebelum Academic QC.

Gunakan untuk pekerjaan yang menghasilkan perubahan teks, struktur, wording, atau substantive content yang perlu diverifikasi manusia.

## 3. Inputs

- production draft;
- original/source document;
- Work Brief;
- approved scope;
- applicable requirements;
- change evidence when available;
- tracked findings/dependencies;
- relevant source/reference material.

## 4. Procedure

### Step 1 — Confirm Review Scope

Pastikan reviewer mengetahui:

- approved service scope;
- document sections in scope;
- known exclusions;
- risk level;
- required review depth;
- known dependencies and findings.

Jangan melakukan review substantif di luar scope tanpa routing sesuai authorization.

### Step 2 — Compare Output to Original

Bandingkan production draft dengan source/original untuk menemukan:

- unintended deletion;
- unintended addition;
- changed claim;
- changed evidence relationship;
- changed terminology;
- changed methodology or research meaning;
- excessive rewriting;
- formatting or language regressions.

Gunakan proportional sampling untuk pekerjaan berisiko rendah dan full review untuk material/high-risk changes sesuai authorization.

### Step 3 — Check E1 Interventions

Pastikan direct edits:

- memperbaiki masalah yang jelas;
- tidak mengubah intent;
- tidak menambahkan substantive content;
- tidak menimbulkan inconsistency baru.

Jika E1 berubah menjadi substantive intervention, reclassify and route through the appropriate authority.

### Step 4 — Check E2 Interventions

Periksa perubahan editorial yang membutuhkan contextual judgment:

- coherence;
- terminology;
- paragraph structure;
- controlled restructuring.

Pastikan perubahan mempertahankan:

- claim;
- intended meaning;
- academic position;
- relationship to surrounding context.

Catat material E2 changes untuk semantic review bila diperlukan.

### Step 5 — Identify E3 Conditions

Cari perubahan atau finding yang menyentuh:

- methodology;
- research design;
- evidence interpretation;
- claim strength;
- conclusions;
- substantive academic position.

Jika ditemukan:

- jangan menyelesaikan secara silent;
- buat finding;
- jelaskan decision dependency;
- route melalui `MC-07`.

### Step 6 — Perform Meaning Preservation Check

Untuk material changes:

```text
Original / Context
        ↓
Proposed Version
        ↓
Meaning Comparison
        ↓
PRESERVED / ALTERED / UNCERTAIN
```

Gunakan normative states dari `Operating_Model.md → MC-06`.

Jika `ALTERED` atau `UNCERTAIN` belum dapat diselesaikan, jangan menandainya selesai.

### Step 7 — Check Over-Editing

Identifikasi perubahan yang:

- hanya mengubah gaya tanpa tujuan scope;
- memperpanjang teks tanpa kebutuhan;
- membuat claim terdengar lebih kuat;
- menambah jargon atau terminology yang tidak diperlukan;
- menghapus kualifikasi/hedging yang penting.

Kembalikan atau route perubahan yang tidak diperlukan sesuai scope.

### Step 8 — Review Findings and Resolution States

Pastikan setiap tracked finding memiliki:

- current status;
- owner;
- evidence/dependency bila relevan;
- next action.

Gunakan resolution state normatif dari `Operating_Model.md`.

Jangan mengubah `OPEN`, `WAITING_AUTHOR`, `WAITING_SOURCE`, atau `ESCALATED` menjadi `RESOLVED` hanya untuk melewati gate.

### Step 9 — Record Review Decision

Untuk material findings, record minimal:

```text
Finding
Evidence
Impact
Authority: E1 / E2 / E3
Review decision
Resolution state
Decision owner when applicable
```

### Step 10 — Determine Review Outcome

Gunakan outcome operasional:

- `ACCEPTED` — draft sesuai scope dan tidak ada material review blocker;
- `REVISE` — perubahan/issue perlu diperbaiki dalam scope;
- `ESCALATED` — memerlukan keputusan manusia/author;
- `BLOCKED` — tidak dapat maju sampai dependency atau control terselesaikan.

### Step 11 — Prepare Handoff to Academic QC

Handoff hanya dilakukan ketika:

- scope review selesai;
- meaning preservation sudah dinilai untuk material changes;
- E3 sudah diroute;
- tracked findings memiliki state yang benar;
- unresolved blockers tetap terlihat.

## 5. Review Checklist

Reviewer minimal memeriksa:

- scope conformity;
- additions/deletions;
- meaning preservation;
- E1/E2/E3 classification;
- unsupported claims or facts introduced by editing;
- methodology/evidence changes;
- over-editing;
- terminology consistency;
- unresolved findings;
- correct resolution states.

## 6. Review Outcome Rules

### ACCEPTED

Tidak ada material issue yang memblokir handoff.

### REVISE

Issue dapat diperbaiki dalam approved scope tanpa E3 decision dependency.

### ESCALATED

Issue membutuhkan author/responsible human decision.

### BLOCKED

Required information, evidence, authorization, or resolution belum tersedia sehingga pekerjaan tidak aman untuk dilanjutkan.

## 7. Outputs

Produce:

1. Human-reviewed draft
2. Review findings
3. Semantic review evidence when required
4. Escalation records when applicable
5. Updated resolution states
6. Review outcome

## 8. Quality Checks

Sebelum handoff:

- setiap material change sudah dinilai;
- tidak ada silent substantive change;
- unresolved findings tidak disembunyikan;
- state/status mencerminkan kondisi sebenarnya;
- review outcome tercatat;
- output sesuai approved scope.

## 9. Handoff

Successful handoff to `06 Academic QC` requires:

```text
Reviewed Draft
+
Review Findings / Evidence
+
Semantic Review Result when applicable
+
Resolution States
+
Review Outcome = ACCEPTED or appropriately routed resolution
```

## 10. Control Traceability

| Control | SOP Step | Evidence |
|---|---|---|
| MC-05 Edit Authority | Steps 3–5 | Intervention classification / review notes |
| MC-06 Meaning Preservation | Step 6 | Original-vs-edited semantic review |
| MC-07 Substantive Change Escalation | Step 5, 9–10 | Escalation record + decision dependency |
| MC-08 Resolution State | Step 8–11 | Finding state + owner + resolution evidence |

Normative control definitions remain in:

`../01_Workflows/Operating_Model.md`

Control specification remains in:

`../01_Workflows/Control_Matrix.md`

## 11. Change Control

Changes to this SOP that alter review authority, semantic verification, escalation behavior, resolution state handling, or required evidence must be reviewed against `Operating_Model.md` and `Control_Matrix.md` before approval.
