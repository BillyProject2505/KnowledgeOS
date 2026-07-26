# Knowledge Catalog Registry (KCR)

**Registry ID:** KCR-001  
**Version:** 1.0  
**Status:** LOCK  
**Category:** Registry  
**Owner:** Knowledge Architecture

---

# 1. Purpose

Knowledge Catalog Registry (KCR) merupakan katalog metadata kanonis yang mencatat seluruh Canonical Document dalam Knowledge Architecture.

KCR menyediakan satu titik referensi untuk mengidentifikasi, menemukan, menelusuri, dan mengelola dokumen pengetahuan secara konsisten.

KCR tidak menyimpan isi knowledge. KCR hanya menyimpan metadata yang merepresentasikan Canonical Document.

---

# 2. Scope

KCR mencakup seluruh Canonical Document yang berada dalam Knowledge Architecture, tanpa membedakan status dokumen.

Dokumen yang dapat dicatat meliputi, namun tidak terbatas pada:

- Principles
- Frameworks
- Standards
- Bibles
- Templates
- Prompts
- References
- Decisions
- Registry

---

# 3. Registry Schema

Setiap Registry Record minimal memiliki atribut berikut.

| Field | Description |
|--------|-------------|
| Document ID | Identifier unik Canonical Document |
| Title | Judul dokumen |
| Category | Jenis dokumen |
| Version | Versi aktif |
| Status | Status lifecycle dokumen |
| Repository Path | Lokasi dokumen dalam repository |

Implementasi dapat menambahkan metadata lain selama tetap mengikuti KCRS-001.

---

# 4. Registry Records

Seluruh Canonical Document dicatat sebagai Registry Record.

Contoh awal:

| Document ID | Title | Category | Version | Status | Repository Path |
|-------------|-------|----------|---------|--------|-----------------|
| KP-001 | KnowledgeOS & Execution Engine Principle | Principle | 2.0 | LOCK | 01_Knowledge/10_Principles |
| KP-002 | Repository-Agnostic Knowledge Principle | Principle | 1.0 | LOCK | 01_Knowledge/10_Principles |
| CPF-001 | Content Production Framework | Framework | 1.0 | LOCK | 01_Knowledge/20_Frameworks |
| KCF-001 | Knowledge Classification Framework | Framework | 1.0 | LOCK | 01_Knowledge/20_Frameworks |
| KCS-001 | Knowledge Capture Standard | Standard | 1.0 | LOCK | 01_Knowledge/30_Standards |
| DNS-001 | Document Naming Standard | Standard | 1.0 | LOCK | 01_Knowledge/30_Standards |
| DTS-001 | Document Template Standard | Standard | 1.0 | LOCK | 01_Knowledge/30_Standards |
| VS-001 | Versioning Standard | Standard | 1.0 | LOCK | 01_Knowledge/30_Standards |
| QGS-001 | Quality Gate Standard | Standard | 1.0 | LOCK | 01_Knowledge/30_Standards |
| PBS-001 | Production Bible Standard | Standard | 1.0 | LOCK | 01_Knowledge/30_Standards |
| PWS-001 | Production Workflow Standard | Standard | 1.0 | LOCK | 01_Knowledge/30_Standards |
| KCRS-001 | Knowledge Catalog Registry Standard | Standard | 1.0 | LOCK | 01_Knowledge/30_Standards |
| KCR-001 | Knowledge Catalog Registry | Registry | 1.0 | LOCK | 01_Knowledge/90_Registry |

Registry Record baru ditambahkan setiap kali Canonical Document baru diterbitkan.

---

# 5. Navigation

Canonical Document dikelompokkan berdasarkan kategorinya untuk memudahkan penelusuran.

## Principles

- KP-001
- KP-002

## Frameworks

- CPF-001
- KCF-001

## Standards

- KCS-001
- DNS-001
- DTS-001
- VS-001
- QGS-001
- PBS-001
- PWS-001
- KCRS-001

## Registry

- KCR-001

---

# 6. Lifecycle Management

KCR mencatat seluruh Canonical Document sepanjang siklus hidupnya.

Status dokumen merupakan metadata yang dikelola dalam Registry Record.

Contoh status meliputi:

- Draft
- LOCK
- Superseded
- Deprecated

Status dapat berubah sesuai governance yang berlaku tanpa memindahkan Registry Record ke katalog lain.

---

# 7. Governance

Knowledge Catalog Registry wajib:

- mengikuti KCRS-001;
- mengikuti KP-001;
- mengikuti KP-002;
- mencatat seluruh Canonical Document;
- memastikan setiap Canonical Document memiliki tepat satu Registry Record;
- menjaga konsistensi metadata seluruh Registry Record.

---

# Canonical Decision

Knowledge Catalog Registry merupakan katalog metadata tunggal bagi seluruh Canonical Document dalam Knowledge Architecture.

Setiap Canonical Document direpresentasikan oleh tepat satu Registry Record yang menyimpan metadata identifikasi, klasifikasi, status, versi, dan lokasi dokumen. KCR menjadi titik referensi utama untuk navigasi, penelusuran, dan pengelolaan dokumen oleh manusia maupun Execution Engine.
