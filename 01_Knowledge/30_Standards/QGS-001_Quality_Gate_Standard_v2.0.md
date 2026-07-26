# Quality Gate Standard (QGS)

**Document ID:** QGS-001
**Version:** 2.0
**Status:** LOCK
**Category:** Standard
**Owner:** Knowledge Architecture
**Applies To:** Seluruh Production Output

---

# 1. Purpose

Quality Gate Standard (QGS) menetapkan mekanisme evaluasi kualitas terhadap Production Output sebelum memperoleh persetujuan dalam Production Workflow.

QGS memastikan setiap Production Output memenuhi Canonical Knowledge, Production Bible, serta standar kualitas yang berlaku sebelum disetujui dan dipublikasikan.

QGS mengevaluasi Production Output, bukan proses pembentukan Canonical Knowledge.

---

# 2. Scope

Standar ini berlaku untuk seluruh Production Output yang dihasilkan melalui Production Workflow.

Contoh:

- Carousel
- Reel
- Poster
- Komik
- Artikel
- Presentasi
- Caption
- Dokumen
- Prompt
- Output produksi lainnya

---

# 3. Quality Principles

## QGS-P01 — Quality Before Completion

Production Output dianggap selesai hanya setelah melewati seluruh Quality Gate yang berlaku.

---

## QGS-P02 — Objective Evaluation

Setiap Quality Gate memiliki kriteria yang jelas, konsisten, dan dapat diverifikasi.

---

## QGS-P03 — Risk-Based Review

Quality Gate diterapkan sesuai tingkat risiko dan karakteristik Production Output.

---

## QGS-P04 — Traceable Decisions

Seluruh keputusan review harus terdokumentasi dan dapat ditelusuri.

---

## QGS-P05 — Consistent Quality

Seluruh Production Output harus memenuhi standar kualitas yang konsisten di seluruh proyek.

---

# 4. Quality Gate Lifecycle

## PASS Flow

```text
Draft Production Output
        │
        ▼
Quality Gates
        │
        ▼
PASS
        │
        ▼
Approval
        │
        ▼
Publication
```

## FAIL Flow

```text
Draft Production Output
        │
        ▼
Quality Gates
        │
        ▼
FAIL
        │
        ▼
Revision
        │
        ▼
Quality Gates
```

---

# 5. Standard Quality Gates

## QG-01 — Knowledge Gate

### Objective

Memastikan Production Output menggunakan Canonical Knowledge yang benar.

### Reusable Canonical Knowledge Check

- Framework sesuai
- Standard sesuai
- Registry sesuai
- Template sesuai
- Reference sesuai

### Project-Specific Canonical Knowledge Check

- Production Bible sesuai
- Tidak bertentangan dengan aturan proyek

---

## QG-02 — Structure Gate

### Objective

Memastikan struktur output mengikuti standar yang berlaku.

### Checklist

- Mengikuti DTS
- Metadata lengkap (apabila relevan)
- Struktur konsisten
- Format benar

---

## QG-03 — Consistency Gate

### Objective

Memastikan konsistensi terhadap Canonical Knowledge.

### Checklist

- Terminologi konsisten
- Tidak bertentangan dengan Canonical Knowledge
- Konsisten dengan dokumen terkait

---

## QG-04 — Brand Gate

### Objective

Memastikan identitas proyek diterapkan dengan benar.

### Checklist

- Production Bible diterapkan
- Identitas visual sesuai
- Tone sesuai
- Branding sesuai

---

## QG-05 — Editorial Gate

### Objective

Memastikan kualitas komunikasi.

### Checklist

- Tata bahasa benar
- Mudah dipahami
- Tidak ambigu
- Istilah konsisten

---

## QG-06 — Technical Gate

### Objective

Memastikan aspek teknis telah memenuhi standar.

### Checklist

- Penamaan sesuai DNS
- Versioning sesuai VS
- Format file benar
- Berkas lengkap

---

## QG-07 — Output Gate

### Objective

Memastikan Production Output siap digunakan.

### Checklist

- Tujuan tercapai
- Deliverables lengkap
- Siap dipublikasikan
- Tidak terdapat blocker

---

# 6. Mandatory and Conditional Gates

## Mandatory Gates

Seluruh Production Output wajib melewati:

- Knowledge Gate
- Structure Gate
- Consistency Gate
- Technical Gate
- Output Gate

---

## Conditional Gates

Gate berikut diterapkan apabila relevan:

- Brand Gate
- Editorial Gate

---

# 7. Quality Gate Matrix

| Production Output | Required Gates |
|-------------------|----------------|
| Framework | QG-01, QG-02, QG-03, QG-06, QG-07 |
| Standard | QG-01, QG-02, QG-03, QG-06, QG-07 |
| Bible | QG-01, QG-02, QG-03, QG-04, QG-05, QG-06, QG-07 |
| Registry | QG-01, QG-02, QG-03, QG-06, QG-07 |
| Template | QG-02, QG-03, QG-06, QG-07 |
| Prompt | QG-01, QG-05, QG-06, QG-07 |
| Production Output | QG-01, QG-04, QG-05, QG-06, QG-07 |

---

# 8. Gate Outcomes

| Result | Meaning |
|---------|---------|
| PASS | Memenuhi seluruh kriteria |
| CONDITIONAL PASS | Memenuhi kriteria utama dengan catatan minor |
| FAIL | Tidak memenuhi kriteria dan wajib direvisi |

---

# 9. Review Record

Setiap proses review wajib menghasilkan Review Record.

Contoh:

```text
Reviewer:
Date:
Output:

Knowledge Gate ........ PASS
Structure Gate ........ PASS
Consistency Gate ...... PASS
Brand Gate ............ PASS
Editorial Gate ........ PASS
Technical Gate ........ PASS
Output Gate ........... PASS

Final Decision:
PASS
```

Review Record menjadi bukti pelaksanaan Quality Review.

---

# 10. Relationship

```text
Reusable Canonical Knowledge
                │
                ▼
Project-Specific Canonical Knowledge
        (Production Bible)
                │
                ▼
Production Workflow
                │
                ▼
Quality Gate Standard
                │
                ▼
Approved Production Output
```

QGS digunakan pada tahap Quality Review dalam Production Workflow sebelum Production Output memperoleh Approval.

---

# 11. Governance

Seluruh Production Output wajib:

- melewati Mandatory Gates;
- menerapkan Conditional Gates apabila relevan;
- memiliki Review Record;
- memperoleh status PASS atau CONDITIONAL PASS sebelum Approval.

Perubahan terhadap Quality Gate hanya dapat dilakukan melalui revisi resmi Quality Gate Standard.

---

# Canonical Decision

Quality Gate Standard (QGS) merupakan standar resmi evaluasi kualitas Production Output dalam Production Architecture.

QGS memastikan setiap Production Output memenuhi Reusable Canonical Knowledge, Project-Specific Canonical Knowledge (Production Bible), serta standar kualitas yang berlaku sebelum memperoleh persetujuan dan dipublikasikan.
