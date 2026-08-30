# BAKU Edit Tugas — SOP-03 Academic Production with AI

**Status:** Approved  
**Version:** 2.1  
**Type:** Standard Operating Procedure  
**Authority:** Derived from `Operating_Model.md` v2.1 and `Control_Matrix.md` v2.1  
**Primary Controls:** MC-05, MC-06, MC-07, MC-10

## 1. Purpose

Menstandarkan cara menjalankan pekerjaan akademik berbantuan AI dalam scope yang telah diotorisasi, dengan batas intervensi yang jelas, preservation of meaning, substantive escalation, dan controlled external processing.

SOP ini menjawab **bagaimana operator menggunakan AI dalam produksi**. Aturan normatif tetap berada di `Operating_Model.md`, sedangkan control specification berada di `Control_Matrix.md`.

## 2. Scope

Berlaku untuk pekerjaan yang telah melewati authorization dan membutuhkan AI assistance pada tahap production.

Gunakan hanya sesuai approved scope dan review depth yang ditetapkan pada authorization.

## 3. Inputs

- approved Work Brief;
- approved scope;
- risk assessment;
- source/reference materials;
- applicable institutional or assignment requirements;
- document/draft;
- identified findings and dependencies;
- data-processing constraints.

## 4. Procedure

### Step 1 — Confirm Production Scope

Sebelum menggunakan AI:

- pastikan task sesuai approved scope;
- pastikan input/source yang diperlukan tersedia;
- identifikasi apakah task hanya language/editorial atau menyentuh substantive academic content;
- cek apakah external processing diperbolehkan berdasarkan data-processing constraints.

Jangan memperluas scope karena kemampuan AI tersedia.

### Step 2 — Prepare the Working Input

Siapkan hanya material yang diperlukan untuk task.

Pisahkan bila memungkinkan:

- text to edit;
- context needed to preserve meaning;
- source/evidence material;
- sensitive/unnecessary information.

Jangan memasukkan data pribadi atau confidential information yang tidak diperlukan.

### Step 3 — Apply External Processing Gate

Sebelum mengirim client material ke external AI/tool, jalankan `MC-10`:

```text
Data classification
    ↓
Need-to-process check
    ↓
Minimize / redact
    ↓
Outbound payload review
    ↓
ALLOW / ESCALATE / BLOCK
```

Jika keputusan bukan `ALLOW`, jangan melakukan processing normal.

### Step 4 — Define the Intended AI Task

Instruksi AI harus menjelaskan task secara spesifik, misalnya:

- correct grammar;
- improve clarity;
- identify redundancy;
- suggest coherence improvements;
- suggest structure changes;
- rephrase within the existing meaning.

Batasi AI dari:

- inventing facts;
- inventing citations/references;
- inventing methodology/results;
- adding unsupported claims;
- deciding substantive academic matters without authorization.

### Step 5 — Classify Interventions

Untuk setiap material intervention, apply `MC-05`:

**E1** — direct mechanical/editorial correction.

**E2** — contextual editorial judgment that must preserve meaning.

**E3** — substantive academic decision requiring human/author decision.

Gunakan control definition dari `Operating_Model.md`; SOP ini hanya menjalankan classification dan routing.

### Step 6 — Execute E1 Work

Untuk E1:

- apply clear grammar/spelling/punctuation corrections;
- remove obvious redundancy;
- preserve intended content;
- avoid unnecessary stylistic rewriting.

Review output against the original when changes are material or numerous.

### Step 7 — Execute E2 Work

Untuk E2:

- compare proposed change with surrounding context;
- verify terminology and coherence;
- preserve claim, intent, and academic position;
- inspect for unnecessary expansion or tone inflation.

Material E2 changes require review under `MC-06`.

### Step 8 — Escalate E3

Jika perubahan menyentuh:

- methodology;
- research design;
- claims or claim strength;
- evidence interpretation;
- conclusions;
- substantive academic position;

jangan menyelesaikan perubahan secara diam-diam.

Buat finding dan route melalui `MC-07`.

Gunakan status yang sesuai, misalnya `WAITING_AUTHOR`, `WAITING_SOURCE`, atau `ESCALATED`.

### Step 9 — Review AI Output

Setelah AI menghasilkan output, operator harus memeriksa:

- apakah requested task benar-benar dilakukan;
- apakah meaning tetap preserved;
- apakah ada unsupported addition;
- apakah terminology/context tetap tepat;
- apakah ada fabricated fact/source;
- apakah ada substantive intervention yang seharusnya E3;
- apakah unresolved findings tetap tercatat.

AI output tidak boleh dianggap final hanya karena grammar atau style terlihat lebih baik.

### Step 10 — Record Material Changes

Untuk perubahan yang material atau membutuhkan review, catat minimal:

```text
Original / context
Proposed change
Authority: E1 / E2 / E3
Review result
Resolution state
Decision owner when applicable
```

Tidak semua micro-edit E1 memerlukan change log individual; gunakan proportional traceability berdasarkan risk dan scope.

### Step 11 — Prepare Handoff

Handoff ke `05 Review` harus menyertakan:

- production draft;
- relevant change evidence;
- unresolved findings;
- source/reference dependencies;
- processing decision evidence when relevant.

## 5. AI Use Boundaries

### Appropriate

- language assistance;
- controlled rephrasing;
- redundancy detection;
- coherence suggestions;
- structure suggestions;
- pattern-based review;
- drafting assistance within approved scope.

### Not Appropriate as Autonomous Final Authority

- factual verification without checking sources;
- citation validation without source inspection;
- methodology invention;
- research-result invention;
- unsupported claim strengthening;
- silent substantive rewriting.

## 6. Meaning Preservation Check

Untuk material changes, lakukan comparison:

```text
Original
   ↓
Proposed edit
   ↓
Meaning comparison
   ↓
PRESERVED / ALTERED / UNCERTAIN
```

Gunakan normative states dari `Operating_Model.md → MC-06`.

Jika hasil `ALTERED` atau unresolved `UNCERTAIN`, route kembali ke review/escalation path.

## 7. Output

Produce:

1. Production draft within approved scope
2. Relevant change/review evidence
3. E3 escalation records when applicable
4. External processing evidence when applicable
5. Updated resolution states for tracked findings

## 8. Quality Checks

Sebelum handoff:

- scope tetap sesuai authorization;
- external processing decision sudah valid;
- E1/E2/E3 classification konsisten;
- meaning preservation diperiksa untuk material changes;
- tidak ada fabricated fact/source/methodology/result;
- E3 tidak diselesaikan secara silent;
- unresolved findings tetap tercatat;
- output siap masuk human review.

## 9. Control Traceability

| Control | SOP Step | Evidence |
|---|---|---|
| MC-05 Edit Authority | Steps 5–7 | Classified interventions / review evidence |
| MC-06 Meaning Preservation | Steps 7, 9 | Original-vs-edit semantic review |
| MC-07 Substantive Change Escalation | Step 8 | Escalation record + decision dependency |
| MC-10 External Processing Gate | Steps 2–3 | Processing decision + minimization/payload evidence |

Normative control definitions remain in:

`../01_Workflows/Operating_Model.md`

Control specification remains in:

`../01_Workflows/Control_Matrix.md`

## 10. Change Control

Changes to this SOP that alter AI-use boundaries, edit authority, external processing decisions, required evidence, or escalation behavior must be reviewed against `Operating_Model.md` and `Control_Matrix.md` before approval.
