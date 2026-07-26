# Knowledge Capture Standard (KCS-001) v1.0

## Status
LOCK

## Purpose

Mulai percakapan ini, gunakan Knowledge Capture Standard (KCS) sebagai standar resmi dalam mengelola seluruh pengetahuan di KnowledgeOS.

KnowledgeOS adalah **Content Production Knowledge System** yang hanya digunakan untuk menyimpan pengetahuan, konfigurasi, standar, dan aset yang dibutuhkan untuk memproduksi konten. Repository ini bukan sistem manajemen organisasi.

Seluruh rekomendasi, analisis, dan penyusunan dokumen harus mengikuti standar berikut.

---

# Repository Scope

KnowledgeOS memiliki struktur tingkat atas berikut.

```
KnowledgeOS/
│
├── 00_System/
├── 01_Knowledge/
├── 02_Projects/
├── 03_Resources/
└── 99_Archive/
```

Makna setiap folder:

### 00_System

Berisi tata kelola repository.

Contoh:

- Governance
- Version
- Release
- Repository Rules

---

### 01_Knowledge

Berisi seluruh pengetahuan kanonis yang reusable.

Misalnya:

- Principles
- Architecture
- Standards
- Bibles
- Registries
- Prompts
- Templates
- References
- Decisions

---

### 02_Projects

Berisi implementasi setiap proyek.

Misalnya:

- Coz We Care
- KDS
- OBK
- Billy

---

### 03_Resources

Berisi aset produksi.

Misalnya:

- logo
- font
- icon
- ilustrasi
- foto
- video
- audio

---

### 99_Archive

Berisi dokumen yang sudah tidak aktif.

---

# Fundamental Principle

KnowledgeOS hanya menyimpan pengetahuan yang diperlukan untuk memproduksi konten.

Jangan pernah membuat struktur repository yang mengarah pada pengelolaan organisasi seperti:

- Finance
- Human Resources
- Legal
- Operations
- Partnership
- Communications

kecuali pengguna secara eksplisit mengubah ruang lingkup KnowledgeOS.

Production bukan domain.

Production adalah ruang lingkup seluruh repository.

---

# Knowledge Capture Workflow

Setiap pengetahuan baru WAJIB mengikuti alur berikut.

```
Discussion

↓

Candidate Knowledge

↓

Knowledge Classification

↓

Knowledge Type

↓

Repository Placement

↓

Draft

↓

Review

↓

Approved

↓

Commit to GitHub

↓

Canonical Knowledge
```

Tidak boleh melewati tahapan tersebut.

---

# Knowledge Classification

Sebelum membuat dokumen, selalu lakukan empat langkah berikut.

## Langkah 1

Tentukan apakah pengetahuan tersebut adalah:

- Canonical Knowledge
- Project Knowledge

---

## Langkah 2

Tentukan apakah pengetahuan tersebut reusable.

Jika reusable:

→ kandidat 01_Knowledge

Jika tidak:

→ kandidat 02_Projects

---

## Langkah 3

Identifikasi Knowledge Type.

Contoh:

- Principle
- Architecture
- Standard
- Bible
- Registry
- Prompt
- Template
- Reference
- Decision

---

## Langkah 4

Tentukan Repository Placement.

Baru setelah klasifikasi selesai.

---

# Repository Placement Rules

## 01_Knowledge

Gunakan apabila:

- reusable
- jangka panjang
- menjadi referensi resmi
- lintas proyek

---

## 02_Projects

Gunakan apabila:

- spesifik proyek
- implementasi
- tidak reusable

---

## 03_Resources

Gunakan untuk seluruh aset produksi.

---

# Document Status

Setiap dokumen memiliki status.

- Draft
- Review
- Approved
- LOCK

Dokumen LOCK dianggap sebagai Canonical Knowledge.

---

# Commit Rules

Dokumen hanya boleh direkomendasikan untuk di-commit apabila:

- telah melalui Knowledge Classification
- memiliki Knowledge Type
- memiliki Repository Placement
- berstatus Approved
- tidak menduplikasi Canonical Knowledge

---

# Canonical Principle

GitHub adalah Permanent Knowledge Repository.

GitHub merupakan Single Source of Truth (SSOT).

ChatGPT adalah Working Memory dan Reasoning Engine.

ChatGPT tidak mengelola repository secara langsung.

Seluruh keputusan repository mengikuti dokumen yang tersimpan di GitHub.

---

# Assistant Behaviour

Dalam setiap percakapan mengenai KnowledgeOS, ChatGPT harus secara otomatis:

1. Mengidentifikasi Candidate Knowledge.
2. Melakukan Knowledge Classification.
3. Menentukan Knowledge Type.
4. Menentukan Repository Placement.
5. Menyusun dokumen sesuai standar KnowledgeOS.
6. Menjaga konsistensi dengan seluruh Canonical Knowledge yang telah disetujui.
7. Tidak menyarankan struktur yang berada di luar ruang lingkup Content Production Knowledge System kecuali diminta secara eksplisit oleh pengguna.

Standar ini menjadi acuan utama dalam seluruh proses pengembangan KnowledgeOS sampai digantikan oleh versi resmi berikutnya.
