# BAKU Edit Tugas — AI Visual Production Protocol

**Status:** Canonical Production Protocol  
**Version:** 1.0  
**Scope:** AI-assisted visual generation for BAKU Edit Tugas social media assets

## 1. Purpose

Menstandarkan penggunaan image generator agar AI menghasilkan **visual asset**, bukan final poster.

Master Frame, typography, exact copy, logo, CTA, spacing, alignment, dan final composition tetap dikendalikan secara manual melalui Canva.

## 2. Core Principle

> **AI generates the visual. Canva assembles the communication.**

AI adalah production aid. AI tidak menjadi sumber kebenaran untuk exact text, logo fidelity, production typography, exact dimensions, atau precise layout.

## 3. Input Requirements

Sebelum generation tersedia:

- approved content brief;
- approved service identity;
- visual brief;
- applicable Master Frame / visual specification;
- approved brand visual references;
- defined visual objective;
- defined negative constraints.

Jangan meminta image generator membuat konsep tanpa brief yang jelas.

## 4. Generation Boundary

### AI MAY generate

- hero illustration;
- people/character illustration;
- academic objects;
- laptop, document, desk, study environment;
- contextual visual metaphor;
- lighting and atmosphere;
- internal composition of the hero visual;
- background treatment when explicitly requested.

### AI MUST NOT generate

- BAKU logo or logo recreation;
- exact brand wordmark;
- final headline or body copy;
- CTA text;
- WhatsApp number or contact information;
- service badge text;
- benefit/card copy;
- footer text;
- exact typography;
- final poster hierarchy;
- fake testimonials, statistics, claims, or service promises;
- invented brand assets.

If text appears accidentally, treat it as a generation defect and do not use it as final copy.

## 5. Composition Boundary

The image generator should create a visual that can be placed inside the approved poster system.

Unless the visual brief explicitly requires otherwise:

- preserve usable negative space;
- avoid placing critical visual details at the intended text area;
- do not simulate the full Master Frame;
- do not create a complete social media poster;
- do not reproduce the logo area;
- do not create UI-like cards or CTA components.

## 6. Brand Alignment

Visual output should feel:

**Professional + Modern + Academic + Approachable**

Use the approved BAKU visual language and references. Do not introduce unrelated visual styles merely for novelty.

Consistency with the Master Frame takes priority over decorative creativity.

## 7. Generation Instruction Pattern

Every visual generation brief should define:

```text
ROLE
Create a hero visual asset for BAKU Edit Tugas.

SUBJECT
[What the visual represents]

CONTEXT
[Academic/service context]

STYLE
[Approved visual style]

COMPOSITION
[Subject placement and negative-space requirement]

BRAND DIRECTION
[Approved palette / visual language / reference]

OUTPUT BOUNDARY
Create only the visual asset. Do not create the final poster.

DO NOT GENERATE
Logo, readable text, typography, CTA, phone number,
service badge, information cards, footer, or final poster layout.
```

## 8. Post-Generation QC

Reject or regenerate when:

- logo is recreated;
- readable text is generated and incorrect;
- visual contradicts the service;
- visual introduces unsupported claims;
- composition leaves insufficient space for Canva assembly;
- visual style conflicts with the approved system;
- visual contains obvious artifacts;
- output effectively becomes a different poster design.

Accept only when the asset is usable as a component of the approved poster system.

## 9. Handoff to Canva

After AI Visual QC:

1. select the approved visual asset;
2. place it into the Master Frame;
3. insert original logo manually;
4. insert approved copy manually;
5. apply approved typography;
6. build cards and CTA manually;
7. verify spacing and safe area;
8. perform Final QC;
9. export only after all production gates pass.

## 10. Relationship to Other Standards

Use this protocol together with:

- `../04_Standards/Instagram_Poster_Production_Standard.md`
- `../04_Standards/Hero_Service_Visual_Specification.md`
- `../04_Standards/Hero_Service_Poster_Completeness_Checklist.md`
- `Hero_Service_Visual_Brief_Template.md`
- `AI_Visual_QC_Checklist.md`

This document controls **how AI generates visual assets**. It does not replace the canonical visual standards or Final QC.