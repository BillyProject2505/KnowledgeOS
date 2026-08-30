# BAKU Edit Tugas — Editing Workflow

**Status:** Active  
**Version:** 2.1  
**Authority:** Derived from `Operating_Model.md` v2.1, `Master_Workflow.md` v2.1, and applicable SOP/QC artifacts  
**Purpose:** Workflow khusus untuk layanan editing dokumen akademik yang mengimplementasikan lifecycle produksi tanpa membuat workflow atau control boundary yang berdiri sendiri.

## 1. Role in Production System

`Editing_Workflow.md` adalah **service-specific workflow view** untuk pekerjaan editing.

Workflow ini tidak menggantikan `Master_Workflow.md` dan tidak menjadi source of truth normatif.

Gunakan lifecycle dan controls dari:

- `Operating_Model.md` sebagai normative architectural source;
- `Master_Workflow.md` sebagai operational execution map;
- SOP/QC sebagai prosedur dan verification layer.

## 2. Editing Flow

Untuk pekerjaan editing, lifecycle Master Workflow diterapkan dengan fokus berikut:

```text
01 Intake
    ↓
02 Diagnose + Risk
    ↓
03 Authorize
    ↓
04 Produce — Editing
    ↓
05 Review — Human Review
    ↓
06 Academic QC [when applicable]
    ↓
07 Originality / AI Review [when applicable]
    ↓
08 Final QC
    ↓
09 Delivery
    ↓
10 Archive
```

Jangan menggunakan flow lama sebagai pengganti lifecycle Master Workflow.

## 3. Editing Scope

### Language

- grammar;
- spelling;
- punctuation;
- sentence clarity;
- word choice;
- academic tone.

### Structure

- paragraph organization;
- flow between sections;
- redundancy;
- heading consistency;
- logical ordering.

### Consistency

- terminology;
- capitalization;
- abbreviations;
- citation style;
- formatting conventions.

Scope aktual tetap mengikuti approved Work Brief dan authorization.

## 4. Non-Destructive Editing

Editing harus menjaga:

- maksud penulis;
- substansi yang diberikan;
- konteks akademik;
- fakta yang tersedia.

Untuk material changes, gunakan `MC-06 Meaning Preservation` dan prosedur human review yang berlaku.

Jangan mengubah argumen, methodology, evidence interpretation, claim strength, atau conclusion secara substantif tanpa routing sesuai control yang berlaku.

## 5. AI-Assisted Editing

AI dapat digunakan untuk appropriate language/editorial assistance sesuai approved scope.

Contoh:

- grammar correction;
- clarity improvement;
- controlled rephrasing;
- redundancy detection;
- coherence suggestions;
- structure suggestions.

Setiap penggunaan AI tetap tunduk pada:

- `MC-05 Edit Authority`;
- `MC-06 Meaning Preservation`;
- `MC-07 Substantive Change Escalation`;
- `MC-10 External Processing Gate` bila external processing berlaku.

Gunakan `SOP-03_Academic_Production_with_AI.md` untuk prosedur detail.

## 6. Human Review

Setelah production:

- bandingkan output dengan original/context;
- periksa material additions/deletions;
- periksa meaning preservation;
- identifikasi E3 conditions;
- review over-editing;
- pastikan findings dan resolution states tercatat.

Gunakan `SOP-04_Human_Review_and_Edit_Boundary.md` dan `QC-02_Production_and_Human_Review_QC.md` untuk prosedur dan verification.

## 7. Academic / Compliance Checks

Ketika editing scope juga mencakup institutional, assignment, source, atau citation compliance, jalankan tahap yang applicable dari Master Workflow.

Gunakan:

- `SOP-05_Academic_Compliance_and_Source_Verification.md`;
- `QC-03_Academic_Compliance_QC.md`.

Jangan menganggap semua pekerjaan editing memerlukan full academic compliance review.

## 8. Completion

Pekerjaan editing mengikuti Definition of Done dan Final QC pada Operating Model.

File yang sudah diedit bukan otomatis final.

Sebelum delivery, required review/QC harus selesai dan tidak boleh ada blocking finding yang unresolved.

Gunakan `SOP-07_Final_QC_Delivery_and_Archive.md` dan `QC-05_Final_QC.md`.

## 9. Traceability

| Function | Authoritative Artifact |
|---|---|
| Normative operating rules | `Operating_Model.md` |
| Production sequence | `Master_Workflow.md` |
| AI-assisted production procedure | `SOP-03_Academic_Production_with_AI.md` |
| Human review procedure | `SOP-04_Human_Review_and_Edit_Boundary.md` |
| Academic compliance procedure | `SOP-05_Academic_Compliance_and_Source_Verification.md` |
| Originality/AI review | `SOP-06_Originality_and_AI_Signal_Review.md` |
| Final QC/delivery/archive | `SOP-07_Final_QC_Delivery_and_Archive.md` |

## 10. Change Control

Changes to this service-specific workflow must remain aligned with `Operating_Model.md` and `Master_Workflow.md`.

Do not introduce a separate lifecycle, status vocabulary, control, or completion rule here without an approved change to the authoritative layers.
