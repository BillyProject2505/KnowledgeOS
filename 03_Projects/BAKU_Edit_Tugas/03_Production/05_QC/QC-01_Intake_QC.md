# BAKU Edit Tugas — QC-01 Intake & Pre-Production Gate Verification

**Status:** Approved  
**Version:** 2.1  
**Type:** Quality Control / Verification  
**Authority:** Verifies `SOP-01` and `SOP-02` outputs against `Operating_Model.md` v2.1 and `Control_Matrix.md` v2.1  
**Primary Controls:** MC-01, MC-02, MC-03, MC-04

## 1. Purpose

QC-01 memverifikasi bahwa hasil intake, diagnosis/risk assessment, dan authorization record telah memenuhi gate sebelum pekerjaan masuk ke `04 Produce`.

QC-01 adalah **verification layer**, bukan sumber normative rule.

- `Operating_Model.md` menetapkan aturan normatif.
- `Control_Matrix.md` menetapkan control specification.
- `SOP-01` menjalankan intake.
- `SOP-02` menjalankan risk assessment dan authorization.
- `QC-01` memverifikasi output kedua SOP tersebut sebelum production.

## 2. Scope

QC-01 berlaku untuk seluruh work item sebelum production dimulai.

Coverage dibagi menjadi dua checkpoint:

1. **Intake Verification** — memverifikasi output `SOP-01` untuk MC-01/MC-04.
2. **Pre-Production Gate Verification** — memverifikasi output `SOP-02` untuk MC-02/MC-03.

QC-01 tidak mengulang diagnosis atau membuat keputusan authorization baru. QC-01 hanya memverifikasi bahwa keputusan yang dibuat melalui SOP-02 memiliki evidence minimum, outcome yang valid, dan tidak melanggar gate yang berlaku.

## 3. Inputs

- Work Brief;
- Requirement Source Inventory;
- Guideline Record when applicable;
- Applicable Requirement List/Matrix when applicable;
- Risk Assessment;
- Risk Rationale;
- Approved Scope;
- Required Review Depth;
- Open Dependencies / Resolution States;
- Authorization Decision.

## 4. Checkpoint A — Intake Verification

### MC-01 Client Requirement Capture

[ ] Service type captured.

[ ] Document type captured.

[ ] Scope is explicit enough for diagnosis.

[ ] Deadline is captured.

[ ] Output format is captured when needed.

[ ] Critical files/materials are present or explicitly recorded as missing.

[ ] Client/instructor/institution requirements are recorded when provided.

[ ] Open questions and dependencies are visible.

### MC-04 Institutional Guideline Gate

[ ] Guideline applicability has been determined when relevant.

[ ] Official/authoritative source is identified when compliance is required.

[ ] Source accessibility/readability is recorded.

[ ] Requirement extraction is traceable when MC-04 is active.

[ ] Unverified or ambiguous requirements are not represented as verified compliance.

### Intake Decision

Use only the applicable outcome:

- `READY_FOR_DIAGNOSIS`
- `CLARIFICATION_REQUIRED`
- `REVIEW / UNVERIFIED`

Do not treat missing information as resolved by assumption.

## 5. Checkpoint B — Pre-Production Gate Verification

This checkpoint closes the verification gap identified for `MC-02` and `MC-03`.

### MC-02 Risk Classification

[ ] Risk level is present: `LOW`, `MEDIUM`, or `HIGH`.

[ ] Risk rationale is specific enough to explain the assigned level.

[ ] Risk rationale is tied to actual work conditions, scope, sensitivity, evidence requirements, or substantive concerns.

[ ] Required review depth is identified where relevant.

### MC-03 Authorization / Integrity Gate

[ ] Approved scope is explicit.

[ ] Integrity boundaries were checked.

[ ] Required evidence/source dependencies are visible.

[ ] Open dependencies are recorded with appropriate resolution state.

[ ] Authorization outcome is one of:

- `AUTHORIZED`
- `CLARIFICATION_REQUIRED`
- `ESCALATED`
- `DECLINED`

[ ] Production is permitted only when authorization outcome is `AUTHORIZED`.

[ ] No prohibited request has been silently accepted.

[ ] Any substantive decision dependency remains visible and attributable to the appropriate decision owner.

### Pre-Production Gate Decision

The verification result is:

- `PASS` — MC-02/MC-03 evidence is present, coherent, and authorization outcome is `AUTHORIZED`;
- `REVIEW` — evidence or applicability is insufficient and requires clarification/review;
- `BLOCKED` — authorization is not `AUTHORIZED`, a blocking dependency remains, or integrity boundary is not satisfied.

**Production must not begin unless Pre-Production Gate Verification = `PASS`.**

## 6. Non-Overlap Boundary

QC-01 does **not**:

- assign the risk level instead of SOP-02;
- make the authorization decision instead of SOP-02;
- redefine MC-02 or MC-03;
- perform production work;
- perform detailed production/human-review checks covered by QC-02.

Its sole role is to verify that the required pre-production decision and evidence exist and satisfy the applicable gate.

## 7. Handoff to Production

Successful handoff to `04 Produce` requires:

```text
Intake Verification = PASS
+
Pre-Production Gate Verification = PASS
+
Authorization Decision = AUTHORIZED
```

If any checkpoint is `REVIEW` or `BLOCKED`, do not start normal production.

Route to the applicable clarification, escalation, or correction path.

## 8. QC Record

Record at minimum:

- work item;
- reviewer;
- intake verification result;
- pre-production verification result;
- risk level and rationale checked;
- authorization outcome checked;
- blocking/review findings;
- evidence references;
- date/time.

Do not store unnecessary personal or sensitive client data in the QC record.

## 9. Control Traceability

| Control | Verified Output | Evidence |
|---|---|---|
| MC-01 | `SOP-01` Work Brief / requirement capture | Work Brief + requirement/source inventory |
| MC-02 | `SOP-02` Risk Assessment | Risk level + rationale |
| MC-03 | `SOP-02` Authorization Decision | Approved scope + authorization outcome + dependencies |
| MC-04 | `SOP-01` guideline gate outputs | Guideline/source record + requirement mapping when applicable |

Normative definitions remain in:

`../01_Workflows/Operating_Model.md`

Control specification remains in:

`../01_Workflows/Control_Matrix.md`

## 10. Relationship to QC-02

`QC-01` verifies the **pre-production gate**.

`QC-02` verifies **production and human review execution**.

QC-02 does not replace the pre-production verification performed here, and QC-01 does not perform post-production review.

## 11. Change Control

Changes to this QC that alter pre-production gate criteria, control applicability, approval conditions, or required evidence must be reviewed against `Operating_Model.md` and `Control_Matrix.md` before approval.
