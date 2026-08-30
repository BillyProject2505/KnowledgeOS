# BAKU Edit Tugas — QC-04 Originality & AI Review QC

**Status:** Approved  
**Version:** 2.1  
**Type:** QC Checklist  
**Authority:** Derived from `Operating_Model.md` v2.1, `Control_Matrix.md` v2.1, and `SOP-06_Originality_and_AI_Signal_Review.md`  
**Primary Controls:** MC-08, MC-09

## 1. Purpose

Memverifikasi bahwa similarity/originality review dan AI-assistance signal review hanya dilakukan ketika applicable, diinterpretasikan berdasarkan konteks dan evidence, serta tidak menghasilkan plagiarism/authorship verdict yang tidak didukung.

QC ini memverifikasi hasil SOP-06; QC tidak membuat policy atau threshold baru.

## 2. Applicability

Wajib ketika originality/similarity review dan/atau AI-assistance screening termasuk scope atau diwajibkan oleh risk/requirements.

## 3. Checklist

### A. Applicability & Tool/Source Metadata

| Check | Result | Evidence / Note |
|---|---|---|
| Review type is within approved scope | PASS / REVIEW | |
| Tool/source applicability was assessed | PASS / REVIEW | |
| Language applicability checked when relevant | PASS / N/A / REVIEW | |
| Document length/type requirements checked when relevant | PASS / N/A / REVIEW | |
| Tool/source and version/date recorded when available | PASS / N/A / REVIEW | |
| Known limitations recorded | PASS / N/A / REVIEW | |

### B. Similarity / Originality Review

| Check | Result | Evidence / Note |
|---|---|---|
| Similarity result is recorded without treating percentage as verdict | PASS / BLOCK | |
| Material matches were identified for contextual review | PASS / REVIEW | |
| Match context was classified | PASS / REVIEW | |
| Quotation matches were considered in context | PASS / N/A / REVIEW | |
| Bibliography/reference matches were considered in context | PASS / N/A / REVIEW | |
| Common academic phrases were not automatically treated as misconduct | PASS / N/A / REVIEW | |
| Material matches have relevant source inspection | PASS / N/A / REVIEW | |
| Unattributed copying concern has evidence beyond score alone | PASS / N/A / REVIEW | |
| Low similarity was not presented as proof of originality | PASS / BLOCK | |
| High similarity was not presented as automatic proof of plagiarism | PASS / BLOCK | |

### C. AI-Assistance Screening

| Check | Result | Evidence / Note |
|---|---|---|
| AI screening applicability was established before use | PASS / REVIEW | |
| Detector output/signal is recorded with available metadata | PASS / REVIEW | |
| Signal is treated as advisory evidence | PASS / BLOCK | |
| No-signal result is not presented as proof of human authorship | PASS / BLOCK | |
| Signal is not presented as proof of plagiarism/misconduct | PASS / BLOCK | |
| Linguistic/contextual observations are separated from provenance claims | PASS / REVIEW | |
| Tool limitations are reflected in interpretation | PASS / REVIEW | |
| Hybrid/AI-assisted text is not forced into an all-or-nothing authorship label | PASS / REVIEW | |

### D. Evidence Sufficiency & Resolution

| Check | Result | Evidence / Note |
|---|---|---|
| Material findings have supporting evidence | PASS / REVIEW | |
| Verdict rationale is traceable to source/document evidence | PASS / REVIEW | |
| `REVIEW` used when evidence is insufficient | PASS / REVIEW | |
| Findings have current resolution states | PASS / REVIEW | |
| `OPEN` / `WAITING_AUTHOR` / `WAITING_SOURCE` / `ESCALATED` are not treated as resolved | PASS / BLOCK | |
| Final disposition is consistent with available evidence and applicable policy | PASS / REVIEW | |

### E. Remediation Integrity

| Check | Result | Evidence / Note |
|---|---|---|
| Remediation addresses academic/process issue rather than detector score | PASS / BLOCK | |
| No rewriting solely to reduce similarity score | PASS / BLOCK | |
| No rewriting solely to reduce AI-detection score | PASS / BLOCK | |
| No detector gaming or evasion instruction was used | PASS / BLOCK | |
| Author clarification/escalation used where appropriate | PASS / N/A / REVIEW | |

## 4. Gate Decision

Choose one:

- `PASS`
- `REVIEW`
- `BLOCKED`

### Gate rule

`PASS` requires applicable review steps to be completed, evidence to be sufficient for the recorded interpretation, material findings to have valid resolution states, and no prohibited score-only verdict or detector-gaming remediation.

Use `REVIEW` when evidence or applicability is incomplete but a blocking failure is not established.

Use `BLOCKED` when a score-only plagiarism/authorship verdict, unsupported misconduct claim, or detector-evasion remediation has occurred, or when another material unresolved control failure prevents reliable completion.

## 5. Failure / Escalation Checks

Block or route to resolution when:

- similarity percentage is used as the sole plagiarism verdict;
- AI detector output is used as proof of authorship or misconduct;
- a no-signal result is treated as proof of human authorship;
- material match context was not inspected;
- evidence is insufficient for the recorded verdict;
- a substantive finding has no valid resolution;
- remediation is aimed at evading a detector rather than addressing the academic issue.

Do not clear these conditions by changing the label alone; require corrected review/evidence.

## 6. Evidence Requirements

Attach or reference, as applicable:

- approved review scope;
- tool/source metadata;
- similarity/originality report or result;
- matched-source evidence;
- match-context assessment;
- AI-assistance signal output;
- applicability/limitations record;
- interpretation/reviewer notes;
- findings and resolution states;
- author clarification or escalation record when applicable.

## 7. QC Result

**Overall Result:** `PASS / REVIEW / BLOCKED`  
**Reviewer:**  
**Date/Time:**  
**Work Item:**  
**Notes:**  

## 8. Control Traceability

| Control | Verification |
|---|---|
| MC-08 Resolution State | Findings remain in valid states until properly resolved. |
| MC-09 Evidence Sufficiency | Similarity/AI interpretations and material findings are supported by traceable evidence and applicability. |

Normative definitions remain in:

`../01_Workflows/Operating_Model.md`

Control specification remains in:

`../01_Workflows/Control_Matrix.md`

Procedure remains in:

`../02_SOP/SOP-06_Originality_and_AI_Signal_Review.md`

## 9. Change Control

Changes to this QC that alter review applicability, evidence requirements, verdict behavior, or remediation boundaries must be reviewed against `Operating_Model.md` and `Control_Matrix.md` before approval.
