# BAKU Edit Tugas — Master Production Workflow

**Status:** Active  
**Version:** 2.1  
**Authority:** Derived from `Operating_Model.md` v2.1  
**Purpose:** Menjadi peta eksekusi operasional pekerjaan klien berdasarkan lifecycle dan mandatory controls yang ditetapkan pada Operating Model.

## 1. Production Workflow

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

## 2. Stage Definitions

### 01 — Intake

**Purpose:** Mengubah permintaan klien menjadi Work Brief yang dapat diproduksi.

**Input:**
- permintaan klien;
- file/draft yang tersedia;
- deadline;
- requirement dan reference yang tersedia.

**Activities:**
- capture service type dan document type;
- capture academic level, institution/program, dan scope;
- capture output format dan deadline;
- capture client/instructor/institution requirements;
- identify applicable institutional guideline;
- record requirement/source inventory.

**Gate:** Minimum information untuk diagnosis tersedia.

**Output:** Work Brief + requirement source inventory.

**Handoff:** Diagnose + Risk.

**Control references:** `Operating_Model.md → MC-01, MC-04`

### 02 — Diagnose + Risk

**Purpose:** Menentukan kondisi dokumen, kebutuhan intervensi, dependency, dan risk level sebelum produksi.

**Input:** Work Brief + source materials + document.

**Activities:**
- inspect document condition;
- identify language, editorial, academic, source/citation, formatting, and data-sensitivity concerns;
- identify missing or ambiguous information;
- classify risk as `LOW`, `MEDIUM`, or `HIGH`.

**Gate:** Scope, dependencies, dan risk cukup jelas untuk authorization.

**Output:** Diagnosis + risk assessment + findings/dependencies.

**Handoff:** Authorize.

**Control references:** `Operating_Model.md → MC-02`

### 03 — Authorize

**Purpose:** Menentukan apakah pekerjaan dapat diproduksi dalam scope yang disetujui.

**Input:** Work Brief + diagnosis + risk assessment.

**Activities:**
- confirm scope and boundaries;
- confirm required evidence/source availability;
- apply integrity and safety boundaries;
- determine required review depth.

**Gate outcomes:**
- `AUTHORIZED`
- `CLARIFICATION_REQUIRED`
- `ESCALATED`
- `DECLINED`

**Output:** Authorization decision + approved scope.

**Handoff:** Produce or resolution path.

**Control references:** `Operating_Model.md → MC-03`

### 04 — Produce

**Purpose:** Mengerjakan scope yang telah diotorisasi.

**Input:** Approved scope + document + applicable requirements.

**Activities:**
- perform approved editing/content-support work;
- use AI assistance where appropriate;
- record or surface substantive decisions;
- maintain required evidence/source references.

**Gate:** Output remains within approved scope and applicable controls.

**Output:** Production draft + findings/change evidence as applicable.

**Handoff:** Review.

**Control references:** `Operating_Model.md → MC-05, MC-06, MC-07, MC-10`

### 05 — Review

**Purpose:** Memeriksa hasil produksi terhadap brief, scope, dan edit boundaries sebelum academic QC.

**Input:** Production draft + Work Brief.

**Activities:**
- verify scope completion;
- review changes for meaning preservation;
- inspect unwanted additions or over-editing;
- identify unresolved findings;
- route substantive items for escalation where required.

**Gate:** No unresolved material issue may be silently carried forward.

**Output:** Reviewed draft + updated findings/resolution states.

**Handoff:** Academic QC.

**Control references:** `Operating_Model.md → MC-05, MC-06, MC-07, MC-08`

### 06 — Academic QC

**Purpose:** Menilai academic compliance dan quality sesuai scope serta requirement yang berlaku.

**Input:** Reviewed draft + applicable requirements + source evidence.

**Activities:**
- apply institutional/assignment requirements where applicable;
- assess structural compliance;
- assess substantive academic quality;
- assess requirement applicability;
- record evidence and findings.

**Gate:** Requirement status menggunakan `PASS / FAIL / N/A / REVIEW` sesuai evidence yang tersedia.

**Output:** Academic QC result + compliance/quality findings.

**Handoff:** Originality / AI Review when applicable; otherwise Final QC.

