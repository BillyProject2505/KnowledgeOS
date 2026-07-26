# Core Knowledge Architecture (CKA)

**Document ID:** CKA-001
**Version:** 1.0
**Status:** LOCK
**Category:** Architecture Overview
**Owner:** Knowledge Architecture
**Applies To:** Seluruh Knowledge Architecture

---

# 1. Purpose

Core Knowledge Architecture (CKA) mendefinisikan fondasi logis yang menjadi dasar seluruh Knowledge Architecture.

CKA tidak mendefinisikan aturan operasional baru. Dokumen ini menjelaskan bagaimana seluruh Canonical Document fondasi saling berhubungan, membentuk satu sistem yang konsisten, serta menjadi Single Source of Truth bagi seluruh domain yang dibangun di atasnya.

CKA berfungsi sebagai pintu masuk resmi (Official Entry Point) untuk memahami keseluruhan fondasi Knowledge Architecture.

---

# 2. Scope

Core Knowledge Architecture mencakup seluruh Canonical Document yang mendefinisikan fondasi universal Knowledge Architecture, yaitu:

- Principles
- Frameworks
- Standards
- Registries

CKA tidak mencakup Domain Architecture maupun implementasi proyek.

Domain seperti Production, Community, Research, maupun proyek seperti KAZ, KDS, dan Coz We Care dibangun di atas Core Knowledge Architecture.

---

# 3. Core Architecture Overview

```text
Knowledge Architecture
│
└── Core Knowledge Architecture
      │
      ├── Principles
      ├── Frameworks
      ├── Standards
      └── Registries
```

Core Knowledge Architecture menyediakan fondasi universal yang digunakan oleh seluruh Domain Architecture.

---

# 4. Foundation Components

Core Knowledge Architecture terdiri atas Canonical Document berikut.

| Category | Document | Responsibility |
|-----------|----------|----------------|
| Principle | KP-001 | Menetapkan prinsip tertinggi hubungan Knowledge Architecture dan Execution Engine. |
| Framework | KCF-001 | Menentukan bagaimana Canonical Knowledge diklasifikasikan sebelum menjadi Canonical Document. |
| Framework | CPF-001 | Mendefinisikan arsitektur produksi konten dan hubungan antar komponen produksi. |
| Standard | KCS-001 | Mengatur pembentukan dan lifecycle Canonical Document. |
| Standard | RAS-001 | Menentukan organisasi logis Canonical Document. |
| Standard | DNS-001 | Menentukan identitas dan penamaan Canonical Document. |
| Standard | DTS-001 | Menentukan struktur internal Canonical Document. |
| Standard | VS-001 | Mengatur evolusi versi Canonical Document. |
| Standard | KCRS-001 | Menentukan standar metadata Canonical Document. |
| Registry | KCR-001 | Mengimplementasikan katalog metadata seluruh Canonical Document. |
| Standard | PWS-001 | Menentukan Production Workflow yang dijalankan Execution Engine. |
| Standard | PBS-001 | Menentukan struktur dan penggunaan Production Bible. |
| Standard | QGS-001 | Menentukan mekanisme Quality Review sebelum Production Output dipublikasikan. |

Seluruh Canonical Document di atas memiliki tanggung jawab yang saling melengkapi dan tidak saling menggantikan.

---

# 5. Foundation Dependency Map

```text
                          Core Knowledge Architecture
                                      │
                                      ▼
                                  KP-001
                                      │
                                      ▼
                                  KCF-001
                                      │
                                      ▼
                                  KCS-001
                                      │
          ┌───────────────┬───────────────┬───────────────┬───────────────┐
          ▼               ▼               ▼               ▼               ▼
      RAS-001         DNS-001         DTS-001         VS-001         KCRS-001
                                                                          │
                                                                          ▼
                                                                      KCR-001

                                      │
                                      ▼
                                  CPF-001
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                 ▼
                PWS-001           PBS-001           QGS-001
```

Diagram ini menunjukkan hubungan konseptual antar Canonical Document fondasi.

Dependency pada diagram ini merupakan dependency arsitektural dan bukan urutan eksekusi.

---

# 6. Reading Path

Urutan pembelajaran yang direkomendasikan adalah:

## Knowledge Foundation

1. KP-001
2. KCF-001
3. KCS-001
4. RAS-001
5. DNS-001
6. DTS-001
7. VS-001
8. KCRS-001
9. KCR-001

## Production Foundation

10. CPF-001
11. PWS-001
12. PBS-001
13. QGS-001

Reading Path ini memastikan pembaca memahami fondasi sebelum memasuki Domain Architecture.

---

# 7. Architectural Boundary

Core Knowledge Architecture berhenti pada level fondasi universal.

