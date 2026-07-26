# RPS-001 — Recovery Package Specification

> **Status:** Draft  
> **Versi:** 1.0  
> **Kategori:** Canonical Document  
> **Kode Dokumen:** RPS-001  
> **Lokasi Repository:** `98_Operator_Manual/RPS-001_Recovery_Package_Specification_v1.0.md`

---

# Purpose

Recovery Package Specification (RPS) mendefinisikan spesifikasi resmi seluruh **Recovery Package** yang digunakan dalam Knowledge Architecture Ecosystem.

RPS menjadi **Single Source of Truth (SSOT)** yang menetapkan:

- konsep Recovery Package;
- struktur standar setiap Recovery Package;
- metadata yang wajib dimiliki;
- aturan dependency;
- aturan prioritas;
- aturan implementasi;
- aturan versioning.

RPS **tidak** mendefinisikan isi operasional suatu Recovery Package.

Daftar dokumen yang digunakan dalam suatu Recovery Package merupakan implementasi yang dapat berubah tanpa mengubah spesifikasi yang ditetapkan oleh RPS.

---

# Scope

Dokumen ini berlaku untuk seluruh Recovery Package yang digunakan dalam:

- Knowledge Architecture
- Production Architecture
- Project Architecture
- Resource Architecture
- Content Production

Seluruh Recovery Package yang digunakan oleh Operator & Recovery Manual Book (OMB) wajib mengikuti spesifikasi yang ditetapkan dalam dokumen ini.

---

# Terminology

Dokumen ini menggunakan istilah berikut.

| Istilah | Definisi |
|---------|----------|
| Recovery Package | Sekumpulan dokumen yang digunakan untuk memulihkan konteks ChatGPT agar suatu pekerjaan dapat dilanjutkan secara efisien. |
| Package ID | Identitas unik yang membedakan setiap Recovery Package. |
| Package Type | Kategori Recovery Package berdasarkan level pekerjaan. |
| Priority | Tingkat kepentingan suatu dokumen di dalam Recovery Package. |
| Upload Order | Urutan dokumen yang direkomendasikan untuk di-upload ke ChatGPT. |
| Dependency | Hubungan antar Recovery Package atau hubungan terhadap dokumen lain yang diperlukan. |
| Required Document | Dokumen yang wajib tersedia agar Recovery Package dapat digunakan. |
| Optional Document | Dokumen tambahan yang digunakan apabila konteks belum mencukupi. |
| Expected Context | Tingkat konteks yang diharapkan setelah seluruh Recovery Package selesai digunakan. |
| Success Criteria | Kondisi yang menunjukkan bahwa proses pemulihan konteks telah berhasil. |

---

# Hubungan dengan Dokumen Lain

RPS merupakan bagian dari Operator Manual Ecosystem.

Hubungan antar dokumen adalah sebagai berikut.

```text
OMB
↓
Menentukan Recovery Package

↓

RPS
↓
Mendefinisikan Recovery Package

↓

Recovery Package
(Implementasi)

↓

GitHub Repository

↓

ChatGPT Context
```

Dengan pembagian ini:

- **OMB** menjelaskan **kapan** suatu Recovery Package digunakan.
- **RPS** menjelaskan **bagaimana** suatu Recovery Package harus dibangun.
- **Recovery Package** merupakan implementasi yang digunakan oleh operator.
- **GitHub Repository** menjadi tempat penyimpanan seluruh implementasi Recovery Package.

---

# Prinsip Dasar

Recovery Package Specification dibangun berdasarkan lima prinsip berikut.

## 1. Standardized Structure

Seluruh Recovery Package wajib menggunakan struktur yang sama agar mudah dipahami dan dipelihara.

---

## 2. Modular Design

Setiap Recovery Package harus dapat digunakan secara mandiri tanpa bergantung pada paket lain, kecuali apabila dependency telah didefinisikan secara eksplisit.

---

## 3. Progressive Context Recovery

Recovery Package harus memungkinkan pemulihan konteks dilakukan secara bertahap, dimulai dari dokumen yang paling penting hingga dokumen tambahan apabila diperlukan.

---

## 4. Minimum Document Set

Recovery Package harus meminimalkan jumlah dokumen yang perlu di-upload tanpa mengurangi kemampuan ChatGPT memahami konteks pekerjaan.

---

## 5. Separation of Specification and Implementation

RPS hanya mendefinisikan spesifikasi Recovery Package.

Isi aktual Recovery Package tidak menjadi bagian dari dokumen ini dan dapat diperbarui tanpa mengubah spesifikasi kanonis yang telah ditetapkan.

---

# Daftar Isi

- Metadata
- Purpose
- Scope
- Terminology
- Hubungan dengan Dokumen Lain
- Prinsip Dasar
- BAB 1 — Recovery Package Concept
- BAB 2 — Recovery Package Architecture
- BAB 3 — Package Specification Standard
- BAB 4 — Recovery Package Types
- BAB 5 — Dependency Rules
- BAB 6 — Priority Rules
- BAB 7 — Implementation Guide
- BAB 8 — Appendix

