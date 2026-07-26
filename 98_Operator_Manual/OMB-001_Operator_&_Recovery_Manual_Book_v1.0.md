# OMB-001 — Operator & Recovery Manual Book

> **Status:** LOCK  
> **Versi:** 1.0  
> **Kategori:** Canonical Document  
> **Kode Dokumen:** OMB-001  
> **Lokasi Repository:** `98_Operator_Manual/OMB-001_Operator_&_Recovery_Manual_Book_v1.0.md`

---

# Slogan

> **Satu Buku. Satu Alur. Satu Panduan Operasional.**

---

# Purpose

Operator & Recovery Manual Book (OMB) adalah panduan operasional yang membantu operator menentukan dokumen yang perlu digunakan untuk suatu pekerjaan serta memulihkan konteks ChatGPT ketika konteks percakapan hilang.

OMB bukan dokumentasi arsitektur.

OMB bukan Production Bible.

OMB bukan Standard.

OMB adalah buku panduan operasional yang menjawab pertanyaan berikut.

- Saya sedang mengerjakan apa?
- Dokumen apa yang harus saya gunakan?
- Dokumen apa yang harus saya download dari GitHub?
- Dokumen apa yang harus saya upload ke ChatGPT?
- Dalam urutan apa dokumen tersebut di-upload?
- Hasil apa yang diharapkan?
- Apa saja catatan yang perlu diperhatikan?

OMB dirancang agar operator dapat bekerja secara efisien tanpa harus mengingat seluruh Knowledge Architecture Ecosystem.

---

# Scope

OMB berlaku untuk seluruh Knowledge Architecture Ecosystem, termasuk namun tidak terbatas pada:

- Knowledge Architecture
- Production Architecture
- Project Architecture
- Resource Architecture
- Content Production

OMB bersifat universal dan tidak bergantung pada proyek tertentu.

---

# Intended Users

Dokumen ini ditujukan bagi:

- Operator Knowledge Architecture
- Repository Maintainer
- Project Architect
- Content Producer
- AI Operator

---

# Kapan Menggunakan OMB

Gunakan OMB ketika:

- memulai chat baru;
- ChatGPT kehilangan konteks;
- berpindah perangkat;
- memulai pekerjaan baru;
- melanjutkan pekerjaan lama;
- ragu menentukan dokumen yang harus digunakan;
- ingin mengetahui dokumen minimum yang perlu di-upload ke ChatGPT.

---

# Daftar Isi

- Panduan Navigasi Cepat

- BAB 1 — Pendahuluan

- BAB 2 — Level Pekerjaan

- BAB 3 — Paket Pemulihan

- BAB 4 — Matriks Pemulihan

- BAB 5 — Matriks Prioritas Pemulihan

- BAB 6 — Skenario Operasional

- BAB 7 — Lampiran

---

# Panduan Navigasi Cepat

Gunakan panduan berikut untuk langsung menuju bagian yang sesuai dengan kebutuhan Anda.

| Jika ingin... | Buka |
|---------------|------|
| Mengetahui tujuan OMB | BAB 1 — Pendahuluan |
| Menentukan level pekerjaan | BAB 2 — Level Pekerjaan |
| Memahami Paket Pemulihan | BAB 3 — Paket Pemulihan |
| Menentukan dokumen yang harus digunakan | BAB 4 — Matriks Pemulihan |
| Menentukan urutan upload dokumen | BAB 5 — Matriks Prioritas Pemulihan |
| Melihat contoh penggunaan OMB | BAB 6 — Skenario Operasional |
| Melihat referensi tambahan | BAB 7 — Lampiran |

---

# BAB 1 — Pendahuluan

## 1.1 Apa itu OMB

Operator & Recovery Manual Book (OMB) adalah buku panduan operasional yang membantu operator menentukan dokumen yang tepat sebelum bekerja menggunakan ChatGPT.

OMB tidak menjelaskan isi setiap Canonical Document.

OMB tidak menggantikan Production Bible maupun Project Bible.

OMB menjadi pusat navigasi operasional yang menghubungkan pekerjaan operator dengan dokumen yang diperlukan.

---

## 1.2 Filosofi OMB

OMB dibangun berdasarkan prinsip berikut.

> Operator tidak perlu mengingat seluruh Knowledge Architecture Ecosystem.

Operator cukup mengetahui:

- pekerjaan yang akan dilakukan;
- Matriks Pemulihan yang sesuai;
- Paket Pemulihan yang digunakan;
- dokumen yang perlu di-download;
- dokumen yang perlu di-upload.

Dengan demikian operator tidak perlu membuka seluruh repository untuk memulai pekerjaan.

---

## 1.3 Cara Menggunakan OMB

Gunakan langkah berikut.

