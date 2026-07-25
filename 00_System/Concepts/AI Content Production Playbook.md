# AI Content Production Playbook (ACPP)

**Document ID** : ACPP-001  
**Version** : 1.0  
**Status** : Canonical  
**Owner** : AI Content Production System  
**Last Updated** : 26 July 2026  
**Document Type** : Production Playbook

---

# 1. Purpose

AI Content Production Playbook (ACPP) adalah panduan operasional yang menjelaskan bagaimana AI menghasilkan konten secara konsisten menggunakan sumber pengetahuan yang telah ditentukan.

ACPP mendefinisikan alur kerja produksi, mulai dari memahami permintaan pengguna hingga menghasilkan konten akhir yang memenuhi standar kualitas.

ACPP tidak menyimpan pengetahuan produksi. Pengetahuan tersebut dikelola melalui AI Content Knowledge Inventory (ACKI).

---

# 2. Overview

Produksi konten yang konsisten memerlukan lebih dari sekadar pengetahuan. AI juga harus mengetahui urutan kerja yang benar dalam menggunakan pengetahuan tersebut.

ACPP menyediakan workflow standar agar setiap proses produksi mengikuti langkah-langkah yang sama, sehingga hasil yang dihasilkan tetap konsisten, efisien, dan dapat direproduksi.

---

# 3. Production Workflow

Seluruh proses produksi mengikuti alur berikut.

```text
User Request
      │
      ▼
Understand Objective
      │
      ▼
Identify Required Knowledge
      │
      ▼
Load Knowledge Sources
      │
      ▼
Plan Content
      │
      ▼
Produce Content
      │
      ▼
Quality Review
      │
      ▼
Final Output
```

---

# 4. Production Stages

## Stage 1 — Understand Objective

AI mengidentifikasi tujuan utama permintaan pengguna.

Output:

- Tujuan konten
- Target audiens
- Platform
- Format
- Batasan khusus

---

## Stage 2 — Identify Required Knowledge

AI menentukan sumber pengetahuan yang diperlukan berdasarkan ACKI.

Contoh:

- Production Bible
- Brand Guideline
- Asset Library
- Caption Structure

Apabila diperlukan, AI juga memuat dokumen tambahan sesuai konteks.

---

## Stage 3 — Load Knowledge Sources

AI membaca sumber pengetahuan berdasarkan prioritas yang ditentukan dalam ACKI.

Prioritas:

1. Mandatory
2. Conditional
3. Optional

AI tidak memuat dokumen yang tidak relevan.

---

## Stage 4 — Plan Content

Sebelum menghasilkan konten, AI menyusun rencana produksi.

Rencana dapat mencakup:

- Struktur konten
- Pesan utama
- Visual
- CTA
- Caption
- Platform

Tahap ini belum menghasilkan konten akhir.

---

## Stage 5 — Produce Content

AI menghasilkan konten berdasarkan:

- tujuan pengguna
- Production Bible
- Brand Guideline
- seluruh sumber pengetahuan yang telah dimuat

Seluruh output harus mengikuti standar yang berlaku.

---

## Stage 6 — Quality Review

Sebelum memberikan hasil kepada pengguna, AI melakukan pemeriksaan terhadap:

- Konsistensi
- Akurasi
- Kepatuhan terhadap Brand Guideline
- Kepatuhan terhadap Production Bible
- Kelengkapan
- Keterbacaan
- Kesesuaian platform

Jika ditemukan ketidaksesuaian, AI melakukan revisi sebelum menghasilkan output akhir.

---

## Stage 7 — Final Output

AI memberikan hasil akhir yang siap digunakan pengguna.

Output harus merupakan hasil terbaik berdasarkan seluruh sumber pengetahuan yang tersedia.

---

# 5. Production Principles

Seluruh proses produksi mengikuti prinsip berikut.

## User-Centered

Produksi selalu berorientasi pada kebutuhan pengguna.

---

## Knowledge-Driven

Seluruh keputusan produksi didasarkan pada sumber pengetahuan yang tersedia.

---

## Consistency

Output harus konsisten terhadap:

- Brand
- Visual
- Editorial
- Struktur
- Terminologi

---

## Efficiency

AI hanya menggunakan pengetahuan yang relevan.

---

## Quality First

Kualitas lebih diutamakan daripada kecepatan.

---

# 6. Relationship with ACKI

ACKI dan ACPP saling melengkapi.

| Component | Responsibility |
|-----------|----------------|
| **ACKI** | Menentukan pengetahuan yang tersedia bagi AI. |
| **ACPP** | Menentukan bagaimana AI menggunakan pengetahuan tersebut. |

ACKI menyediakan **Knowledge Manifest**.

ACPP menyediakan **Production Workflow**.

---

# 7. Version History

| Version | Date | Summary |
|----------|------|---------|
| 1.0 | 26 July 2026 | Initial canonical release. |

---

# Core Principle

> **Consistent content is produced through a consistent production process.**

---

# Design Principles

ACPP dibangun berdasarkan prinsip-prinsip berikut.

- **Workflow-first** — Seluruh produksi mengikuti alur kerja yang terstandarisasi.
- **Knowledge-driven** — Setiap keputusan produksi didasarkan pada sumber pengetahuan yang relevan.
- **Context-aware** — AI hanya memuat pengetahuan yang diperlukan.
- **Quality-first** — Seluruh output harus melalui proses pemeriksaan kualitas.
- **Reusable** — Workflow dapat diterapkan pada berbagai brand, platform, dan jenis konten.

---

# Compliance

Seluruh proses produksi konten AI harus mengikuti workflow yang ditetapkan dalam ACPP.

Perubahan terhadap workflow dilakukan melalui versioning sehingga seluruh produksi tetap menggunakan prosedur yang terdokumentasi dan konsisten.

ACPP menjadi referensi operasional kanonik bagi AI dalam menjalankan proses produksi konten.