- # BAB 1 — Recovery Package Concept

## 1.1 Apa itu Recovery Package

Recovery Package adalah sekumpulan dokumen yang digunakan untuk memulihkan konteks ChatGPT sehingga suatu pekerjaan dapat dilanjutkan secara konsisten tanpa harus meng-upload seluruh repository.

Recovery Package tidak berisi pengetahuan baru.

Recovery Package merupakan mekanisme untuk menyajikan pengetahuan yang telah ada ke dalam percakapan ChatGPT secara efisien.

---

## 1.2 Tujuan Recovery Package

Recovery Package dibuat untuk mencapai tujuan berikut.

- Mempercepat pemulihan konteks.
- Mengurangi jumlah dokumen yang perlu di-upload.
- Menghemat kapasitas konteks ChatGPT.
- Menjamin konsistensi informasi.
- Mengurangi risiko penggunaan dokumen yang tidak relevan.
- Mempermudah operator dalam memulai pekerjaan.

---

## 1.3 Fungsi Recovery Package

Recovery Package memiliki fungsi sebagai berikut.

### Sebagai Paket Konteks

Recovery Package mengelompokkan dokumen yang saling berkaitan sehingga dapat digunakan sebagai satu paket pemulihan.

---

### Sebagai Panduan Upload

Recovery Package menentukan urutan dokumen yang direkomendasikan untuk di-upload ke ChatGPT.

---

### Sebagai Penghubung

Recovery Package menghubungkan Operator & Recovery Manual Book (OMB) dengan dokumen implementasi yang berada di GitHub Repository.

---

### Sebagai Standar Operasional

Recovery Package memastikan seluruh operator menggunakan kumpulan dokumen yang sama untuk pekerjaan yang sama.

---

## 1.4 Karakteristik Recovery Package

Setiap Recovery Package wajib memiliki karakteristik berikut.

- Modular
- Konsisten
- Mudah diperbarui
- Dapat digunakan kembali
- Independen
- Memiliki dependency yang jelas
- Memiliki prioritas upload yang jelas

---

## 1.5 Siklus Hidup Recovery Package

Setiap Recovery Package mengikuti siklus hidup berikut.

```text
Dirancang
↓
Dispesifikasikan
↓
Diimplementasikan
↓
Digunakan
↓
Direvisi
↓
Dipublikasikan
↓
Diarsipkan
```

Seluruh perubahan terhadap Recovery Package harus mengikuti mekanisme versioning yang ditetapkan dalam dokumen ini.

---

## 1.6 Hubungan dengan OMB

Operator tidak memilih dokumen secara langsung.

Operator menggunakan alur berikut.

```text
Operator
↓
OMB
↓
RM-ID
↓
Recovery Package
↓
GitHub Repository
↓
Download
↓
Upload ke ChatGPT
↓
Mulai bekerja
```

Dengan demikian:

- OMB menentukan **Recovery Package** yang digunakan.
- Recovery Package menentukan **dokumen** yang digunakan.
- GitHub menyediakan implementasi dokumen tersebut.

---

# BAB 2 — Recovery Package Architecture

## 2.1 Gambaran Arsitektur

Recovery Package terdiri atas dua lapisan utama.

```text
Specification Layer
↓
Implementation Layer
```

Lapisan spesifikasi bersifat stabil dan jarang berubah.

Lapisan implementasi dapat berubah mengikuti perkembangan proyek tanpa mengubah spesifikasi.

---

## 2.2 Arsitektur Recovery Package

Struktur umum Recovery Package adalah sebagai berikut.

```text
Recovery Package
│
├── Package Metadata
│
├── Package Type
│
├── Dependency
│
├── Upload Priority
│
├── Upload Order
│
├── Required Documents
│
├── Optional Documents
│
├── Expected Context
│
└── Success Criteria
```

Seluruh Recovery Package wajib mengikuti struktur ini.

---

## 2.3 Lapisan Arsitektur

Recovery Package dibangun menggunakan tiga lapisan.

### Layer 1 — Specification

Menjelaskan aturan dan struktur Recovery Package.

Contoh.

- Metadata
- Package Structure
- Dependency Rules
- Priority Rules

Layer ini didefinisikan oleh **RPS**.

---

### Layer 2 — Package

Merupakan implementasi dari spesifikasi.

Contoh.

- RP-KN
- RP-PD
- RP-PJ
- RP-RS
- RP-CT

Layer ini menggunakan aturan yang ditetapkan oleh RPS.

---

### Layer 3 — Repository

Merupakan kumpulan dokumen aktual yang digunakan oleh setiap Recovery Package.

Contoh.

- Principle
- Framework
- Standard
- Workflow
- Production Bible
- Project Bible
- Character Bible

Layer ini dapat berubah tanpa mengubah RPS.

---

## 2.4 Hubungan Antar Layer

```text
RPS
↓
Recovery Package
↓
Repository
↓
ChatGPT Context
```

Hubungan tersebut memastikan bahwa perubahan pada dokumen implementasi tidak memengaruhi spesifikasi Recovery Package.

---

## 2.5 Komponen Recovery Package

