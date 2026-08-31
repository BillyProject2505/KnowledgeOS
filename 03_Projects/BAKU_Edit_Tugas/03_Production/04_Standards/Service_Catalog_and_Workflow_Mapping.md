# BAKU Edit Tugas — Service Catalog & Workflow Mapping

**Status:** Active  
**Version:** 1.0  
**Type:** Service-to-Production Mapping  
**Authority:** Derived from the current BAKU Edit Tugas service catalog presented on the production website and mapped to `Operating_Model.md` v2.1.  
**Normative Source:** `../01_Workflows/Operating_Model.md`  
**Operational Source:** `../01_Workflows/Master_Workflow.md`

## 1. Purpose

Dokumen ini menerjemahkan layanan yang ditawarkan BAKU Edit Tugas ke dalam Production System.

Dokumen ini **bukan normative operating model** dan tidak membuat lifecycle, control, status, atau completion rule baru.

Fungsinya adalah menjawab:

> "Jika pelanggan memilih layanan tertentu, bagian mana dari Production System yang applicable?"

## 2. Current Service Catalog

Berdasarkan service catalog website yang direview pada 31 Agustus 2026, layanan yang terlihat adalah:

1. Editing Grammar
2. Proofreading
3. Formatting
4. Sitasi & Referensi
5. Review Skripsi
6. Konsultasi Tulis

Website juga menampilkan service promises berupa **1x revisi gratis** dan **selesai 24 jam**. Promise tersebut merupakan service/marketing information dan belum dianggap sebagai operational SLA control dalam Production System.

## 3. Service Families

Untuk tujuan routing produksi, layanan dikelompokkan menjadi tiga family:

### A. Editorial / Document Production

- Editing Grammar
- Proofreading
- Formatting

### B. Academic Review / Verification

- Sitasi & Referensi
- Review Skripsi

### C. Advisory

- Konsultasi Tulis

Grouping ini adalah routing aid, bukan kategori normative baru.

## 4. Service-to-Workflow Matrix

| Service | Family | Typical Scope | Primary Workflow | Primary Controls | SOP | QC | Typical Deliverable | Risk Note |
|---|---|---|---|---|---|---|---|---|
| Editing Grammar | Editorial / Document Production | Ejaan, tanda baca, grammar, clarity, academic tone | 01 → 02 → 03 → 04 → 05 → 08 → 09 → 10 | MC-01, MC-02, MC-03, MC-05, MC-06, MC-08, MC-11 | SOP-01, SOP-02, SOP-03, SOP-04, SOP-07 | QC-01, QC-02, QC-05 | Edited document | Umumnya LOW; naik jika requested changes affect meaning or academic claims |
| Proofreading | Editorial / Document Production | Konsistensi istilah, koherensi paragraf, alur argumentasi, selain pemeriksaan bahasa | 01 → 02 → 03 → 04 → 05 → 08 → 09 → 10 | MC-01, MC-02, MC-03, MC-05, MC-06, MC-07, MC-08, MC-11 | SOP-01, SOP-02, SOP-03, SOP-04, SOP-07 | QC-01, QC-02, QC-05 | Proofread/reviewed document | Dapat menjadi MEDIUM bila review menyentuh substantive argumentation |
| Formatting | Editorial / Document Production | Margin, font, spacing, numbering, TOC, header/footer, formatting conventions | 01 → 02 → 03 → 05 → 08 → 09 → 10 | MC-01, MC-02, MC-03, MC-04 when guideline applies, MC-05, MC-08, MC-11 | SOP-01, SOP-02, SOP-03, SOP-04, SOP-05 when guideline applies, SOP-07 | QC-01, QC-02, QC-03 when guideline applies, QC-05 | Formatted document | Umumnya LOW; institutional formatting requirement dapat meningkatkan review depth |
| Sitasi & Referensi | Academic Review / Verification | Reference-list formatting dan, bila termasuk scope, citation/source verification | 01 → 02 → 03 → 05 → 06/07 when applicable → 08 → 09 → 10 | MC-01, MC-02, MC-03, MC-04, MC-05, MC-06, MC-08, MC-09, MC-11 | SOP-01, SOP-02, SOP-03, SOP-04, SOP-05, SOP-06 when applicable, SOP-07 | QC-01, QC-02, QC-03, QC-04 when applicable, QC-05 | Corrected reference/citation set or reviewed document | MEDIUM; distinguish formatting from source/claim verification |
| Review Skripsi | Academic Review / Verification | Review alur BAB I–V dan konsistensi judul–rumusan–metode–kesimpulan | 01 → 02 → 03 → 04 → 05 → 06 → 08 → 09 → 10 | MC-01 through MC-09 as applicable, MC-11 | SOP-01 through SOP-07 as applicable | QC-01 through QC-05 as applicable | Review findings / recommendations and/or reviewed document | MEDIUM–HIGH; academic decisions remain with author and E3 must not be silently resolved |
| Konsultasi Tulis | Advisory | Feedback tertulis terhadap draft dan saran perbaikan konkret | 01 → 02 → 03 → 04 → 05 → 06 when applicable → 08 → 09 → 10 | MC-01, MC-02, MC-03, MC-06, MC-07, MC-08, MC-09 when evidence/source review is in scope, MC-11 | SOP-01, SOP-02, SOP-03 when AI is used, SOP-04, SOP-05 when applicable, SOP-07 | QC-01, QC-02, QC-03 when applicable, QC-05 | Consultation feedback / recommendations | MEDIUM–HIGH when advice approaches substantive academic decision-making |

