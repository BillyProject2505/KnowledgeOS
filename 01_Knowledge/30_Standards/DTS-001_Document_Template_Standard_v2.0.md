# Document Template Standard (DTS)

**Document ID:** DTS-001  
**Version:** 1.0  
**Status:** LOCK  
**Category:** Standard  
**Owner:** KnowledgeOS  
**Applies To:** Seluruh dokumen dalam KnowledgeOS

---

# 1. Purpose

Document Template Standard (DTS) menetapkan struktur baku untuk seluruh dokumen di KnowledgeOS agar konsisten, mudah dibaca, mudah dipelihara, dan mudah digunakan kembali.

DTS mengatur kerangka penulisan dokumen, bukan isi spesifik dari setiap dokumen.

---

# 2. Scope

Standar ini berlaku untuk seluruh kategori dokumen dalam KnowledgeOS, termasuk:

- Principles
- Frameworks
- Standards
- Bibles
- Registries
- Templates
- Prompts
- References
- Decisions
- README

---

# 3. Template Principles

## DTS-P01 — Consistency First

Dokumen dalam kategori yang sama harus menggunakan struktur yang konsisten.

---

## DTS-P02 — Purpose Before Detail

Setiap dokumen harus menjelaskan tujuan sebelum menjelaskan implementasi.

---

## DTS-P03 — Logical Flow

Dokumen disusun dari konsep umum menuju rincian operasional.

---

## DTS-P04 — Reusable Structure

Template harus dapat digunakan kembali lintas proyek.

---

## DTS-P05 — Human & AI Readable

Dokumen harus mudah dipahami oleh manusia maupun diproses oleh AI.

---

# 4. Universal Document Structure

Seluruh dokumen menggunakan struktur dasar berikut.

```text
Metadata
Purpose
Scope
Definitions (Optional)
Core Content
Relationships
Governance
Canonical Decision (If Applicable)
```

---

# 5. Metadata Standard

## Mandatory Metadata

- Document ID
- Title
- Version
- Status
- Category
- Owner
- Applies To

## Optional Metadata

- Created Date
- Last Updated
- Supersedes
- Superseded By

---

# 6. Standard Templates by Document Category

## 6.1 Principle

### Mandatory Sections

- Metadata
- Purpose
- Core Principles
- Relationship
- Governance

### Optional Sections

- Definitions
- Examples

---

## 6.2 Framework

### Mandatory Sections

- Metadata
- Purpose
- Scope
- Core Philosophy
- Architecture
- Core Components
- Relationships
- Governance
- Canonical Decision

### Optional Sections

- Examples
- Diagrams
- Reference Models

---

## 6.3 Standard

### Mandatory Sections

- Metadata
- Purpose
- Scope
- Principles
- Rules
- Procedures
- Relationships
- Governance
- Canonical Decision

### Optional Sections

- Examples
- Checklists
- Exceptions

---

## 6.4 Bible

### Mandatory Sections

- Metadata
- Purpose
- Scope
- Domain Knowledge
- Operational Rules
- Relationships
- Governance

### Optional Sections

- Examples
- Best Practices
- FAQs

---

## 6.5 Registry

### Mandatory Sections

- Metadata
- Purpose
- Registry Structure
- Registered Objects
- Relationships
- Governance

### Optional Sections

- Notes
- Change Log

---

## 6.6 Template

### Mandatory Sections

- Metadata
- Purpose
- Template Structure
- Usage
- Governance

### Optional Sections

- Examples
- Recommendations

---

## 6.7 Prompt

### Mandatory Sections

- Metadata
- Purpose
- Input
- Prompt
- Expected Output

### Optional Sections

- Notes
- Constraints
- Examples

---

## 6.8 Reference

### Mandatory Sections

- Metadata
- Purpose
- Source
- Summary

### Optional Sections

- Usage Notes
- Related References

---

## 6.9 Decision

### Mandatory Sections

- Metadata
- Context
- Decision
- Rationale
- Consequences
- Status

### Optional Sections

- Alternatives Considered
- Review Notes

---

# 7. Heading Convention

Gunakan heading Markdown secara konsisten.

```text
# 1. Purpose

# 2. Scope

# 3. ...

## 3.1 ...

### 3.1.1 ...
```

Aturan:

- Level 1 (`#`) digunakan untuk bagian utama.
- Level 2 (`##`) digunakan untuk subbagian.
- Level 3 (`###`) digunakan bila diperlukan.
- Hindari level yang lebih dalam kecuali benar-benar diperlukan.

---

# 8. Relationship

```text
Knowledge Classification Framework
            │
            ▼
Document Template Standard
            │
            ▼
Frameworks
Standards
Bibles
Registries
Templates
Prompts
References
Decisions
```

DTS memastikan seluruh dokumen yang dihasilkan melalui KnowledgeOS memiliki struktur yang seragam.

---

# 9. Governance

Seluruh dokumen baru dalam KnowledgeOS:

- wajib menggunakan template sesuai kategorinya;
- wajib menyertakan seluruh mandatory metadata;
- wajib menyertakan seluruh mandatory sections;
- dapat menambahkan optional sections sesuai kebutuhan;
- tidak boleh mengubah struktur inti tanpa pembaruan resmi terhadap DTS.

---

# Canonical Decision

Document Template Standard (DTS) merupakan standar resmi yang mengatur struktur seluruh dokumen dalam KnowledgeOS.

Seluruh dokumen wajib menggunakan template sesuai kategorinya, mengikuti metadata standar, serta mempertahankan keseimbangan antara konsistensi dan fleksibilitas melalui penggunaan mandatory sections dan optional sections. Dengan demikian, seluruh KnowledgeOS tetap menjadi Single Source of Truth yang terstruktur, mudah dipelihara, dan mudah digunakan kembali.
