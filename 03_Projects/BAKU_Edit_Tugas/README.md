# BAKU Edit Tugas

## Purpose

Project-level source of truth for the BAKU Edit Tugas brand, content, assets, production system, approved decisions, and current work.

This directory contains durable project context and production references. Execution state belongs in the appropriate execution workspace and should not be inferred solely from this README.

## Project Scope

BAKU Edit Tugas provides:

1. Jasa editing tugas
2. Jasa pengerjaan tugas
3. Jasa konsultasi

Primary audience:

- siswa;
- mahasiswa.

Primary platforms:

- Instagram
- Facebook
- WhatsApp Business
- TikTok

Brand direction:

**Professional + Modern + Academic + Approachable**

Communication should remain santai tetapi profesional, jelas, natural, ramah, dan meyakinkan without unsupported claims or excessive hard-selling.

## Repository Structure

```text
BAKU_Edit_Tugas/
├── 00_Context/
├── 01_Content/
├── 02_Assets/
├── 03_Production/
└── README.md
```

### `00_Context/`

Durable project context, approved decisions, changelog, platform references, and other canonical project-state documents.

### `01_Content/`

Canonical content state for active and approved content work.

### `02_Assets/`

Canonical project assets such as approved brand files.

### `03_Production/`

Production operating system for client work, including workflows, SOPs, AI assistance, standards, QC, templates, knowledge, and governance.

## Authority & Source of Truth

Use the project files in this directory as the durable source of truth for project-level decisions and approved production context.

Authority order remains:

`Repository / System Authority → Project Context → Production Documentation → Working Content → Exploratory Output`

Exploratory conversation output, generated mockups, and unapproved variants are not canonical unless explicitly approved and recorded.

## Current Workstream

**Instagram Story Highlight — FAQ**

Purpose of the FAQ Highlight:

`Profile → FAQ Highlight → Trust → Inquiry → Conversion`

The Highlight is a persistent decision-support asset for prospective customers who have already reached the BAKU profile. It is not primarily treated as a daily reach-oriented format.

## Current Production State

The four-story FAQ structure is canonical.

- **Story 1:** visual baseline approved.
- **Stories 2–4:** next production items; not yet final.
- **Visual system:** approved flat editorial illustration.
- **Logo:** canonical assets stored in `02_Assets/Brand/` and added manually in Canva.
- **Finalization layer:** Canva for typography, logo placement, alignment, spacing, copy, CTA, and final QC.

The earlier realistic/cinematic treatment is superseded and must not be reintroduced unless explicitly revised.

## Approved FAQ Structure

### Story 1 — Positioning

Hook: `Ini joki skripsi ya?`

Answer:

`Bukang! Torang itu dampingi`

`Supaya ngana mangarti`

Supporting copy: `Konsultasi & revisi sesuai kebutuhan.`

### Story 2 — Speed

Hook: `Berapa lama?`

Answer: `1–3 hari`

Supporting copy: `Tergantung panjang & tingkat pengerjaan.`

### Story 3 — Privacy

Hook: `Privasi aman?`

Answer: `Aman. File tidak disebarkan.`

Supporting copy: `Bisa request hapus setelah selesai.`

### Story 4 — Accessibility + Conversion

Hook: `Bisa luar Manado?`

Answer: `Bisa. 100% online.`

CTA: `Butuh bantuan? Chat BAKU →`

## Approved Visual System

Use one reusable Story Frame derived from the approved Story 1 composition.

Maintain consistency in:

- layout structure;
- typography hierarchy;
- logo relationship;
- safe-area treatment;
- question and answer treatment;
- color relationships;
- branding;
- flat editorial illustration language;
- spacing rhythm and composition logic.

Variable elements may include the character, scene, objects, visual metaphor, and supporting imagery.

Core principles:

`Consistency > novelty`

`Clarity > decoration`

`Function > aesthetics`

`Conversion > vanity`

Instagram Story format is **9:16**, target **1080 × 1920 px**, static image. No video or animation for this FAQ Highlight system.

## Brand Assets

Canonical logo assets:

- `02_Assets/Brand/BAKU_Edit_Tugas_logo-primary.png`
- `02_Assets/Brand/BAKU_Edit_Tugas_logo-transparent.png`

Use only canonical brand assets. Do not replace the official logo with AI-generated artwork.

## Production System

Client-work production is governed by the dedicated production system in `03_Production/`.

Master workflow:

```text
Client Request
    ↓
Intake
    ↓
Requirement Analysis
    ↓
Document Diagnosis
    ↓
Editing Plan
    ↓
AI-Assisted Editing
    ↓
Human Review
    ↓
Fact & Citation Verification
    ↓
Formatting
    ↓
Final QC
    ↓
Delivery
```

Core principle:

> AI assists the work; human owns the academic responsibility.

## Claim & Evidence Boundaries

Project documentation must distinguish verified guidance, observation, hypothesis, and unknowns.

Do not present unsupported claims as facts, including guarantees about reach, recommendation, engagement, privacy/security, or fabricated statistics/social proof.

Official Meta guidance is maintained separately in `00_Context/META_PLATFORM_GUIDELINES.md` and must be re-verified as platform policies or product behavior change.

## Maintenance Rule

When a project decision becomes approved, record it in `00_Context/DECISIONS.md` before relying on it as canonical production state.

Keep `01_Content/`, `02_Assets/`, and `03_Production/` aligned with the approved project state. Superseded decisions and stale placeholders should be replaced or explicitly marked rather than silently retained.

## Current Status

**ACTIVE — FAQ Highlight production continues with Stories 2–4.**

For detailed decisions and history, use `00_Context/PROJECT_CONTEXT.md`, `00_Context/DECISIONS.md`, and `00_Context/CHANGELOG.md`.
