# BAKU Edit Tugas — Control Matrix

**Status:** Approved
**Version:** 2.1
**Authority:** Derived from `Operating_Model.md` v2.1
**Purpose:** Menjadi specification layer untuk menerjemahkan mandatory controls pada Operating Model menjadi kontrol yang dapat dijalankan, diverifikasi, dan dipetakan ke workflow/SOP/QC.

## 1. Scope

Control Matrix ini tidak membuat normative rule baru. `Operating_Model.md` v2.1 tetap menjadi normative architectural source of truth.

Matrix ini menjelaskan untuk setiap mandatory control:

- objective;
- applicability/trigger;
- owner;
- required input/evidence;
- control action;
- gate/decision;
- output/evidence;
- resolution expectation;
- primary workflow stage;
- implementation references.

Jika terdapat konflik dengan Operating Model, Operating Model berlaku sampai ada perubahan yang disetujui melalui change control.

## 2. Control Matrix

| ID | Control | Objective | Applicability / Trigger | Owner | Required Input / Evidence | Control Action | Gate / Decision | Output / Evidence | Primary Stage |
|---|---|---|---|---|---|---|---|---|---|
| MC-01 | Client Requirement Capture | Memastikan scope dan requirement cukup jelas sebelum produksi. | Semua pekerjaan. | Production operator | Client request, files, scope, deadline, output requirements, available guidance. | Capture and normalize applicable requirements into Work Brief. | Minimum requirements available → proceed; otherwise `CLARIFICATION_REQUIRED`. | Work Brief + requirement/source inventory. | 01 Intake |
| MC-02 | Risk Classification | Menentukan kedalaman kontrol berdasarkan risk. | Semua pekerjaan setelah diagnosis awal. | Production operator / reviewer | Document condition, scope, sensitivity, substantive concerns, requirement complexity. | Classify `LOW` / `MEDIUM` / `HIGH`. | Risk assigned and justified enough for authorization. | Risk assessment. | 02 Diagnose + Risk |
| MC-03 | Authorization / Integrity Gate | Mencegah pekerjaan yang tidak dapat diproduksi secara sah/bertanggung jawab. | Semua pekerjaan sebelum production. | Production lead / responsible operator | Work Brief, diagnosis, risk, scope boundaries. | Confirm scope, integrity boundaries, evidence availability, and required review depth. | `AUTHORIZED` / `CLARIFICATION_REQUIRED` / `ESCALATED` / `DECLINED`. | Authorization decision + approved scope. | 03 Authorize |
| MC-04 | Institutional Guideline Gate | Mencegah false compliance dan false failure terhadap external requirements. | Saat client/instructor/institutional guideline menjadi requirement. | Production operator / academic reviewer | Official guideline source, applicability metadata, extracted requirements. | Validate source, extract requirements, assess applicability, and map requirements to document. | If source/applicability/evidence is insufficient → `UNVERIFIED` / `REVIEW`, not automatic `PASS`. | Guideline record + requirement matrix/compliance evidence. | 01 Intake / 06 Academic QC |
| MC-05 | Edit Authority | Mengendalikan tingkat kewenangan intervensi editing. | Setiap intervention. | Editor/reviewer | Proposed change + context. | Classify intervention as `E1`, `E2`, or `E3` before/while applying it. | E1 direct; E2 contextual with meaning preservation; E3 human/author decision. | Classified change record where needed. | 04 Produce / 05 Review |
| MC-06 | Meaning Preservation | Mencegah perubahan substansi yang tidak disengaja. | Material editorial/academic changes. | Editor + reviewer | Original text, proposed edit, relevant context. | Compare original vs edited meaning; classify `PRESERVED` / `ALTERED` / `UNCERTAIN`. | `ALTERED` or unresolved `UNCERTAIN` → further review/block. | Semantic review evidence. | 04 Produce / 05 Review |
| MC-07 | Substantive Change Escalation | Mencegah AI/editor mengambil keputusan akademik substantif secara diam-diam. | E3 changes or equivalent substantive issues. | Reviewer / responsible human | Finding affecting method, claim, evidence, interpretation, design, or conclusion. | Flag, explain, and route for human/author decision. | Decision recorded before substantive change is finalized. | Escalation record + decision. | 03 Authorize / 04 Produce / 05 Review |
| MC-08 | Resolution State | Menjaga traceability status finding sampai benar-benar selesai. | Semua findings/dependencies yang memerlukan resolution. | Assigned owner | Finding + evidence + decision dependency. | Maintain one of `RESOLVED`, `OPEN`, `WAITING_AUTHOR`, `WAITING_SOURCE`, `ESCALATED`. | Only `RESOLVED` may satisfy completion; blocking states prevent appropriate progression. | Resolution record/status. | 05 Review / 07 Originality & AI Review / 08 Final QC |
| MC-09 | Evidence Sufficiency | Mencegah PASS/FAIL atau academic claim tanpa evidence yang cukup. | Compliance, factual, source, originality, or quality verdicts. | Reviewer / academic QC | Source, document evidence, applicable requirement, verification result. | Assess whether evidence is sufficient, applicable, and traceable for the intended verdict. | Sufficient evidence → verdict; insufficient evidence → `REVIEW` / `UNVERIFIED`. | Evidence trail + verdict rationale. | 06 Academic QC / 07 Originality & AI Review / 08 Final QC |
| MC-10 | External Processing Gate | Mencegah unnecessary exposure of client/sensitive data to external AI/tools. | Any external AI/tool processing of client material. | Operator / data-handling owner | Data classification, task need, tool capability/privacy constraints, proposed payload. | Minimize/redact unnecessary sensitive data; inspect outbound payload; decide allow/escalate/block. | `ALLOW` / `ESCALATE` / `BLOCK`. | Processing decision + payload minimization evidence where required. | 04 Produce |
| MC-11 | Fail-Closed Final QC | Mencegah delivery ketika required controls atau blocking issues belum selesai. | Semua pekerjaan sebelum delivery. | Final reviewer / production lead | Approved scope, QC results, resolution states, evidence. | Verify completion, required reviews, evidence, file integrity, and blocking findings. | Critical unresolved findings → `BLOCK`; delivery only after approval. | Final QC approval or blocked status. | 08 Final QC |

