# BAKU Edit Tugas — Operating Model

**Status:** Approved
**Version:** 2.1
**Role:** Production operating model and control architecture

## 1. Purpose

Operating Model ini mendefinisikan bagaimana pekerjaan klien BAKU Edit Tugas bergerak dari intake sampai delivery, kontrol apa yang wajib diterapkan, dan kapan pekerjaan harus berhenti atau dieskalasikan.

Model ini berlaku untuk pekerjaan akademik berbantuan AI dan menjadi dasar penurunan Master Workflow, SOP, QC, templates, dan governance.

> **AI assists the work; human owns the academic responsibility.**

## 2. Operating Principles

1. Client requirements come before production.
2. Institutional requirements govern compliance when they are applicable and available.
3. AI is a production capability, not the final authority.
4. Human judgment controls academic, factual, source, and substantive decisions.
5. Similarity is not the same as plagiarism.
6. AI-detection signal is not proof of AI authorship or misconduct.
7. Evidence must be sufficient before a compliance or quality verdict is issued.
8. Unresolved critical issues block completion and delivery.
9. Repository documentation stores durable production knowledge; client files belong in the appropriate production workspace.

## 3. End-to-End Lifecycle

```text
01 INTAKE
    ↓
02 DIAGNOSE + RISK
    ↓
03 AUTHORIZE
    ↓
04 PRODUCE
    ↓
05 REVIEW
    ↓
06 ACADEMIC QC
    ↓
07 ORIGINALITY / AI REVIEW [conditional]
    ↓
08 FINAL QC
    ↓
09 DELIVER
    ↓
10 ARCHIVE
```

## 4. Stage Model

### 01 — Intake

**Purpose:** Turn the client request into a workable brief.

Capture what is applicable:

- service type;
- document type;
- academic level;
- institution and program;
- scope;
- deadline;
- output format;
- client requirements;
- instructor/institution requirements;
- reference/source material;
- applicable institutional guideline.

**Gate:** Minimum requirements must be available before diagnosis.

**Outputs:** Work Brief, intake status, requirement source inventory.

### 02 — Diagnose + Risk

**Purpose:** Understand the actual work before production.

Determine:

- document condition;
- scope of intervention;
- language/structure issues;
- source/citation issues;
- ambiguity or missing information;
- substantive academic concerns;
- privacy/sensitivity concerns;
- risk level: `LOW`, `MEDIUM`, or `HIGH`.

Separate:

- language/format problems;
- editorial problems;
- academic/substantive problems.

**Gate:** Scope and risk must be clear enough to authorize production.

### 03 — Authorize

**Purpose:** Decide whether the requested work may proceed.

Possible outcomes:

- `AUTHORIZED`
- `CLARIFICATION_REQUIRED`
- `ESCALATED`
- `DECLINED`

Authorization must consider academic-integrity and scope boundaries. Do not accept requests to fabricate evidence, fabricate sources/data, conceal unattributed copying, or manipulate detection systems.

### 04 — Produce

**Purpose:** Perform the approved work.

AI may be used for appropriate assistance such as:

- grammar and spelling;
- clarity and readability;
- controlled rephrasing;
- coherence suggestions;
- structure suggestions;
- pattern-based checks;
- drafting assistance within approved scope.

AI must not silently:

- invent facts;
- invent citations or references;
- invent methodology or research results;
- strengthen claims beyond available evidence;
- replace substantive academic decisions without authorization.

#### Edit Authority

Each intervention must be treated as one of:

**E1 — Direct Edit**  
Clear mechanical/editorial correction. Example: typo, grammar, punctuation, obvious redundancy.

**E2 — Editorial Judgment**  
Change requires contextual judgment while preserving meaning. Example: coherence, terminology, paragraph structure.

**E3 — Academic Decision**  
Change affects methodology, evidence, claims, interpretation, research design, or conclusions. E3 requires human/author decision and must not be silently rewritten.

### 05 — Review

**Purpose:** Check the produced draft against the approved brief and edit boundaries.

Review:

- scope completion;
- meaning preservation;
- E1/E2/E3 handling;
- unwanted additions;
- over-editing;
- unsupported changes;
- unresolved findings.

#### Meaning Preservation

For material changes classify:

- `PRESERVED`
- `ALTERED`
- `UNCERTAIN`

`ALTERED` or unresolved `UNCERTAIN` requires further review before finalization.

### 06 — Academic QC

**Purpose:** Determine whether the work is academically compliant and supportable within its approved scope.

Where an institutional or assignment guideline applies, use the guideline as the compliance source of truth.

Separate:

#### Structural Compliance

Whether the document follows required sections, headings, numbering, and other structural rules.

#### Substantive Academic Quality

Whether the content under those structures is sufficiently coherent, supported, and methodologically appropriate for the task.

#### Requirement Applicability

A requirement must first be classified as applicable, not applicable, or unresolved for the actual document and research design.

Use:

- `PASS` — requirement is clearly met;
- `FAIL` — requirement is clearly not met and evidence is sufficient;
- `N/A` — requirement is not applicable;
- `REVIEW` — evidence, applicability, or requirement interpretation is insufficient.

Do not issue `FAIL` merely because evidence is missing; first determine whether the evidence base is sufficient.

### 07 — Originality / AI Review (Conditional)

This stage is activated when the scope or risk requires it.

#### Similarity / Originality Review

Use the sequence:

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

Similarity score is not a plagiarism verdict.

