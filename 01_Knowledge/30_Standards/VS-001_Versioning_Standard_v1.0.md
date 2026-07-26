# Versioning Standard (VS)

**Document ID:** VS-001  
**Version:** 1.0  
**Status:** LOCK  
**Category:** Standard  
**Owner:** KnowledgeOS  
**Applies To:** Seluruh dokumen dalam KnowledgeOS

---

# 1. Purpose

Versioning Standard (VS) menetapkan aturan resmi mengenai pemberian nomor versi, pengelolaan revisi, status dokumen, kompatibilitas, dan riwayat perubahan di seluruh KnowledgeOS.

Tujuannya adalah memastikan setiap perubahan dapat ditelusuri, dipahami, dan dikelola tanpa mengurangi integritas KnowledgeOS sebagai Single Source of Truth.

---

# 2. Scope

Standar ini berlaku untuk seluruh kategori dokumen dalam KnowledgeOS, termasuk:

- Principles
- Frameworks
- Standards
- Bibles
- Registries
- Templates
- Prompts
- References
- Decisions
- README

---

# 3. Versioning Principles

## VS-P01 — Every Change Is Traceable

Setiap perubahan harus terdokumentasi dan dapat ditelusuri.

---

## VS-P02 — One Canonical Version

Pada satu waktu hanya boleh ada satu versi berstatus LOCK untuk setiap Document ID.

---

## VS-P03 — Backward Awareness

Setiap perubahan harus mempertimbangkan dampaknya terhadap dokumen lain yang bergantung padanya.

---

## VS-P04 — Explicit Versioning

Nomor versi wajib dicantumkan secara eksplisit pada metadata dokumen.

---

## VS-P05 — Immutable LOCK Release

Dokumen berstatus LOCK tidak boleh diubah secara langsung. Perubahan dilakukan melalui penerbitan versi baru.

---

# 4. Version Numbering

KnowledgeOS menggunakan format:

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

## Minor Version

Versi minor meningkat apabila terjadi penambahan atau penyempurnaan yang tetap kompatibel dengan versi sebelumnya.

Contoh:

```text
v1.0
↓
v1.1
↓
v1.2
```

---

# 5. Document Status

Setiap dokumen memiliki salah satu status berikut.

| Status | Deskripsi |
|---------|-----------|
| Draft | Sedang disusun |
| Review | Sedang ditinjau |
| Approved | Disetujui, belum dikunci |
| LOCK | Versi kanonis aktif |
| Superseded | Digantikan oleh versi yang lebih baru |
| Archived | Tidak lagi digunakan |

---

# 6. Version Lifecycle

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

# 7. Compatibility Rules

## Minor Update

- Tetap kompatibel dengan versi sebelumnya.
- Tidak mengubah konsep inti.
- Tidak mengubah Document ID.

## Major Update

- Dapat mengubah struktur maupun konsep.
- Tetap menggunakan Document ID yang sama.
- Menggantikan versi LOCK sebelumnya setelah memperoleh status LOCK.

---

# 8. Change Log Standard

Setiap dokumen dapat menyertakan riwayat perubahan.

Contoh:

| Version | Date | Summary |
|----------|------|---------|
| 1.0 | YYYY-MM-DD | Initial LOCK release |
| 1.1 | YYYY-MM-DD | Clarified governance |
| 2.0 | YYYY-MM-DD | Major restructuring |

---

# 9. Compatibility Statement

Untuk setiap versi baru, khususnya versi mayor, dokumen dapat menyertakan informasi berikut.

- **Backward Compatible:** Yes / No
- **Migration Required:** Yes / No
- **Affected Documents:** Daftar Document ID yang perlu ditinjau atau diperbarui.

Compatibility Statement membantu mengidentifikasi dampak perubahan terhadap KnowledgeOS secara keseluruhan.

---

# 10. Relationship

```text
Document Naming Standard
            │
            ▼
Versioning Standard
            │
            ▼
All KnowledgeOS Documents
```

VS memastikan evolusi seluruh dokumen berlangsung secara terkontrol dan dapat ditelusuri.

---

# 11. Governance

Setiap perubahan dokumen harus memenuhi ketentuan berikut.

- Nomor versi wajib diperbarui.
- Ringkasan perubahan wajib dicatat.
- Status dokumen wajib diperbarui sesuai lifecycle.
- Dokumen yang digantikan diberi status Superseded.
- Hanya satu versi LOCK yang menjadi referensi kanonis untuk setiap Document ID.

---

# Canonical Decision

Versioning Standard (VS) merupakan standar resmi pengelolaan versi seluruh dokumen dalam KnowledgeOS.

Seluruh perubahan harus mengikuti aturan versioning yang konsisten, menggunakan status dokumen yang jelas, serta memastikan hanya terdapat satu versi LOCK sebagai referensi kanonis untuk setiap Document ID. Dengan demikian, evolusi KnowledgeOS tetap terkontrol, dapat diaudit, dan mendukung prinsip Single Source of Truth.
