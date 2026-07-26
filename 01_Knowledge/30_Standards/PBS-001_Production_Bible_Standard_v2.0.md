# Production Bible Standard (PBS)

**Document ID:** PBS-001
**Version:** 2.0
**Status:** LOCK
**Category:** Standard
**Owner:** Knowledge Architecture
**Applies To:** Seluruh Production Bible

---

# 1. Purpose

Production Bible Standard (PBS) menetapkan standar resmi untuk penyusunan, pengelolaan, dan penggunaan Production Bible sebagai Canonical Knowledge yang bersifat spesifik proyek.

Production Bible menyediakan aturan operasional yang digunakan selama proses produksi untuk memastikan seluruh Production Output konsisten dengan identitas, tujuan, dan kebutuhan proyek.

PBS tidak mengatur struktur dokumen maupun workflow produksi. Kedua aspek tersebut diatur oleh Document Template Standard (DTS) dan Production Workflow Standard (PWS).

---

# 2. Scope

Standar ini berlaku untuk seluruh Production Bible dalam Knowledge Architecture, termasuk namun tidak terbatas pada:

- Coz We Care Production Bible
- KDS Production Bible
- OBK Production Bible
- Personal Brand Production Bible
- Production Bible proyek lain di masa depan

---

# 3. Production Bible Principles

## PBS-P01 — One Bible per Project

Setiap proyek memiliki satu Production Bible utama sebagai sumber referensi kanonis.

---

## PBS-P02 — Single Source of Truth

Seluruh aturan spesifik proyek harus berasal dari Production Bible.

---

## PBS-P03 — Project-Specific Canonical Knowledge

Production Bible hanya menyimpan Canonical Knowledge yang bersifat spesifik terhadap suatu proyek.

Knowledge yang dapat digunakan kembali lintas proyek harus ditempatkan sebagai Reusable Canonical Knowledge dalam Knowledge Architecture.

---

## PBS-P04 — Modular Organization

Production Bible disusun dalam modul-modul yang dapat dikembangkan secara independen tanpa mengubah keseluruhan struktur.

---

## PBS-P05 — Integration with Canonical Knowledge

Production Bible dibangun di atas Framework, Standard, Registry, Template, Reference, dan Canonical Knowledge lain yang relevan.

---

# 4. Production Bible Architecture

Production Bible merupakan lapisan Project-Specific Canonical Knowledge yang menghubungkan Canonical Knowledge dengan Production Workflow.

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
Production Output
```

---

# 5. Module Classification

Production Bible dapat disusun secara modular sesuai kebutuhan proyek.

## 5.1 Core Modules (Mandatory)

Seluruh Production Bible wajib memiliki modul inti berikut:

- Project Overview
- Brand Identity
- Audience
- Communication Strategy
- Editorial Guidelines
- Visual Guidelines
- Content Strategy
- Production Rules
- Quality Requirements
- Governance

---

## 5.2 Domain Modules (Conditional)

Ditambahkan sesuai karakteristik proyek.

Contoh:

- Character Bible
- World Bible
- Story Bible
- Campaign Bible
- Platform Guidelines
- Accessibility Guidelines
- Terminology Guide

---

## 5.3 Extension Modules (Optional)

Modul tambahan yang dapat dikembangkan tanpa mengubah struktur inti.

Contoh:

- Asset Library
- FAQ
- Integration Notes
- Workflow Extensions
- Domain-specific Modules

---

# 6. Production Bible Lifecycle

```text
Create
   │
   ▼
Develop
   │
   ▼
Review
   │
   ▼
LOCK
   │
   ▼
Maintain
   │
   ▼
Version Update
```

Seluruh perubahan mengikuti Versioning Standard (VS).

Dokumen yang telah berstatus LOCK tidak diubah secara langsung, tetapi melalui penerbitan versi baru.

---

# 7. Relationship

```text
KP-001
        │
KP-002
        │
        ▼
Reusable Canonical Knowledge
        │
        ▼
Production Bible
(Project-Specific Canonical Knowledge)
        │
        ▼
Production Workflow (PWS)
        │
        ▼
Production Output
```

Production Bible menyediakan aturan operasional spesifik proyek yang digunakan selama Production Workflow.

---

# 8. Governance

Seluruh Production Bible wajib:

- mengikuti Canonical Knowledge yang berlaku;
- mengikuti Document Template Standard (DTS);
- mengikuti Document Naming Standard (DNS);
- mengikuti Versioning Standard (VS);
- melewati Quality Gate Standard (QGS) sebelum memperoleh status LOCK;
- digunakan sebagai referensi utama dalam Production Workflow Standard (PWS).

Perubahan terhadap Production Bible dilakukan melalui mekanisme versioning dan tidak mengubah dokumen LOCK secara langsung.

---

# Canonical Decision

Production Bible Standard (PBS) merupakan standar resmi yang mengatur Production Bible sebagai Project-Specific Canonical Knowledge dalam Knowledge Architecture.

Production Bible menjadi sumber aturan operasional yang digunakan selama Production Workflow untuk menghasilkan Production Output yang konsisten, tanpa menggantikan Framework, Standard, Registry, Template, maupun Reusable Canonical Knowledge yang berlaku lintas proyek.