```text
Core Knowledge Architecture
            │
            ▼
Production Architecture
            │
            ▼
Project Architecture
            │
            ▼
Project Implementations
```

Core Knowledge Architecture tidak mendefinisikan aturan khusus suatu domain maupun implementasi proyek.

Seluruh Domain Architecture wajib dibangun di atas fondasi yang disediakan oleh Core Knowledge Architecture.

---

# 8. Governance

Core Knowledge Architecture merupakan fondasi resmi Knowledge Architecture.

Seluruh Canonical Document yang termasuk dalam fondasi wajib mematuhi prinsip berikut:

- Separation of Concerns
- Single Source of Truth
- Technology Independence
- Canonical Consistency
- Backward Compatibility apabila memungkinkan

CKA tidak menggantikan tanggung jawab Canonical Document lainnya.

CKA hanya menjelaskan bagaimana seluruh fondasi bekerja sebagai satu Architecture Overview yang terpadu.

---

# Canonical Decision

Core Knowledge Architecture (CKA-001) merupakan dokumen arsitektur induk (Architecture Overview) yang mendefinisikan fondasi universal Knowledge Architecture.

CKA mengintegrasikan Principles, Frameworks, Standards, dan Registries ke dalam satu Architecture Overview yang konsisten tanpa menggantikan tanggung jawab masing-masing Canonical Document.

Seluruh Domain Architecture, Project Architecture, Resource Architecture, serta implementasi proyek wajib dibangun di atas fondasi yang didefinisikan oleh CKA.

---

# Appendix A — Canonical Foundation Inventory

## Purpose

Appendix A merupakan inventaris resmi seluruh Canonical Document yang membentuk Core Knowledge Architecture.

Inventaris ini berfungsi sebagai:

- referensi resmi fondasi;
- indeks navigasi Canonical Document;
- acuan validasi kelengkapan fondasi;
- referensi ketika melakukan penambahan atau revisi Canonical Document.

Appendix ini tidak menggantikan metadata resmi yang dikelola melalui KCR-001.

---

## Canonical Foundation Inventory

| ID | Category | Document | Version | Status | Responsibility |
|----|----------|----------|---------|--------|----------------|
| KP-001 | Principle | Knowledge Architecture & Execution Engine Principle | 3.0 | LOCK | Menetapkan prinsip tertinggi hubungan antara Knowledge Architecture dan Execution Engine. |
| KCF-001 | Framework | Knowledge Classification Framework | 2.0 | LOCK | Mengklasifikasikan Canonical Knowledge sebelum menjadi Canonical Document. |
| CPF-001 | Framework | Content Production Framework | 2.0 | LOCK | Mendefinisikan arsitektur produksi konten dan hubungan antar komponen produksi. |
| KCS-001 | Standard | Knowledge Capture Standard | 2.0 | LOCK | Mengatur pembentukan dan lifecycle Canonical Document. |
| RAS-001 | Standard | Repository Architecture Standard | 1.0 | LOCK | Menentukan organisasi logis Canonical Document. |
| DNS-001 | Standard | Document Naming Standard | 2.0 | LOCK | Menentukan identitas dan penamaan Canonical Document. |
| DTS-001 | Standard | Document Template Standard | 2.0 | LOCK | Menentukan struktur internal Canonical Document. |
| VS-001 | Standard | Versioning Standard | 2.0 | LOCK | Mengatur evolusi versi Canonical Document. |
| KCRS-001 | Standard | Knowledge Catalog Registry Standard | 2.0 | LOCK | Menentukan standar metadata Canonical Document. |
| KCR-001 | Registry | Knowledge Catalog Registry | 1.0 | LOCK | Mengimplementasikan katalog metadata seluruh Canonical Document. |
| PWS-001 | Standard | Production Workflow Standard | 2.0 | LOCK | Menentukan Production Workflow yang dijalankan Execution Engine. |
| PBS-001 | Standard | Production Bible Standard | 2.0 | LOCK | Menentukan struktur dan penggunaan Production Bible. |
| QGS-001 | Standard | Quality Gate Standard | 2.0 | LOCK | Menentukan mekanisme Quality Review sebelum Production Output dipublikasikan. |

---

## Inventory Rules

1. Seluruh Canonical Document yang termasuk dalam Core Knowledge Architecture wajib tercantum dalam Appendix A.
2. Penambahan Canonical Document fondasi wajib disertai pembaruan Appendix A.
3. Perubahan versi atau status Canonical Document harus tercermin pada Appendix A.
4. Appendix A berfungsi sebagai Architecture Inventory, sedangkan metadata operasional tetap dikelola oleh KCR-001 sesuai KCRS-001.
5. Appendix A tidak menggantikan Registry dan tidak menjadi sumber metadata operasional.