```text
Tentukan pekerjaan
↓
Buka BAB 4 — Matriks Pemulihan
↓
Cari melalui Tampilan Operator
atau
Tampilan Arsitektur
↓
Temukan RM-ID
↓
Lihat Paket Pemulihan
↓
Download dokumen dari GitHub
↓
Upload ke ChatGPT
↓
Mulai bekerja
```

---

## 1.4 Prinsip Dasar

OMB menggunakan lima prinsip utama.

### 1. Minimum Document Set

Gunakan dokumen sesedikit mungkin.

### 2. Maximum Context Recovery

Pulihkan konteks sebanyak mungkin.

### 3. Need to Know

Gunakan hanya dokumen yang benar-benar diperlukan.

### 4. Progressive Context

Tambahkan dokumen secara bertahap sesuai kebutuhan.

### 5. Universal Workflow

Workflow yang sama berlaku untuk seluruh proyek.

---

# BAB 2 — Level Pekerjaan

Sebelum menentukan dokumen yang diperlukan, operator harus menentukan level pekerjaan.

Seluruh pekerjaan dikelompokkan ke dalam lima level.

| Level | Fokus | Contoh |
|--------|-------|---------|
| Knowledge | Pengembangan Knowledge Architecture | Principle, Framework, Standard, Registry |
| Production | Sistem Produksi | Workflow, Production Bible |
| Project | Pengembangan Proyek | Project Bible, Character Bible, World Bible |
| Resource | Pengelolaan Resource | Asset Library, Repository Asset |
| Content | Produksi Konten | Carousel, Poster, Video, Komik |

---

## Hubungan Antar Level

```text
Knowledge
↓
Production
↓
Project
↓
Resource
↓
Content
```

Perubahan pada level yang lebih tinggi dapat memengaruhi level di bawahnya.

Sebaliknya, perubahan pada level yang lebih rendah tidak selalu memengaruhi level di atasnya.

---

## 2.1 Knowledge

Digunakan ketika pekerjaan berkaitan dengan:

- Principle
- Framework
- Standard
- Registry
- Repository Rule
- Metadata Rule

Hasil:

Knowledge Architecture bertambah atau berubah.

---

## 2.2 Production

Digunakan ketika pekerjaan berkaitan dengan:

- Workflow
- Production Bible
- Production Process
- Quality Gate

Hasil:

Sistem produksi bertambah atau berubah.

---

## 2.3 Project

Digunakan ketika pekerjaan berkaitan dengan:

- Project Architecture
- Project Bible
- Character Bible
- World Bible

Hasil:

Dokumen proyek bertambah atau berubah.

---

## 2.4 Resource

Digunakan ketika pekerjaan berkaitan dengan:

- Asset Library
- Repository Asset
- Resource Management

Hasil:

Resource bertambah atau berubah.

---

## 2.5 Content

Digunakan ketika pekerjaan berkaitan dengan:

- Carousel
- Poster
- Video
- Komik
- Caption

Hasil:

Konten siap dipublikasikan.

---

# BAB 3 — Paket Pemulihan

## 3.1 Definisi

Paket Pemulihan adalah kumpulan dokumen yang direkomendasikan untuk dipulihkan ke dalam percakapan ChatGPT agar suatu pekerjaan dapat dilanjutkan tanpa perlu meng-upload seluruh repository.

Paket Pemulihan menerapkan dua prinsip utama:

- Minimum Document Set
- Maximum Context Recovery

---

## 3.2 Tujuan Paket Pemulihan

Paket Pemulihan dibuat untuk:

- mempercepat pemulihan konteks;
- mengurangi jumlah dokumen yang di-upload;
- menghemat ruang konteks ChatGPT;
- memastikan ChatGPT menerima dokumen yang relevan.

---

## 3.3 Struktur Paket Pemulihan

Setiap Paket Pemulihan memiliki struktur yang sama.

| Komponen | Fungsi |
|----------|--------|
| Tujuan | Menjelaskan pekerjaan yang didukung |
| Download | Dokumen yang perlu di-download dari GitHub |
| Upload | Urutan upload ke ChatGPT |
| Prioritas | Tingkat prioritas dokumen |
| Hasil | Hasil yang diharapkan |
| Catatan | Informasi tambahan atau pengecualian |

---

## 3.4 Jenis Paket Pemulihan

OMB menyediakan lima Paket Pemulihan.

| Paket Pemulihan | Digunakan Untuk |
|-----------------|-----------------|
| Knowledge | Pengembangan Knowledge Architecture |
| Production | Pengembangan sistem produksi |
| Project | Pengembangan proyek |
| Resource | Pengelolaan resource |
| Content | Produksi konten |

---

## 3.5 Aturan Penggunaan Paket Pemulihan

1. Mulailah dengan satu Paket Pemulihan.

2. Gunakan BAB 4 — Matriks Pemulihan sebagai pintu masuk utama.

3. Ikuti urutan upload yang direkomendasikan.

4. Tambahkan dokumen hanya jika konteks belum mencukupi.

