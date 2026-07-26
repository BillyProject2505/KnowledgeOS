# Knowledge Capture Standard (KCS)

**Document ID:** KCS-001
**Version:** 2.0
**Status:** LOCK
**Category:** Standard
**Owner:** Knowledge Architecture
**Applies To:** Seluruh proses Knowledge Capture

---

# 1. Purpose

Knowledge Capture Standard (KCS) mendefinisikan proses standar untuk mengidentifikasi, mengevaluasi, mengklasifikasikan, dan menetapkan knowledge menjadi Canonical Document dalam Knowledge Architecture.

KCS mengatur proses lahirnya Canonical Document, bukan implementasi repository maupun media penyimpanannya.

---

# 2. Scope

Standar ini berlaku untuk seluruh proses Knowledge Capture sebelum sebuah knowledge ditetapkan sebagai Canonical Document.

---

# 3. Core Principles

## KCS-P01 — Capture Before Documentation

Setiap knowledge harus diidentifikasi terlebih dahulu sebelum didokumentasikan.

---

## KCS-P02 — Classification Before Placement

Knowledge harus diklasifikasikan sebelum ditentukan kategori maupun penempatan logisnya.

---

## KCS-P03 — Canonical Evaluation

Tidak semua knowledge menjadi Canonical Document.

Setiap knowledge harus melalui proses evaluasi terlebih dahulu.

---

## KCS-P04 — No Duplicate Canonical Knowledge

Knowledge yang telah memiliki Canonical Document tidak boleh dibuat ulang sebagai Canonical Document baru.

---

## KCS-P05 — Traceable Capture

Seluruh keputusan selama proses Knowledge Capture harus dapat ditelusuri.

---

# 4. Knowledge Capture Workflow

Seluruh knowledge mengikuti alur berikut.

```text
Discussion

↓

Candidate Knowledge

↓

Knowledge Classification

↓

Canonical Evaluation

↓

Knowledge Type Identification

↓

Logical Placement

↓

Draft

↓

Review

↓

Approved

↓

Canonical Document
```

Tidak boleh melewati tahapan tersebut.

---

# 5. Knowledge Classification

Knowledge Classification dilakukan melalui empat langkah.

## Langkah 1

Menentukan apakah knowledge merupakan:

- Canonical Knowledge
- Project Knowledge

---

## Langkah 2

Menentukan Knowledge Type.

Contoh:

- Principle
- Framework
- Standard
- Bible
- Template
- Prompt
- Reference
- Decision
- Registry

---

## Langkah 3

Menentukan Logical Placement sesuai Repository Architecture Standard (RAS).

---

## Langkah 4

Menyiapkan Candidate Canonical Document.

---

# 6. Canonical Evaluation

Sebelum menjadi Canonical Document, knowledge harus memenuhi seluruh kriteria berikut.

- reusable;
- tidak menduplikasi Canonical Knowledge yang sudah ada;
- memiliki ruang lingkup yang jelas;
- memiliki nilai jangka panjang;
- konsisten dengan Canonical Knowledge yang telah disetujui.

Knowledge yang tidak memenuhi kriteria tersebut tidak ditetapkan sebagai Canonical Document.

---

# 7. Document Lifecycle

Canonical Document mengikuti siklus berikut.

```text
Draft

↓

Review

↓

Approved

↓

LOCK
```

Status LOCK menunjukkan bahwa dokumen telah menjadi Canonical Document resmi.

---

# 8. Relationship

```text
KP-001
        │
KP-002
        │
        ▼
Knowledge Capture Standard
        │
        ├── uses → KCF-001
        ├── uses → DNS-001
        ├── uses → DTS-001
        ├── uses → RAS-001
        └── produces → Canonical Document
                        │
                        ▼
                 Registered in KCR-001
```

---

# 9. Governance

Seluruh proses Knowledge Capture wajib mengikuti standar ini.

Perubahan terhadap workflow maupun prinsip dasar hanya dapat dilakukan melalui revisi resmi KCS.

---

# Canonical Decision

Knowledge Capture Standard merupakan standar resmi yang mengatur proses lahirnya Canonical Document dalam Knowledge Architecture.

KCS memastikan bahwa setiap Canonical Document berasal dari proses identifikasi, evaluasi, klasifikasi, dan penempatan logis yang konsisten, dapat ditelusuri, serta selaras dengan seluruh Canonical Knowledge yang telah ditetapkan.
