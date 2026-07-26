# Knowledge Classification Framework (KCF)

**Document ID:** KCF-001  
**Version:** 2.1  
**Status:** LOCK  
**Category:** Framework  
**Owner:** Knowledge Architecture  
**Applies To:** Seluruh Knowledge Architecture

---

# 1. Purpose

Knowledge Classification Framework (KCF) mendefinisikan sistem klasifikasi resmi yang digunakan untuk mengidentifikasi, mengelompokkan, dan membedakan seluruh Canonical Document dalam Knowledge Architecture.

Framework ini memastikan bahwa setiap Canonical Document memiliki tujuan yang jelas, tanggung jawab yang tidak tumpang tindih, serta posisi yang konsisten dalam keseluruhan arsitektur pengetahuan.

---

# 2. Scope

KCF berlaku untuk seluruh Canonical Document yang menjadi bagian dari Knowledge Architecture.

Framework ini mengatur:

- Document Type
- Tujuan setiap Document Type
- Kriteria pemilihan Document Type
- Hubungan antar Document Type

KCF tidak mengatur struktur internal dokumen maupun metadata. Ketentuan tersebut didefinisikan oleh Document Template Standard (DTS) dan Knowledge Catalog Registry Standard (KCRS).

---

# 3. Classification Principles

Seluruh klasifikasi Canonical Document harus mematuhi prinsip berikut:

- **Single Responsibility** — Setiap Document Type memiliki satu tujuan utama.
- **Mutually Exclusive** — Sebuah Canonical Document hanya memiliki satu Document Type utama.
- **Collectively Exhaustive** — Seluruh kebutuhan dokumentasi harus dapat dipetakan ke salah satu Document Type resmi.
- **Canonical Consistency** — Penggunaan Document Type harus konsisten di seluruh Knowledge Architecture.
- **Technology Independent** — Klasifikasi tidak bergantung pada platform atau teknologi tertentu.

---

# 4. Official Document Types

Knowledge Architecture mengenal Document Type resmi berikut.

| Document Type | Purpose |
|---------------|---------|
| **Architecture Overview** | Menjelaskan struktur, ruang lingkup, hubungan, dan batas suatu arsitektur tanpa mendefinisikan aturan operasional baru. |
| **Principle** | Menetapkan prinsip fundamental yang menjadi dasar seluruh keputusan arsitektur. |
| **Framework** | Menyediakan model konseptual untuk mengorganisasi suatu domain. |
| **Standard** | Menetapkan aturan normatif yang wajib dipatuhi. |
| **Bible** | Mendokumentasikan pengetahuan kanonis suatu domain secara komprehensif. |
| **Registry** | Menyimpan inventaris atau metadata kanonis. |
| **Template** | Menyediakan struktur baku untuk penyusunan artefak. |
| **Prompt** | Mendefinisikan instruksi standar bagi AI atau proses otomatis. |
| **Reference** | Menyediakan informasi pendukung yang tidak bersifat normatif. |
| **Decision** | Mendokumentasikan keputusan arsitektural beserta alasan dan implikasinya. |

---

# 5. Document Type Selection Guide

Gunakan pertanyaan berikut untuk menentukan Document Type yang tepat.

```text
Apakah tujuan dokumen adalah menjelaskan keseluruhan arsitektur?
        │
       Ya
        ▼
Architecture Overview
        │
      Tidak
        ▼
Apakah mendefinisikan prinsip fundamental?
        │
       Ya
        ▼
Principle
        │
      Tidak
        ▼
Apakah menyediakan model konseptual?
        │
       Ya
        ▼
Framework
        │
      Tidak
        ▼
Apakah menetapkan aturan normatif?
        │
       Ya
        ▼
Standard
        │
      Tidak
        ▼
Apakah mendokumentasikan pengetahuan domain secara lengkap?
        │
       Ya
        ▼
Bible
        │
      Tidak
        ▼
Apakah menyimpan inventaris atau metadata?
        │
       Ya
        ▼
Registry
        │
      Tidak
        ▼
Apakah menyediakan struktur baku?
        │
       Ya
        ▼
Template
        │
      Tidak
        ▼
Apakah berisi instruksi AI?
        │
       Ya
        ▼
Prompt
        │
      Tidak
        ▼
Apakah hanya informasi pendukung?
        │
       Ya
        ▼
Reference
        │
      Tidak
        ▼
Decision
```

---

# 6. Usage Rules

## Architecture Overview

Digunakan hanya untuk:

- menjelaskan keseluruhan struktur arsitektur;
- menjelaskan hubungan antar komponen;
- mendefinisikan ruang lingkup arsitektur;
- mendefinisikan batas (boundary) arsitektur.

Tidak boleh digunakan untuk:

- menetapkan aturan normatif;
- menggantikan Standard;
- menggantikan Framework;
- mendokumentasikan pengetahuan domain seperti Bible.

---

## Principle

Menjelaskan prinsip fundamental yang menjadi dasar seluruh keputusan arsitektur.

---

## Framework

Menyediakan model konseptual untuk mengorganisasi suatu domain.

---

## Standard

Menetapkan aturan normatif yang wajib dipatuhi.

---

## Bible

Mendokumentasikan pengetahuan kanonis secara komprehensif.

---

## Registry

Menyimpan inventaris atau metadata kanonis.

---

## Template

Menyediakan struktur baku penyusunan artefak.

---

## Prompt

Menyediakan instruksi standar untuk AI atau proses otomatis.

---

## Reference

Menyediakan informasi pendukung yang tidak bersifat normatif.

---

## Decision

Mendokumentasikan keputusan arsitektural beserta alasan dan implikasinya.

---

# 7. Relationship Between Document Types

```text
Architecture Overview
        │
        ▼
Principles
        │
        ▼
Frameworks
        │
        ▼
Standards
        │
        ├──────────────┐
        ▼              ▼
Registries         Templates
        │              │
        └──────┬───────┘
               ▼
            Bibles
               │
        ┌──────┴──────┐
        ▼             ▼
   References     Prompts
               │
               ▼
           Decisions
```

Diagram ini menunjukkan hubungan konseptual antar Document Type dan bukan dependency implementasi.

---

# 8. Governance

Seluruh Canonical Document wajib menggunakan salah satu Document Type resmi yang didefinisikan dalam KCF.

Penambahan Document Type baru hanya dapat dilakukan melalui keputusan arsitektural resmi yang menjaga konsistensi keseluruhan Knowledge Architecture.

---

# Canonical Decision

Knowledge Classification Framework menetapkan sepuluh Document Type resmi:

1. Architecture Overview
2. Principle
3. Framework
4. Standard
5. Bible
6. Registry
7. Template
8. Prompt
9. Reference
10. Decision

Document Type **Architecture Overview** diperkenalkan pada versi 2.1 sebagai tipe dokumen resmi untuk mendeskripsikan keseluruhan struktur suatu arsitektur tanpa mendefinisikan aturan operasional baru.

Seluruh Canonical Document wajib diklasifikasikan menggunakan salah satu Document Type resmi yang didefinisikan dalam KCF.
