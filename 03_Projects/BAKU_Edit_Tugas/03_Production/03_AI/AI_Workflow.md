# BAKU AI-Assisted Editing Workflow

## Objective

Menggunakan AI untuk mempercepat pekerjaan editing tanpa menghilangkan human judgment, verification, atau academic responsibility.

## Workflow

### 1. Prepare

Editor memahami requirement, scope editing, dokumen sumber, dan constraint sebelum membuat prompt.

**Input:** client requirement + source document + editing scope.

**Output:** editing context yang jelas.

### 2. Diagnose

Identifikasi masalah yang hendak dibantu AI: grammar, clarity, coherence, redundancy, structure, terminology, atau issue lain yang relevan.

AI tidak digunakan sebelum editor mengetahui masalah yang hendak diselesaikan.

### 3. Prompt

Prompt harus memberikan konteks yang cukup dan batasan yang jelas, terutama:

- jangan mengubah meaning;
- jangan mengarang fakta atau citation;
- pertahankan istilah teknis yang benar;
- keluarkan bagian yang perlu diverifikasi bila relevan.

### 4. Generate

AI menghasilkan saran atau draft edit.

Output AI belum dianggap final.

### 5. Review AI Output

Editor menilai setiap output dengan keputusan:

`ACCEPT` — dapat digunakan.

`MODIFY` — berguna tetapi perlu diperbaiki.

`REJECT` — tidak sesuai, tidak aman, atau tidak diperlukan.

### 6. Verify

Untuk perubahan yang menyentuh fakta, citation, data, metodologi, teori, atau kesimpulan, lakukan verifikasi terhadap sumber atau requirement yang relevan.

### 7. Human Edit

Editor mengintegrasikan hasil yang valid ke dokumen sambil menjaga meaning, intent, consistency, dan style.

### 8. Final QC

Dokumen tetap melewati Final QC BAKU. AI tidak dapat memberikan status final `READY FOR DELIVERY`.

## Prompt Design Principles

Gunakan prompt yang:

1. spesifik terhadap task;
2. memiliki context yang cukup;
3. menjelaskan constraint;
4. meminta preservasi meaning;
5. memisahkan editing dari factual invention;
6. meminta uncertainty ditandai, bukan diisi dengan tebakan.

## AI Failure Handling

Jika output AI:

- mengubah makna → reject/repair;
- menambahkan fakta tanpa sumber → reject dan verifikasi;
- menghasilkan citation tidak ditemukan → reject;
- terlalu mengubah gaya penulis → modify;
- memperbaiki grammar dengan benar → accept setelah context check;
- tidak yakin → jangan dipaksa menjadi jawaban.

## Traceability

Untuk pekerjaan yang kompleks, catat secara internal:

- task yang dibantu AI;
- jenis perubahan;
- keputusan accept/modify/reject;
- verification yang dilakukan;
- issue yang tetap membutuhkan human decision.

Tujuannya bukan menyimpan seluruh percakapan AI, tetapi menjaga traceability yang berguna untuk quality control dan improvement workflow.