5. Setelah konteks berhasil dipulihkan, lanjutkan pekerjaan.

6. Hindari meng-upload seluruh repository kecuali benar-benar diperlukan.

---

## 3.6 Hubungan Paket Pemulihan dengan Matriks Pemulihan

Paket Pemulihan menjelaskan dokumen yang digunakan untuk memulihkan konteks.

Matriks Pemulihan membantu operator menentukan Paket Pemulihan yang tepat berdasarkan pekerjaan yang sedang dilakukan.

Dengan kata lain:

- Paket Pemulihan menjelaskan **apa yang digunakan**.
- Matriks Pemulihan menjelaskan **kapan paket tersebut digunakan**.

- # BAB 4 — Matriks Pemulihan

Matriks Pemulihan merupakan pusat navigasi OMB.

Operator dapat menggunakan Matriks Pemulihan melalui dua cara.

1. Berdasarkan pekerjaan yang akan dilakukan (**Tampilan Operator**).
2. Berdasarkan level pekerjaan (**Tampilan Arsitektur**).

Disarankan menggunakan **Tampilan Operator** karena lebih cepat dan sesuai dengan cara berpikir operator.

---

# 4.1 Cara Menggunakan Matriks Pemulihan

Gunakan langkah berikut.

```text
Tentukan pekerjaan
↓
Buka Tampilan Operator
atau
Tampilan Arsitektur
↓
Temukan RM-ID
↓
Lihat Paket Pemulihan
↓
Download dokumen dari GitHub
↓
Upload ke ChatGPT
↓
Mulai bekerja
```

---

# 4.2 Tampilan Operator

Cari pekerjaan berdasarkan kata kerja yang paling sesuai.

**Tabel 4-1. Tampilan Operator**

| Kata Kerja | RM-ID |
|------------|--------|
| Membuat | RM-001 s.d. RM-013 |
| Merevisi | RM-014 s.d. RM-017 |
| Mengubah | RM-018 s.d. RM-022 |
| Mengelola | RM-023 s.d. RM-024 |
| Memulai | RM-025 |
| Memulihkan | RM-026 |

Contoh penggunaan.

Saya ingin membuat Standard.

```text
Membuat
↓
RM-003
↓
Lihat Paket Pemulihan
↓
Mulai bekerja
```

---

# 4.3 Tampilan Arsitektur

Gunakan tampilan ini apabila operator telah mengetahui level pekerjaan yang sedang dilakukan.

**Tabel 4-2. Tampilan Arsitektur**

| Level | RM-ID |
|--------|--------|
| Knowledge | RM-001 s.d. RM-010 |
| Production | RM-011 s.d. RM-015 |
| Project | RM-016 s.d. RM-020 |
| Resource | RM-021 s.d. RM-022 |
| Content | RM-023 s.d. RM-025 |
| Pemulihan Konteks | RM-026 |

---

# 4.4 Matriks Pemulihan

Matriks berikut menjadi pusat pengambilan keputusan dalam OMB.

Gunakan RM-ID untuk menentukan Paket Pemulihan yang sesuai sebelum melakukan download dokumen dari GitHub dan upload ke ChatGPT.

**Tabel 4-3. Matriks Pemulihan**

| RM-ID | Saya sedang... | Pemicu | Level | Paket Pemulihan | Download dari GitHub | Upload ke ChatGPT | Hasil | Catatan |
|-------|----------------|---------|-------|-----------------|----------------------|-------------------|-------|----------|

---

## Knowledge

