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
- acceptance evidence;
- failure/escalation;
- primary workflow stage;
- implementation references.

Jika terdapat konflik dengan Operating Model, Operating Model berlaku sampai ada perubahan yang disetujui melalui change control.

## 2. Control Matrix

| ID | Control | Objective | Applicability / Trigger | Owner | Required Input / Evidence | Control Action | Gate / Decision | Output / Evidence | Acceptance Evidence | Failure / Escalation | Primary Stage |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MC-01 | Client Requirement Capture | Memastikan scope dan requirement cukup jelas sebelum produksi. | Semua pekerjaan. | Production operator | Client request, files, scope, deadline, output requirements, available guidance. | Capture and normalize applicable requirements into Work Brief. | Minimum requirements available → proceed; otherwise `CLARIFICATION_REQUIRED`. | Work Brief + requirement/source inventory. | Applicable scope, deadline, output format, and key requirements are captured; missing critical inputs are recorded. | Missing critical requirements → `CLARIFICATION_REQUIRED`. | 01 Intake |
| MC-02 | Risk Classification | Menentukan kedalaman kontrol berdasarkan risk. | Semua pekerjaan setelah diagnosis awal. | Production operator / reviewer | Document condition, scope, sensitivity, substantive concerns, requirement complexity. | Classify `LOW` / `MEDIUM` / `HIGH`. | Risk assigned and sufficiently justified for authorization. | Risk assessment. | Risk level has documented rationale tied to identified conditions. | Unclear risk → additional diagnosis or escalation. | 02 Diagnose + Risk |
| MC-03 | Authorization / Integrity Gate | Mencegah pekerjaan yang tidak dapat diproduksi secara bertanggung jawab dalam scope yang disetujui. | Semua pekerjaan sebelum production. | Production lead / responsible operator | Work Brief, diagnosis, risk, scope boundaries. | Confirm scope, integrity boundaries, evidence availability, and required review depth. | `AUTHORIZED` / `CLARIFICATION_REQUIRED` / `ESCALATED` / `DECLINED`. | Authorization decision + approved scope. | Decision is recorded and approved scope/boundaries are explicit. | Integrity/scope issue → `ESCALATED` or `DECLINED`. | 03 Authorize |
| MC-04 | Institutional Guideline Gate | Mencegah false compliance dan false failure terhadap external requirements. | Saat client/instructor/institutional guideline menjadi requirement. | Production operator / academic reviewer | Official guideline source, applicability metadata, extracted requirements. | Validate source, extract requirements, assess applicability, and map requirements to document. | If source/applicability/evidence is insufficient → `UNVERIFIED` / `REVIEW`, not automatic `PASS`. | Guideline record + requirement matrix/compliance evidence. | Source is identified and applicable; each relevant requirement has an evidence-backed mapping; unresolved items are recorded. | Guideline inaccessible, ambiguous, or inapplicable → `REVIEW` / `UNVERIFIED`. | 01 Intake / 06 Academic QC |
| MC-05 | Edit Authority | Mengendalikan tingkat kewenangan intervensi editing. | Setiap intervention. | Editor/reviewer | Proposed change + context. | Classify intervention as `E1`, `E2`, or `E3` before/while applying it. | E1 direct; E2 contextual with meaning preservation; E3 human/author decision. | Classified change record where needed. | Intervention is classified consistently and E3 decisions are explicitly routed for human/author decision. | Misclassified E3 or silent substantive edit → escalate/review. | 04 Produce / 05 Review |
| MC-06 | Meaning Preservation | Mencegah perubahan substansi yang tidak disengaja. | Material editorial/academic changes. | Editor + reviewer | Original text, proposed edit, relevant context. | Compare original vs edited meaning; classify material change. | Use the normative states defined in `Operating_Model.md`; unresolved alteration → further review/block. | Semantic review evidence. | Material changes have documented comparison/result; no unresolved unauthorized semantic alteration remains at final QC. | `ALTERED` or unresolved `UNCERTAIN` → review/block. | 04 Produce / 05 Review |
| MC-07 | Substantive Change Escalation | Mencegah AI/editor mengambil keputusan akademik substantif secara diam-diam. | E3 changes or equivalent substantive issues. | Reviewer / responsible human | Finding affecting method, claim, evidence, interpretation, design, or conclusion. | Flag, explain, and route for human/author decision. | Decision must be recorded before substantive change is finalized. | Escalation record + decision. | Responsible decision-maker and decision are recorded; substantive change is attributable to an authorized decision. | No decision/authority → `WAITING_AUTHOR` or `ESCALATED`; no finalization. | 03 Authorize / 04 Produce / 05 Review |
| MC-08 | Resolution State | Menjaga traceability status finding sampai benar-benar selesai. | Semua findings/dependencies yang memerlukan resolution. | Assigned owner | Finding + evidence + decision dependency. | Maintain the normative resolution state defined in `Operating_Model.md`. | Only `RESOLVED` may satisfy completion; blocking states prevent appropriate progression. | Resolution record/status. | Every tracked finding has one current state, owner, and resolution evidence when `RESOLVED`. | `OPEN`, `WAITING_AUTHOR`, `WAITING_SOURCE`, or `ESCALATED` remain unresolved until properly cleared. | 05 Review / 07 Originality & AI Review / 08 Final QC |
| MC-09 | Evidence Sufficiency | Mencegah PASS/FAIL atau academic claim tanpa evidence yang cukup. | Compliance, factual, source, originality, or quality verdicts. | Reviewer / academic QC | Source, document evidence, applicable requirement, verification result. | Assess whether evidence is sufficient, applicable, and traceable for intended verdict. | Sufficient evidence → verdict; insufficient evidence → `REVIEW` / `UNVERIFIED`. | Evidence trail + verdict rationale. | Verdict can be traced to specific source/document evidence and applicability basis. | Insufficient evidence → `REVIEW` / `UNVERIFIED`; do not force `FAIL` or `PASS`. | 06 Academic QC / 07 Originality & AI Review / 08 Final QC |
| MC-10 | External Processing Gate | Mencegah unnecessary exposure of client/sensitive data to external AI/tools. | Any external AI/tool processing of client material. | Operator / data-handling owner | Data classification, task need, tool capability/privacy constraints, proposed payload. | Minimize/redact unnecessary sensitive data; inspect outbound payload; decide allow/escalate/block. | `ALLOW` / `ESCALATE` / `BLOCK`. | Processing decision + payload minimization evidence where required. | Data need is justified; unnecessary sensitive fields are removed/redacted; outbound payload is reviewed before processing. | Sensitive/unnecessary data remains or constraints are unresolved → `BLOCK` / `ESCALATE`. | 04 Produce |
| MC-11 | Fail-Closed Final QC | Mencegah delivery ketika required controls atau blocking issues belum selesai. | Semua pekerjaan sebelum delivery. | Final reviewer / production lead | Approved scope, QC results, resolution states, evidence. | Verify completion, required reviews, evidence, file integrity, and blocking findings. | Critical unresolved findings → `BLOCK`; delivery only after approval. | Final QC approval or blocked status. | Scope, required checks, evidence, file integrity, and resolution states are reviewed and approval is recorded. | Any blocking condition → `BLOCK`; return to resolution path. | 08 Final QC |

