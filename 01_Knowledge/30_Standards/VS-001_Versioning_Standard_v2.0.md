# Versioning Standard (VS)

**Document ID:** VS-001
**Version:** 2.0
**Status:** LOCK
**Category:** Standard
**Owner:** Knowledge Architecture
**Applies To:** Seluruh Canonical Document

---

# 1. Purpose

Versioning Standard (VS) menetapkan aturan resmi mengenai pengelolaan versi, status, kompatibilitas, dan evolusi Canonical Document dalam Knowledge Architecture.

Tujuannya adalah memastikan setiap perubahan dapat ditelusuri, dipahami, dan dikelola tanpa mengurangi integritas Canonical Document sebagai Single Source of Truth.

---

# 2. Scope

Standar ini berlaku untuk seluruh Canonical Document dalam Knowledge Architecture.

---

# 3. Versioning Principles

## VS-P01 — Every Change Is Traceable

Setiap perubahan harus terdokumentasi dan dapat ditelusuri.

---

## VS-P02 — One Active LOCK Version

Pada satu waktu hanya boleh terdapat satu versi berstatus **LOCK** yang menjadi referensi kanonis aktif untuk setiap Document ID.

Versi sebelumnya tetap dipertahankan sebagai bagian dari riwayat dokumen.

---

## VS-P03 — Backward Awareness

Setiap perubahan harus mempertimbangkan dampaknya terhadap Canonical Document lain yang bergantung padanya.

---

## VS-P04 — Explicit Versioning

Nomor versi wajib dicantumkan secara eksplisit pada metadata dokumen.

---

## VS-P05 — Immutable LOCK Release

Dokumen berstatus LOCK tidak boleh diubah secara langsung.

Perubahan dilakukan melalui penerbitan versi baru.

---

# 4. Version Numbering

Versioning menggunakan format:

```text
MAJOR.MINOR
```

Contoh:

```text
v1.0
v1.1
v1.2
v2.0
v2.1
```

## Major Version

Versi mayor meningkat apabila terjadi perubahan yang memengaruhi struktur, ruang lingkup, atau makna utama dokumen.

Contoh:

```text
v1.0
↓
v2.0
```

---

## Minor Version

Versi minor meningkat apabila terjadi penyempurnaan yang tetap kompatibel dengan versi sebelumnya.

Contoh:

```text
v1.0
↓
v1.1
↓
v1.2
```

---

# 5. Document Version and Status

Setiap Canonical Document memiliki tiga identitas yang berbeda.

| Element | Purpose |
|---------|---------|
| Document ID | Identitas tetap dokumen |
| Version | Edisi dari dokumen |
| Status | Keadaan dari versi tersebut |

Contoh:

| Document ID | Version | Status |
|-------------|---------|--------|
| KCS-001 | 2.0 | LOCK |
| KCS-001 | 1.0 | Superseded |

Status merupakan bagian dari lifecycle Canonical Document dan tidak mengubah Document ID.

---

# 6. Document Status

Setiap versi dokumen memiliki salah satu status berikut.

| Status | Deskripsi |
|---------|-----------|
| Draft | Sedang disusun |
| Review | Sedang ditinjau |
| Approved | Disetujui, belum dikunci |
| LOCK | Versi kanonis aktif |
| Superseded | Digantikan oleh versi yang lebih baru |
| Archived | Tidak lagi digunakan |

---

# 7. Version Lifecycle

```text
Draft
   │
   ▼
Review
   │
   ▼
Approved
   │
   ▼
LOCK
   │
   ├──────────────┐
   ▼              ▼
Minor Update   Major Update
   │              │
   ▼              ▼
New Version    New Version
   │
   ▼
Superseded
   │
   ▼
Archived (if applicable)
```

---

# 8. Compatibility Rules

## Minor Update

- Tetap kompatibel dengan versi sebelumnya.
- Tidak mengubah konsep inti.
- Tidak mengubah Document ID.

---

## Major Update

- Dapat mengubah struktur maupun konsep.
- Tetap menggunakan Document ID yang sama.
- Menggantikan versi LOCK sebelumnya setelah memperoleh status LOCK.

---

# 9. Change Log Standard

Setiap dokumen dapat menyertakan riwayat perubahan.

Contoh:

| Version | Date | Summary |
|----------|------|---------|
| 1.0 | YYYY-MM-DD | Initial LOCK Release |
| 1.1 | YYYY-MM-DD | Editorial improvements |
| 2.0 | YYYY-MM-DD | Major architectural revision |

---

# 10. Compatibility Statement

Setiap versi baru, khususnya Major Version, dapat menyertakan informasi berikut.

- **Backward Compatible:** Yes / No
- **Migration Required:** Yes / No
- **Affected Canonical Documents:** Daftar Document ID yang perlu ditinjau atau diperbarui.

Compatibility Statement membantu mengidentifikasi dampak perubahan terhadap Knowledge Architecture.

---

# 11. Relationship

```text
Canonical Document
        │
        ├── Document Naming Standard (DNS)
        ├── Document Template Standard (DTS)
        ├── Repository Architecture Standard (RAS)
        ├── Versioning Standard (VS)
        └── Knowledge Catalog Registry Standard (KCRS)
```

VS mengatur evolusi Canonical Document melalui pengelolaan versi dan status sepanjang lifecycle dokumen.

---

# 12. Governance

Seluruh perubahan Canonical Document wajib memenuhi ketentuan berikut.

- Nomor versi wajib diperbarui.
- Status dokumen wajib diperbarui sesuai lifecycle.
- Ringkasan perubahan wajib dicatat.
- Document ID tidak boleh berubah akibat perubahan versi.
- Dokumen yang digantikan diberi status Superseded.
- Hanya satu versi LOCK yang menjadi referensi kanonis aktif untuk setiap Document ID.

Perubahan terhadap aturan versioning hanya dapat dilakukan melalui revisi resmi Versioning Standard.

---

# Canonical Decision

Versioning Standard (VS) merupakan standar resmi yang mengatur evolusi Canonical Document dalam Knowledge Architecture melalui pengelolaan versi, status, lifecycle, kompatibilitas, dan riwayat perubahan.

VS memastikan setiap Canonical Document berevolusi secara terkendali tanpa kehilangan identitas, keterlacakan, maupun integritas sebagai Single Source of Truth.