| RM-ID | Saya sedang... | Pemicu | Level | Paket Pemulihan | Download dari GitHub | Upload ke ChatGPT | Hasil | Catatan |
|-------|----------------|---------|-------|-----------------|----------------------|-------------------|-------|----------|
| RM-001 | Membuat Principle | Saya ingin membuat Principle baru. | Knowledge | Knowledge | Lihat Paket Pemulihan Knowledge | Ikuti urutan pada Paket Pemulihan | Principle baru | Gunakan versi terbaru seluruh dokumen. |
| RM-002 | Membuat Framework | Saya ingin membuat Framework baru. | Knowledge | Knowledge | Lihat Paket Pemulihan Knowledge | Ikuti urutan pada Paket Pemulihan | Framework baru | Upload Framework lama jika merupakan revisi. |
| RM-003 | Membuat Standard | Saya ingin membuat atau mengubah Standard. | Knowledge | Knowledge | Lihat Paket Pemulihan Knowledge | Ikuti urutan pada Paket Pemulihan | Standard baru atau revisi | Gunakan Standard terakhir sebagai referensi bila tersedia. |
| RM-004 | Membuat Registry | Saya ingin membuat Registry baru. | Knowledge | Knowledge | Lihat Paket Pemulihan Knowledge | Ikuti urutan pada Paket Pemulihan | Registry baru | Pastikan Document ID tidak bertabrakan. |
| RM-005 | Mengubah Repository | Saya ingin mengubah struktur repository. | Knowledge | Knowledge | Lihat Paket Pemulihan Knowledge | Ikuti urutan pada Paket Pemulihan | Repository diperbarui | Periksa dampak terhadap seluruh repository. |
| RM-006 | Mengubah Metadata | Saya ingin mengubah metadata dokumen. | Knowledge | Knowledge | Lihat Paket Pemulihan Knowledge | Ikuti urutan pada Paket Pemulihan | Metadata diperbarui | Pastikan konsisten dengan aturan metadata. |
| RM-007 | Membuat Document Type | Saya ingin membuat jenis dokumen baru. | Knowledge | Knowledge | Lihat Paket Pemulihan Knowledge | Ikuti urutan pada Paket Pemulihan | Document Type baru | Pastikan tidak bertabrakan dengan tipe yang sudah ada. |
| RM-008 | Membuat Naming Rule | Saya ingin membuat aturan penamaan baru. | Knowledge | Knowledge | Lihat Paket Pemulihan Knowledge | Ikuti urutan pada Paket Pemulihan | Naming Rule baru | Pastikan berlaku konsisten di seluruh repository. |
| RM-009 | Mengubah Template | Saya ingin mengubah template dokumen. | Knowledge | Knowledge | Lihat Paket Pemulihan Knowledge | Ikuti urutan pada Paket Pemulihan | Template baru | Periksa kompatibilitas dengan Canonical Document. |
| RM-010 | Mengubah Versioning | Saya ingin mengubah aturan versi. | Knowledge | Knowledge | Lihat Paket Pemulihan Knowledge | Ikuti urutan pada Paket Pemulihan | Versioning baru | Pastikan backward compatibility. |

---

## Production

| RM-ID | Saya sedang... | Pemicu | Level | Paket Pemulihan | Download dari GitHub | Upload ke ChatGPT | Hasil | Catatan |
|-------|----------------|---------|-------|-----------------|----------------------|-------------------|-------|----------|
| RM-011 | Membuat Workflow | Saya ingin membuat Workflow baru. | Production | Production | Lihat Paket Pemulihan Production | Ikuti urutan pada Paket Pemulihan | Workflow baru | Pastikan selaras dengan sistem produksi. |
| RM-012 | Merevisi Workflow | Saya ingin merevisi Workflow. | Production | Production | Lihat Paket Pemulihan Production | Ikuti urutan pada Paket Pemulihan | Workflow diperbarui | Sertakan Workflow sebelumnya bila tersedia. |
| RM-013 | Membuat Production Bible | Saya ingin membuat Production Bible. | Production | Production | Lihat Paket Pemulihan Production | Ikuti urutan pada Paket Pemulihan | Production Bible baru | Tambahkan referensi jika ada standar produksi terkait. |
| RM-014 | Merevisi Production Bible | Saya ingin merevisi Production Bible. | Production | Production | Lihat Paket Pemulihan Production | Ikuti urutan pada Paket Pemulihan | Production Bible diperbarui | Gunakan versi terakhir sebagai acuan. |
| RM-015 | Membuat Quality Gate | Saya ingin membuat Quality Gate. | Production | Production | Lihat Paket Pemulihan Production | Ikuti urutan pada Paket Pemulihan | Quality Gate baru | Pastikan terintegrasi dengan Workflow. |

---

## Project

| RM-ID | Saya sedang... | Pemicu | Level | Paket Pemulihan | Download dari GitHub | Upload ke ChatGPT | Hasil | Catatan |
|-------|----------------|---------|-------|-----------------|----------------------|-------------------|-------|----------|
| RM-016 | Memulai Proyek Baru | Saya ingin membuat proyek baru. | Project | Project | Lihat Paket Pemulihan Project | Ikuti urutan pada Paket Pemulihan | Struktur proyek baru | Tambahkan Brand Bible bila diperlukan. |
| RM-017 | Membuat Project Bible | Saya ingin membuat Project Bible. | Project | Project | Lihat Paket Pemulihan Project | Ikuti urutan pada Paket Pemulihan | Project Bible baru | Pastikan konsisten dengan Production Bible. |
| RM-018 | Membuat Character Bible | Saya ingin membuat Character Bible. | Project | Project | Lihat Paket Pemulihan Project | Ikuti urutan pada Paket Pemulihan | Character Bible baru | Tambahkan World Bible bila diperlukan. |
| RM-019 | Membuat World Bible | Saya ingin membuat World Bible. | Project | Project | Lihat Paket Pemulihan Project | Ikuti urutan pada Paket Pemulihan | World Bible baru | Pastikan selaras dengan Project Bible. |
| RM-020 | Merevisi Project Architecture | Saya ingin merevisi Project Architecture. | Project | Project | Lihat Paket Pemulihan Project | Ikuti urutan pada Paket Pemulihan | Project Architecture diperbarui | Pastikan tidak bertentangan dengan Knowledge Architecture. |