Setiap Recovery Package wajib memiliki komponen berikut.

| Komponen | Fungsi |
|----------|--------|
| Package Metadata | Identitas resmi Recovery Package. |
| Package Type | Menentukan kategori paket. |
| Dependency | Menentukan hubungan dengan paket lain. |
| Upload Priority | Menentukan tingkat prioritas dokumen. |
| Upload Order | Menentukan urutan upload ke ChatGPT. |
| Required Documents | Menentukan dokumen wajib. |
| Optional Documents | Menentukan dokumen tambahan. |
| Expected Context | Menjelaskan konteks yang diharapkan setelah paket digunakan. |
| Success Criteria | Menentukan indikator keberhasilan pemulihan konteks. |

---

## 2.6 Prinsip Arsitektur

Arsitektur Recovery Package mengikuti prinsip berikut.

### Single Responsibility

Satu Recovery Package hanya memiliki satu tujuan utama.

---

### Low Coupling

Recovery Package tidak boleh bergantung secara berlebihan pada paket lain.

---

### High Cohesion

Seluruh dokumen dalam satu Recovery Package harus saling berkaitan dan mendukung tujuan yang sama.

---

### Reusability

Recovery Package harus dapat digunakan kembali pada berbagai proyek tanpa perubahan struktur.

---

### Extensibility

Recovery Package harus dapat diperluas dengan penambahan dokumen implementasi tanpa mengubah spesifikasi yang telah ditetapkan oleh RPS.

---

## Ringkasan

Recovery Package dibangun menggunakan pemisahan yang jelas antara spesifikasi dan implementasi.

```text
RPS
↓
Mendefinisikan Struktur
↓
Recovery Package
↓
Mengelompokkan Dokumen
↓
Repository
↓
Menyimpan Dokumen
↓
ChatGPT
↓
Menggunakan Konteks
```

Pendekatan ini memastikan bahwa Recovery Package tetap konsisten, mudah dipelihara, dan dapat berkembang tanpa mengubah spesifikasi kanonis.

# BAB 3 — Package Specification Standard

BAB ini menetapkan spesifikasi resmi yang wajib digunakan oleh seluruh Recovery Package.

Seluruh Recovery Package harus mengikuti struktur, metadata, dan aturan yang dijelaskan pada bab ini agar memiliki format yang konsisten di seluruh Knowledge Architecture Ecosystem.

---

# 3.1 Tujuan

Package Specification Standard bertujuan untuk:

- menyeragamkan struktur seluruh Recovery Package;
- mempermudah proses pemeliharaan;
- memastikan kompatibilitas dengan OMB;
- mendukung versioning yang konsisten;
- memungkinkan pengembangan Recovery Package tanpa mengubah spesifikasi.

---

# 3.2 Struktur Standar Recovery Package

Setiap Recovery Package wajib menggunakan struktur berikut.

```text
Recovery Package
│
├── Metadata
├── Purpose
├── Scope
├── Package Information
├── Dependency
├── Required Documents
├── Optional Documents
├── Upload Priority
├── Upload Order
├── Expected Context
├── Success Criteria
├── Notes
└── Revision History
```

Struktur ini merupakan format resmi yang harus dipertahankan pada seluruh Recovery Package.

---

# 3.3 Metadata Standar

Setiap Recovery Package wajib memiliki metadata berikut.

| Metadata | Keterangan |
|----------|------------|
| Package ID | Identitas unik Recovery Package. |
| Package Name | Nama resmi Recovery Package. |
| Version | Versi paket. |
| Status | Draft, Review, atau LOCK. |
| Package Type | Jenis Recovery Package. |
| Repository Location | Lokasi penyimpanan paket di GitHub. |
| Last Updated | Tanggal pembaruan terakhir. |

Metadata harus ditempatkan pada bagian awal dokumen.

---

# 3.4 Package Information

Bagian ini menjelaskan informasi dasar Recovery Package.

Minimal harus berisi:

| Komponen | Fungsi |
|----------|--------|
| Purpose | Tujuan Recovery Package. |
| Scope | Ruang lingkup penggunaan. |
| Applicable RM-ID | Daftar RM-ID yang menggunakan paket ini. |
| Applicable Level | Level pekerjaan yang didukung. |

Recovery Package hanya boleh digunakan untuk RM-ID yang telah ditentukan.

---

# 3.5 Dependency Specification

Dependency menjelaskan hubungan Recovery Package dengan paket atau dokumen lain.

Dependency dibagi menjadi tiga kategori.

| Jenis | Keterangan |
|-------|------------|
| Mandatory | Wajib tersedia sebelum paket digunakan. |
| Recommended | Sangat disarankan untuk digunakan. |
| Optional | Digunakan apabila diperlukan. |

Dependency harus dinyatakan secara eksplisit.

Recovery Package tidak boleh memiliki dependency tersembunyi.

---

# 3.6 Required Documents

Required Documents merupakan dokumen minimum yang wajib tersedia agar Recovery Package dapat digunakan.

Aturan:

