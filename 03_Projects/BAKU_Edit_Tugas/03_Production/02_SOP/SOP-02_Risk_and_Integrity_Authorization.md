# BAKU Edit Tugas — SOP-02 Risk & Integrity Authorization

**Status:** Approved  
**Version:** 2.1  
**Type:** Standard Operating Procedure  
**Authority:** Derived from `Operating_Model.md` v2.1 and `Control_Matrix.md` v2.1  
**Primary Controls:** MC-02, MC-03

## 1. Purpose

Menstandarkan cara mengklasifikasikan risiko pekerjaan dan menentukan apakah pekerjaan dapat diproduksi dalam scope yang disetujui.

SOP ini menjawab **bagaimana operator menjalankan risk assessment dan authorization**. Aturan normatif tetap berada di `Operating_Model.md`.

## 2. Scope

Berlaku setelah intake/requirement analysis dan sebelum production dimulai.

SOP ini digunakan untuk semua pekerjaan klien, dengan kedalaman assessment yang disesuaikan dengan risk level dan scope.

## 3. Inputs

Gunakan input yang tersedia dan relevan:

- Work Brief;
- requirement/source inventory;
- client/instructor/institution requirements;
- document/draft;
- diagnosis awal atau findings;
- source/reference materials;
- guideline record when applicable;
- known dependencies;
- data-sensitivity observations;
- requested service scope.

## 4. Procedure

### Step 1 — Confirm the Work Brief

Pastikan Work Brief memuat minimal informasi yang diperlukan untuk menilai pekerjaan:

- service;
- document;
- scope;
- deadline;
- applicable requirements;
- known dependencies.

Jika informasi kritis belum tersedia, jangan memaksakan risk classification final. Kembalikan ke clarification path sesuai `MC-01`.

### Step 2 — Identify Risk Factors

Periksa sekurang-kurangnya:

- complexity of the document/task;
- scope of intervention;
- substantive academic content;
- methodology/evidence issues;
- source/citation verification needs;
- institutional compliance requirements;
- privacy/sensitive data concerns;
- originality/AI-review requirements;
- deadline or dependency constraints.

Catat kondisi yang dapat memengaruhi kedalaman review.

### Step 3 — Assign Risk Level

Gunakan tiga level:

- `LOW`
- `MEDIUM`
- `HIGH`

Risk level harus didasarkan pada kondisi aktual pekerjaan, bukan pada harga atau preferensi operator.

Gunakan judgment konservatif bila beberapa faktor menunjukkan kebutuhan review yang lebih tinggi.

### Step 4 — Document Risk Rationale

Catat alasan singkat dan spesifik untuk level yang dipilih.

Contoh struktur:

```text
Risk level: HIGH
Reasons:
- institutional guideline compliance requested;
- substantive methodology review required;
- source verification required;
- sensitive participant data present.
```

Jangan hanya menulis `HIGH` tanpa rationale.

### Step 5 — Determine Authorization Conditions

Berdasarkan Work Brief dan risk assessment, tentukan:

- apakah scope cukup jelas;
- apakah required evidence/source tersedia;
- apakah pekerjaan berada dalam service scope;
- apakah ada issue integrity yang mengharuskan escalation/decline;
- review depth yang diperlukan sebelum delivery.

Gunakan control boundaries pada `Operating_Model.md` dan keputusan service scope yang telah disetujui.

### Step 6 — Check Integrity Boundaries

Periksa apakah permintaan atau kondisi pekerjaan memerlukan tindakan yang tidak dapat diterima dalam workflow produksi.

Contoh yang harus dihentikan atau dieskalasikan:

- fabrication of data, evidence, or sources;
- fabricated research results;
- concealment of unattributed copying;
- detector gaming intended to evade review;
- substantive academic decision being requested without appropriate authority.

Jangan mencari cara alternatif untuk melakukan permintaan yang berada di luar boundary tersebut.

### Step 7 — Confirm Required Evidence and Dependencies

Catat dependency yang masih terbuka, misalnya:

- missing source;
- missing guideline;
- unclear research method;
- missing author decision;
- missing client file;
- unresolved scope question.

Route each dependency to the appropriate resolution state rather than silently assuming it is resolved.

### Step 8 — Make the Authorization Decision

Gunakan outcome berikut:

- `AUTHORIZED` — pekerjaan dapat masuk production dalam scope yang disetujui;
- `CLARIFICATION_REQUIRED` — informasi kritis belum cukup;
- `ESCALATED` — membutuhkan keputusan manusia/responsible reviewer;
- `DECLINED` — pekerjaan berada di luar boundary yang dapat diterima.

### Step 9 — Record the Decision

Authorization record minimal harus menyimpan:

```text
Work item
Risk level
Risk rationale
Approved scope
Required review depth
Open dependencies
Authorization outcome
Decision owner
Date/status
```

## 5. Risk Assessment Guidance

Gunakan faktor berikut sebagai assessment prompts, bukan sebagai automatic scoring formula:

| Risk Factor | Lower-risk indication | Higher-risk indication |
|---|---|---|
| Scope | proofreading/formatting | substantive rewriting/academic assistance |
| Academic substance | language-only | methodology, claims, interpretation, conclusions |
| Requirements | simple client brief | institution/journal compliance |
| Evidence | supplied and clear | missing or requires verification |
| Data sensitivity | no sensitive data | personal/research-participant data |
| Originality/AI review | not in scope | explicit review required |
| Dependencies | none/materially resolved | multiple unresolved dependencies |

Do not convert this table into an automatic numeric score unless separately approved through change control.

## 6. Authorization Gate

Production may begin only when:

- risk level has been assigned;
- scope is sufficiently explicit;
- required boundary decisions are clear;
- critical dependencies are recorded;
- authorization outcome is `AUTHORIZED`.

`CLARIFICATION_REQUIRED`, `ESCALATED`, or `DECLINED` must route away from normal production until appropriately resolved.

## 7. Outputs

Produce:

1. **Risk Assessment**
2. **Risk Rationale**
3. **Approved Scope**
4. **Required Review Depth**
5. **Open Dependencies / Resolution State**
6. **Authorization Decision**

## 8. Quality Checks

Before handoff to `04 Produce`, verify:

- risk classification is documented;
- rationale is specific enough to audit;
- scope is explicit;
- prohibited or integrity-sensitive requests were checked;
- required evidence/dependencies are visible;
- authorization outcome is recorded;
- review depth is appropriate to risk.

## 9. Handoff

Successful handoff to `04 Produce` requires:

```text
Work Brief
+
Risk Assessment
+
Approved Scope
+
Authorization Decision = AUTHORIZED
+
Required Review Depth
+
Known Dependencies / Resolution States
```

## 10. Control Traceability

| Control | SOP Step | Evidence |
|---|---|---|
| MC-02 Risk Classification | Steps 1–4 | Risk Assessment + rationale |
| MC-03 Authorization / Integrity Gate | Steps 5–9 | Authorization record + approved scope + dependencies |

Normative control definitions remain in:

`../01_Workflows/Operating_Model.md`

Control specification remains in:

`../01_Workflows/Control_Matrix.md`

## 11. Change Control

Changes to this SOP that alter risk applicability, authorization outcomes, required evidence, or integrity boundaries must be reviewed against `Operating_Model.md` and `Control_Matrix.md` before approval.