## 3. Control Reference Rules

Detailed normative definitions remain in `Operating_Model.md` v2.1. Use control IDs rather than duplicating those definitions downstream.

### Edit Authority

`MC-05` governs application of `E1`, `E2`, and `E3` as defined normatively by the Operating Model.

### Resolution State

`MC-08` verifies application of the normative resolution states defined by the Operating Model.

### Compliance Status

`MC-09` verifies that requirement mappings use the normative statuses defined by the Operating Model:

- `PASS`
- `FAIL`
- `N/A`
- `REVIEW`

Do not convert missing evidence directly into `FAIL` without applying MC-09.

### Originality / AI Review

`MC-09` governs evidence sufficiency for originality/AI findings. The normative interpretation boundaries and states are defined in `Operating_Model.md` v2.1.

### External Processing

`MC-10` verifies application of the External Processing Gate defined in `Operating_Model.md` v2.1.

## 4. Control-to-Workflow Mapping

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

## 5. Implementation Notes

The Control Matrix is the bridge specification between the Operating Model and execution documents.

- `Operating_Model.md` defines the normative rule.
- `Control_Matrix.md` specifies how the control is evidenced and exercised.
- `Master_Workflow.md` specifies where the control is exercised in the sequence.
- SOPs specify repeatable operator procedures.
- QC artifacts verify outcomes.

Avoid duplicating full control definitions across downstream documents. Downstream documents should reference the control ID whenever practical.

## 6. Change Control

Changes to control definitions, applicability, gates, or required evidence are material changes and must be reviewed against `Operating_Model.md` before approval.
