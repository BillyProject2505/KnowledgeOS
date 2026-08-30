# BAKU Edit Tugas — QC-02 Production & Human Review QC

**Status:** Approved  
**Version:** 2.1  
**Type:** QC Checklist  
**Authority:** Derived from `Operating_Model.md` v2.1, `Control_Matrix.md` v2.1, `SOP-03_Academic_Production_with_AI.md`, and `SOP-04_Human_Review_and_Edit_Boundary.md`  
**Primary Controls:** MC-05, MC-06, MC-07, MC-08

## 1. Purpose

Memverifikasi bahwa hasil production berbantuan AI tetap berada dalam approved scope, perubahan diklasifikasikan dengan benar, meaning preservation diperiksa, substantive changes dieskalasikan, dan semua findings memiliki resolution state yang jelas.

QC ini memverifikasi hasil SOP-03 dan SOP-04; QC tidak membuat aturan normatif baru.

## 2. Applicability

Wajib untuk pekerjaan yang telah melalui AI-assisted production atau human review.

Kedalaman pemeriksaan disesuaikan dengan risk dan scope pekerjaan.

## 3. Checklist

### A. Scope & Production Boundary

| Check | Result | Evidence / Note |
|---|---|---|
| Production stayed within approved scope | PASS / REVIEW | |
| No unauthorized scope expansion | PASS / REVIEW | |
| Required source/context was available or dependency recorded | PASS / REVIEW | |
| AI use was limited to approved task | PASS / REVIEW | |
| No prohibited fabrication or unsupported addition introduced | PASS / REVIEW | |

### B. Edit Authority

| Check | Result | Evidence / Note |
|---|---|---|
| Material interventions classified as E1/E2/E3 where applicable | PASS / REVIEW | |
| E1 changes are direct mechanical/editorial corrections | PASS / REVIEW | |
| E2 changes received contextual review | PASS / REVIEW | |
| E3 changes identified and routed for human/author decision | PASS / BLOCK | |
| No substantive academic change was silently finalized | PASS / BLOCK | |

### C. Meaning Preservation

| Check | Result | Evidence / Note |
|---|---|---|
| Original and edited meaning were compared for material changes | PASS / REVIEW | |
| Claims and author intent remain preserved where required | PASS / REVIEW | |
| Methodology/research design was not changed silently | PASS / BLOCK | |
| Evidence interpretation was not altered silently | PASS / BLOCK | |
| Claim strength was not inappropriately increased | PASS / REVIEW | |
| Material semantic status is resolved | PASS / BLOCK | |

### D. AI Output Quality

| Check | Result | Evidence / Note |
|---|---|---|
| Requested task was actually completed | PASS / REVIEW | |
| AI output does not contain fabricated facts | PASS / BLOCK | |
| AI output does not contain fabricated citations/references | PASS / BLOCK | |
| AI output does not invent methodology/results | PASS / BLOCK | |
| Terminology remains contextually appropriate | PASS / REVIEW | |
| No unnecessary stylistic inflation or over-editing remains | PASS / REVIEW | |

### E. Findings & Resolution

| Check | Result | Evidence / Note |
|---|---|---|
| Material findings are recorded | PASS / REVIEW | |
| Each tracked finding has a current resolution state | PASS / REVIEW | |
| `OPEN` items are visibly unresolved | PASS / REVIEW | |
| `WAITING_AUTHOR` items are retained until author decision | PASS / REVIEW | |
| `WAITING_SOURCE` items are retained until evidence is available | PASS / REVIEW | |
| `ESCALATED` items are retained until responsible decision is recorded | PASS / REVIEW | |
| No finding was marked resolved without adequate evidence/decision | PASS / BLOCK | |

## 4. Gate Decision

Choose one:

- `PASS`
- `REVIEW`
- `BLOCKED`

### Gate rule

`PASS` requires approved scope completion for this stage, no unresolved blocking issue, correct handling of material changes, and sufficient review evidence.

Use `REVIEW` when evidence is incomplete but the issue is not yet established as a blocking failure.

Use `BLOCKED` when an unauthorized substantive change, fabricated content, or other blocking condition is present.

## 5. Failure / Escalation Checks

Block or route to resolution when:

- an E3 change was finalized without appropriate decision;
- material meaning was altered or remains uncertain;
- fabricated facts, citations, methodology, or results are present;
- a substantive issue was silently rewritten;
- a tracked blocking finding has no valid resolution;
- production materially exceeded approved scope.

Do not resolve these conditions by editing the QC record alone.

## 6. Evidence Requirements

Attach or reference, as applicable:

- approved Work Brief/scope;
- production draft;
- original-vs-edited comparison for material changes;
- E1/E2/E3 classification evidence;
- escalation/decision record;
- findings and resolution states;
- relevant source/reference evidence.

## 7. QC Result

**Overall Result:** `PASS / REVIEW / BLOCKED`

**Reviewer:**  
**Date/Time:**  
**Work Item:**  
**Notes:**  

## 8. Control Traceability

| Control | Verification |
|---|---|
| MC-05 Edit Authority | Material interventions are classified and handled according to the approved authority boundary. |
| MC-06 Meaning Preservation | Material changes have semantic comparison evidence and no unresolved unauthorized alteration. |
| MC-07 Substantive Change Escalation | E3 issues have appropriate human/author routing and recorded decisions. |
| MC-08 Resolution State | Tracked findings retain current states and are not treated as resolved prematurely. |

Normative definitions remain in:

`../01_Workflows/Operating_Model.md`

Control specification remains in:

`../01_Workflows/Control_Matrix.md`

Procedures remain in:

`../02_SOP/SOP-03_Academic_Production_with_AI.md`  
`../02_SOP/SOP-04_Human_Review_and_Edit_Boundary.md`

## 9. Change Control

Changes to this QC that alter gate behavior, evidence requirements, edit authority, semantic review, escalation, or resolution handling must be reviewed against `Operating_Model.md` and `Control_Matrix.md` before approval.
