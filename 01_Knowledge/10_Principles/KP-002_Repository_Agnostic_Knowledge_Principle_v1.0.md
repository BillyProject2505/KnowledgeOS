# Repository-Agnostic Knowledge Principle (KP)

**Document ID:** KP-002  
**Version:** 1.0  
**Status:** LOCK  
**Category:** Principle  
**Owner:** Knowledge  
**Applies To:** Seluruh arsitektur knowledge

---

# 1. Purpose

Menetapkan bahwa seluruh pengetahuan harus bersifat independen terhadap media penyimpanan sehingga dapat digunakan pada repository, platform, maupun teknologi apa pun tanpa mengubah makna, struktur, atau perilakunya.

Prinsip ini memastikan bahwa nilai utama sistem berada pada knowledge, bukan pada tempat knowledge tersebut disimpan.

---

# 2. Core Principles

## KP-P01 — Knowledge First

Knowledge merupakan aset utama.

Repository hanyalah media penyimpanan.

---

## KP-P02 — Repository Independence

Principles, Frameworks, Standards, Bibles, Registries, Templates, Prompts, References, dan Decisions tidak boleh bergantung secara konseptual pada repository tertentu.

Seluruh dokumen harus tetap valid meskipun dipindahkan ke media penyimpanan lain.

---

## KP-P03 — Repository as Storage

Repository hanya bertanggung jawab menyimpan, mengorganisasi, dan menyediakan akses terhadap knowledge.

Repository tidak mendefinisikan aturan, tidak menjalankan workflow, dan tidak menghasilkan output.

---

## KP-P04 — Implementation Separation

Penyimpanan knowledge merupakan detail implementasi.

Knowledge harus tetap terpisah dari implementasi repository.

---

# 3. Documentation Rule

Seluruh dokumen harus ditulis dengan fokus pada:

- knowledge;
- aturan;
- arsitektur;
- proses;
- hubungan antar objek pengetahuan.

Repository hanya disebut apabila pembahasannya berkaitan dengan:

- struktur penyimpanan;
- organisasi folder;
- navigasi repository;
- implementasi penyimpanan;
- manajemen repository.

Repository tidak boleh menjadi subjek utama dalam definisi Framework, Standard, Bible, Registry, Template, Prompt, maupun dokumen kanonis lainnya.

---

# 4. Repository Independence Test

Sebuah dokumen memenuhi prinsip ini apabila:

> Dokumen tersebut tetap benar dan tetap dapat digunakan meskipun seluruh knowledge dipindahkan ke repository, platform, atau media penyimpanan lain.

Apabila makna dokumen berubah karena repository berubah, maka dokumen tersebut belum memenuhi prinsip Repository-Agnostic.

---

# 5. Governance

Seluruh dokumen kanonis harus memisahkan dengan jelas:

- knowledge;
- execution;
- repository.

Repository diperlakukan sebagai implementasi penyimpanan, bukan sebagai bagian dari definisi konseptual knowledge.

---

# Canonical Decision

Knowledge merupakan inti dari arsitektur.

Repository hanyalah media penyimpanan.

Seluruh Principles, Frameworks, Standards, Bibles, Registries, Templates, Prompts, References, dan Decisions harus bersifat repository-agnostic sehingga tetap dapat digunakan tanpa perubahan pada media penyimpanan apa pun.
