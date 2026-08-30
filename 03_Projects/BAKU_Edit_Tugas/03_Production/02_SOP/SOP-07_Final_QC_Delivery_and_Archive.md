# BAKU Edit Tugas — SOP-07 Final QC, Delivery & Archive

**Status:** Approved  
**Version:** 2.1  
**Type:** Standard Operating Procedure  
**Authority:** Derived from `Operating_Model.md` v2.1 and `Control_Matrix.md` v2.1  
**Primary Controls:** MC-08, MC-10, MC-11

## 1. Purpose

Menstandarkan cara memastikan pekerjaan benar-benar siap dikirim, menjalankan delivery, dan menyimpan evidence operasional minimum untuk traceability.

SOP ini menjawab **bagaimana operator menjalankan Final QC, delivery, dan archive**. Aturan normatif tetap berada di `Operating_Model.md`, sedangkan control specification berada di `Control_Matrix.md`.

## 2. Scope

Berlaku setelah seluruh production/review/QC yang relevan selesai dan sebelum delivery serta archive.

## 3. Inputs

- approved scope;
- final candidate deliverable;
- Work Brief;
- applicable requirements;
- QC and verification results;
- findings and resolution states;
- required evidence;
- file/version information;
- delivery instructions.

## 4. Procedure

### Step 1 — Confirm Scope Completion

Periksa bahwa seluruh pekerjaan dalam approved scope telah dikerjakan atau dependency yang tidak dapat diselesaikan telah dicatat secara eksplisit.

Jangan menganggap file final berarti scope selesai.

### Step 2 — Check Required Reviews and Verifications

Pastikan review yang diwajibkan oleh scope/risk telah dilakukan, misalnya:

- human review;
- academic compliance;
- source/citation verification;
- originality review;
- AI-signal review;
- formatting review.

Tahap yang tidak applicable boleh dilewati jika status applicability dapat dibuktikan.

### Step 3 — Review Findings and Resolution States

Periksa seluruh finding yang masih terbuka.

Gunakan `MC-08` untuk memastikan setiap tracked finding memiliki current resolution state.

Jangan menganggap:

- `OPEN`;
- `WAITING_AUTHOR`;
- `WAITING_SOURCE`;
- `ESCALATED`

sebagai resolved hanya karena tidak ada action lanjutan yang sedang dilakukan.

### Step 4 — Verify Evidence Completeness

Pastikan evidence yang diwajibkan oleh scope/risk tersedia dan dapat ditelusuri.

Contoh:

- Work Brief;
- requirement/compliance evidence;
- source verification evidence;
- originality/AI review record when applicable;
- escalation/decision record;
- final review notes.

Jangan membuat evidence setelah fakta tanpa dasar hanya untuk memenuhi checklist.

### Step 5 — Check Final File Integrity

Periksa:

- final filename/version;
- correct file type;
- document opens correctly;
- required pages/sections are present;
- tracked changes/comments are handled according to scope;
- no accidental placeholders or working artifacts remain;
- delivery package contains the intended files only.

### Step 6 — Apply Fail-Closed Final QC

Gunakan `MC-11`.

Jika terdapat critical unresolved finding, decision dependency, atau kondisi blocking lain sesuai scope/risk:

`BLOCK`

Kembalikan pekerjaan ke resolution path.

Jika semua required controls dan checks terpenuhi:

`APPROVED_FOR_DELIVERY`

### Step 7 — Record Final QC Decision

Catat minimal:

```text
Work item
Approved scope
Required checks
Resolution-state review
Evidence review
File/version check
Final QC decision
Reviewer
Date/time
```

### Step 8 — Prepare Delivery Package

Siapkan hanya output yang telah disetujui.

Sertakan catatan ketika relevan:

- ringkasan revisi;
- limitation/dependency yang telah diterima secara eksplisit;
- required next action.

Jangan menyampaikan unresolved issue sebagai resolved.

### Step 9 — Deliver

Delivery hanya dilakukan setelah:

`Final QC = APPROVED_FOR_DELIVERY`

Pastikan file/package yang dikirim sesuai dengan versi yang telah diperiksa.

### Step 10 — Archive Operational Evidence

Simpan minimum evidence yang diperlukan untuk traceability di production workspace yang sesuai.

Repository bukan default client-file storage.

Archive hanya informasi yang memang diperlukan untuk operasional, audit internal, atau future reference yang sah.

### Step 11 — Close the Work Item

Setelah delivery berhasil:

- update status work item;
- record delivery completion;
- confirm archive completed where required;
- retain unresolved client dependencies only in the appropriate tracked state.

## 5. Final QC Checklist

| Check | Result |
|---|---|
| Scope complete | PASS / REVIEW |
| Applicable requirements addressed | PASS / REVIEW |
| Required reviews completed | PASS / REVIEW |
| Findings/resolution states reviewed | PASS / BLOCK |
| Required evidence present | PASS / REVIEW |
| File/version integrity | PASS / BLOCK |
| Delivery package correct | PASS / BLOCK |
| Final QC decision recorded | YES / NO |

A single `BLOCK` condition prevents delivery.

## 6. Delivery Gate

Delivery is allowed only when:

```text
Approved scope
+
Required reviews complete
+
Blocking findings resolved
+
Required evidence recorded
+
Final file verified
+
Final QC = APPROVED_FOR_DELIVERY
```

Do not bypass a blocking state by changing labels or omitting the finding from the final record.

## 7. Archive Rules

Archive only operationally necessary evidence.

Minimum examples:

- final work identifier;
- final status;
- final QC decision;
- material decision/resolution records where required;
- delivery metadata.

Keep client files and sensitive personal data in the designated production workspace rather than the repository unless a documented exception is approved.

## 8. Outputs

Produce:

1. **Final QC Record**
2. **Approved Delivery Package** or **Blocked Status**
3. **Delivery Record** when delivered
4. **Operational Archive Record**
5. Updated finding/resolution status where applicable

## 9. Handoff / Closure

Successful closure requires:

```text
Final QC approved
        ↓
Delivery completed
        ↓
Operational evidence archived
        ↓
Work item closed
```

A blocked work item returns to the appropriate resolution path rather than closing.

## 10. Control Traceability

| Control | SOP Step | Evidence |
|---|---|---|
| MC-08 Resolution State | Steps 3, 7, 11 | Finding/resolution review + closure state |
| MC-10 External Processing Gate | Step 10 | Archive location decision consistent with data-processing constraints |
| MC-11 Fail-Closed Final QC | Steps 2–9 | Final QC record + approval/block + delivery record |

Normative control definitions remain in:

`../01_Workflows/Operating_Model.md`

Control specification remains in:

`../01_Workflows/Control_Matrix.md`

## 11. Change Control

Changes to this SOP that alter final approval, blocking behavior, required evidence, delivery conditions, or archive boundaries must be reviewed against `Operating_Model.md` and `Control_Matrix.md` before approval.