1. Harus merupakan dokumen resmi.
2. Harus menggunakan versi terbaru yang berlaku.
3. Tidak boleh digantikan oleh dokumen lain kecuali telah ditetapkan secara resmi.

Required Documents menjadi dasar proses pemulihan konteks.

---

# 3.7 Optional Documents

Optional Documents merupakan dokumen tambahan yang digunakan apabila konteks yang diperoleh dari Required Documents belum mencukupi.

Aturan:

- hanya digunakan bila diperlukan;
- tidak menggantikan Required Documents;
- dapat ditambahkan secara bertahap.

---

# 3.8 Upload Priority

Setiap dokumen dalam Recovery Package wajib memiliki tingkat prioritas.

**Tabel 3-1. Upload Priority**

| Prioritas | Arti |
|-----------|------|
| ★★★★★ | Wajib |
| ★★★★☆ | Sangat Disarankan |
| ★★★☆☆ | Disarankan |
| ★★☆☆☆ | Referensi |
| ★☆☆☆☆ | Opsional |

Prioritas menentukan urutan upload ketika kapasitas konteks ChatGPT terbatas.

---

# 3.9 Upload Order

Upload Order menentukan urutan dokumen yang direkomendasikan.

Urutan umum adalah sebagai berikut.

```text
Required Documents
★★★★★
↓
Recommended Documents
★★★★☆
↓
Additional Documents
★★★☆☆
↓
Reference Documents
★★☆☆☆
↓
Optional Documents
★☆☆☆☆
```

Operator harus mengikuti urutan ini kecuali terdapat pengecualian yang telah didefinisikan.

---

# 3.10 Expected Context

Expected Context menjelaskan kondisi yang diharapkan setelah Recovery Package selesai digunakan.

Contoh Expected Context.

- ChatGPT memahami struktur pekerjaan.
- ChatGPT mengenali terminologi yang digunakan.
- ChatGPT memahami hubungan antar dokumen.
- ChatGPT mampu melanjutkan pekerjaan tanpa meminta konteks dasar lagi.

Expected Context harus dapat diverifikasi oleh operator.

---

# 3.11 Success Criteria

Success Criteria menentukan kapan proses pemulihan konteks dianggap berhasil.

Minimal memenuhi seluruh kondisi berikut.

- Required Documents telah di-upload.
- ChatGPT memahami konteks pekerjaan.
- ChatGPT mengenali istilah utama.
- ChatGPT mampu memberikan respons yang konsisten.
- Operator dapat melanjutkan pekerjaan tanpa mengulang penjelasan dasar.

Apabila salah satu kondisi belum terpenuhi, operator dapat menambahkan Optional Documents sesuai prioritas.

---

# 3.12 Notes

Bagian Notes digunakan untuk mencatat informasi tambahan yang tidak termasuk ke dalam struktur utama.

Contoh.

- pengecualian penggunaan;
- batasan Recovery Package;
- kondisi khusus;
- rekomendasi implementasi.

Bagian ini bersifat opsional.

---

# 3.13 Revision History

Seluruh Recovery Package wajib memiliki riwayat revisi.

**Tabel 3-2. Revision History**

| Version | Date | Status | Description |
|---------|------|--------|-------------|
| 1.0 | YYYY-MM-DD | Draft | Initial Release |

Riwayat revisi harus diperbarui setiap kali Recovery Package mengalami perubahan.

---

# 3.14 Template Recovery Package

Seluruh Recovery Package harus mengikuti template berikut.

```text
Metadata

Purpose

Scope

Package Information

Dependency

Required Documents

Optional Documents

Upload Priority

Upload Order

Expected Context

Success Criteria

Notes

Revision History
```

Template ini menjadi format resmi seluruh Recovery Package.

---

# Ringkasan

Package Specification Standard memastikan seluruh Recovery Package memiliki struktur yang seragam.

```text
Recovery Package
↓
Metadata
↓
Dependency
↓
Documents
↓
Priority
↓
Upload Order
↓
Expected Context
↓
Success Criteria
```

Dengan spesifikasi ini, seluruh Recovery Package dapat dikembangkan, dipelihara, dan digunakan secara konsisten tanpa mengubah struktur dasar yang telah ditetapkan oleh **RPS-001 — Recovery Package Specification**.

# BAB 4 — Recovery Package Types

BAB ini menetapkan jenis-jenis Recovery Package yang diakui secara resmi dalam Knowledge Architecture Ecosystem.

Setiap Recovery Package harus termasuk ke dalam salah satu Package Type yang didefinisikan pada bab ini.

Package Type menentukan ruang lingkup penggunaan, level pekerjaan, dan hubungan dengan Recovery Package lainnya.

---

# 4.1 Daftar Package Type

**Tabel 4-1. Recovery Package Types**

| Package ID | Package Name | Level | Digunakan Untuk |
|------------|--------------|-------|-----------------|
| RP-KN | Knowledge Recovery Package | Knowledge | Pekerjaan Knowledge Architecture |
| RP-PD | Production Recovery Package | Production | Pekerjaan Production Architecture |
| RP-PJ | Project Recovery Package | Project | Pekerjaan Project Architecture |
| RP-RS | Resource Recovery Package | Resource | Pekerjaan Resource Architecture |
| RP-CT | Content Recovery Package | Content | Produksi Konten |

