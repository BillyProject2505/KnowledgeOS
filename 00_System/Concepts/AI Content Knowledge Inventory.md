# AI Content Knowledge Inventory (ACKI)

**Document ID** : ACKI-001  
**Version** : 1.0  
**Status** : Canonical  
**Owner** : AI Content Production System  
**Last Updated** : 26 July 2026  
**Document Type** : Knowledge Manifest

---

# 1. Purpose

AI Content Knowledge Inventory (ACKI) adalah **manifest pengetahuan resmi** yang mendefinisikan seluruh sumber pengetahuan yang harus tersedia bagi AI sebelum menghasilkan konten.

ACKI tidak menyimpan isi pengetahuan tersebut. Sebaliknya, ACKI berfungsi sebagai peta (Knowledge Manifest) yang mengarahkan AI menuju sumber pengetahuan yang tepat sesuai kebutuhan produksi.

ACKI menjadi **entry point** bagi AI untuk membangun kembali konteks produksi konten secara konsisten, baik pada sesi ChatGPT baru maupun implementasi AI lainnya.

---

# 2. Overview

Produksi konten yang konsisten memerlukan lebih dari sekadar prompt. AI harus mengetahui dokumen apa yang tersedia, dokumen mana yang wajib digunakan, serta hubungan antar dokumen dalam ekosistem produksi.

ACKI menyediakan struktur tersebut melalui inventarisasi seluruh sumber pengetahuan yang digunakan AI. Dengan demikian, setiap proses produksi dapat dimulai dari fondasi pengetahuan yang sama.

ACKI tidak menggantikan Production Bible, Brand Guideline, maupun dokumen operasional lainnya. ACKI hanya mengarahkan AI ke dokumen-dokumen tersebut.

---

# 3. Knowledge Categories

Seluruh sumber pengetahuan dikelompokkan ke dalam kategori operasional berikut.

## 3.1 Core Knowledge

Pengetahuan utama yang menjadi fondasi hampir seluruh proses produksi konten.

Contoh:

- Production Bible
- Brand Guideline
- Asset Library
- Caption Structure

---

## 3.2 Editorial Knowledge

Pengetahuan yang mengatur gaya komunikasi dan penulisan.

Contoh:

- Editorial Guideline
- Tone of Voice
- CTA Guideline
- Hashtag Guideline

---

## 3.3 Design Knowledge

Pengetahuan yang mengatur aspek visual.

Contoh:

- Layout System
- Typography Guide
- Color System
- Component Library
- Icon Library
- Illustration Guide

---

## 3.4 Platform Knowledge

Pengetahuan yang berkaitan dengan platform publikasi.

Contoh:

- Instagram Guideline
- TikTok Guideline
- Facebook Guideline
- Website Guideline

---

## 3.5 Content Knowledge

Pengetahuan substantif yang menjadi bahan utama pembuatan konten.

Contoh:

- Topic Library
- FAQ Library
- Myth vs Fact Library
- Reference Library
- Glossary

---

## 3.6 Quality Knowledge

Pengetahuan yang digunakan untuk mengevaluasi hasil produksi.

Contoh:

- Quality Checklist
- Compliance Guide
- Accessibility Guide

---

# 4. Knowledge Registry

Knowledge Registry merupakan daftar resmi seluruh sumber pengetahuan yang digunakan AI.

| ID | Knowledge Source | Category | Status | Required |
|----|------------------|----------|--------|----------|
| K001 | Production Bible | Core Knowledge | Active | Yes |
| K002 | Brand Guideline | Core Knowledge | Active | Yes |
| K003 | Asset Library | Core Knowledge | Active | Yes |
| K004 | Caption Structure | Core Knowledge | Active | Yes |

Dokumen baru ditambahkan ke registry ketika telah disetujui sebagai bagian dari sistem produksi.

ACKI hanya mereferensikan keberadaan dokumen dan tidak menggandakan isinya.

---

# 5. Loading Priority

Tidak seluruh pengetahuan harus dimuat dalam setiap proses produksi. Oleh karena itu, ACKI menetapkan tiga tingkat prioritas.

## 5.1 Mandatory

Dokumen yang selalu dimuat sebelum AI memulai produksi.

Contoh:

- Production Bible
- Brand Guideline
- Asset Library
- Caption Structure

---

## 5.2 Conditional

Dokumen yang dimuat apabila relevan dengan permintaan pengguna.

Contoh:

- Instagram Guideline
- TikTok Guideline
- Character Bible
- World Bible

---

## 5.3 Optional

Dokumen yang hanya dimuat apabila diperlukan secara khusus.

Contoh:

- Research Library
- Archive
- Historical Content
- Supporting References

---

# 6. Dependencies

ACKI mendokumentasikan hubungan antar sumber pengetahuan untuk membantu AI memahami konteks tanpa menggandakan isi dokumen.

Contoh:

```text
Production Bible
│
├── Brand Guideline
├── Asset Library
├── Caption Structure
└── Quality Checklist
```

Model dependency akan diperluas seiring bertambahnya dokumen dalam sistem.

---

# 7. Version History

| Version | Date | Summary |
|----------|------|---------|
| 1.0 | 26 July 2026 | Initial canonical release. |

---

# Core Principle

> **ACKI does not store knowledge. ACKI directs AI to the right knowledge.**

---

# Design Principles

ACKI dibangun berdasarkan prinsip-prinsip berikut:

- **Single Manifest** — Satu dokumen sebagai pintu masuk utama seluruh sumber pengetahuan AI.
- **Knowledge-first** — Mengidentifikasi kebutuhan pengetahuan sebelum membangun struktur repository.
- **Non-duplicative** — Tidak menduplikasi isi dokumen lain.
- **Operational** — Hanya mencatat pengetahuan yang benar-benar digunakan dalam produksi.
- **Versioned** — Berkembang melalui versioning tanpa dipecah menjadi banyak dokumen.

---

# Relationship with ACPP

ACKI dan AI Content Production Playbook (ACPP) memiliki tanggung jawab yang berbeda namun saling melengkapi.

| Component | Responsibility |
|-----------|----------------|
| **ACKI** | Menentukan pengetahuan yang harus tersedia bagi AI. |
| **ACPP** | Menentukan bagaimana AI menggunakan pengetahuan tersebut selama proses produksi. |

ACKI menyediakan **Knowledge Manifest**, sedangkan ACPP menyediakan **Execution Workflow**.

---

# Compliance

Seluruh dokumen yang menjadi prasyarat bagi AI dalam menghasilkan konten harus terdaftar di dalam ACKI.

Setiap penambahan, perubahan, atau penghapusan sumber pengetahuan harus tercermin pada versi ACKI berikutnya.

ACKI menjadi referensi kanonik bagi AI untuk membangun konteks produksi konten secara konsisten pada setiap sesi baru.
