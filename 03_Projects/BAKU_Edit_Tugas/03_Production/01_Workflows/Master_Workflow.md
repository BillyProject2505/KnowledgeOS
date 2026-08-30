# BAKU Edit Tugas — Master Production Workflow

**Status:** Active
**Version:** 2.1
**Authority:** Derived from `Operating_Model.md` v2.1
**Purpose:** Menjadi workflow produksi operasional yang menurunkan lifecycle dan mandatory controls dari Operating Model BAKU Edit Tugas.

## 1. Production Principle

BAKU menyediakan bantuan akademik berbasis AI dengan human oversight.

> AI assists the work; human owns the academic responsibility.

AI tidak dianggap sebagai sumber kebenaran tunggal. Output AI harus diperlakukan sebagai draft atau assistance sampai diverifikasi.

## 2. End-to-End Workflow

```text
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

## 3. Stage Definitions

### 01 — Intake

**Objective:** Mengubah permintaan klien menjadi Work Brief yang dapat diproduksi.

Capture what is applicable:
- service type;
- document type;
- academic level;
- institution and program;
- scope;
- deadline;
- output format;
- client/instructor requirements;
- source/reference materials;
- applicable institutional guideline.

**Gate:** Minimum requirements tersedia sebelum diagnosis.

### 02 — Diagnose + Risk

**Objective:** Menentukan kondisi dokumen, scope intervensi, masalah, dependency, privacy/sensitivity concern, dan risk level.

Risk:
- `LOW`
- `MEDIUM`
- `HIGH`

Pisahkan language/format, editorial, dan substantive academic issues.

### 03 — Authorize

**Objective:** Menentukan apakah pekerjaan boleh diproduksi.

Outcomes:
- `AUTHORIZED`
- `CLARIFICATION_REQUIRED`
- `ESCALATED`
- `DECLINED`

Jangan menerima fabrication of evidence/data/sources, concealment of unattributed copying, atau detector gaming.

### 04 — Produce

**Objective:** Mengerjakan scope yang telah diotorisasi dengan human control.

AI dapat digunakan untuk language assistance, controlled rephrasing, coherence suggestions, structure suggestions, dan pattern checks.

#### Edit Authority

**E1 — Direct Edit**  
Mechanical/editorial corrections yang jelas.

**E2 — Editorial Judgment**  
Contextual editing dengan kewajiban mempertahankan makna.

**E3 — Academic Decision**  
Perubahan terhadap methodology, evidence, claims, interpretation, research design, atau conclusions. Harus di-review/diotorisasi manusia dan tidak boleh silent rewrite.

### 05 — Review

**Objective:** Memastikan hasil produksi sesuai Work Brief, scope, edit authority, dan meaning preservation.

Material changes diklasifikasikan:
- `PRESERVED`
- `ALTERED`
- `UNCERTAIN`

`ALTERED` atau unresolved `UNCERTAIN` membutuhkan review sebelum finalization.

### 06 — Academic QC

**Objective:** Menilai academic compliance dan supportability.

Jika guideline institusi/assignment berlaku:

```text
Guideline Source
    ↓
Requirement Extraction
    ↓
Applicability Assessment
    ↓
Document Mapping
    ↓
PASS / FAIL / N/A / REVIEW
```

Pisahkan:
- structural compliance;
- substantive academic quality;
- requirement applicability.

`FAIL` hanya jika evidence cukup untuk menetapkan non-compliance. Jika evidence tidak cukup, gunakan `REVIEW`.

### 07 — Originality / AI Review [Conditional]

Aktif hanya bila scope atau risk membutuhkan.

#### Similarity / Originality

```text
Similarity Detection
    ↓
Match Context Classification
    ↓
Source Inspection
    ↓
Human Interpretation
    ↓
Resolution
```

Similarity score bukan plagiarism verdict.

#### AI-Assistance Screening

AI screening adalah advisory signal, bukan proof of authorship atau misconduct.

Pastikan screening applicable berdasarkan capability tool, language, document length/type, dan documented limitations.

### 08 — Final QC

**Objective:** Memastikan pekerjaan siap delivery.

Verify:
- approved scope completed;
- applicable requirements addressed;
- required reviews/verifications completed;
- critical findings resolved;
- required evidence recorded;
- final version correct;
- file integrity;
- delivery package correct.

Unresolved states that materially remain:
- `OPEN`
- `WAITING_AUTHOR`
- `WAITING_SOURCE`
- `ESCALATED`

harus memblokir final approval sesuai risk/scope; critical unresolved findings selalu block delivery.

### 09 — Delivery

Delivery hanya setelah Final QC approval.

### 10 — Archive

Simpan minimum operational evidence untuk traceability. Jangan gunakan repository sebagai default client-file storage.

## 4. Mandatory Controls

Workflow ini mengoperasikan mandatory controls yang didefinisikan pada `Operating_Model.md` v2.1:

- MC-01 Client Requirement Capture
- MC-02 Risk Classification
- MC-03 Authorization / Integrity Gate
- MC-04 Institutional Guideline Gate [conditional]
- MC-05 Edit Authority
- MC-06 Meaning Preservation
- MC-07 Substantive Change Escalation
- MC-08 Resolution State
- MC-09 Evidence Sufficiency
- MC-10 External Processing Gate
- MC-11 Fail-Closed Final QC

## 5. Completion Rule

Pekerjaan tidak dianggap selesai hanya karena AI menghasilkan output atau file telah dibuat.

Definition of Done mengikuti `Operating_Model.md` v2.1.

## 6. Authority & Change Control

`Operating_Model.md` adalah source of truth arsitektural. SOP, AI workflow, QC, dan templates harus diturunkan dari model tersebut dan tidak boleh diam-diam menyimpang.

Setiap perubahan material pada workflow harus mengikuti change control project.
