# Content Production Framework (CPF)

**Document ID:** CPF-001
**Version:** 2.0
**Status:** LOCK
**Category:** Framework
**Owner:** Knowledge Architecture
**Applies To:** Seluruh Production Architecture

---

# 1. Purpose

Content Production Framework (CPF) mendefinisikan arsitektur Production Architecture yang menghubungkan Reusable Canonical Knowledge dengan proses produksi melalui Production Workflow.

CPF menjelaskan hubungan antar komponen Production Architecture, pembagian tanggung jawab setiap komponen, serta bagaimana Execution Engine menerapkan Canonical Knowledge untuk menghasilkan Production Output.

CPF tidak mendefinisikan workflow operasional maupun prosedur quality review secara rinci.

---

# 2. Scope

Framework ini berlaku untuk seluruh Production Architecture yang digunakan oleh Execution Engine dalam menghasilkan Production Output.

CPF bersifat project-independent dan dapat digunakan kembali oleh seluruh proyek.

---

# 3. Core Philosophy

Seluruh Production Architecture mengikuti prinsip berikut.

## CPF-P01 — Knowledge First

Seluruh keputusan produksi harus didasarkan pada Canonical Knowledge yang telah terdokumentasi.

---

## CPF-P02 — Reusable by Default

Canonical Knowledge diutamakan agar dapat digunakan kembali oleh lebih dari satu proyek.

---

## CPF-P03 — Single Source of Truth

Seluruh komponen Production Architecture harus mengacu pada Canonical Knowledge sebagai satu-satunya sumber pengetahuan resmi.

---

## CPF-P04 — Project Independence

Framework bersifat umum dan tidak bergantung pada identitas suatu proyek.

---

## CPF-P05 — AI as Execution Engine

Execution Engine menerapkan Canonical Knowledge untuk menjalankan Production Workflow.

Execution Engine bukan pembuat kebijakan maupun sumber Canonical Knowledge.

---

# 4. Production Architecture

Production Architecture mengikuti hubungan berikut.

```text
User Request
        │
        ▼
Production Planning
        │
        ▼
Reusable Canonical Knowledge
        │
        ▼
Project-Specific Canonical Knowledge
        │
        ▼
Production Workflow
        │
        ▼
Quality Review
        │
        ▼
Approved Production Output
```

Setiap komponen memiliki tanggung jawab yang berbeda dan tidak saling menggantikan.

---

# 5. Production Architecture Layers

```text
Knowledge Architecture
        │
        ▼
Reusable Canonical Knowledge
        │
        ▼
Production Architecture
        │
        ├── Production Workflow Standard (PWS)
        ├── Production Bible Standard (PBS)
        └── Quality Gate Standard (QGS)
        │
        ▼
Production Output
```

Knowledge Architecture menyediakan Canonical Knowledge.

Production Architecture menerapkan Canonical Knowledge menjadi Production Output.

---

# 6. Production Workflow

Workflow operasional produksi didefinisikan oleh Production Workflow Standard (PWS).

CPF hanya mendefinisikan hubungan konseptual antar komponen Production Architecture.

---

# 7. Component Responsibilities

| Component | Responsibility |
|-----------|----------------|
| Principles | Filosofi dasar |
| Frameworks | Arsitektur konseptual |
| Standards | Aturan operasional |
| Production Workflow Standard (PWS) | Workflow produksi |
| Production Bible Standard (PBS) | Project-Specific Canonical Knowledge |
| Quality Gate Standard (QGS) | Evaluasi Production Output |
| Execution Engine | Menerapkan Canonical Knowledge |
| Human | Review, validasi, dan persetujuan akhir |

---

# 8. Quality Review

Quality Review dilaksanakan sesuai Quality Gate Standard (QGS).

CPF tidak mendefinisikan Quality Gates maupun prosedur evaluasi secara rinci.

---

# 9. Relationship

```text
Knowledge Architecture
        │
        ▼
Reusable Canonical Knowledge
        │
        ▼
Content Production Framework
        │
        ├── Production Workflow Standard
        ├── Production Bible Standard
        └── Quality Gate Standard
        │
        ▼
Production Output
```

CPF menjadi framework induk yang menghubungkan seluruh komponen Production Architecture.

---

# 10. Governance

Perubahan terhadap CPF harus memenuhi ketentuan berikut.

- Selaras dengan Principles.
- Konsisten dengan Knowledge Architecture.
- Tidak mendefinisikan workflow operasional.
- Tidak mendefinisikan prosedur quality review.
- Mempertahankan sifat project-independent.
- Melalui proses review sebelum memperoleh status LOCK.

---

# Canonical Decision

Content Production Framework (CPF) merupakan framework induk Production Architecture yang mendefinisikan hubungan antara Reusable Canonical Knowledge, Project-Specific Canonical Knowledge, Production Workflow, Quality Review, dan Production Output.

CPF tidak mendefinisikan prosedur operasional maupun quality review secara rinci, melainkan menjadi kerangka konseptual yang menghubungkan seluruh komponen Production Architecture sehingga membentuk sistem produksi yang konsisten, dapat digunakan kembali, dan independen terhadap proyek maupun Execution Engine.
