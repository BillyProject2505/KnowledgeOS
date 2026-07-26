# Knowledge Catalog Registry Standard (KCRS)

**Document ID:** KCRS-001  
**Version:** 2.1  
**Status:** LOCK  
**Category:** Standard  
**Owner:** Knowledge Architecture  
**Applies To:** Seluruh Knowledge Architecture

---

# 1. Purpose

Knowledge Catalog Registry Standard (KCRS) menetapkan standar metadata yang digunakan untuk mengidentifikasi, mengelola, dan memvalidasi seluruh Canonical Document dalam Knowledge Architecture.

Standar ini memastikan bahwa setiap Canonical Document memiliki metadata yang konsisten, dapat ditelusuri, serta dapat diregistrasikan secara seragam ke dalam Knowledge Catalog Registry (KCR).

---

# 2. Scope

KCRS berlaku untuk seluruh Canonical Document yang berada dalam Knowledge Architecture.

Standar ini mengatur:

- struktur metadata;
- atribut wajib dan opsional;
- validasi metadata;
- hubungan dengan Knowledge Catalog Registry (KCR).

KCRS tidak mengatur isi dokumen maupun struktur internal dokumen. Ketentuan tersebut berada pada Document Template Standard (DTS).

---

# 3. Metadata Schema

Seluruh Canonical Document wajib memiliki metadata berikut.

| Field | Required | Description |
|--------|----------|-------------|
| Document ID | Yes | Identitas unik Canonical Document. |
| Title | Yes | Nama resmi dokumen. |
| Document Type | Yes | Jenis Canonical Document sesuai KCF. |
| Version | Yes | Nomor versi resmi dokumen. |
| Status | Yes | Draft, Review, atau LOCK. |
| Owner | Yes | Pemilik atau pengelola dokumen. |
| Applies To | Yes | Lingkup keberlakuan dokumen. |
| Created | Optional | Tanggal pembuatan awal. |
| Updated | Optional | Tanggal revisi terakhir. |
| Supersedes | Optional | Dokumen yang digantikan. |
| Superseded By | Optional | Dokumen pengganti. |
| Related Documents | Optional | Dokumen yang memiliki hubungan langsung. |

---

# 4. Official Document Types

Field **Document Type** hanya boleh menggunakan nilai resmi berikut.

```text
Architecture Overview
Principle
Framework
Standard
Bible
Registry
Template
Prompt
Reference
Decision
```

Definisi setiap Document Type mengikuti Knowledge Classification Framework (KCF).

---

# 5. Document Type Definitions

| Document Type | Description |
|---------------|-------------|
| Architecture Overview | Menjelaskan struktur, ruang lingkup, hubungan, dan batas suatu arsitektur tanpa mendefinisikan aturan operasional baru. |
| Principle | Menetapkan prinsip fundamental. |
| Framework | Menyediakan model konseptual. |
| Standard | Menetapkan aturan normatif. |
| Bible | Mendokumentasikan pengetahuan kanonis suatu domain. |
| Registry | Menyimpan inventaris atau metadata kanonis. |
| Template | Menyediakan struktur baku penyusunan dokumen. |
| Prompt | Menyediakan instruksi standar untuk AI atau proses otomatis. |
| Reference | Menyediakan informasi pendukung yang tidak bersifat normatif. |
| Decision | Mendokumentasikan keputusan arsitektural. |

---

# 6. Metadata Validation Rules

Metadata Canonical Document harus memenuhi ketentuan berikut.

1. Document ID wajib unik.
2. Title wajib unik dalam lingkup yang sama.
3. Version wajib mengikuti Versioning Standard.
4. Status wajib menggunakan nilai resmi.
5. Document Type wajib menggunakan salah satu nilai resmi yang didefinisikan oleh KCF.
6. Owner wajib ditentukan.
7. Applies To wajib ditentukan.

Metadata yang tidak memenuhi aturan di atas tidak boleh diregistrasikan ke dalam Knowledge Catalog Registry.

---

# 7. Metadata Example

Contoh metadata Canonical Document.

```yaml
Document ID: CKA-001
Title: Core Knowledge Architecture
Document Type: Architecture Overview
Version: 1.0
Status: LOCK
Owner: Knowledge Architecture
Applies To: Seluruh Knowledge Architecture
```

---

# 8. Relationship with KCR

Knowledge Catalog Registry (KCR) menggunakan metadata yang didefinisikan oleh KCRS sebagai sumber validasi resmi.

KCR bertanggung jawab menyimpan metadata tersebut, sedangkan KCRS mendefinisikan struktur dan aturan validasinya.

---

# 9. Governance

Seluruh Canonical Document wajib mematuhi metadata yang didefinisikan dalam KCRS.

Perubahan terhadap struktur metadata maupun nilai resmi Document Type hanya dapat dilakukan melalui revisi resmi terhadap KCF dan KCRS.

---

# Canonical Decision

Knowledge Catalog Registry Standard menetapkan metadata resmi bagi seluruh Canonical Document.

Mulai versi 2.1, field **Document Type** secara resmi mengadopsi taxonomy yang didefinisikan oleh Knowledge Classification Framework (KCF), termasuk penambahan nilai **Architecture Overview** sebagai Document Type yang sah.

Seluruh metadata Canonical Document wajib menggunakan salah satu Document Type resmi yang didefinisikan oleh KCF.
