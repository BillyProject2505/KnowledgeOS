# BAKU Edit Tugas — Assets

## Purpose

Folder ini berisi **canonical project assets** untuk BAKU Edit Tugas yang digunakan dalam kebutuhan brand, content production, dan pekerjaan visual yang telah disetujui.

README ini berfungsi sebagai **asset index and usage guide**. Detail authority, keputusan project, dan status canonical tetap mengikuti project context dan decision register.

## Asset Scope

Asset yang berada di folder ini dapat mencakup:

- brand assets;
- production assets yang telah disetujui;
- visual references yang diperlukan untuk produksi;
- file pendukung lain yang memiliki status dan provenance yang jelas.

Jangan menjadikan folder ini sebagai penyimpanan default untuk file klien, file sementara, atau hasil eksplorasi yang belum disetujui.

## Current Structure

```text
02_Assets/
└── Brand/
    ├── BAKU_Edit_Tugas_logo-primary.png
    ├── BAKU_Edit_Tugas_logo-transparent.png
    └── README.md
```

### `Brand/`

Berisi canonical BAKU Edit Tugas brand assets, khususnya logo resmi yang digunakan dalam production.

Detail penggunaan dan aturan brand asset berada pada `Brand/README.md`.

## Canonical Brand Assets

Saat ini tersedia dua logo canonical:

| Asset | Status | Primary Use |
|---|---|---|
| `Brand/BAKU_Edit_Tugas_logo-primary.png` | `CANONICAL` | Default brand mark untuk penggunaan umum. |
| `Brand/BAKU_Edit_Tugas_logo-transparent.png` | `CANONICAL` | Penggunaan overlay atau layout yang membutuhkan background transparan. |

Gunakan hanya asset dengan status `CANONICAL` untuk production.

## Asset Authority

Authority untuk asset mengikuti hirarki project:

`Repository / System Authority → Project Context → Approved Asset Decision → Canonical Asset → Production Use`

Asset tidak menjadi canonical hanya karena file tersebut berada di repository.

Asset baru harus memiliki keputusan atau approval yang cukup sebelum digunakan sebagai official production asset ketika status tersebut memang diperlukan.

## Brand Asset Rules

- Jangan mengganti official logo dengan AI-generated replacement.
- Jangan mengubah proporsi, geometry, atau identity logo.
- Gunakan primary logo sebagai default kecuali layout membutuhkan transparent variant.
- Canva digunakan sebagai finalization layer untuk logo placement, sizing, alignment, spacing, dan treatment ketika presisi visual diperlukan.
- Exploratory variants dan mockups tidak boleh diperlakukan sebagai canonical asset tanpa approval eksplisit.

## Reference vs Canonical

Bedakan tiga kondisi berikut:

- `CANONICAL` — asset resmi yang boleh digunakan untuk production.
- `REFERENCE` — asset untuk referensi visual atau eksplorasi; bukan official production asset.
- `EXPLORATORY` — output percobaan yang belum memiliki status canonical.

Jangan menghapus provenance atau mengubah status asset secara diam-diam.

## Relationship to Other Project Layers

- `../README.md` — project-level entry point.
- `../00_Context/` — project decisions, context, and asset approval history.
- `../01_Content/` — canonical content state yang menggunakan asset.
- `../03_Production/` — production workflows, SOPs, standards, QC, dan governance.

Asset folder menyediakan file yang digunakan oleh layer produksi; folder ini bukan sumber utama untuk strategic decisions atau production workflow.

## Data Boundary

Folder ini bukan tempat penyimpanan utama:

- dokumen klien;
- data pribadi atau informasi sensitif;
- file kerja sementara;
- export sementara;
- cache atau intermediate production files.

Tambahkan file hanya jika terdapat kebutuhan operasional yang jelas dan file tersebut aman untuk disimpan di repository.

## Maintenance Rules

1. Setiap canonical asset harus memiliki nama file yang jelas dan provenance yang dapat ditelusuri.
2. Jangan membuat duplicate canonical asset tanpa kebutuhan nyata.
3. Jangan menyimpan exploratory output hanya untuk arsip jika tidak memiliki nilai operasional.
4. Perubahan pada official brand asset harus diselaraskan dengan `../00_Context/DECISIONS.md` dan, bila relevan, `../00_Context/CHANGELOG.md`.
5. Jika asset lama digantikan, tandai statusnya sebagai `SUPERSEDED` atau hapus dari canonical set sesuai keputusan yang berlaku.
6. Jangan menambah struktur subfolder sebelum kebutuhan produksi nyata muncul.

## Current Status

**ACTIVE** — folder asset berisi canonical BAKU Edit Tugas brand assets dan menjadi sumber file asset resmi untuk production yang relevan.
