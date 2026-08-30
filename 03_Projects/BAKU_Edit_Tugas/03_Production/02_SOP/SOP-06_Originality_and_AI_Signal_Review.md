# BAKU Edit Tugas — SOP-06 Originality & AI-Signal Review

**Status:** Approved  
**Version:** 2.1  
**Type:** Standard Operating Procedure  
**Authority:** Derived from `Operating_Model.md` v2.1 and `Control_Matrix.md` v2.1  
**Primary Controls:** MC-08, MC-09

## 1. Purpose

Menstandarkan cara menjalankan originality/similarity review dan AI-assistance signal review ketika tahap tersebut diaktifkan oleh scope atau risk.

SOP ini menjawab **bagaimana operator menjalankan review dan mencatat hasilnya**. Aturan normatif tetap berada di `Operating_Model.md`, sedangkan control specification berada di `Control_Matrix.md`.

## 2. Scope

Berlaku ketika pekerjaan memerlukan salah satu atau kedua hal berikut:

- similarity/originality review;
- AI-assistance signal screening.

Tahap ini tidak menentukan plagiarism atau authorship secara otomatis dan tidak boleh digunakan sebagai alat untuk menghindari detection.

## 3. Inputs

- QC-ready document;
- approved review scope;
- applicable academic/institutional policy when relevant;
- available source material;
- review tool and documented capabilities/limitations;
- existing findings and resolution states.

## 4. Procedure

### Step 1 — Confirm Review Applicability

Tentukan apakah originality review dan/atau AI screening memang termasuk scope atau diperlukan berdasarkan risk.

Untuk AI screening, cek minimal:

- language support;
- document length/type requirements;
- tool capability;
- documented limitations;
- whether the result can be meaningfully interpreted for this task.

Jika tidak applicable, catat `NOT_APPLICABLE` dan jangan memaksakan screening.

### Step 2 — Capture Tool Metadata

Untuk setiap external detector/tool yang digunakan, catat bila tersedia:

```text
Tool
Model/version
Date/time
Input type/language
Relevant settings or exclusions
Known limitations
```

Jangan menyimpan detector result tanpa konteks tool dan applicability yang memadai.

### Step 3 — Run Similarity / Originality Review

Jika similarity review berlaku:

1. jalankan similarity detection;
2. identifikasi match yang relevan;
3. kumpulkan matched source;
4. klasifikasikan context.

Gunakan context seperti:

- quotation;
- proper paraphrase;
- bibliography/reference;
- common academic phrase;
- potential unattributed copying;
- close paraphrase.

### Step 4 — Interpret Similarity Context

Untuk setiap material match:

```text
Match
  ↓
Context
  ↓
Attribution
  ↓
Source inspection
  ↓
Human interpretation
```

Jangan menggunakan similarity percentage sebagai plagiarism verdict.

### Step 5 — Determine Originality Outcome

Gunakan outcome kontekstual:

- `NO_MATERIAL_CONCERN`;
- `REVIEW`;
- `MATERIAL_CONCERN`.

`MATERIAL_CONCERN` berarti ada evidence yang layak ditindaklanjuti, bukan otomatis menetapkan academic misconduct.

Jika evidence tidak cukup, pertahankan `REVIEW`.

### Step 6 — Run AI-Assistance Screening When Applicable

Jika AI screening applicable:

- proses teks melalui tool yang tersedia;
- catat signal/result;
- catat limitations;
- jangan mengubah result menjadi authorship verdict.

Gunakan state operasional:

- `NOT_APPLICABLE`;
- `NO_SIGNAL`;
- `SIGNAL_REVIEW`;
- `INCONCLUSIVE`;
- `ESCALATED`.

### Step 7 — Human Interpretation of AI Signal

Untuk signal yang relevan, review konteks dokumen dan evidence yang tersedia.

Pertimbangkan, bila memang tersedia dan sesuai scope:

- writing sample/history;
- revision history;
- author explanation;
- AI-use disclosure;
- source/citation context;
- applicable institutional policy.

AI signal adalah evidence pendukung, bukan proof of authorship, human authorship, plagiarism, atau misconduct.

### Step 8 — Maintain Resolution State

Setiap material finding harus memiliki resolution state sesuai `MC-08`.

Contoh:

```text
Potential unattributed copying → REVIEW
AI signal requiring clarification → WAITING_AUTHOR
Missing source for verification → WAITING_SOURCE
Confirmed and addressed issue → RESOLVED
```

Jangan mengubah status menjadi `RESOLVED` hanya karena detector run sudah selesai.

### Step 9 — Decide Remediation

Remediation harus mengatasi academic/process issue, bukan mengejar angka detector.

Examples:

- proper attribution/quotation/paraphrase review;
- source verification;
- author clarification;
- policy clarification;
- escalation.

Jangan melakukan:

- rewriting solely to lower similarity;
- rewriting solely to lower AI-detection score;
- detector gaming;
- automatic accusation from a score.

### Step 10 — Record Review Evidence

Record minimal:

```text
Review type
Tool/Source
Applicability
Observed result
Context interpretation
Evidence
Outcome
Resolution state
Reviewer
Date/time
```

## 5. Similarity Review Rules

### High percentage does not automatically mean plagiarism

Interpret the matches and attribution context before assigning a concern.

### Low percentage does not automatically mean originality is proven

A low score may coexist with a material copied passage or other issue outside the detector's coverage.

### Quotation and bibliography may be benign matches

Review context before action.

### Source inspection is required for material concerns

Do not issue a substantive finding solely from a similarity percentage.

## 6. AI-Signal Review Rules

### Signal

Treat detector output as a signal requiring interpretation.

### No signal

Do not conclude human authorship solely from the absence of a signal.

### Tool limitation

If language, length, file type, or other constraints make the result unreliable or unavailable, use `NOT_APPLICABLE` or `INCONCLUSIVE` as appropriate.

### Policy dependency

Final implications depend on applicable institutional/client policy. Do not invent a universal academic rule.

## 7. Quality Checks

Before handoff to Final QC:

- review applicability is documented;
- tool/source metadata is retained when available;
- similarity matches are interpreted in context;
- material sources are inspected;
- no score-only plagiarism verdict is issued;
- AI signal is not treated as proof of authorship/misconduct;
- limitations are recorded;
- material findings have resolution states;
- remediation does not target detector evasion.

## 8. Outputs

Produce, as applicable:

1. **Similarity / Originality Review Record**
2. **AI-Assistance Review Record**
3. **Source/Match Evidence**
4. **Findings and Resolution States**
5. **Escalation / Author Clarification Record**

## 9. Handoff

Handoff to `08 Final QC` requires:

```text
Applicable review results
+
Evidence / source records
+
Findings and resolution states
+
Escalation records when applicable
```

Material unresolved findings remain subject to the delivery gate defined by the Operating Model.

## 10. Control Traceability

| Control | SOP Step | Evidence |
|---|---|---|
| MC-08 Resolution State | Steps 8–10 | Finding/resolution record |
| MC-09 Evidence Sufficiency | Steps 2–10 | Tool metadata, source evidence, interpretation, verdict rationale |

Normative control definitions remain in:

`../01_Workflows/Operating_Model.md`

Control specification remains in:

`../01_Workflows/Control_Matrix.md`

## 11. Change Control

Changes to this SOP that alter review applicability, evidence requirements, interpretation boundaries, resolution behavior, or remediation rules must be reviewed against `Operating_Model.md` and `Control_Matrix.md` before approval.