Seluruh Recovery Package wajib menggunakan salah satu Package ID di atas.

---

# 4.2 RP-KN — Knowledge Recovery Package

## Tujuan

Digunakan untuk memulihkan konteks pekerjaan pada level Knowledge Architecture.

## Ruang Lingkup

Mendukung pekerjaan seperti:

- Principle
- Framework
- Standard
- Registry
- Metadata
- Repository Rule

## Karakteristik

- Menjadi dasar bagi seluruh Package Type lainnya.
- Memiliki dependency paling sedikit.
- Tidak bergantung pada Project tertentu.

---

# 4.3 RP-PD — Production Recovery Package

## Tujuan

Digunakan untuk memulihkan konteks sistem produksi.

## Ruang Lingkup

Mendukung pekerjaan seperti:

- Workflow
- Production Bible
- Quality Gate
- Production Process

## Karakteristik

- Bergantung pada Knowledge Recovery Package apabila diperlukan.
- Menjadi dasar bagi Project Recovery Package.

---

# 4.4 RP-PJ — Project Recovery Package

## Tujuan

Digunakan untuk memulihkan konteks suatu proyek.

## Ruang Lingkup

Mendukung pekerjaan seperti:

- Project Bible
- Character Bible
- World Bible
- Brand Bible

## Karakteristik

- Bergantung pada Production Recovery Package.
- Dapat memiliki dokumen khusus sesuai kebutuhan proyek.

---

# 4.5 RP-RS — Resource Recovery Package

## Tujuan

Digunakan untuk memulihkan konteks pengelolaan resource.

## Ruang Lingkup

Mendukung pekerjaan seperti:

- Asset Library
- Repository Asset
- Resource Management
- Template Repository

## Karakteristik

- Digunakan ketika pekerjaan berkaitan dengan aset.
- Bersifat lintas proyek.

---

# 4.6 RP-CT — Content Recovery Package

## Tujuan

Digunakan untuk memulihkan konteks produksi konten.

## Ruang Lingkup

Mendukung pekerjaan seperti:

- Carousel
- Poster
- Video
- Comic
- Caption

## Karakteristik

- Merupakan Package Type yang paling dekat dengan proses produksi akhir.
- Dapat bergantung pada Project Recovery Package.

---

# 4.7 Hubungan Antar Package Type

Hubungan antar Package Type mengikuti hierarki berikut.

```text
RP-KN
(Knowledge)
↓
RP-PD
(Production)
↓
RP-PJ
(Project)
↓
RP-RS
(Resource)
↓
RP-CT
(Content)
```

Hierarki ini menunjukkan arah ketergantungan konseptual, bukan kewajiban bahwa seluruh Package Type harus selalu digunakan bersama.

---

# BAB 5 — Dependency Rules

BAB ini menetapkan aturan resmi mengenai dependency antar Recovery Package.

Dependency memastikan setiap Recovery Package hanya menggunakan dokumen yang benar-benar diperlukan.

---

# 5.1 Prinsip Dependency

Recovery Package mengikuti prinsip berikut.

1. Dependency harus eksplisit.
2. Dependency harus seminimal mungkin.
3. Dependency tidak boleh membentuk siklus (circular dependency).
4. Dependency harus terdokumentasi.
5. Dependency dapat berubah tanpa mengubah struktur RPS.

---

# 5.2 Jenis Dependency

**Tabel 5-2. Dependency Type**

| Jenis | Keterangan |
|--------|------------|
| Mandatory | Wajib tersedia sebelum Recovery Package digunakan. |
| Recommended | Sangat disarankan untuk meningkatkan kualitas konteks. |
| Optional | Digunakan hanya apabila diperlukan. |

---

# 5.3 Dependency Matrix

**Tabel 5-3. Dependency Matrix**

| Package | Mandatory | Recommended | Optional |
|---------|-----------|-------------|----------|
| RP-KN | — | — | — |
| RP-PD | RP-KN | — | RP-RS |
| RP-PJ | RP-PD | RP-KN | RP-RS |
| RP-RS | RP-KN | RP-PD | RP-PJ |
| RP-CT | RP-PJ | RP-PD | RP-RS |

Matriks ini menunjukkan dependency konseptual antar Package Type.

Implementasi dapat menggunakan subset dari dependency tersebut sesuai kebutuhan pekerjaan.

---

# 5.4 Circular Dependency

Circular Dependency tidak diperbolehkan.

Contoh yang benar.

```text
RP-KN
↓
RP-PD
↓
RP-PJ
```

Contoh yang tidak diperbolehkan.

```text
RP-KN
↓
RP-PD
↓
RP-PJ
↑
└──────────────┘
```

Dependency harus selalu membentuk alur satu arah.

---

# 5.5 Dependency Resolution

Apabila sebuah Recovery Package memiliki dependency, operator menggunakan urutan berikut.

```text
Mandatory
↓
Recommended
↓
Optional
```

