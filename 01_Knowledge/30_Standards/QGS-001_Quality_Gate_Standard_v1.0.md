# Quality Gate Standard (QGS)

**Document ID:** QGS-001  
**Version:** 1.0  
**Status:** LOCK  
**Category:** Standard  
**Owner:** KnowledgeOS  
**Applies To:** Seluruh output yang dihasilkan melalui KnowledgeOS

---

# 1. Purpose

Quality Gate Standard (QGS) mendefinisikan mekanisme evaluasi kualitas yang diterapkan oleh execution engine sebelum suatu output dinyatakan selesai dan dapat disetujui atau dipublikasikan.

Standar ini menyediakan kriteria evaluasi yang konsisten, terdokumentasi, dan dapat diaudit.

QGS memastikan bahwa setiap hasil produksi memenuhi standar KnowledgeOS secara konsisten, terdokumentasi, dan dapat diaudit.

---

# 2. Scope

Standar ini berlaku untuk seluruh output yang dihasilkan melalui KnowledgeOS, termasuk namun tidak terbatas pada:

- Dokumen knowledge
- Konten media sosial
- Desain visual
- Komik
- Presentasi
- Artikel
- Prompt
- Template
- Production Bible
- Output lainnya

---

# 3. Quality Principles

## QGS-P01 — Quality Before Completion

Pekerjaan dianggap selesai hanya setelah melewati seluruh Quality Gate yang berlaku.

---

## QGS-P02 — Objective Evaluation

Setiap Quality Gate memiliki kriteria yang jelas dan dapat diverifikasi.

---

## QGS-P03 — Risk-Based Review

Quality Gate diterapkan berdasarkan tingkat risiko dan jenis output.

---

## QGS-P04 — Traceable Decisions

Keputusan lulus atau tidak lulus harus terdokumentasi dan dapat ditelusuri.

---

## QGS-P05 — Continuous Improvement

Temuan selama proses review menjadi masukan untuk penyempurnaan KnowledgeOS.

---

# 4. Quality Gate Lifecycle

```text
Draft
   │
   ▼
Quality Gates
   │
   ├── PASS
   │      │
   │      ▼
   │   Approval
   │
   └── FAIL
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

Memastikan knowledge yang digunakan benar, lengkap, dan relevan.

### Checklist

- Framework sesuai
- Standard sesuai
- Bible sesuai
- Reference tersedia
- Fakta tervalidasi

---

## QG-02 — Structure Gate

### Objective

Memastikan struktur output mengikuti standar dokumentasi.

### Checklist

- Mengikuti DTS
- Heading benar
- Metadata lengkap
- Format konsisten

---

## QG-03 — Consistency Gate

### Objective

Memastikan konsistensi dengan KnowledgeOS.

### Checklist

- Terminologi konsisten
- Struktur konsisten
- Selaras dengan dokumen terkait
- Tidak ada konflik dengan dokumen kanonis

---

## QG-04 — Brand Gate

### Objective

Memastikan kesesuaian dengan identitas proyek.

### Checklist

- Production Bible diikuti
- Logo benar
- Warna benar
- Tone sesuai
- Visual sesuai

---

## QG-05 — Editorial Gate

### Objective

Memastikan kualitas komunikasi.

### Checklist

- Tata bahasa benar
- Kalimat jelas
- Mudah dipahami
- Tidak ambigu
- Istilah konsisten

---

## QG-06 — Technical Gate

### Objective

Memastikan aspek teknis telah memenuhi standar.

### Checklist

- Format file benar
- Penamaan sesuai DNS
- Versi sesuai VS
- Link valid
- Berkas lengkap

---

## QG-07 — Output Gate

### Objective

Memastikan output siap digunakan.

### Checklist

- Tujuan tercapai
- Deliverables lengkap
- Tidak ada blocker
- Siap dipublikasikan atau digunakan

---

# 6. Mandatory and Conditional Gates

## Mandatory Gates

Gate berikut wajib diterapkan sesuai matriks yang berlaku:

- Knowledge Gate
- Structure Gate
- Consistency Gate
- Technical Gate
- Output Gate

## Conditional Gates

Gate berikut diterapkan apabila relevan dengan jenis output:

- Brand Gate
- Editorial Gate

---

# 7. Quality Gate Matrix

| Output | Required Gates |
|---------|----------------|
| Framework | QG-01, QG-02, QG-03, QG-06, QG-07 |
| Standard | QG-01, QG-02, QG-03, QG-06, QG-07 |
| Bible | QG-01, QG-02, QG-03, QG-04, QG-05, QG-06, QG-07 |
| Registry | QG-01, QG-02, QG-03, QG-06, QG-07 |
| Template | QG-02, QG-03, QG-06, QG-07 |
| Prompt | QG-01, QG-05, QG-06, QG-07 |
| Visual Content | QG-01, QG-04, QG-05, QG-06, QG-07 |

---

# 8. Gate Outcomes

| Result | Meaning |
|---------|---------|
| PASS | Memenuhi seluruh kriteria |
| CONDITIONAL PASS | Memenuhi kriteria utama, terdapat catatan minor yang tidak menghalangi penggunaan |
| FAIL | Tidak memenuhi kriteria dan wajib direvisi |

---

# 9. Review Record

Setiap proses review harus menghasilkan Review Record.

Contoh:

```text
Reviewer:
Date:
Output:
Applicable Gates:

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

Review Record menjadi bukti pelaksanaan Quality Assurance.

---

# 10. Relationship

```text
Production Workflow Standard
            │
            ▼
Quality Gate Standard
            │
            ▼
Review Stage
            │
            ▼
Approval
```

QGS menjadi standar resmi yang digunakan pada tahap Review dalam Production Workflow Standard.

---

# 11. Governance

Seluruh output yang diproduksi melalui KnowledgeOS:

- wajib melewati seluruh Quality Gate yang relevan;
- tidak boleh melewati Mandatory Gate tanpa alasan yang terdokumentasi;
- wajib memiliki Review Record;
- hanya dapat memasuki tahap Approval apabila seluruh Mandatory Gate berstatus PASS atau CONDITIONAL PASS sesuai kebijakan yang berlaku.

Quality Gate diterapkan oleh execution engine selama tahap Review sebagaimana didefinisikan dalam Production Workflow Standard. KnowledgeOS berfungsi sebagai sumber standar evaluasi dan tidak melakukan proses review secara langsung.
---

# Canonical Decision

Quality Gate Standard (QGS) merupakan standar resmi evaluasi kualitas dalam KnowledgeOS.

Seluruh output wajib melalui Quality Gate yang sesuai dengan jenisnya sebelum disetujui atau dipublikasikan. Dengan penerapan Mandatory Gates, Conditional Gates, Review Record, dan evaluasi berbasis risiko, QGS memastikan seluruh output KnowledgeOS memiliki kualitas yang konsisten, dapat diaudit, dan mendukung prinsip Single Source of Truth.
