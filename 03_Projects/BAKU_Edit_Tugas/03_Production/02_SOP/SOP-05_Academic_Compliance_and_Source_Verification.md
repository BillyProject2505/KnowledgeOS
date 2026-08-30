# BAKU Edit Tugas — SOP-05 Academic Compliance & Source Verification

**Status:** Approved  
**Version:** 2.1  
**Type:** Standard Operating Procedure  
**Authority:** Derived from `Operating_Model.md` v2.1 and `Control_Matrix.md` v2.1  
**Primary Controls:** MC-04, MC-09

## 1. Purpose

Menstandarkan cara memeriksa academic compliance dan melakukan source verification ketika pekerjaan memiliki guideline, requirement, claim, citation, atau evidence yang perlu diverifikasi.

SOP ini menjawab **bagaimana operator menjalankan compliance review dan source verification**. Aturan normatif tetap berada di `Operating_Model.md`, sedangkan control specification berada di `Control_Matrix.md`.

## 2. Scope

Berlaku untuk pekerjaan yang membutuhkan:

- compliance terhadap guideline institusi, dosen, jurnal, atau assignment;
- verification terhadap claim atau citation;
- pemeriksaan source/evidence yang relevan;
- academic quality review yang membutuhkan evidence.

MC-04 aktif ketika external requirement menjadi bagian dari scope/compliance requirement. MC-09 berlaku ketika verdict bergantung pada evidence.

## 3. Inputs

- reviewed document/draft;
- Work Brief;
- applicable requirements;
- official guideline/source;
- citation/reference list;
- source materials;
- research/design context when relevant;
- existing findings/dependencies;
- prior verification evidence.

## 4. Procedure

### Step 1 — Confirm Review Scope

Tentukan apa yang benar-benar perlu diverifikasi berdasarkan approved scope.

Pisahkan:

- structural compliance;
- substantive academic quality;
- factual/source verification;
- citation/reference verification.

Jangan memperluas audit di luar scope tanpa authorization.

### Step 2 — Establish the Source of Truth

Untuk setiap external requirement atau source-dependent judgment, identifikasi authority yang berlaku.

Prioritaskan:

- official institutional guideline;
- official journal/instructor requirement;
- primary source when appropriate;
- authoritative source relevant to the claim.

Catat:

```text
Source title
Issuing authority
Version/year when available
URL/file
Applicability
Access status
```

Jangan menggunakan sumber sekunder sebagai pengganti sumber resmi bila sumber resmi tersedia dan relevan.

### Step 3 — Validate Source Applicability

Pastikan source:

- berasal dari authority yang relevan;
- berlaku untuk institution/program/document type yang diperiksa;
- versi/tahun sesuai atau dapat dipertanggungjawabkan;
- dapat dibaca secara memadai.

Jika applicability atau source validity tidak dapat ditentukan:

`REVIEW / UNVERIFIED`

Jangan mengklaim compliance.

### Step 4 — Extract Requirements

Untuk guideline yang berlaku, ekstrak requirement menjadi unit yang dapat diuji.

Minimal:

```text
Requirement ID
Requirement summary
Guideline section/page
Applicable condition
Expected document evidence
```

Jangan mengubah preferensi editor menjadi requirement institusi.

### Step 5 — Determine Requirement Applicability

Untuk setiap requirement, tentukan apakah requirement:

- berlaku untuk dokumen/desain penelitian;
- tidak berlaku;
- membutuhkan klarifikasi.

Pertimbangkan research design atau document context bila requirement bergantung pada jenis pekerjaan.

Jangan memaksakan requirement kuantitatif pada penelitian kualitatif, atau sebaliknya, tanpa dasar guideline.

### Step 6 — Map Requirement to Document Evidence

Untuk setiap applicable requirement:

```text
Requirement
    ↓
Document section / evidence
    ↓
Assessment
```

Catat lokasi evidence secara spesifik, misalnya section, heading, paragraph, table, appendix, atau page.

### Step 7 — Assign Compliance Status

Gunakan hanya status:

- `PASS` — requirement jelas terpenuhi dan evidence cukup;
- `FAIL` — requirement jelas tidak terpenuhi dan evidence cukup untuk menetapkan non-compliance;
- `N/A` — requirement tidak berlaku;
- `REVIEW` — evidence, applicability, atau interpretation belum cukup.

Jangan menetapkan `FAIL` hanya karena evidence belum ditemukan. Terapkan MC-09 terlebih dahulu.

### Step 8 — Verify Claims and Citations

Untuk citation/claim yang masuk scope:

- locate cited source;
- verify bibliographic identity;
- inspect relevant source content;
- determine whether source actually supports the claim;
- record uncertainty when support cannot be established.

Bedakan:

```text
Citation exists
≠
Source supports claim
```

Jangan mengubah claim substantif hanya untuk membuat citation terlihat cocok.

### Step 9 — Record Findings

Setiap finding yang membutuhkan action harus dicatat minimal:

```text
Finding ID
Requirement / claim
Evidence
Assessment
Status
Recommended action
Owner/dependency when applicable
```

### Step 10 — Route Substantive Academic Issues

Jika review menemukan masalah yang menyentuh:

- methodology;
- research design;
- claim strength;
- evidence interpretation;
- substantive conclusion;

jangan melakukan silent correction. Route sesuai `MC-07 Substantive Change Escalation`.

### Step 11 — Close or Carry Forward Findings

Setiap finding harus memiliki resolution state sesuai `MC-08`.

Jangan mengubah finding menjadi resolved hanya karena rekomendasi sudah ditulis.

### Step 12 — Produce Compliance / Verification Record

Output harus menunjukkan:

- source of truth;
- extracted requirements;
- applicability;
- document evidence;
- compliance status;
- source verification result;
- unresolved items;
- escalation/dependency where applicable.

## 5. Compliance Matrix Minimum

Gunakan format:

| ID | Requirement | Guideline/Source | Document Evidence | Applicability | Status | Evidence Sufficiency | Action |
|---|---|---|---|---|---|---|---|
| C-01 | ... | ... | ... | Applicable | PASS | Sufficient | None |
| C-02 | ... | ... | ... | Applicable | REVIEW | Insufficient | Verify |

Untuk pekerjaan high-risk, tambahkan severity dan owner/dependency bila dibutuhkan.

## 6. Source Verification Rules

### Source verified and supportive

Status dapat dinyatakan `VERIFIED` sesuai evidence yang tersedia.

### Source exists but support is uncertain

Status:

`REVIEW`

### Source unavailable or unreadable

Status:

`UNVERIFIED`

### Citation exists without source support

Catat sebagai finding; jangan otomatis menyimpulkan misconduct tanpa contextual review.

## 7. Quality Checks

Sebelum handoff:

- source of truth identified;
- source applicability checked;
- requirement extraction traceable;
- each relevant requirement mapped;
- PASS/FAIL/N/A/REVIEW supported by evidence;
- source claims actually inspected when in scope;
- substantive issues escalated;
- unresolved dependencies retained.

## 8. Outputs

Produce:

1. **Compliance Matrix** when MC-04 applies or high-risk review requires it;
2. **Source Verification Record** when source verification is in scope;
3. **Academic Quality Findings** when applicable;
4. **Open / Escalated Findings**;
5. **Resolution State updates**.

## 9. Handoff

Handoff to the next stage requires:

```text
Compliance/verification result
+
Evidence trail
+
Open findings and resolution states
+
Escalation records when applicable
```

If required evidence is insufficient, carry the item as `REVIEW` / `UNVERIFIED`; do not present it as verified.

## 10. Control Traceability

| Control | SOP Step | Evidence |
|---|---|---|
| MC-04 Institutional Guideline Gate | Steps 2–7, 12 | Guideline record + requirement extraction + compliance matrix |
| MC-09 Evidence Sufficiency | Steps 7–12 | Evidence trail + verdict rationale |

Normative control definitions remain in:

`../01_Workflows/Operating_Model.md`

Control specification remains in:

`../01_Workflows/Control_Matrix.md`

## 11. Change Control

Changes to this SOP that alter source authority, compliance statuses, applicability, required evidence, or verification behavior must be reviewed against `Operating_Model.md` and `Control_Matrix.md` before approval.