Dependency dengan prioritas lebih tinggi harus diselesaikan terlebih dahulu sebelum menggunakan dependency berikutnya.

---

# 5.6 Prinsip Implementasi Dependency

Seluruh implementasi Recovery Package harus mengikuti prinsip berikut.

### Explicit

Dependency harus dinyatakan secara jelas.

---

### Minimal

Gunakan dependency sesedikit mungkin.

---

### Predictable

Urutan dependency harus konsisten.

---

### Reusable

Dependency harus dapat digunakan kembali oleh Recovery Package lain.

---

### Maintainable

Perubahan dependency tidak boleh mengubah struktur dasar Recovery Package.

---

# Ringkasan

Recovery Package Type menentukan **kategori** sebuah Recovery Package.

Dependency Rules menentukan **hubungan** antar Recovery Package.

```text
Package Type
↓
Dependency
↓
Recovery Package
↓
Repository
↓
ChatGPT Context
```

Dengan aturan ini, seluruh Recovery Package dapat saling berinteraksi secara konsisten tanpa menghasilkan dependency yang kompleks atau sulit dipelihara.

# BAB 6 — Priority Rules

BAB ini menetapkan aturan resmi mengenai prioritas dokumen dalam setiap Recovery Package.

Tujuannya adalah memastikan proses pemulihan konteks dilakukan secara efisien dengan menggunakan dokumen yang paling penting terlebih dahulu.

---

# 6.1 Tujuan Priority Rules

Priority Rules dibuat untuk:

- mengurangi jumlah dokumen yang perlu di-upload;
- menghemat kapasitas konteks ChatGPT;
- mempercepat proses pemulihan konteks;
- menjaga konsistensi antar Recovery Package;
- menjadi dasar pengambilan keputusan bagi operator.

---

# 6.2 Tingkat Prioritas

Seluruh Recovery Package menggunakan lima tingkat prioritas.

**Tabel 6-1. Priority Level**

| Prioritas | Nama | Penggunaan |
|-----------|------|------------|
| ★★★★★ | Required | Wajib di-upload terlebih dahulu. |
| ★★★★☆ | Recommended | Sangat disarankan untuk meningkatkan kualitas konteks. |
| ★★★☆☆ | Supporting | Digunakan apabila konteks tambahan diperlukan. |
| ★★☆☆☆ | Reference | Digunakan sebagai referensi. |
| ★☆☆☆☆ | Optional | Digunakan hanya pada kondisi tertentu. |

Prioritas ditetapkan pada tingkat dokumen, bukan pada tingkat Recovery Package.

---

# 6.3 Aturan Penentuan Prioritas

Penentuan prioritas harus mempertimbangkan faktor berikut.

### Kontribusi terhadap Konteks

Semakin besar kontribusi suatu dokumen terhadap pemahaman ChatGPT, semakin tinggi prioritasnya.

---

### Ketergantungan

Dokumen yang menjadi dependency utama harus memiliki prioritas lebih tinggi.

---

### Frekuensi Penggunaan

Dokumen yang digunakan hampir pada setiap pekerjaan sebaiknya memiliki prioritas yang lebih tinggi dibanding dokumen yang hanya digunakan pada kasus tertentu.

---

### Stabilitas

Dokumen yang jarang berubah lebih layak ditempatkan pada prioritas tinggi dibanding dokumen yang sering berubah.

---

# 6.4 Strategi Upload

Operator harus menggunakan strategi berikut.

```text
Upload
★★★★★
↓
Verifikasi Konteks
↓
Sudah Memadai?
↓
YA
↓
Mulai Bekerja

ATAU

TIDAK
↓
Upload
★★★★☆
↓
Verifikasi Kembali
↓
Masih Belum Cukup?
↓
Upload
★★★☆☆
↓
Lanjutkan Hingga Konteks Memadai
```

Dokumen dengan prioritas lebih rendah hanya digunakan apabila konteks belum memadai.

---

# 6.5 Penghentian Upload

Operator harus menghentikan proses upload apabila:

- ChatGPT telah memahami konteks pekerjaan;
- Expected Context telah tercapai;
- Success Criteria telah terpenuhi.

Menambahkan dokumen setelah kondisi tersebut tercapai tidak direkomendasikan kecuali terdapat kebutuhan khusus.

---

# BAB 7 — Implementation Guide

BAB ini menjelaskan aturan implementasi Recovery Package.

RPS hanya mendefinisikan spesifikasi.

Implementasi Recovery Package dilakukan melalui dokumen Recovery Package yang mengikuti spesifikasi tersebut.

---

# 7.1 Prinsip Implementasi

Setiap Recovery Package harus:

- mengikuti struktur standar pada BAB 3;
- menggunakan Package Type pada BAB 4;
- mengikuti Dependency Rules pada BAB 5;
- mengikuti Priority Rules pada BAB 6.

Tidak diperbolehkan membuat Recovery Package di luar spesifikasi yang ditetapkan oleh RPS.

---

# 7.2 Versioning

Seluruh Recovery Package menggunakan sistem versioning.

