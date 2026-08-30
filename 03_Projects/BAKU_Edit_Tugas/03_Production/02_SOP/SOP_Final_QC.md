# SOP — Final Quality Control

## 1. Purpose

Memastikan dokumen yang akan dikirim telah memenuhi scope, requirement, quality standard, dan seluruh pemeriksaan wajib BAKU.

## 2. Input

- Final working document.
- Client requirements.
- Editing Plan.
- Human Review findings.
- Verification results.

## 3. QC Gates

### Gate 1 — Requirement

[ ] Semua requirement yang disepakati terpenuhi.

[ ] Tidak ada pekerjaan penting yang terlewat.

[ ] Tidak ada perubahan di luar scope tanpa alasan/approval.

### Gate 2 — Content

[ ] Meaning dan intent penulis terjaga.

[ ] Struktur dan alur logis.

[ ] Tidak ada klaim unsupported yang diterima begitu saja.

[ ] Data, angka, istilah, dan fakta kritis telah diperiksa sesuai kebutuhan.

### Gate 3 — AI Output

[ ] Tidak ada hallucinated source/citation.

[ ] Tidak ada AI artifact yang mengganggu hasil.

[ ] Tidak ada wording yang membuat klaim lebih kuat dari bukti aslinya.

[ ] Perubahan substantif telah ditinjau manusia.

### Gate 4 — Language

[ ] Grammar.

[ ] Spelling.

[ ] Punctuation.

[ ] Clarity.

[ ] Consistency of terminology.

[ ] Academic tone sesuai requirement.

### Gate 5 — Citation & References

[ ] Citation sesuai sumber yang tersedia/terverifikasi.

[ ] Kutipan dan attribution diperiksa.

[ ] In-text citation dan reference list konsisten jika pekerjaan mencakup bagian tersebut.

### Gate 6 — Formatting

[ ] Heading konsisten.

[ ] Font, spacing, margin, numbering sesuai requirement.

[ ] Table/figure/layout tidak rusak.

[ ] Page breaks diperiksa.

[ ] Tidak ada placeholder, comment, atau track-change yang tidak seharusnya ikut terkirim.

### Gate 7 — Delivery

[ ] File dapat dibuka.

[ ] Nama file sesuai standar.

[ ] Versi final teridentifikasi dengan jelas.

[ ] Tidak ada data/internal note yang bocor kepada klien.

## 4. Severity

### Critical

Harus diperbaiki sebelum delivery. Contoh: factual error material, citation fabricated, file rusak, requirement utama tidak terpenuhi.

### Major

Tidak boleh dibiarkan tanpa keputusan eksplisit. Contoh: struktur bermasalah, perubahan meaning, formatting signifikan.

### Minor

Masalah kecil yang tidak mengubah substansi tetapi tetap diperbaiki jika memungkinkan.

## 5. Final Decision

Dokumen hanya boleh diberi status **READY FOR DELIVERY** apabila tidak ada Critical issue yang terbuka dan seluruh mandatory QC gates telah dilewati.

Jika ada issue yang membutuhkan input klien, status harus **BLOCKED — CLIENT CLARIFICATION** dan jangan dipaksakan menjadi final.

## 6. QC Record

Simpan ringkasan:

- QC date;
- reviewer;
- scope checked;
- critical/major findings;
- verification notes;
- final status.

Jangan menyimpan data pribadi klien di repository GitHub sebagai bagian dari QC record.
