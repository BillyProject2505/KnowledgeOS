# Document Template Standard (DTS)

**Document ID:** DTS-001  
**Version:** 2.1  
**Status:** LOCK  
**Category:** Standard  
**Owner:** Knowledge Architecture  
**Applies To:** Seluruh Knowledge Architecture

---

# 1. Purpose

Document Template Standard (DTS) menetapkan struktur baku yang wajib digunakan oleh seluruh Canonical Document dalam Knowledge Architecture.

Standar ini memastikan bahwa seluruh Canonical Document memiliki format yang konsisten, mudah dibaca, mudah dipelihara, serta dapat divalidasi secara seragam.

---

# 2. Scope

DTS berlaku untuk seluruh Canonical Document yang berada dalam Knowledge Architecture.

Standar ini mengatur:

- struktur umum Canonical Document;
- urutan bagian (sections);
- metadata header;
- aturan penyusunan dokumen.

DTS tidak mengatur klasifikasi Document Type maupun metadata. Ketentuan tersebut didefinisikan oleh KCF dan KCRS.

---

# 3. Canonical Metadata Header

Seluruh Canonical Document wajib diawali dengan metadata berikut.

```yaml
Document ID:
Version:
Status:
Category:
Owner:
Applies To:
```

Field di atas merupakan metadata minimum yang wajib dimiliki oleh seluruh Canonical Document.

---

# 4. Valid Category Values

Field **Category** hanya boleh menggunakan salah satu Document Type resmi yang didefinisikan oleh Knowledge Classification Framework (KCF).

Nilai yang diperbolehkan adalah:

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

Tidak diperbolehkan menggunakan nilai lain di luar taxonomy resmi tersebut.

---

# 5. Canonical Document Structure

Urutan umum Canonical Document adalah sebagai berikut.

1. Metadata Header
2. Purpose
3. Scope
4. Core Content
5. Governance (jika diperlukan)
6. Canonical Decision (jika diperlukan)
7. Appendix (opsional)

Section tambahan diperbolehkan apabila diperlukan oleh Document Type tertentu, selama tidak mengubah struktur dasar di atas.

---

# 6. Template Validation Rules

Setiap Canonical Document harus memenuhi aturan berikut.

1. Menggunakan metadata header resmi.
2. Menggunakan Document ID yang valid.
3. Menggunakan Version sesuai Versioning Standard.
4. Menggunakan Status resmi.
5. Menggunakan Category yang merupakan Document Type resmi menurut KCF.
6. Menggunakan struktur dasar Canonical Document sebagaimana didefinisikan oleh DTS.

Dokumen yang tidak memenuhi aturan di atas tidak dapat dianggap sebagai Canonical Document.

---

# 7. Example Template

Contoh template Canonical Document.

```text
# Document Title

Document ID: CKA-001
Version: 1.0
Status: LOCK
Category: Architecture Overview
Owner: Knowledge Architecture
Applies To: Seluruh Knowledge Architecture

---

# 1. Purpose

...

---

# 2. Scope

...

---

# 3. Core Content

...

---

# Canonical Decision

...
```

Contoh di atas hanya menunjukkan struktur dasar. Isi setiap section disesuaikan dengan Document Type yang digunakan.

---

# 8. Governance

Seluruh Canonical Document wajib mengikuti struktur yang didefinisikan dalam DTS.

Perubahan terhadap struktur dasar maupun metadata header hanya dapat dilakukan melalui revisi resmi terhadap Document Template Standard.

---

# Canonical Decision

Document Template Standard menetapkan struktur baku bagi seluruh Canonical Document.

Mulai versi 2.1, field **Category** secara resmi mendukung **Architecture Overview** sebagai Document Type yang sah sesuai taxonomy yang didefinisikan oleh Knowledge Classification Framework (KCF) dan divalidasi melalui Knowledge Catalog Registry Standard (KCRS).

Seluruh Canonical Document wajib menggunakan template yang didefinisikan oleh DTS agar konsisten di seluruh Knowledge Architecture.