---

## Resource

| RM-ID | Saya sedang... | Pemicu | Level | Paket Pemulihan | Download dari GitHub | Upload ke ChatGPT | Hasil | Catatan |
|-------|----------------|---------|-------|-----------------|----------------------|-------------------|-------|----------|
| RM-021 | Mengelola Asset Library | Saya ingin membuat atau memperbarui Asset Library. | Resource | Resource | Lihat Paket Pemulihan Resource | Ikuti urutan pada Paket Pemulihan | Asset Library diperbarui | Pastikan struktur aset tetap konsisten. |
| RM-022 | Mengelola Repository Asset | Saya ingin mengubah repository aset. | Resource | Resource | Lihat Paket Pemulihan Resource | Ikuti urutan pada Paket Pemulihan | Repository Asset diperbarui | Pastikan referensi aset tidak terputus. |

---

## Content

| RM-ID | Saya sedang... | Pemicu | Level | Paket Pemulihan | Download dari GitHub | Upload ke ChatGPT | Hasil | Catatan |
|-------|----------------|---------|-------|-----------------|----------------------|-------------------|-------|----------|
| RM-023 | Membuat Carousel | Saya ingin membuat carousel. | Content | Content | Lihat Paket Pemulihan Content | Ikuti urutan pada Paket Pemulihan | Carousel siap dipublikasikan | Ikuti standar visual proyek. |
| RM-024 | Membuat Poster | Saya ingin membuat poster. | Content | Content | Lihat Paket Pemulihan Content | Ikuti urutan pada Paket Pemulihan | Poster siap dipublikasikan | Pastikan mengikuti identitas visual proyek. |
| RM-025 | Membuat Video | Saya ingin membuat video. | Content | Content | Lihat Paket Pemulihan Content | Ikuti urutan pada Paket Pemulihan | Video siap dipublikasikan | Tambahkan storyboard bila diperlukan. |

---

## Pemulihan Konteks

| RM-ID | Saya sedang... | Pemicu | Level | Paket Pemulihan | Download dari GitHub | Upload ke ChatGPT | Hasil | Catatan |
|-------|----------------|---------|-------|-----------------|----------------------|-------------------|-------|----------|
| RM-026 | Memulihkan Konteks | Saya membuka chat baru atau ChatGPT kehilangan konteks. | Pemulihan Konteks | Sesuai pekerjaan | Lihat Paket Pemulihan sesuai pekerjaan | Ikuti urutan prioritas pada BAB 5 — Matriks Prioritas Pemulihan | Konteks berhasil dipulihkan | Tambahkan dokumen secara bertahap hingga konteks memadai. |

# BAB 5 — Matriks Prioritas Pemulihan

Matriks Prioritas Pemulihan membantu operator menentukan urutan dokumen yang perlu di-upload ketika ruang konteks ChatGPT terbatas.

Prinsip utamanya adalah:

- mulai dari dokumen yang paling penting;
- tambahkan dokumen secara bertahap;
- hentikan upload ketika konteks telah memadai.

BAB ini digunakan setelah operator menentukan RM-ID pada **BAB 4 — Matriks Pemulihan**.

---

# 5.1 Tujuan

Tidak semua pekerjaan memerlukan seluruh dokumen.

Dalam banyak kasus, operator cukup meng-upload beberapa dokumen utama agar ChatGPT memahami konteks pekerjaan.

Matriks Prioritas Pemulihan membantu operator:

- menentukan dokumen yang harus di-upload terlebih dahulu;
- menghemat ruang konteks ChatGPT;
- mempercepat proses pemulihan konteks;
- menghindari upload dokumen yang tidak diperlukan.

---

# 5.2 Tingkat Prioritas

OMB menggunakan lima tingkat prioritas.

**Tabel 5-1. Tingkat Prioritas**

| Prioritas | Arti | Penggunaan |
|-----------|------|------------|
| ★★★★★ | Wajib | Selalu di-upload terlebih dahulu. |
| ★★★★☆ | Sangat Disarankan | Di-upload apabila konteks belum mencukupi. |
| ★★★☆☆ | Disarankan | Digunakan ketika pekerjaan membutuhkan informasi tambahan. |
| ★★☆☆☆ | Referensi | Digunakan hanya bila diperlukan. |
| ★☆☆☆☆ | Opsional | Digunakan pada kondisi khusus. |

---

# 5.3 Strategi Pemulihan

Gunakan urutan berikut.

```text
Upload dokumen
★★★★★
↓
Verifikasi konteks
↓
Sudah cukup?
↓
YA
↓
Mulai bekerja

ATAU

TIDAK
↓
Upload dokumen
★★★★☆
↓
Verifikasi kembali
↓
Masih belum cukup?
↓
Upload dokumen
★★★☆☆
↓
Lanjutkan hingga konteks memadai
```