Review match context such as:

- quotation;
- proper paraphrase;
- bibliography/reference;
- common academic phrase;
- potential unattributed copying;
- close paraphrase.

Use conservative statuses such as:

- `NO_MATERIAL_CONCERN`
- `REVIEW`
- `MATERIAL_CONCERN`

Do not rewrite text solely to reduce a similarity score.

#### AI-Assistance Screening

AI screening is an advisory signal only.

Determine first whether screening is applicable based on tool capability, language, document length/type, and other documented limitations.

Possible states:

- `NOT_APPLICABLE`
- `NO_SIGNAL`
- `SIGNAL_REVIEW`
- `INCONCLUSIVE`
- `ESCALATED`

AI signal must not be treated as proof of authorship, human authorship, plagiarism, or misconduct.

### 08 — Final QC

**Purpose:** Confirm the work is actually ready for delivery.

At minimum verify:

- approved scope completed;
- applicable requirements addressed;
- required academic/originality checks completed;
- no unresolved critical issue;
- required evidence recorded;
- final version correct;
- file opens correctly;
- no unintended working artifacts remain;
- delivery package is correct.

#### Fail-Closed Rule

The work is not done when unresolved findings remain.

At minimum, these states block final approval where they remain materially unresolved:

- `OPEN`
- `WAITING_AUTHOR`
- `WAITING_SOURCE`
- `ESCALATED`

Critical unresolved findings always block delivery.

### 09 — Deliver

Delivery occurs only after Final QC approval.

Include, when relevant:

- final file;
- concise revision summary;
- limitations or unresolved client dependencies that have been explicitly accepted;
- next action.

### 10 — Archive

Archive the minimum durable operational evidence needed for traceability. Do not use the repository as default storage for client documents or sensitive client data.

## 5. Mandatory Controls

The following controls are mandatory parts of the operating model:

| ID | Control | Application |
|---|---|---|
| MC-01 | Client Requirement Capture | All work |
| MC-02 | Risk Classification | All work |
| MC-03 | Authorization / Integrity Gate | All work |
| MC-04 | Institutional Guideline Gate | Conditional: when compliance is claimed or required |
| MC-05 | Edit Authority | All editing/rewriting work |
| MC-06 | Meaning Preservation | All material editing/rewriting |
| MC-07 | Substantive Change Escalation | Whenever E3 is encountered |
| MC-08 | Resolution State | All tracked findings |
| MC-09 | Evidence Sufficiency | All compliance/quality verdicts |
| MC-10 | External Processing Gate | Before sensitive client data is sent to external AI/tools |
| MC-11 | Fail-Closed Final QC | All delivery-bound work |

## 6. Resolution States

Use the following finding states consistently:

- `RESOLVED` — issue has been adequately addressed.
- `OPEN` — issue remains and needs action.
- `WAITING_AUTHOR` — requires author/client decision or material.
- `WAITING_SOURCE` — requires source/evidence.
- `ESCALATED` — requires higher-level review or decision.

Only `RESOLVED` findings satisfy completion requirements.

## 7. External Processing Gate

Before any document or excerpt is processed by an external AI/tool:

```text
Classify data
    ↓
Identify sensitive/unnecessary data
    ↓
Minimize / redact where possible
    ↓
Review outbound payload
    ↓
ALLOW / ESCALATE / BLOCK
```

Do not send unnecessary personal, confidential, research-participant, or client-sensitive information to an external AI/tool.

## 8. Evidence & Traceability

Evidence requirements must be proportional to risk.

### LOW

Minimum viable evidence:

- Work Brief;
- Final QC result;
- final deliverable.

### MEDIUM

Add relevant:

- diagnosis;
- review notes;
- academic/source findings.

### HIGH

Add, when applicable:

- guideline/source record;
- compliance matrix;
- source verification evidence;
- originality review;
- escalation/decision records;
- final QC evidence.

## 9. Service Scope & Definition of Done

Quality expectations are bounded by the purchased/approved service scope.

Examples:

- `Editorial & Formatting Only`
- `Academic Editing + Compliance Review`
- `Academic Assistance`
- `Consultation`

A work item is **DONE** only when its approved scope and applicable requirements are satisfied, required reviews and verifications are complete, critical findings are resolved, required evidence is recorded, and Final QC approves the output.

Similarity score, AI-detector score, or file creation alone never constitutes completion.

## 10. Authority Rules

When sources or requirements conflict, do not silently choose a preferred interpretation.

Use this hierarchy for ordinary production decisions:

```text
Applicable institutional / assignment requirement
        ↓
Client-approved requirement
        ↓
BAKU internal standard
        ↓
Editorial preference
```

Academic-integrity constraints apply independently and cannot be overridden by client preference.

## 11. Repository Boundary

GitHub is the durable source of truth for approved operating knowledge, standards, SOPs, templates, governance, and other project documentation.

Working drafts, client files, personal data, and production evidence belong in the appropriate production workspace unless a specific, documented reason justifies repository storage.

Exploratory conversation output is not canonical until explicitly approved and recorded.

## 12. Change Control

This Operating Model is the architectural baseline for production documentation.

Changes must be intentional and documented. SOPs, AI workflows, QC checklists, and templates must not silently contradict this model.

When this model changes materially:

1. update the Operating Model;
2. identify affected SOPs/QC/templates;
3. update dependent documents;
4. record the approved project decision and changelog entry.
