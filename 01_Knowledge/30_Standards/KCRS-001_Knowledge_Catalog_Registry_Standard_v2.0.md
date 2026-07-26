# Knowledge Catalog Registry Standard (KCRS)

**Document ID:** KCRS-001
**Version:** 2.0
**Status:** LOCK
**Category:** Standard
**Owner:** Knowledge Architecture
**Applies To:** Seluruh Knowledge Catalog Registry

---

# 1. Purpose

Knowledge Catalog Registry Standard (KCRS) menetapkan standar resmi untuk membangun, mengelola, dan memelihara Knowledge Catalog Registry sebagai katalog metadata Canonical Document dalam Knowledge Architecture.

Standar ini mendefinisikan aturan registry, struktur metadata, dan Registry Record, bukan implementasi registry tertentu.

KCRS tidak mendefinisikan Canonical Knowledge, melainkan mengatur bagaimana Canonical Document diregistrasikan dan ditemukan secara konsisten.

---

# 2. Scope

Standar ini berlaku untuk:

- seluruh Knowledge Catalog Registry;
- seluruh Registry Record;
- metadata Canonical Document.

---

# 3. Core Principles

## KCRS-P01 — Metadata, Not Knowledge

Knowledge Catalog Registry hanya mengelola metadata.

Registry tidak mendefinisikan Principle, Framework, Standard, Bible, Template, Prompt, Reference, Registry, maupun Decision.

---

## KCRS-P02 — One Canonical Document ↔ One Registry Record

Setiap Canonical Document wajib memiliki tepat satu Registry Record.

Setiap Registry Record hanya boleh merepresentasikan satu Canonical Document.

Hubungan keduanya bersifat one-to-one.

---

## KCRS-P03 — Traceability

Setiap Registry Record harus memiliki referensi yang jelas menuju Canonical Document yang direpresentasikan.

---

## KCRS-P04 — Discoverability

Knowledge Catalog Registry harus memungkinkan manusia maupun Execution Engine menemukan Canonical Document secara konsisten dan efisien.

---

## KCRS-P05 — Consistency

Seluruh Registry Record harus menggunakan struktur metadata yang konsisten sehingga dapat diproses secara seragam.

---

# 4. Registry Architecture

Knowledge Catalog Registry terdiri atas kumpulan Registry Record yang masing-masing merepresentasikan satu Canonical Document.

```text
Canonical Document
        │
        ▼
Registry Record
        │
        ▼
Knowledge Catalog Registry
```

Knowledge Catalog Registry merupakan katalog metadata.

Registry bukan penyimpan isi Canonical Knowledge.

---

# 5. Registry Record Schema

Setiap Registry Record minimal memiliki atribut berikut.

| Field | Required |
|--------|:--------:|
| Document ID | ✔ |
| Title | ✔ |
| Category | ✔ |
| Version | ✔ |
| Status | ✔ |
| Owner | ✔ |
| Logical Category | ✔ |
| Repository Path | Optional |

Repository Path merupakan atribut implementasi dan tidak wajib apabila Knowledge Catalog Registry diimplementasikan melalui mekanisme lain.

Implementasi dapat menambahkan atribut lain selama tetap konsisten dengan standar ini.

---

# 6. Validation Rules

Knowledge Catalog Registry dinyatakan valid apabila:

- setiap Canonical Document memiliki tepat satu Registry Record;
- setiap Registry Record merepresentasikan tepat satu Canonical Document;
- tidak terdapat Registry Record tanpa Canonical Document;
- tidak terdapat Canonical Document tanpa Registry Record.

---

# 7. Registry Lifecycle

```text
Canonical Document LOCK
        │
        ▼
Registry Record Created
        │
        ▼
Registry Published
        │
        ▼
Maintain Through Versioning
```

Registry hanya mencatat Canonical Document yang telah memperoleh status LOCK.

Perubahan Registry Record mengikuti Versioning Standard (VS).

---

# 8. Relationship

```text
Knowledge Capture Standard (KCS)
                │
                ▼
Canonical Document
                │
                ▼
Knowledge Catalog Registry Standard (KCRS)
                │
                ▼
Knowledge Catalog Registry (KCR)
                │
                ▼
Discovery
```

KCS menghasilkan Canonical Document.

KCRS mendefinisikan aturan registrasi.

KCR mengimplementasikan aturan tersebut sebagai katalog metadata.

---

# 9. Governance

Seluruh Knowledge Catalog Registry wajib:

- mengikuti Repository Architecture Standard (RAS);
- mengikuti Document Template Standard (DTS);
- mengikuti Document Naming Standard (DNS);
- mengikuti Versioning Standard (VS);
- menjaga konsistensi antara Canonical Document dan Registry Record.

Perubahan terhadap struktur registry hanya dapat dilakukan melalui revisi resmi Knowledge Catalog Registry Standard.

---

# Canonical Decision

Knowledge Catalog Registry Standard (KCRS) merupakan standar resmi yang mengatur struktur metadata, Registry Record, dan tata kelola Knowledge Catalog Registry dalam Knowledge Architecture.

KCRS mendefinisikan bagaimana Canonical Document diregistrasikan, diindeks, dan ditemukan secara konsisten, tanpa mendefinisikan ataupun menggantikan isi Canonical Knowledge.