**Control references:** `Operating_Model.md → MC-04, MC-09`

### 07 — Originality / AI Review [Conditional]

**Purpose:** Menjalankan review originality atau AI-assistance hanya ketika scope/risk membutuhkannya dan tool dapat diterapkan secara valid.

**Input:** QC-ready document + applicable review scope + available tool/source evidence.

**Activities:**
- run applicable similarity/originality checks;
- classify match context and inspect relevant sources;
- run AI-assistance screening when applicable;
- record signal, limitations, interpretation, and resolution state.

**Gate:** Screening must be applicable; unresolved material findings follow resolution/escalation path.

**Output:** Originality/AI review result + findings.

**Handoff:** Final QC or resolution path.

**Control references:** `Operating_Model.md → MC-08, MC-09`

### 08 — Final QC

**Purpose:** Memastikan pekerjaan benar-benar siap untuk delivery.

**Input:** Reviewed/verified output + all applicable QC results.

**Activities:**
- verify approved scope is complete;
- verify applicable requirements and required reviews are addressed;
- confirm required evidence is recorded;
- confirm final version and file integrity;
- verify unresolved findings do not violate delivery gates;
- prepare final delivery package.

**Gate:** Critical unresolved findings always block delivery. Other unresolved states are handled according to risk and scope.

**Output:** Final QC approval or blocked status.

**Handoff:** Delivery when approved; resolution path when blocked.

**Control references:** `Operating_Model.md → MC-08, MC-09, MC-11`

### 09 — Delivery

**Purpose:** Menyerahkan output yang telah disetujui secara jelas dan traceable.

**Input:** Final QC approved deliverable.

**Activities:**
- provide final file/package;
- include relevant revision or limitation notes;
- communicate required next action when applicable.

**Gate:** Final QC approval exists.

**Output:** Delivered work package.

**Handoff:** Archive.

**Control references:** `Operating_Model.md → MC-11`

### 10 — Archive

**Purpose:** Menyimpan evidence operasional yang diperlukan untuk traceability tanpa menjadikan repository sebagai default client-file storage.

**Input:** Delivered work + required operational evidence.

**Activities:**
- record required production metadata and evidence;
- retain relevant decision/resolution records;
- preserve approved operational knowledge;
- keep client data in the appropriate production workspace.

**Gate:** Archive only after delivery decision is complete.

**Output:** Archived operational record.

## 3. Workflow Control References

The workflow executes the mandatory controls defined by `Operating_Model.md` v2.1. The Operating Model is normative; this document only identifies where controls are exercised in the lifecycle.

| Control | Primary workflow stage(s) |
|---|---|
| MC-01 Client Requirement Capture | 01 Intake |
| MC-02 Risk Classification | 02 Diagnose + Risk |
| MC-03 Authorization / Integrity Gate | 03 Authorize |
| MC-04 Institutional Guideline Gate | 01 Intake, 06 Academic QC |
| MC-05 Edit Authority | 04 Produce, 05 Review |
| MC-06 Meaning Preservation | 04 Produce, 05 Review |
| MC-07 Substantive Change Escalation | 03 Authorize, 04 Produce, 05 Review |
| MC-08 Resolution State | 05 Review, 07 Originality / AI Review, 08 Final QC |
| MC-09 Evidence Sufficiency | 06 Academic QC, 07 Originality / AI Review, 08 Final QC |
| MC-10 External Processing Gate | 04 Produce |
| MC-11 Fail-Closed Final QC | 08 Final QC, 09 Delivery |

## 4. Completion Rule

A work item is complete only when the approved scope and applicable requirements have been addressed, required reviews/verifications are completed, required evidence is recorded, unresolved blocking findings are cleared, and Final QC approves delivery.

The normative Definition of Done and delivery rules are defined in `Operating_Model.md` v2.1.

## 5. Authority & Change Control

`Operating_Model.md` v2.1 is the **normative architectural source of truth**. This document is the **operational execution map** derived from it.

This document must not redefine normative controls. If an operational interpretation conflicts with the Operating Model, the Operating Model prevails until formally changed.

Changes to this workflow must remain aligned with the Operating Model and follow project change control. SOPs, AI workflows, QC artifacts, and templates must be derived from these authoritative layers rather than creating competing rules.
