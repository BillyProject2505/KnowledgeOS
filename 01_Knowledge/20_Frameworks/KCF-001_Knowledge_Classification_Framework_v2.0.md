# Knowledge Classification Framework (KCF)

**Document ID:** KCF-001
**Version:** 2.0
**Status:** LOCK
**Category:** Framework
**Owner:** Knowledge Architecture
**Applies To:** Seluruh Canonical Knowledge dalam Knowledge Architecture

---

# 1. Purpose

Knowledge Classification Framework (KCF) mendefinisikan bagaimana Canonical Knowledge diklasifikasikan sebelum dibentuk menjadi Canonical Document dalam Knowledge Architecture.

Framework ini memastikan setiap knowledge:

- memiliki ruang lingkup yang jelas;
- memiliki lapisan (layer) yang tepat;
- memiliki lokasi logis yang sesuai;
- dapat digunakan kembali apabila memungkinkan.

KCF menjadi tahap klasifikasi sebelum proses pembentukan Canonical Document dimulai.

---

# 2. Scope

Framework ini berlaku untuk seluruh Canonical Knowledge yang akan dikelola dalam Knowledge Architecture, termasuk namun tidak terbatas pada:

- Principles
- Frameworks
- Standards
- Bibles
- Registries
- Templates
- Prompts
- References
- Decisions

---

# 3. Classification Principles

## KCF-P01 — Every Knowledge Has a Logical Home

Setiap Canonical Knowledge harus memiliki lokasi logis yang jelas dalam Knowledge Architecture.

---

## KCF-P02 — Classify Before Create

Canonical Knowledge wajib diklasifikasikan sebelum dibentuk menjadi Canonical Document.

---

## KCF-P03 — Single Primary Classification

Setiap Canonical Document memiliki satu klasifikasi utama yang menentukan lokasi logisnya.

---

## KCF-P04 — Reusable by Default

Apabila suatu knowledge dapat digunakan kembali oleh lebih dari satu proyek, maka knowledge tersebut harus diklasifikasikan sebagai Reusable Canonical Knowledge.

---

## KCF-P05 — Project-Specific Only When Necessary

Project-Specific Canonical Knowledge hanya dibuat apabila knowledge memang bersifat khusus untuk proyek tertentu.

---

# 4. Classification Dimensions

Seluruh Canonical Knowledge diklasifikasikan melalui lima dimensi berikut.

## 4.1 Knowledge Scope

- Reusable Canonical Knowledge
- Project-Specific Canonical Knowledge

---

## 4.2 Knowledge Layer

- Principle
- Framework
- Standard
- Bible
- Registry
- Template
- Prompt
- Reference
- Decision

---

## 4.3 Logical Placement

- 01_Knowledge
- 02_Projects
- 03_Resources
- 99_Archive

---

## 4.4 Lifecycle

- Draft
- Review
- Approved
- LOCK
- Archived

---

## 4.5 Ownership

- Global
- Project
- Shared

---

# 5. Classification Workflow

```text
New Knowledge
       │
       ▼
Reusable?
       │
 ┌─────┴─────┐
 │           │
Yes         No
 │           │
 ▼           ▼
Reusable     Project-Specific
Canonical    Canonical
Knowledge    Knowledge
       │
       ▼
Determine Layer
       │
       ▼
Determine Logical Placement
       │
       ▼
Assign Document ID
       │
       ▼
Create Canonical Document
```

---

# 6. Knowledge Decision Matrix

| Question | Result |
|----------|--------|
| Berlaku lintas proyek? | Reusable Canonical Knowledge |
| Hanya berlaku untuk satu proyek? | Project-Specific Canonical Knowledge |
| Menjelaskan filosofi? | Principle |
| Menjelaskan arsitektur? | Framework |
| Menjelaskan aturan operasional? | Standard |
| Menjelaskan knowledge proyek? | Bible |
| Berisi metadata atau daftar? | Registry |
| Menyediakan struktur baku? | Template |
| Berisi instruksi eksekusi? | Prompt |
| Berisi referensi? | Reference |
| Mencatat keputusan resmi? | Decision |

---

# 7. Logical Placement Mapping

```text
Principles
    ↓
01_Knowledge/10_Principles

Frameworks
    ↓
01_Knowledge/20_Frameworks

Standards
    ↓
01_Knowledge/30_Standards

Bibles
    ↓
01_Knowledge/40_Bibles

Registries
    ↓
01_Knowledge/50_Registries

Prompts
    ↓
01_Knowledge/60_Prompts

Templates
    ↓
01_Knowledge/70_Templates

References
    ↓
01_Knowledge/80_References

Decisions
    ↓
01_Knowledge/90_Decisions
```

Logical Placement ditentukan oleh Repository Architecture Standard (RAS).

---

# 8. Relationship

```text
Knowledge Capture Standard
            │
            ▼
Knowledge Classification Framework
            │
            ▼
Repository Architecture Standard
            │
            ▼
Document Naming Standard
            │
            ▼
Canonical Document
```

KCF menentukan klasifikasi Canonical Knowledge sebelum dibentuk menjadi Canonical Document.

---

# 9. Classification Record

Sebelum Canonical Document dibuat, harus disusun sebuah Classification Record.

Contoh:

```text
Knowledge Scope:
☑ Reusable Canonical Knowledge

Knowledge Layer:
☑ Framework

Logical Placement:
☑ 01_Knowledge

Logical Category:
☑ 20_Frameworks

Document ID:
☑ KCF-001

Filename:
☑ KCF-001_Knowledge_Classification_Framework_v2.0.md
```

Classification Record menjadi dasar keputusan klasifikasi sebelum proses dokumentasi dimulai.

---

# 10. Governance

Perubahan terhadap KCF harus:

- mempertahankan kompatibilitas dengan Knowledge Capture Standard (KCS);
- selaras dengan Repository Architecture Standard (RAS);
- selaras dengan Document Naming Standard (DNS);
- tidak mendefinisikan struktur Canonical Document;
- tidak mendefinisikan workflow produksi;
- menjaga konsistensi klasifikasi seluruh Canonical Knowledge.

---

# Canonical Decision

Knowledge Classification Framework (KCF) merupakan framework resmi yang mengatur klasifikasi Canonical Knowledge sebelum dibentuk menjadi Canonical Document dalam Knowledge Architecture.

KCF memastikan setiap knowledge memperoleh ruang lingkup, lapisan, dan lokasi logis yang tepat sehingga dapat dikelola secara konsisten, digunakan kembali, dan diintegrasikan ke dalam keseluruhan arsitektur.
