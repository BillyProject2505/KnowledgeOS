# Document Naming Standard (DNS)

**Document ID:** DNS-001
**Version:** 2.0
**Status:** LOCK
**Category:** Standard
**Owner:** Knowledge Architecture
**Applies To:** Seluruh Canonical Document

---

# 1. Purpose

Document Naming Standard (DNS) menetapkan aturan penamaan Canonical Document agar seluruh Knowledge Architecture memiliki identitas dokumen yang konsisten, mudah dikenali, mudah dicari, dan stabil sepanjang siklus hidupnya.

DNS mengatur identitas dan penamaan dokumen, bukan organisasi repository maupun struktur penyimpanannya.

---

# 2. Scope

Standar ini berlaku untuk seluruh Canonical Document dalam Knowledge Architecture.

---

# 3. Naming Principles

## DNS-P01 — Human Readable

Nama dokumen harus mudah dibaca oleh manusia.

---

## DNS-P02 — Self Descriptive

Nama file harus mampu menggambarkan isi dokumen tanpa harus dibuka.

---

## DNS-P03 — Stable

Nama dokumen harus stabil dan tidak sering berubah.

---

## DNS-P04 — Unique

Setiap Canonical Document memiliki nama dan Document ID yang unik.

---

## DNS-P05 — Consistent

Seluruh Canonical Document menggunakan pola penamaan yang konsisten.

---

# 4. Standard File Naming Format

Seluruh Canonical Document menggunakan format berikut.

```text
<Document ID>_<Document_Title>_v<Version>.md
```

Contoh:

```text
DNS-001_Document_Naming_Standard_v2.0.md

KCS-001_Knowledge_Capture_Standard_v2.0.md

RAS-001_Repository_Architecture_Standard_v1.0.md
```

---

# 5. Document ID Rules

Document ID merupakan bagian yang tidak terpisahkan dari Document Naming Standard.

Format:

```text
<Abbreviation>-<Number>
```

Contoh:

```text
KCS-001

DNS-001

RAS-001

KCRS-001
```

Ketentuan:

- menggunakan singkatan dokumen;
- nomor menggunakan tiga digit;
- setiap Document ID bersifat unik;
- satu Document ID hanya boleh dimiliki oleh satu Canonical Document.

---

# 6. Document Title Rules

Judul menggunakan Title Case.

Pada nama file, setiap kata dipisahkan menggunakan underscore (`_`).

Contoh:

```text
Knowledge_Capture_Standard

Repository_Architecture_Standard

Knowledge_Catalog_Registry_Standard
```

---

# 7. Version Rules

Versi selalu ditulis pada akhir nama file.

Format:

```text
v1.0

v1.1

v2.0
```

Tidak diperbolehkan menggunakan:

```text
latest

final

new

fix

revisi
```

---

# 8. File Extension

Seluruh Canonical Document menggunakan format:

```text
.md
```

---

# 9. Prohibited Naming

Tidak diperbolehkan menggunakan nama seperti:

```text
Final.doc

Final_Final.doc

New.doc

Copy.md

Test.md

Revisi3.md
```

---

# 10. Renaming Rules

Perubahan nama hanya diperbolehkan apabila:

- ruang lingkup dokumen berubah secara signifikan;
- Document ID berubah;
- judul tidak lagi merepresentasikan isi.

Perubahan versi tidak mengubah struktur nama file selain nomor versinya.

---

# 11. Relationship

```text
KP-001
        │
KP-002
        │
        ▼
Document Naming Standard
        │
        ├── supports → DTS-001
        ├── supports → RAS-001
        ├── supports → KCRS-001
        └── identifies → Canonical Document
```

---

# 12. Governance

Seluruh Canonical Document wajib mengikuti standar ini.

Perubahan terhadap pola penamaan hanya dapat dilakukan melalui revisi resmi DNS.

---

# Canonical Decision

Document Naming Standard merupakan standar resmi yang mengatur identitas dan penamaan Canonical Document dalam Knowledge Architecture.

Dengan menerapkan pola penamaan yang konsisten, setiap Canonical Document memiliki identitas yang unik, stabil, mudah dikenali, dan mudah digunakan sepanjang siklus hidupnya.