---

# 5.4 Aturan Prioritas

Gunakan aturan berikut.

1. Jangan langsung meng-upload seluruh repository.

2. Mulailah dari dokumen dengan prioritas ★★★★★.

3. Tambahkan dokumen secara bertahap.

4. Hentikan upload ketika konteks telah mencukupi.

5. Gunakan dokumen referensi hanya apabila benar-benar diperlukan.

---

# 5.5 Paket Pemulihan

Setiap RM-ID pada **BAB 4 — Matriks Pemulihan** akan mengarahkan operator ke salah satu Paket Pemulihan berikut.

**Tabel 5-2. Paket Pemulihan**

| Paket Pemulihan | Digunakan Untuk |
|-----------------|-----------------|
| Knowledge | Pekerjaan pada Knowledge Architecture |
| Production | Pekerjaan pada Production Architecture |
| Project | Pekerjaan pada Project Architecture |
| Resource | Pekerjaan pada Resource Architecture |
| Content | Produksi konten |

---

## 5.5.1 Paket Pemulihan Knowledge

### Tujuan

Digunakan untuk seluruh pekerjaan pada Knowledge Architecture.

### Prioritas Upload

★★★★★

Dokumen inti Knowledge Architecture.

★★★★☆

Dokumen pendukung Knowledge Architecture.

★★★☆☆

Dokumen referensi Knowledge Architecture.

★★☆☆☆

Dokumen referensi tambahan.

★☆☆☆☆

Dokumen khusus apabila diperlukan.

### Aturan

- Selalu mulai dari dokumen inti.
- Tambahkan dokumen hanya bila konteks belum cukup.
- Hindari upload seluruh repository.

---

## 5.5.2 Paket Pemulihan Production

### Tujuan

Digunakan untuk seluruh pekerjaan pada Production Architecture.

### Prioritas Upload

★★★★★

Dokumen inti Production.

★★★★☆

Workflow dan Quality Gate.

★★★☆☆

Dokumen pendukung produksi.

★★☆☆☆

Referensi produksi.

★☆☆☆☆

Dokumen khusus.

### Aturan

- Mulailah dari Production Bible.
- Tambahkan Workflow bila diperlukan.
- Gunakan referensi hanya bila konteks belum mencukupi.

---

## 5.5.3 Paket Pemulihan Project

### Tujuan

Digunakan untuk seluruh pekerjaan pada Project Architecture.

### Prioritas Upload

★★★★★

Project Bible dan Project Architecture.

★★★★☆

Character Bible atau World Bible.

★★★☆☆

Brand Bible.

★★☆☆☆

Dokumen pendukung proyek.

★☆☆☆☆

Dokumen khusus.

### Aturan

- Mulailah dari Project Bible.
- Tambahkan Character Bible atau World Bible sesuai kebutuhan.
- Gunakan Brand Bible apabila proyek memiliki identitas visual khusus.

---

## 5.5.4 Paket Pemulihan Resource

### Tujuan

Digunakan untuk pengelolaan resource.

### Prioritas Upload

★★★★★

Dokumen inti Resource.

★★★★☆

Asset Library.

★★★☆☆

Dokumen pendukung Resource.

★★☆☆☆

Referensi Resource.

★☆☆☆☆

Dokumen khusus.

### Aturan

- Gunakan Asset Library apabila pekerjaan berkaitan dengan aset.
- Tambahkan referensi hanya bila diperlukan.

---

## 5.5.5 Paket Pemulihan Content

### Tujuan

Digunakan untuk produksi konten.

### Prioritas Upload

★★★★★

Project Bible dan Production Bible.

★★★★☆

Workflow dan Quality Gate.

★★★☆☆

Character Bible atau World Bible apabila diperlukan.

★★☆☆☆

Asset Library.

★☆☆☆☆

Dokumen tambahan.

### Aturan

- Mulailah dari Project Bible.
- Tambahkan Workflow apabila proses produksi membutuhkannya.
- Upload Character Bible hanya apabila menggunakan karakter tetap.

---

# 5.6 Contoh Penggunaan

### Contoh 1

Pekerjaan

Membuat Standard.

```text
RM-003
↓
Paket Pemulihan Knowledge
↓
Upload dokumen
★★★★★
↓
Verifikasi konteks
↓
Tambahkan
★★★★☆
bila diperlukan
↓
Mulai bekerja
```

---

### Contoh 2

Pekerjaan

Membuat Carousel.

```text
RM-023
↓
Paket Pemulihan Content
↓
Upload dokumen
★★★★★
↓
Verifikasi konteks
↓
Tambahkan
★★★★☆
bila diperlukan
↓
Mulai bekerja
```

---

### Contoh 3

Pekerjaan

ChatGPT kehilangan konteks.

