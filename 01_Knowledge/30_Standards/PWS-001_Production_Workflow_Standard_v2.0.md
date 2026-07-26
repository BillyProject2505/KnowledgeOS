# Production Workflow Standard (PWS)

**Document ID:** PWS-001
**Version:** 2.0
**Status:** LOCK
**Category:** Standard
**Owner:** Knowledge Architecture
**Applies To:** Seluruh Production Workflow

---

# 1. Purpose

Production Workflow Standard (PWS) mendefinisikan workflow standar untuk menghasilkan Production Output secara konsisten, terdokumentasi, dapat diulang, dan dapat diaudit.

PWS mengatur proses produksi, bukan proses pembentukan Canonical Knowledge.

Knowledge baru yang ditemukan selama proses produksi harus diproses melalui Knowledge Capture Standard (KCS).

---

# 2. Scope

Standar ini berlaku untuk seluruh aktivitas produksi yang menghasilkan Production Output berdasarkan Canonical Knowledge yang telah tersedia.

---

# 3. Workflow Principles

## PWS-P01 — Production Starts with Existing Knowledge

Seluruh produksi dimulai menggunakan Canonical Knowledge yang telah tersedia.

---

## PWS-P02 — Planning Before Production

Setiap produksi harus memiliki Production Plan sebelum proses produksi dimulai.

---

## PWS-P03 — Standards Before Creativity

Seluruh kreativitas harus tetap mengikuti Canonical Knowledge dan Production Bible yang berlaku.

---

## PWS-P04 — Review Before Approval

Seluruh Production Output wajib melewati Quality Gate sebelum memperoleh persetujuan.

---

## PWS-P05 — Traceable Production

Keputusan penting selama proses produksi harus dapat ditelusuri.

---

## PWS-P06 — Knowledge Discovery

Apabila selama proses produksi ditemukan knowledge baru, knowledge tersebut harus dirujuk ke Knowledge Capture Standard (KCS) dan tidak diproses di dalam workflow produksi.

---

# 4. Standard Workflow

```text
Request
    │
    ▼
Planning
    │
    ▼
Production
    │
    ▼
Quality Review
    │
    ▼
Approval
    │
    ▼
Publication
```

Workflow ini hanya mengatur proses produksi.

Seluruh aktivitas Knowledge Capture berada di luar ruang lingkup PWS.

---

# 5. Workflow Stages

Setiap tahap workflow menggunakan struktur baku:

- Objective
- Input
- Activities
- Output

---

## Stage 1 — Request

### Objective

Memahami kebutuhan produksi.

### Input

- User Request

### Activities

- Memahami kebutuhan pengguna
- Menentukan tujuan produksi

### Output

- Production Objective

---

## Stage 2 — Planning

### Objective

Menyusun rencana produksi.

### Input

- Production Objective

### Activities

- Mengidentifikasi Canonical Knowledge yang diperlukan
- Mengidentifikasi Production Bible
- Menentukan format output
- Menyusun Production Plan

### Output

- Production Plan

---

## Stage 3 — Production

### Objective

Menghasilkan draft Production Output.

### Input

- Production Plan

### Activities

- Membuat draft
- Mengikuti Production Bible
- Menggunakan Canonical Knowledge yang berlaku

### Output

- Draft Production Output

---

## Stage 4 — Quality Review

### Objective

Memastikan kualitas Production Output.

### Input

- Draft Production Output

### Activities

- Menjalankan Quality Gate yang relevan
- Mendokumentasikan hasil review

### Output

- Review Result

---

## Stage 5 — Approval

### Objective

Memberikan persetujuan akhir.

### Input

- Review Result

### Activities

- Validasi akhir
- Persetujuan apabila memenuhi standar

### Output

- Approved Production Output

---

## Stage 6 — Publication

### Objective

Mempublikasikan Production Output.

### Input

- Approved Production Output

### Activities

- Menyiapkan aset
- Mempublikasikan output sesuai media yang dituju

### Output

- Published Production Output

---

# 6. Knowledge Discovery

Apabila selama proses produksi ditemukan knowledge baru, workflow produksi tidak diperluas untuk memproses knowledge tersebut.

Knowledge baru harus dirujuk ke Knowledge Capture Standard (KCS).

```text
Production
      │
      ▼
New Knowledge Found?
      │
 ┌────┴────┐
 │         │
No        Yes
 │         │
 ▼         ▼
Continue   Refer to KCS
Production
```

---

# 7. Workflow Deliverables

| Stage | Deliverable |
|--------|-------------|
| Request | Production Objective |
| Planning | Production Plan |
| Production | Draft Production Output |
| Quality Review | Review Result |
| Approval | Approved Production Output |
| Publication | Published Production Output |

---

# 8. Relationship

```text
KP-001
        │
KP-002
        │
        ▼
Content Production Framework (CPF)
        │
        ▼
Production Workflow Standard (PWS)
        │
        ├── uses → Production Bible (PBS)
        ├── uses → Quality Gate Standard (QGS)
        ├── uses → Canonical Knowledge
        │
        ├── refers new knowledge → Knowledge Capture Standard (KCS)
        │
        └── produces → Production Output
```

PWS menggunakan Canonical Knowledge sebagai masukan utama untuk menghasilkan Production Output.

Knowledge baru yang ditemukan selama produksi diproses melalui KCS.

---

# 9. Governance

Seluruh Production Workflow wajib:

- mengikuti Content Production Framework (CPF);
- menggunakan Canonical Knowledge yang berlaku;
- menggunakan Production Bible sebagai aturan spesifik proyek;
- menerapkan Quality Gate Standard (QGS) pada tahap Quality Review;
- merujuk knowledge baru ke Knowledge Capture Standard (KCS).

Perubahan terhadap workflow hanya dapat dilakukan melalui revisi resmi Production Workflow Standard.

---

# Canonical Decision

Production Workflow Standard (PWS) merupakan standar resmi workflow produksi dalam Knowledge Architecture.

Seluruh Production Output dihasilkan melalui workflow yang konsisten dengan memanfaatkan Canonical Knowledge yang telah tersedia.

Knowledge baru yang ditemukan selama proses produksi tidak diproses di dalam workflow produksi, tetapi dirujuk ke Knowledge Capture Standard (KCS) agar tetap menjaga pemisahan yang jelas antara pengelolaan knowledge dan proses produksi.
