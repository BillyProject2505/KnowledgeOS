# CWC Asset 004 — Footer Platform (CANDIDATE)

## Status

`NOT YET CANONICAL` — matches Linear (`BUS-22` / CWC Reference Sheet). This
directory holds a **CANDIDATE** production build only. It does not modify,
lock, or supersede the CRS's locked specification.

Two distinct value sets are described in the CRS. This build uses the
**visual-size candidate under review** (64 px pill / 28 px icons / 18 px
type), not the currently locked 48 px / 20 px / 14 px configuration. Do not
promote these files to canonical without an explicit Owner decision
recorded against `BUS-22`.

## Files

| File | Description |
| --- | --- |
| `CWC_Asset004_Footer_MASTER_CANDIDATE.svg` | Vector master, candidate geometry, Blue treatment |
| `CWC_Asset004_Footer_Blue_CANDIDATE.svg` / `.png` | Variant 01 — Monochrome Blue `#0B3D9E`, transparent background |
| `CWC_Asset004_Footer_White_CANDIDATE.svg` / `.png` | Variant 02 — Monochrome White `#FFFFFF`, transparent background |
| `QA_ContextPreview_Blue_on_White_CANDIDATE.png` | Blue variant placed at bottom of a 1080×1350 white QA canvas (preview only — not for production use) |
| `QA_ContextPreview_White_on_Blue_CANDIDATE.png` | White variant placed at bottom of a 1080×1350 `#0B3D9E` QA canvas (preview only — not for production use) |
| `qa_layout_measurements.json` | Analytic layout math (content-group centering, padding) |
| `qa_pixel_report.json` | Automated pixel-level QA results against the rendered PNGs |

Production PNG assets (`*_CANDIDATE.png`, excluding the two `QA_ContextPreview_*` files) are transparent-background, 1070×64 px, matching the candidate pill geometry exactly (no hidden fill layer).

## Known limitation — icon fidelity

The four Owner-provided reference images (Facebook, Instagram, WhatsApp,
TikTok) were supplied as vision input in the originating conversation only.
This build environment had **no on-disk file access to those attachments**,
so an automated raster trace (potrace-style silhouette extraction) against
the actual reference pixels could not be run.

The icon paths in this build were instead hand-constructed as clean vector
geometry via close visual reference to the supplied images — i.e. each
platform's foreground brand mark only (Facebook's lowercase *f*, Instagram's
camera-outline mark, WhatsApp's bubble+handset mark, TikTok's note mark),
with the colored circular badge/background discarded per spec. This is a
best-effort visual reconstruction, not a pixel-verified automated trace of
the supplied files.

If pixel-exact fidelity to the specific supplied PNGs is required, that
needs either (a) the reference files placed on disk in a future session so
an automated trace pass can run, or (b) manual Owner sign-off that the
hand-constructed shapes in this build are an acceptable match.

## QA summary

All 22 automated pixel/geometry checks pass (`qa_pixel_report.json`):

- Canvas: both QA context previews measure exactly 1080×1350.
- Pill: both variant PNGs measure exactly 1070×64 (candidate height), fully
  transparent outside the stroke, no hidden fill rectangle.
- Color: every fully-opaque pixel in each variant equals its single
  treatment color exactly (`#0B3D9E` / `#FFFFFF`); anti-aliased edge pixels
  stay within expected alpha-blending rounding noise of that color — no
  second hue, no gradient, no colored circular badge.
- Alignment: content-group center measured at X = 535.0 px against a pill
  center of 535.0 px (0.0 px deviation); vertical content bbox centers at
  Y ≈ 31.5–32 against the Y = 32 primary axis.
- Horizontal padding: ≈157.7 px each side (well above the 18 px minimum).
- Order: Instagram → Facebook → TikTok → WhatsApp.
- Text: `@cozwecare.id`, `@teshivmdo`, `@cozwecare.id`, `0822-9255-2915`
  rendered verbatim in Montserrat Medium 500, actual font (not a fallback).
- Variant parity: Blue and White variants are pixel-identical in geometry
  (alpha channel), differing only in treatment color.

Visual QA (both context previews, inspected at native and 3× zoom): icons
read clearly at Instagram scale, spacing feels even, no crowding, no
platform-native color leakage, no filled circular icon backgrounds, Blue
and White variants match structurally.

**Overall verdict: PASS WITH MINOR REVISION** — held to "minor revision"
rather than a clean PASS solely because of the icon-fidelity limitation
above (hand-reconstructed vs. automated pixel-trace of the actual supplied
files); every other locked construction, alignment, color, and typography
requirement passes without qualification.

Linear: https://linear.app/bussiness-content-os/issue/BUS-22/cwc-reference-sheet-crs