```text
Tentukan pekerjaan
↓
Cari RM-ID
↓
Pilih Paket Pemulihan
↓
Upload dokumen
★★★★★
↓
Verifikasi konteks
↓
Tambahkan
★★★★☆
bila diperlukan
↓
Lanjutkan pekerjaan
```

---

# Ringkasan

Gunakan BAB 5 setelah menentukan RM-ID pada **BAB 4 — Matriks Pemulihan**.

Selalu gunakan prinsip berikut.

```text
RM-ID
↓
Paket Pemulihan
↓
Upload
★★★★★
↓
Verifikasi
↓
Tambahkan
★★★★☆
bila diperlukan
↓
Mulai bekerja
```

Dengan mengikuti urutan tersebut, operator dapat memulihkan konteks ChatGPT secara efisien tanpa harus meng-upload seluruh repository.

# BAB 6 — Skenario Operasional

BAB ini berisi contoh penggunaan OMB dalam berbagai situasi operasional.

Tujuannya adalah membantu operator menentukan **RM-ID** dan **Paket Pemulihan** yang tepat tanpa harus membaca seluruh OMB.

Seluruh skenario mengikuti alur kerja yang sama.

```text
Tentukan pekerjaan
↓
Cari RM-ID
↓
Pilih Paket Pemulihan
↓
Download dokumen dari GitHub
↓
Upload ke ChatGPT
↓
Mulai bekerja
```

---

# 6.1 Daftar Skenario

**Tabel 6-1. Skenario Operasional**

| Kode | Kasus | RM-ID | Paket Pemulihan | Ringkasan Langkah |
|------|-------|-------|-----------------|-------------------|
| SO-001 | Membuat Principle | RM-001 | Knowledge | Gunakan Paket Pemulihan Knowledge lalu mulai membuat Principle. |
| SO-002 | Membuat Framework | RM-002 | Knowledge | Gunakan Paket Pemulihan Knowledge lalu mulai membuat Framework. |
| SO-003 | Membuat Standard | RM-003 | Knowledge | Gunakan Paket Pemulihan Knowledge lalu mulai membuat Standard. |
| SO-004 | Membuat Registry | RM-004 | Knowledge | Gunakan Paket Pemulihan Knowledge lalu mulai membuat Registry. |
| SO-005 | Mengubah Repository | RM-005 | Knowledge | Gunakan Paket Pemulihan Knowledge sebelum mengubah repository. |
| SO-006 | Membuat Workflow | RM-011 | Production | Gunakan Paket Pemulihan Production sebelum membuat Workflow. |
| SO-007 | Membuat Production Bible | RM-013 | Production | Gunakan Paket Pemulihan Production sebelum membuat Production Bible. |
| SO-008 | Memulai Proyek Baru | RM-016 | Project | Gunakan Paket Pemulihan Project sebelum menyusun struktur proyek. |
| SO-009 | Membuat Character Bible | RM-018 | Project | Gunakan Paket Pemulihan Project sebelum membuat Character Bible. |
| SO-010 | Membuat World Bible | RM-019 | Project | Gunakan Paket Pemulihan Project sebelum membuat World Bible. |
| SO-011 | Membuat Carousel | RM-023 | Content | Gunakan Paket Pemulihan Content sebelum membuat carousel. |
| SO-012 | Membuat Poster | RM-024 | Content | Gunakan Paket Pemulihan Content sebelum membuat poster. |
| SO-013 | Membuat Video | RM-025 | Content | Gunakan Paket Pemulihan Content sebelum membuat video. |
| SO-014 | Memulihkan Konteks | RM-026 | Sesuai Pekerjaan | Tentukan pekerjaan terlebih dahulu, kemudian gunakan Paket Pemulihan yang sesuai. |

---

# 6.2 Contoh Alur Operasional

## Contoh 1 — Membuat Standard

Operator ingin membuat Standard baru.

```text
Membuat Standard
↓
RM-003
↓
Paket Pemulihan Knowledge
↓
Download dokumen dari GitHub
↓
Upload ke ChatGPT
↓
Mulai membuat Standard
```

---

## Contoh 2 — Membuat Character Bible

Operator ingin membuat Character Bible.

```text
Membuat Character Bible
↓
RM-018
↓
Paket Pemulihan Project
↓
Download dokumen dari GitHub
↓
Upload ke ChatGPT
↓
Mulai membuat Character Bible
```

---

## Contoh 3 — Membuat Carousel

Operator ingin membuat carousel.

```text
Membuat Carousel
↓
RM-023
↓
Paket Pemulihan Content
↓
Download dokumen dari GitHub
↓
Upload ke ChatGPT
↓
Mulai membuat carousel
```

---

## Contoh 4 — ChatGPT Kehilangan Konteks

Operator membuka chat baru atau ChatGPT tidak lagi memahami konteks pekerjaan.

