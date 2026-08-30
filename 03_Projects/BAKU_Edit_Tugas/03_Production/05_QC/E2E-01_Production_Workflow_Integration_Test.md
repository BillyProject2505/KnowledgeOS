# BAKU Edit Tugas — E2E-01 Production Workflow Integration Test

**Status:** Approved
**Version:** 2.1
**Type:** End-to-End Integration Test Artifact
**Authority:** Derived from `Operating_Model.md` v2.1, `Control_Matrix.md` v2.1, `Master_Workflow.md` v2.1, SOP layer, and QC layer

## 1. Purpose

Menguji apakah production system BAKU dapat menjalankan satu work item dari intake sampai archive dengan traceability antar-stage, control, evidence, gate, dan handoff yang konsisten.

Artifact ini menguji integrasi sistem. Ia tidak membuat normative rule baru.

## 2. Test Principle

A work item must not advance merely because an output file exists. Each stage must produce the evidence and decision state required by the next stage, and blocking conditions must remain blocking.

## 3. Test Fixture

Use a synthetic academic editing request:

```text
Service: Academic Editing + Compliance Review
Document: Undergraduate thesis Chapter III
Institution/Program: Example institution/program
Scope: language editing, coherence improvement, formatting, guideline compliance review
Deadline: synthetic
External review: similarity and AI-signal review required
Data condition: synthetic student/participant identifiers included to test data handling
```

No real client data is required.

## 4. Positive Path

### Stage 01 — Intake

Expected:

- Work Brief created;
- requirements/source inventory created;
- applicable guideline identified when in scope;
- intake gate = `READY_FOR_DIAGNOSIS`.

Controls: `MC-01`, `MC-04`.

### Stage 02 — Diagnose + Risk

Expected:

- document condition diagnosed;
- privacy/sensitivity identified;
- academic/source concerns identified;
- risk level assigned with rationale.

Control: `MC-02`.

### Stage 03 — Authorize

Expected:

- scope and boundaries confirmed;
- integrity boundaries checked;
- authorization decision = `AUTHORIZED`;
- required review depth recorded.

Control: `MC-03`.

### Stage 04 — Produce

Expected:

- approved scope executed;
- interventions classified as applicable E1/E2/E3;
- external-processing gate applied before sensitive processing;
- material changes surfaced.

Controls: `MC-05`, `MC-06`, `MC-07`, `MC-10`.

### Stage 05 — Review

Expected:

- original vs edited output reviewed;
- meaning preservation checked for material changes;
- E3 items escalated;
- findings have current resolution states;
- review outcome recorded.

Controls: `MC-05`, `MC-06`, `MC-07`, `MC-08`.

### Stage 06 — Academic QC

Expected:

- applicable guideline requirements mapped;
- source/citation checks completed when in scope;
- compliance statuses use `PASS / FAIL / N/A / REVIEW`;
- evidence sufficiency assessed.

Controls: `MC-04`, `MC-09`.

### Stage 07 — Originality / AI Review

Expected:

- applicability confirmed;
- tool/source metadata recorded when used;
- similarity matches interpreted contextually;
- AI signal treated as advisory;
- findings receive resolution states.

Controls: `MC-08`, `MC-09`.

### Stage 08 — Final QC

Expected:

- required reviews complete;
- evidence complete;
- blocking findings cleared;
- file/version integrity verified;
- final decision = `APPROVED_FOR_DELIVERY` only when gates are satisfied.

Controls: `MC-08`, `MC-09`, `MC-11`.

### Stage 09 — Delivery

Expected:

- only the approved deliverable is sent;
- delivery record identifies the approved version.

Control: `MC-11`.

### Stage 10 — Archive

Expected:

- minimum operational evidence archived;
- client-sensitive files remain in the designated production workspace;
- work item closure recorded.

## 5. Negative Path A — Unresolved Author Dependency

Inject:

```text
Finding: substantive methodological wording requires author decision
Resolution state: WAITING_AUTHOR
```

Expected behavior:

```text
WAITING_AUTHOR
    ↓
Final QC
    ↓
BLOCK
    ↓
No Delivery
```

Failure condition:

Any workflow that changes the item to `RESOLVED` without the required decision, or delivers despite the unresolved dependency, FAILS this test.

## 6. Negative Path B — Unresolved Source Dependency

Inject:

```text
Finding: material claim requires unavailable source
Resolution state: WAITING_SOURCE
```

Expected behavior:

```text
WAITING_SOURCE
    ↓
Final QC
    ↓
BLOCK / REVIEW
    ↓
No unsupported verification claim
```

## 7. Negative Path C — Sensitive External Processing

Inject synthetic PII into the document and request an external AI transformation.

Expected behavior:

```text
Sensitive data
    ↓
MC-10
    ↓
Minimize / Redact
    ↓
Outbound payload review
    ↓
ALLOW only if safe
```

Failure condition:

Raw sensitive payload is sent without justification/minimization/review.

## 8. Negative Path D — Similarity Score Shortcut

Inject a high similarity percentage caused primarily by quotation and bibliography.

Expected behavior:

- contextual match review;
- no automatic plagiarism verdict;
- source inspection for material matches.

Failure condition:

`High similarity → plagiarism` without contextual review.

## 9. Negative Path E — AI Detection Shortcut

Inject an AI-detector signal.

Expected behavior:

- applicability checked;
- signal recorded as advisory;
- human interpretation required;
- no authorship/misconduct verdict from score alone.

Failure condition:

`AI signal → confirmed AI authorship/misconduct` without sufficient evidence/policy basis.

## 10. Integration Assertions

The system passes only if all assertions hold:

1. Every stage has a defined input and output.
2. Required control IDs can be traced from Operating Model → Control Matrix → Workflow → SOP/QC.
3. Required evidence is produced before a stage is considered complete.
4. Unresolved material findings retain their resolution state.
5. `OPEN`, `WAITING_AUTHOR`, `WAITING_SOURCE`, and `ESCALATED` do not become completion states by omission.
6. Sensitive external processing cannot bypass MC-10.
7. Similarity score cannot independently establish plagiarism.
8. AI-assistance signal cannot independently establish authorship or misconduct.
9. E3 substantive decisions are not silently finalized.
10. Final delivery requires `APPROVED_FOR_DELIVERY`.
11. Archive preserves operational traceability without becoming default client-file storage.

## 11. Test Result

Record:

```text
Test run ID:
Date/time:
Reviewer:
Fixture version:

Positive Path: PASS / FAIL
Negative A: PASS / FAIL
Negative B: PASS / FAIL
Negative C: PASS / FAIL
Negative D: PASS / FAIL
Negative E: PASS / FAIL

Overall: PASS / FAIL / REVIEW
Findings:
```

## 12. Traceability

| Layer | Artifact |
|---|---|
| Normative architecture | `01_Workflows/Operating_Model.md` |
| Control specification | `01_Workflows/Control_Matrix.md` |
| Execution sequence | `01_Workflows/Master_Workflow.md` |
| Procedures | `02_SOP/` |
| Verification | `05_QC/` |
| Integration test | This artifact |

## 13. Change Control

Changes to this integration test that alter assertions, negative paths, or acceptance criteria must be reviewed against the current Operating Model and Control Matrix before approval.
