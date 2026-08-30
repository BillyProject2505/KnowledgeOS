# BAKU Edit Tugas — QC-05 Final QC

**Status:** Approved  
**Version:** 2.1  
**Type:** QC Checklist  
**Authority:** Derived from `Operating_Model.md` v2.1, `Control_Matrix.md` v2.1, and `SOP-07_Final_QC_Delivery_and_Archive.md`  
**Primary Controls:** MC-08, MC-10, MC-11

## 1. Purpose

Memverifikasi bahwa pekerjaan telah memenuhi approved scope, required reviews, evidence requirements, resolution requirements, file integrity, dan delivery gate sebelum diserahkan kepada klien.

QC ini memverifikasi hasil SOP-07; QC tidak membuat requirement atau policy baru.

## 2. Applicability

Wajib untuk semua pekerjaan yang akan masuk delivery.

Kedalaman pemeriksaan disesuaikan dengan approved scope dan risk level.

## 3. Checklist

### A. Scope & Requirements

| Check | Result | Evidence / Note |
|---|---|---|
| Approved scope is complete | PASS / REVIEW | |
| Applicable requirements are addressed | PASS / REVIEW | |
| Any accepted limitation/dependency is explicitly recorded | PASS / N/A / REVIEW | |
| Final output matches the approved service scope | PASS / REVIEW | |

### B. Required Reviews & Verification

| Check | Result | Evidence / Note |
|---|---|---|
| Required human review completed | PASS / REVIEW | |
| Required academic/compliance review completed | PASS / N/A / REVIEW | |
| Required source/citation verification completed | PASS / N/A / REVIEW | |
| Required originality review completed | PASS / N/A / REVIEW | |
| Required AI-signal review completed | PASS / N/A / REVIEW | |
| Required formatting review completed | PASS / REVIEW | |
| Any skipped stage has documented non-applicability where required | PASS / REVIEW | |

### C. Findings & Resolution State

| Check | Result | Evidence / Note |
|---|---|---|
| All tracked material findings are identified | PASS / REVIEW | |
| Each tracked finding has a current resolution state | PASS / REVIEW | |
| No `OPEN` finding is presented as resolved | PASS / BLOCK | |
| No `WAITING_AUTHOR` finding is presented as resolved | PASS / BLOCK | |
| No `WAITING_SOURCE` finding is presented as resolved | PASS / BLOCK | |
| No `ESCALATED` finding is presented as resolved without recorded decision | PASS / BLOCK | |
| All blocking findings are cleared before delivery approval | PASS / BLOCK | |

### D. Evidence Completeness

| Check | Result | Evidence / Note |
|---|---|---|
| Required evidence is present | PASS / REVIEW | |
| Evidence is traceable to the work item | PASS / REVIEW | |
| Material decisions have supporting records where required | PASS / REVIEW | |
| No evidence was fabricated or backfilled without basis | PASS / BLOCK | |
| Final QC rationale is recorded | PASS / REVIEW | |

### E. External Processing & Data Boundary

Complete when external AI/tool processing occurred or relevant data controls apply.

| Check | Result | Evidence / Note |
|---|---|---|
| External processing decision was completed where applicable | PASS / N/A / REVIEW | |
| Required sensitive-data minimization/redaction was performed | PASS / N/A / REVIEW | |
| Outbound payload was reviewed before external processing when required | PASS / N/A / REVIEW | |
| Repository was not used as default storage for client-sensitive data | PASS / N/A / REVIEW | |
| Any processing constraint/deviation is recorded | PASS / N/A / REVIEW | |

### F. File & Delivery Integrity

| Check | Result | Evidence / Note |
|---|---|---|
| Correct final filename/version | PASS / BLOCK | |
| Correct file type | PASS / BLOCK | |
| File opens correctly | PASS / BLOCK | |
| Required pages/sections are present | PASS / REVIEW | |
| Track changes/comments handled according to scope | PASS / N/A / REVIEW | |
| No unintended placeholders or working artifacts remain | PASS / BLOCK | |
| Delivery package contains intended files only | PASS / BLOCK | |

## 4. Final Gate Decision

Choose one:

- `APPROVED_FOR_DELIVERY`
- `REVIEW_REQUIRED`
- `BLOCKED`

### Gate rule

`APPROVED_FOR_DELIVERY` requires:

```text
Approved scope complete
+
Required reviews complete
+
Material findings appropriately resolved
+
Required evidence recorded
+
External-processing controls satisfied when applicable
+
Final file verified
+
No blocking condition remains
```

A single blocking condition prevents delivery.

## 5. Failure / Escalation Checks

Use `BLOCKED` or route to the appropriate resolution path when:

- critical unresolved finding remains;
- a material finding is still `OPEN` / `WAITING_AUTHOR` / `WAITING_SOURCE` / `ESCALATED` without resolution;
- required evidence is missing and a reliable completion decision cannot be made;
- unauthorized substantive changes remain unresolved;
- sensitive data handling requirements were not satisfied;
- final file integrity is not assured.

Do not bypass a block by changing a label without resolving the underlying condition.

## 6. Evidence Requirements

Attach or reference, as applicable:

- Work Brief / approved scope;
- required review/QC results;
- compliance/source evidence;
- originality/AI review records;
- findings and resolution records;
- external processing decision;
- final file/version check;
- final QC decision.

## 7. QC Result

**Overall Result:** `APPROVED_FOR_DELIVERY / REVIEW_REQUIRED / BLOCKED`  
**Reviewer:**  
**Date/Time:**  
**Work Item:**  
**Notes:**  

## 8. Delivery Verification

Before handing over the file, confirm:

- final package is the version that passed QC;
- only approved files are included;
- any limitation/dependency note is accurate;
- delivery record will identify the approved output.

## 9. Closure Verification

After successful delivery:

- delivery record is captured;
- required operational evidence is archived in the appropriate workspace;
- work item can be closed only after delivery completion.

A blocked item returns to the resolution path and is not closed as complete.

## 10. Control Traceability

| Control | Verification |
|---|---|
| MC-08 Resolution State | All tracked findings are reviewed and blocking states prevent approval. |
| MC-10 External Processing Gate | External-processing decisions and data-handling controls are verified when applicable. |
| MC-11 Fail-Closed Final QC | Final approval, file integrity, blocking conditions, and delivery authorization are verified. |

Normative definitions remain in:

`../01_Workflows/Operating_Model.md`

Control specification remains in:

`../01_Workflows/Control_Matrix.md`

Procedure remains in:

`../02_SOP/SOP-07_Final_QC_Delivery_and_Archive.md`

## 11. Change Control

Changes to this QC that alter final approval, blocking behavior, evidence requirements, external-processing verification, or closure conditions must be reviewed against `Operating_Model.md` and `Control_Matrix.md` before approval.