**Tabel 7-1. Version Status**

| Status | Keterangan |
|--------|------------|
| Draft | Sedang disusun. |
| Review | Sedang ditinjau. |
| LOCK | Versi kanonis yang telah disetujui. |

Perubahan terhadap Recovery Package dilakukan melalui versi baru.

Versi yang telah berstatus **LOCK** tidak diubah secara langsung.

---

# 7.3 Revisi

Setiap revisi harus:

1. memiliki alasan yang jelas;
2. memperbarui Version;
3. memperbarui Revision History;
4. menjaga kompatibilitas terhadap OMB dan RPS.

---

# 7.4 Kompatibilitas

Recovery Package harus kompatibel dengan:

- Operator & Recovery Manual Book (OMB);
- Recovery Package Specification (RPS);
- Knowledge Architecture Ecosystem.

Implementasi tidak boleh bertentangan dengan spesifikasi yang telah ditetapkan.

---

# BAB 8 — Appendix

## Lampiran A — Struktur Recovery Package

```text
Metadata
↓
Purpose
↓
Scope
↓
Package Information
↓
Dependency
↓
Required Documents
↓
Optional Documents
↓
Upload Priority
↓
Upload Order
↓
Expected Context
↓
Success Criteria
↓
Notes
↓
Revision History
```

---

## Lampiran B — Hubungan Dokumen

```text
OMB
↓
Menentukan Recovery Package
↓
RPS
↓
Mendefinisikan Recovery Package
↓
Recovery Package
↓
Mengelompokkan Dokumen
↓
GitHub Repository
↓
ChatGPT Context
```

---

## Lampiran C — Daftar Singkatan

| Singkatan | Kepanjangan |
|-----------|-------------|
| RPS | Recovery Package Specification |
| RP | Recovery Package |
| RP-KN | Knowledge Recovery Package |
| RP-PD | Production Recovery Package |
| RP-PJ | Project Recovery Package |
| RP-RS | Resource Recovery Package |
| RP-CT | Content Recovery Package |
| OMB | Operator & Recovery Manual Book |
| RM | Recovery Matrix |
| SSOT | Single Source of Truth |

---

## Lampiran D — Riwayat Revisi

| Versi | Tanggal | Status | Keterangan |
|--------|---------|--------|------------|
| 1.0 | 27 Juli 2026 | Draft | Penyusunan awal RPS-001. |

---

# Penutup

Recovery Package Specification (RPS) menetapkan spesifikasi resmi yang menjadi dasar penyusunan seluruh Recovery Package dalam Knowledge Architecture Ecosystem.

Dengan memisahkan **spesifikasi** dari **implementasi**, RPS memastikan bahwa Recovery Package dapat berkembang tanpa mengubah struktur dasar yang telah ditetapkan.

Bersama **Operator & Recovery Manual Book (OMB)**, RPS membentuk fondasi sistem pemulihan konteks yang konsisten, modular, dan mudah dipelihara.

---

# Status Dokumen

**Nama Dokumen**

RPS-001 — Recovery Package Specification

**Versi**

1.0

**Status**

Draft

**Kategori**

Canonical Document

# BAB 6 — Priority Rules

BAB ini menetapkan aturan resmi mengenai prioritas dokumen dalam setiap Recovery Package.

Tujuannya adalah memastikan proses pemulihan konteks dilakukan secara efisien dengan menggunakan dokumen yang paling penting terlebih dahulu.

---

# 6.1 Tujuan Priority Rules

Priority Rules dibuat untuk:

- mengurangi jumlah dokumen yang perlu di-upload;
- menghemat kapasitas konteks ChatGPT;
- mempercepat proses pemulihan konteks;
- menjaga konsistensi antar Recovery Package;
- menjadi dasar pengambilan keputusan bagi operator.

---

# 6.2 Tingkat Prioritas

Seluruh Recovery Package menggunakan lima tingkat prioritas.

**Tabel 6-1. Priority Level**

| Prioritas | Nama | Penggunaan |
|-----------|------|------------|
| ★★★★★ | Required | Wajib di-upload terlebih dahulu. |
| ★★★★☆ | Recommended | Sangat disarankan untuk meningkatkan kualitas konteks. |
| ★★★☆☆ | Supporting | Digunakan apabila konteks tambahan diperlukan. |
| ★★☆☆☆ | Reference | Digunakan sebagai referensi. |
| ★☆☆☆☆ | Optional | Digunakan hanya pada kondisi tertentu. |

Prioritas ditetapkan pada tingkat dokumen, bukan pada tingkat Recovery Package.

---

# 6.3 Aturan Penentuan Prioritas

Penentuan prioritas harus mempertimbangkan faktor berikut.

### Kontribusi terhadap Konteks

Semakin besar kontribusi suatu dokumen terhadap pemahaman ChatGPT, semakin tinggi prioritasnya.

---

### Ketergantungan

Dokumen yang menjadi dependency utama harus memiliki prioritas lebih tinggi.

---

### Frekuensi Penggunaan

