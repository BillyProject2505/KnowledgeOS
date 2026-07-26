# Content Production Framework (CPF)

**Document ID:** CPF-001  
**Version:** 1.0  
**Status:** LOCK  
**Category:** Framework  
**Owner:** KnowledgeOS  
**Applies To:** Seluruh proyek produksi konten dalam KnowledgeOS

---

# 1. Purpose

Content Production Framework (CPF) mendefinisikan arsitektur produksi konten yang digunakan oleh seluruh proyek dalam KnowledgeOS.

CPF menjelaskan bagaimana pengetahuan diorganisasi, bagaimana setiap komponen saling berinteraksi, serta bagaimana proses produksi berlangsung dari permintaan awal hingga publikasi akhir.

CPF tidak mendefinisikan aturan desain, branding, editorial, ataupun gaya visual. Aturan tersebut dikelola oleh dokumen lain sesuai tanggung jawabnya.

---

# 2. Scope

Framework ini berlaku untuk seluruh proyek produksi konten yang dikelola melalui KnowledgeOS, termasuk namun tidak terbatas pada:

- Coz We Care
- KDS
- OBK
- Personal Brand
- Proyek-proyek baru di masa depan

CPF bersifat **project-independent** dan dapat digunakan kembali oleh seluruh proyek.

---

# 3. Core Philosophy

Seluruh proses produksi mengikuti lima prinsip utama.

## CPF-P01 — Knowledge First

Seluruh keputusan produksi harus didasarkan pada pengetahuan yang terdokumentasi.

## CPF-P02 — Reusable by Default

Pengetahuan harus dapat digunakan kembali oleh lebih dari satu proyek.

## CPF-P03 — Single Source of Truth

Setiap informasi hanya memiliki satu sumber kanonis.

## CPF-P04 — Project Independence

Framework bersifat umum dan tidak bergantung pada identitas suatu proyek.

## CPF-P05 — AI as Executor

AI menjalankan proses produksi berdasarkan pengetahuan yang telah ditetapkan. AI bukan sumber kebenaran maupun pembuat kebijakan.

---

# 4. Production Architecture

Seluruh produksi konten mengikuti arsitektur berikut.

```text
User Request
        │
        ▼
Content Objective
        │
        ▼
Knowledge Discovery
        │
        ▼
Framework Selection
        │
        ▼
Applicable Standards
        │
        ▼
Project Bible
        │
        ▼
Templates
        │
        ▼
Prompts
        │
        ▼
AI Execution
        │
        ▼
Quality Gates
        │
        ▼
Final Content
```

Setiap lapisan memiliki tanggung jawab yang berbeda dan tidak saling menggantikan.

---

# 5. Knowledge Layers

KnowledgeOS menggunakan hirarki pengetahuan berikut.

```text
Principles
      │
      ▼
Frameworks
      │
      ▼
Standards
      │
      ▼
Bibles
      │
      ▼
Registries
      │
      ▼
Templates
      │
      ▼
Prompts
      │
      ▼
Projects
```

Setiap lapisan hanya bergantung pada lapisan di atasnya.

---

# 6. Production Lifecycle

Seluruh produksi konten mengikuti siklus berikut.

```text
Request
    ↓
Classify
    ↓
Research
    ↓
Plan
    ↓
Produce
    ↓
Review
    ↓
Approve
    ↓
Publish
    ↓
Archive
    ↓
Learn
```

Tahap **Learn** memastikan hasil produksi menjadi masukan untuk penyempurnaan KnowledgeOS.

---

# 7. Component Responsibilities

| Component | Responsibility |
|-----------|----------------|
| Principles | Filosofi dasar |
| Frameworks | Arsitektur sistem |
| Standards | Aturan operasional |
| Bibles | Pengetahuan proyek |
| Registries | Referensi terstruktur |
| Templates | Struktur dokumen |
| Prompts | Instruksi eksekusi AI |
| AI | Menghasilkan output sesuai pengetahuan |
| Human | Review, validasi, dan persetujuan akhir |

---

# 8. Quality Gates

Setiap produksi harus melewati Quality Gate yang relevan.

- Knowledge Gate
- Structure Gate
- Consistency Gate
- Brand Gate
- Editorial Gate
- Visual Gate
- Output Gate

Konten hanya dapat dipublikasikan apabila seluruh gate yang berlaku telah terpenuhi.

---

# 9. Relationship

Hubungan antar komponen KnowledgeOS digambarkan sebagai berikut.

```text
Knowledge Principles
          │
          ▼
Content Production Framework
          │
          ├──────────────┐
          ▼              ▼
Standards          Production Bibles
          │              │
          └──────┬───────┘
                 ▼
             Templates
                 ▼
              Prompts
                 ▼
            AI Production
```

CPF berfungsi sebagai penghubung antara fondasi pengetahuan dan implementasi produksi.

---

# 10. Governance

Perubahan terhadap CPF harus memenuhi ketentuan berikut.

- Selaras dengan Principles.
- Tidak bertentangan dengan Standards.
- Mempertahankan kompatibilitas dengan Production Bibles.
- Mendukung penggunaan kembali lintas proyek.
- Melalui proses review sebelum memperoleh status LOCK.

---

# Canonical Decision

Content Production Framework (CPF) merupakan framework induk yang menjelaskan arsitektur produksi konten dalam KnowledgeOS.

CPF tidak menggantikan Standards, Bibles, Templates, Registries, maupun Prompts. CPF mengatur hubungan, alur, dan tanggung jawab seluruh komponen tersebut sehingga membentuk satu sistem produksi konten yang konsisten, dapat digunakan kembali, dan bersifat project-independent.