## 5. Service-Specific Boundaries

### 5.1 Editing Grammar

Primary objective is language-level improvement.

Allowed work normally falls within E1. If an edit changes substantive meaning, claim strength, methodology, evidence interpretation, or conclusion, route through the applicable E2/E3 controls rather than treating it as ordinary grammar correction.

### 5.2 Proofreading

The website description includes terminology consistency, paragraph coherence, and argument flow. Therefore this service is broader than typo-only proofreading.

Editorial judgment may occur under E2. Substantive academic decisions remain outside silent editing authority and must follow MC-07 and applicable human review.

### 5.3 Formatting

Formatting is primarily document presentation work. Institutional or assignment-specific formatting requirements activate the guideline gate when applicable.

Formatting changes must not be used as a mechanism to alter substantive academic content.

### 5.4 Sitasi & Referensi

Separate:

```text
Reference / citation formatting
            vs.
Source / claim verification
```

Formatting can be editorial work. Verification that a source supports a claim requires the evidence and source-verification controls in MC-04/MC-09 when included in scope.

### 5.5 Review Skripsi

The service reviews consistency and flow across major thesis components. Recommendations must not be presented as authoritative academic decisions belonging to the author.

Potential E3 conditions must be surfaced and routed according to MC-07 rather than silently rewritten.

### 5.6 Konsultasi Tulis

The deliverable is advisory feedback rather than necessarily an edited document.

The Master Workflow remains applicable, but Stage 04 Produce may produce a consultation analysis/feedback artifact instead of a revised document.

## 6. E1 / E2 / E3 Routing

Service selection does not determine edit authority by itself.

Use the authoritative definitions and controls in `Operating_Model.md` and `Control_Matrix.md`.

General routing:

```text
E1
→ direct editorial/document operation

E2
→ editorial judgment
→ human review

E3
→ academic decision
→ do not silently finalize
→ escalate / route to author decision as required
```

A service marketed as editing, proofreading, or consultation does not grant permission to perform E3 decisions silently.

## 7. Conditional Controls

Not every service requires every stage or control at the same depth.

Applicability must be determined from:

- approved Work Brief;
- client request;
- institutional/assignment requirements;
- risk assessment;
- data condition;
- whether originality/AI review is actually in scope;
- whether source/citation verification is actually in scope.

Conditional stages must not be skipped without a clear, recorded applicability decision where required by the operating model.

## 8. Website Promise vs Production Control

The website currently communicates:

- 1x free revision;
- completion within 24 hours.

These are **service promises**, not automatically production controls.

Before converting them into workflow/SLA controls, the business must define at minimum:

- when the 24-hour clock starts;
- what counts as a complete input;
- page/word limits or complexity boundaries, if any;
- whether the promise applies to every service;
- what happens when client clarification is pending;
- what happens when source/guideline dependencies are unavailable;
- what counts as the first delivery;
- how the free revision scope is bounded.

Until those requirements are explicitly decided, do not add a 24-hour SLA control to the Operating Model.

## 9. Routing Principle

Use the simplest applicable production path.

```text
Website Service
      ↓
Service Family
      ↓
Approved Work Brief
      ↓
Risk / Authorization
      ↓
Applicable Production Stages
      ↓
Applicable SOP / QC
      ↓
Final QC
      ↓
Delivery / Archive
```

Do not create a separate workflow for each website service unless real production experience demonstrates that the shared lifecycle cannot adequately handle the service.

## 10. Change Control

Changes to website services do not automatically change the Operating Model.

When a new or changed service is introduced:

1. update this mapping;
2. determine applicable controls/SOP/QC;
3. identify any genuine workflow gap;
4. only then consider changes to the authoritative operating layer.

If a new service cannot be safely routed using the current Operating Model, document the gap before introducing a new normative rule or workflow.

## 11. Traceability

| Layer | Role |
|---|---|
| Website service catalog | Defines what is publicly offered |
| Service Catalog & Workflow Mapping | Translates service offering into production routing |
| Operating Model | Normative production architecture |
| Control Matrix | Control specification and verification requirements |
| Master Workflow | Lifecycle execution map |
| SOP | Operator procedure |
| QC | Execution verification |