Dokumen yang digunakan hampir pada setiap pekerjaan sebaiknya memiliki prioritas yang lebih tinggi dibanding dokumen yang hanya digunakan pada kasus tertentu.

---

### Stabilitas

Dokumen yang jarang berubah lebih layak ditempatkan pada prioritas tinggi dibanding dokumen yang sering berubah.

---

# 6.4 Strategi Upload

Operator harus menggunakan strategi berikut.

```text
Upload
★★★★★
↓
Verifikasi Konteks
↓
Sudah Memadai?
↓
YA
↓
Mulai Bekerja

ATAU

TIDAK
↓
Upload
★★★★☆
↓
Verifikasi Kembali
↓
Masih Belum Cukup?
↓
Upload
★★★☆☆
↓
Lanjutkan Hingga Konteks Memadai
```

Dokumen dengan prioritas lebih rendah hanya digunakan apabila konteks belum memadai.

---

# 6.5 Penghentian Upload

Operator harus menghentikan proses upload apabila:

- ChatGPT telah memahami konteks pekerjaan;
- Expected Context telah tercapai;
- Success Criteria telah terpenuhi.

Menambahkan dokumen setelah kondisi tersebut tercapai tidak direkomendasikan kecuali terdapat kebutuhan khusus.

---

# BAB 7 — Implementation Guide

BAB ini menjelaskan aturan implementasi Recovery Package.

RPS hanya mendefinisikan spesifikasi.

Implementasi Recovery Package dilakukan melalui dokumen Recovery Package yang mengikuti spesifikasi tersebut.

---

# 7.1 Prinsip Implementasi

Setiap Recovery Package harus:

- mengikuti struktur standar pada BAB 3;
- menggunakan Package Type pada BAB 4;
- mengikuti Dependency Rules pada BAB 5;
- mengikuti Priority Rules pada BAB 6.

Tidak diperbolehkan membuat Recovery Package di luar spesifikasi yang ditetapkan oleh RPS.

---

# 7.2 Versioning

Seluruh Recovery Package menggunakan sistem versioning.

**Tabel 7-1. Version Status**

| Status | Keterangan |
|--------|------------|
| Draft | Sedang disusun. |
| Review | Sedang ditinjau. |
| LOCK | Versi kanonis yang telah disetujui. |

Perubahan terhadap Recovery Package dilakukan melalui versi baru.

Versi yang telah berstatus **LOCK** tidak diubah secara langsung.

---

# 7.3 Revisi

Setiap revisi harus:

1. memiliki alasan yang jelas;
2. memperbarui Version;
3. memperbarui Revision History;
4. menjaga kompatibilitas terhadap OMB dan RPS.

---

# 7.4 Kompatibilitas

Recovery Package harus kompatibel dengan:

- Operator & Recovery Manual Book (OMB);
- Recovery Package Specification (RPS);
- Knowledge Architecture Ecosystem.

Implementasi tidak boleh bertentangan dengan spesifikasi yang telah ditetapkan.

---

# BAB 8 — Appendix

## Lampiran A — Struktur Recovery Package

```text
Metadata
↓
Purpose
↓
Scope
↓
Package Information
↓
Dependency
↓
Required Documents
↓
Optional Documents
↓
Upload Priority
↓
Upload Order
↓
Expected Context
↓
Success Criteria
↓
Notes
↓
Revision History
```

---

## Lampiran B — Hubungan Dokumen

```text
OMB
↓
Menentukan Recovery Package
↓
RPS
↓
Mendefinisikan Recovery Package
↓
Recovery Package
↓
Mengelompokkan Dokumen
↓
GitHub Repository
↓
ChatGPT Context
```

---

## Lampiran C — Daftar Singkatan

| Singkatan | Kepanjangan |
|-----------|-------------|
| RPS | Recovery Package Specification |
| RP | Recovery Package |
| RP-KN | Knowledge Recovery Package |
| RP-PD | Production Recovery Package |
| RP-PJ | Project Recovery Package |
| RP-RS | Resource Recovery Package |
| RP-CT | Content Recovery Package |
| OMB | Operator & Recovery Manual Book |
| RM | Recovery Matrix |
| SSOT | Single Source of Truth |

---

## Lampiran D — Riwayat Revisi

| Versi | Tanggal | Status | Keterangan |
|--------|---------|--------|------------|
| 1.0 | 27 Juli 2026 | Draft | Penyusunan awal RPS-001. |

---

# Penutup

Recovery Package Specification (RPS) menetapkan spesifikasi resmi yang menjadi dasar penyusunan seluruh Recovery Package dalam Knowledge Architecture Ecosystem.

Dengan memisahkan **spesifikasi** dari **implementasi**, RPS memastikan bahwa Recovery Package dapat berkembang tanpa mengubah struktur dasar yang telah ditetapkan.

Bersama **Operator & Recovery Manual Book (OMB)**, RPS membentuk fondasi sistem pemulihan konteks yang konsisten, modular, dan mudah dipelihara.

---

# Status Dokumen

**Nama Dokumen**

RPS-001 — Recovery Package Specification

**Versi**

1.0

**Status**

Draft

**Kategori**

Canonical Document

