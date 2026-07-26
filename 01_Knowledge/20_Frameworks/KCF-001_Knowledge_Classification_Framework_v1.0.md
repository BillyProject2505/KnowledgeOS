# Knowledge Classification Framework (KCF)

**Document ID:** KCF-001  
**Version:** 1.0  
**Status:** LOCK  
**Category:** Framework  
**Owner:** KnowledgeOS  
**Applies To:** Seluruh knowledge dalam KnowledgeOS

---

# 1. Purpose

Knowledge Classification Framework (KCF) mendefinisikan bagaimana seluruh knowledge diklasifikasikan sebelum disimpan ke dalam KnowledgeOS.

Framework ini memastikan setiap knowledge:

- memiliki kategori yang jelas;
- memiliki lokasi repository yang tepat;
- memiliki jenis dokumen yang benar;
- dapat digunakan kembali apabila memungkinkan.

KCF menjadi gerbang masuk seluruh knowledge sebelum proses pembuatan dokumen dimulai.

---

# 2. Scope

Framework ini berlaku untuk seluruh knowledge yang akan disimpan dalam KnowledgeOS, termasuk namun tidak terbatas pada:

- Ide
- Principles
- Frameworks
- Standards
- Bibles
- Registries
- Templates
- Prompts
- References
- Decisions
- Workflow
- Panduan operasional

---

# 3. Classification Principles

## KCF-P01 — Every Knowledge Has a Home

Setiap knowledge harus memiliki lokasi penyimpanan yang jelas di dalam repository.

---

## KCF-P02 — Classify Before Create

Seluruh knowledge wajib diklasifikasikan sebelum dokumen dibuat.

---

## KCF-P03 — Single Primary Classification

Setiap dokumen memiliki satu klasifikasi utama yang menentukan lokasi penyimpanannya.

---

## KCF-P04 — Knowledge Before Project

Apabila suatu knowledge dapat digunakan kembali oleh lebih dari satu proyek, maka knowledge tersebut harus ditempatkan di KnowledgeOS sebelum dipertimbangkan sebagai dokumen proyek.

---

## KCF-P05 — Project Last

Dokumen proyek hanya dibuat apabila knowledge memang bersifat khusus untuk proyek tersebut.

---

# 4. Classification Dimensions

Seluruh knowledge diklasifikasikan melalui lima dimensi berikut.

## 4.1 Knowledge Scope

- Reusable
- Project Specific

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

## 4.3 Repository Placement

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
- Archive

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
Knowledge   Project
 │
 ▼
Determine Layer
 │
 ▼
Determine Repository
 │
 ▼
Assign Document ID
 │
 ▼
Create Document
```

---

# 6. Knowledge Decision Matrix

| Question | Result |
|----------|--------|
| Berlaku untuk semua proyek? | Knowledge |
| Hanya berlaku pada satu proyek? | Project |
| Menjelaskan filosofi? | Principle |
| Menjelaskan arsitektur sistem? | Framework |
| Menjelaskan aturan operasional? | Standard |
| Menjelaskan pengetahuan proyek? | Bible |
| Berisi daftar objek? | Registry |
| Menyediakan struktur baku? | Template |
| Berisi instruksi AI? | Prompt |
| Berisi referensi? | Reference |
| Mencatat keputusan resmi? | Decision |

---

# 7. Repository Mapping

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

---

# 8. Relationship

```text
Knowledge Capture Standard
            │
            ▼
Knowledge Classification Framework
            │
            ▼
Document Naming Standard
            │
            ▼
Repository
            │
            ▼
Content Production Framework
```

KCF memastikan seluruh knowledge telah memiliki identitas dan lokasi yang tepat sebelum mengikuti proses produksi maupun pengelolaan repository.

---

# 9. Knowledge Classification Record (KCR)

Sebelum dokumen dibuat, harus disusun sebuah Knowledge Classification Record.

Contoh:

```text
Knowledge Scope:
☑ Reusable

Knowledge Layer:
☑ Framework

Repository:
☑ 01_Knowledge

Folder:
☑ 20_Frameworks

Document ID:
☑ KCF-001

Filename:
☑ KCF-001_Knowledge_Classification_Framework_v1.0.md
```

KCR menjadi identitas awal setiap dokumen sebelum proses penulisan dimulai.

---

# 10. Governance

Perubahan terhadap KCF harus:

- mempertahankan kompatibilitas dengan Knowledge Capture Standard (KCS);
- tidak bertentangan dengan Document Naming Standard (DNS);
- tidak mengubah struktur repository tanpa persetujuan;
- menjaga konsistensi klasifikasi seluruh KnowledgeOS.

---

# Canonical Decision

Knowledge Classification Framework (KCF) merupakan framework resmi yang mengatur klasifikasi seluruh knowledge dalam KnowledgeOS.

Setiap knowledge wajib diklasifikasikan sebelum dibuat, memiliki satu klasifikasi utama, dan ditempatkan pada lokasi repository yang sesuai. KCF memastikan seluruh knowledge tersusun secara konsisten, dapat digunakan kembali, dan mendukung pengelolaan KnowledgeOS sebagai Single Source of Truth.