```text
Tentukan pekerjaan
↓
Cari RM-ID
↓
Pilih Paket Pemulihan
↓
Download dokumen dari GitHub
↓
Upload ke ChatGPT
↓
Lanjutkan pekerjaan
```

---

# 6.3 Prinsip Penggunaan

Gunakan BAB 6 sebagai referensi cepat.

Apabila kasus yang dihadapi belum tersedia pada tabel di atas, lakukan langkah berikut.

1. Tentukan pekerjaan yang akan dilakukan.

2. Cari RM-ID melalui **BAB 4 — Matriks Pemulihan**.

3. Gunakan Paket Pemulihan yang direkomendasikan.

4. Ikuti urutan prioritas upload pada **BAB 5 — Matriks Prioritas Pemulihan**.

5. Setelah konteks mencukupi, lanjutkan pekerjaan.

---

# Ringkasan

BAB 6 menunjukkan cara menggunakan OMB dalam situasi nyata.

Operator tidak perlu menghafal seluruh isi OMB.

Cukup ikuti alur berikut.

```text
Pekerjaan
↓
RM-ID
↓
Paket Pemulihan
↓
Download dari GitHub
↓
Upload ke ChatGPT
↓
Mulai bekerja
```

Dengan pendekatan ini, OMB dapat digunakan secara konsisten untuk seluruh pekerjaan dalam Knowledge Architecture Ecosystem.

# BAB 7 — Lampiran

Lampiran berisi referensi tambahan yang membantu operator memahami struktur kerja OMB tanpa harus membaca seluruh isi dokumen.

Lampiran tidak menggantikan BAB 1 sampai BAB 6, tetapi berfungsi sebagai referensi cepat.

---

# Lampiran A — Peta Level Pekerjaan

Seluruh pekerjaan dalam Knowledge Architecture Ecosystem dikelompokkan ke dalam lima level.

```text
Knowledge
↓
Production
↓
Project
↓
Resource
↓
Content
```

## Penjelasan

### Knowledge

Berisi dokumen yang mendefinisikan aturan dasar sistem.

Contoh:

- Principle
- Framework
- Standard
- Registry

---

### Production

Berisi dokumen yang mengatur proses produksi.

Contoh:

- Workflow
- Production Bible
- Quality Gate

---

### Project

Berisi dokumen yang mendefinisikan suatu proyek.

Contoh:

- Project Bible
- Character Bible
- World Bible

---

### Resource

Berisi pengelolaan seluruh sumber daya proyek.

Contoh:

- Asset Library
- Repository Asset
- Template
- Resource Management

---

### Content

Berisi hasil akhir produksi.

Contoh:

- Carousel
- Poster
- Video
- Komik
- Caption

---

# Lampiran B — Alur Penggunaan OMB

Gunakan alur berikut setiap kali memulai pekerjaan.

```text
Operator
↓
BAB 4
Matriks Pemulihan
↓
RM-ID
↓
BAB 5
Paket Pemulihan
↓
Download dokumen dari GitHub
↓
Upload ke ChatGPT
↓
Mulai bekerja
```

Apabila konteks belum mencukupi, tambahkan dokumen sesuai prioritas hingga ChatGPT memiliki konteks yang memadai.

---

# Lampiran C — Daftar Singkatan

| Singkatan | Kepanjangan |
|-----------|-------------|
| OMB | Operator & Recovery Manual Book |
| RM | Recovery Matrix |
| RM-ID | Recovery Matrix Identifier |
| KA | Knowledge Architecture |
| PP | Paket Pemulihan |
| SSOT | Single Source of Truth |

---

# Lampiran D — Riwayat Revisi

| Versi | Tanggal | Status | Keterangan |
|--------|---------|--------|------------|
| 1.0 | 27 Juli 2026 | LOCK | Rilis kanonis pertama OMB-001. |

---

# Penutup

Operator & Recovery Manual Book (OMB) merupakan panduan operasional resmi untuk membantu operator menentukan dokumen yang diperlukan dan memulihkan konteks ChatGPT secara efisien.

OMB menerapkan prinsip:

- **Minimum Document Set**
- **Maximum Context Recovery**
- **Need to Know**
- **Progressive Context**
- **Universal Workflow**

Dengan mengikuti alur yang dijelaskan dalam dokumen ini, operator dapat:

- menentukan pekerjaan dengan cepat;
- memilih RM-ID yang sesuai;
- menggunakan Paket Pemulihan yang tepat;
- mengurangi jumlah dokumen yang perlu di-upload;
- memulihkan konteks secara efisien;
- memulai pekerjaan tanpa harus membuka seluruh repository.

---

# Status Dokumen

**Nama Dokumen**

OMB-001 — Operator & Recovery Manual Book

**Versi**

1.0

**Status**

LOCK

**Kategori**

Canonical Document

**Slogan**

> **Satu Buku. Satu Alur. Satu Panduan Operasional.**
>
> 