## 3. Edit Authority

| Authority | Meaning | Typical Examples | Default Action |
|---|---|---|---|
| **E1** | Clear mechanical/editorial correction | typo, spelling, punctuation, obvious grammar, obvious redundancy | Direct edit |
| **E2** | Contextual editorial judgment with meaning preservation | coherence, terminology, paragraph structure, controlled restructuring | Edit + review |
| **E3** | Substantive academic decision | methodology, research design, claim strength, evidence interpretation, conclusion | Escalate / human-author decision |

## 4. Resolution States

| State | Meaning | Can Count as Done? |
|---|---|---|
| `RESOLVED` | Finding/dependency has an accepted and evidenced resolution. | Yes, subject to all other gates. |
| `OPEN` | Issue identified but no accepted resolution yet. | No. |
| `WAITING_AUTHOR` | Requires information, clarification, or decision from author/client. | No. |
| `WAITING_SOURCE` | Requires a source, verification, or external evidence before decision. | No. |
| `ESCALATED` | Routed to responsible human decision-maker. | No until resolved. |

## 5. Compliance Status

Use only these statuses for requirement mapping:

- `PASS` — requirement is clearly met and evidence is sufficient.
- `FAIL` — requirement is clearly not met and evidence is sufficient to establish non-compliance.
- `N/A` — requirement is not applicable to the actual document/research design.
- `REVIEW` — evidence, applicability, or requirement interpretation is insufficient.

Do not convert missing evidence directly into `FAIL` without applying MC-09 Evidence Sufficiency.

## 6. Originality / AI Review States

### Similarity / Originality

Similarity evidence must be interpreted in context:

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

Use contextual outcomes such as:

- `NO_MATERIAL_CONCERN`
- `REVIEW`
- `MATERIAL_CONCERN`

Similarity percentage alone is not a plagiarism verdict.

### AI-Assistance Screening

AI detection is an advisory signal only and must first pass applicability checks such as tool capability, language, document length/type, and documented limitations.

Use:

- `NOT_APPLICABLE`
- `NO_SIGNAL`
- `SIGNAL_REVIEW`
- `INCONCLUSIVE`
- `ESCALATED`

AI signal is not proof of authorship, human authorship, plagiarism, or misconduct.

## 7. External Processing Decision

For client material processed through external AI/tools:

```text
Data Classification
    ↓
Need-to-Process Check
    ↓
Minimize / Redact
    ↓
Outbound Payload Review
    ↓
ALLOW / ESCALATE / BLOCK
```

Repository is not the default location for client documents or sensitive personal data.

## 8. Control-to-Workflow Mapping

| Workflow Stage | Primary Controls |
|---|---|
| 01 Intake | MC-01, MC-04 |
| 02 Diagnose + Risk | MC-02 |
| 03 Authorize | MC-03, MC-07 |
| 04 Produce | MC-05, MC-06, MC-07, MC-10 |
| 05 Review | MC-05, MC-06, MC-07, MC-08 |
| 06 Academic QC | MC-04, MC-09 |
| 07 Originality / AI Review | MC-08, MC-09 |
| 08 Final QC | MC-08, MC-09, MC-11 |
| 09 Delivery | MC-11 |
| 10 Archive | Traceability/evidence retention derived from approved workflow and governance |

## 9. Implementation Notes

The Control Matrix is the bridge specification between the Operating Model and execution documents.

- `Operating_Model.md` defines the normative rule.
- `Control_Matrix.md` specifies how the control is evidenced and exercised.
- `Master_Workflow.md` specifies where the control is exercised in the sequence.
- SOPs specify repeatable operator procedures.
- QC artifacts verify outcomes.

Avoid duplicating the full control definitions across downstream documents. Downstream documents should reference the control ID whenever practical.

## 10. Change Control

Changes to control definitions, applicability, gates, or required evidence are material changes and must be reviewed against `Operating_Model.md` before approval.
