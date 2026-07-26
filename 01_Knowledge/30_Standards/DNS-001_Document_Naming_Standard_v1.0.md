# Document Naming Standard (DNS-001)

**Document ID:** DNS-001  
**Version:** 1.0  
**Status:** LOCK  
**Category:** Standard  
**Owner:** KnowledgeOS  
**Applies To:** Seluruh dokumen dalam KnowledgeOS

---

# 1. Purpose

Document Naming Standard (DNS) menetapkan aturan penamaan dokumen agar seluruh KnowledgeOS memiliki struktur yang konsisten, mudah dicari, mudah dipahami, dan mudah dipelihara sepanjang siklus hidup repository.

Standar ini juga menetapkan penggunaan **Document ID** sebagai bagian yang tidak terpisahkan dari penamaan dokumen untuk mempercepat workflow dan menjaga konsistensi identitas setiap dokumen.

---

# 2. Scope

Standar ini berlaku untuk seluruh dokumen yang disimpan dalam KnowledgeOS, termasuk:

- Principles
- Architectures
- Standards
- Bibles
- Registries
- Prompts
- Templates
- References
- Decisions

---

# 3. Naming Principles

## DNS-P01 — Human Readable

Nama dokumen harus mudah dibaca oleh manusia.

---

## DNS-P02 — Self Descriptive

Nama file harus dapat menjelaskan isi dokumen tanpa perlu dibuka.

Contoh:

```
DNS-001_Document_Naming_Standard_v1.0.md
```

lebih baik daripada

```
Standard01.md
```

---

## DNS-P03 — Stable

Nama dokumen tidak boleh sering berubah.

---

## DNS-P04 — Unique

Setiap dokumen memiliki nama yang unik.

---

## DNS-P05 — Consistent

Seluruh repository menggunakan pola penamaan yang sama.

---

# 4. Standard File Naming Format

Seluruh dokumen menggunakan format berikut.

```
<Document ID>_<Document_Title>_v<Version>.md
```

Contoh:

```
KCS-001_Knowledge_Capture_Standard_v1.0.md

DNS-001_Document_Naming_Standard_v1.0.md

PBS-001_Production_Bible_Standard_v1.0.md
```

---

# 5. Document ID Rules

Document ID merupakan bagian dari Document Naming Standard.

Format:

```
<Abbreviation>-<Number>
```

Contoh:

```
KCS-001

DNS-001

RSS-001

PWS-001
```

Ketentuan:

- menggunakan singkatan dokumen;
- nomor menggunakan tiga digit;
- setiap Document ID bersifat unik;
- satu Document ID hanya boleh dimiliki satu dokumen.

---

# 6. Document Title Rules

Judul menggunakan **Title Case**.

Pada nama file, setiap kata dipisahkan menggunakan underscore (`_`).

Contoh:

```
Knowledge_Capture_Standard

Prompt_Writing_Standard

Character_Bible

Visual_Style_Guide
```

---

# 7. Version Rules

Versi selalu ditulis di akhir nama file.

Format:

```
v1.0

v1.1

v2.0
```

Tidak diperbolehkan menggunakan:

```
latest

final

new

fix

revisi
```

---

# 8. File Extension

Seluruh dokumen menggunakan format:

```
.md
```

---

# 9. Folder Naming Rules

Folder menggunakan format:

```
NN_Category
```

Contoh:

```
10_Principles

20_Architecture

30_Standards

40_Bibles

50_Registries

60_Prompts

70_Templates

80_References

90_Decisions
```

---

# 10. Prohibited Naming

Tidak diperbolehkan menggunakan nama seperti:

```
Final.doc

Final_Final.doc

New.doc

Copy.md

Test.md

Revisi3.md
```

---

# 11. Renaming Rules

Perubahan nama hanya diperbolehkan apabila:

- ruang lingkup dokumen berubah secara signifikan;
- Document ID berubah;
- judul tidak lagi merepresentasikan isi.

Perubahan versi tidak mengubah struktur nama file selain nomor versinya.

---

# 12. Examples

| Jenis Dokumen | Nama File |
|---------------|-----------|
| Standard | `KCS-001_Knowledge_Capture_Standard_v1.0.md` |
| Standard | `DNS-001_Document_Naming_Standard_v1.0.md` |
| Bible | `PBB-001_Production_Bible_v1.0.md` |
| Architecture | `PAS-001_Production_Architecture_v1.0.md` |
| Prompt | `PGP-001_Comic_Generation_Prompt_v1.0.md` |

---

# 13. Compliance

Seluruh dokumen baru dalam KnowledgeOS wajib mengikuti DNS-001.

Dokumen yang tidak memenuhi standar ini harus diperbaiki sebelum memperoleh status **Approved** atau **LOCK**.

---

# Canonical Decision

Document ID merupakan bagian yang tidak terpisahkan dari Document Naming Standard.

KnowledgeOS menggabungkan pengaturan Document ID dan penamaan dokumen ke dalam satu standar karena keduanya selalu digunakan dalam satu workflow.

Pemisahan keduanya hanya dilakukan apabila di masa depan terdapat kebutuhan operasional yang nyata.
