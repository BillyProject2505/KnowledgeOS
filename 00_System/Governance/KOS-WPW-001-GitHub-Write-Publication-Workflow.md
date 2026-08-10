# KnowledgeOS GitHub Write & Publication Workflow

**Document ID:** KOS-WPW-001  
**Version:** 1.0  
**Status:** Canonical / Locked  
**System:** KnowledgeOS  
**Repository:** `BillyProject2505/KnowledgeOS`  
**Default Branch:** `main`

---

## 1. Purpose

The KnowledgeOS GitHub Write & Publication Workflow defines the controlled process for creating, validating, storing, reviewing, publishing, updating, and archiving Knowledge Objects within the KnowledgeOS GitHub repository.

The workflow establishes GitHub as the controlled persistence and version-management layer for KnowledgeOS while preserving KnowledgeOS as the canonical organizational system for reusable knowledge.

The workflow ensures that Knowledge Objects are stored in the correct canonical location, canonical knowledge is not duplicated unnecessarily, project-specific implementation remains separated from universal knowledge, changes are traceable through Git history, `main` represents the approved KnowledgeOS state, AI-assisted writing does not automatically equal canonical publication, and publication occurs only after appropriate validation and governance checks.

---

## 2. Core Principle

> **Creation is not Publication.**

A document created by ChatGPT is initially a **Working Knowledge Artifact**. It becomes **Canonical Knowledge** only after it passes the required validation and publication process.

```text
Create
  ↓
Validate
  ↓
Classify
  ↓
Place
  ↓
Review
  ↓
Publish
  ↓
Canonical
```

No document becomes canonical merely because it exists in ChatGPT or has been written to GitHub.

---

## 3. Source of Truth Model

KnowledgeOS operates using three distinct states:

### 3.1 Working State

Temporary or actively developed material, including drafts, proposed standards, incomplete bibles, working notes, AI-generated first drafts, and proposed governance structures.

Working material is not canonical.

### 3.2 Review State

Material prepared for publication but not yet accepted as canonical, including release candidates, proposed Knowledge Objects, structural refactors, revisions requiring review, and migration candidates.

### 3.3 Canonical State

Approved Knowledge Objects recognized as authoritative within KnowledgeOS. Canonical material has identifiable object or document identity, approved location, defined version, traceable publication history, applicable governance, and may serve as a source for other projects.

---

## 4. Repository Authority

The KnowledgeOS GitHub repository is the persistent version-controlled repository for KnowledgeOS.

The default branch `main` represents the **approved published state** and must not be treated as a personal scratchpad.

---

## 5. Repository Layering

```text
KnowledgeOS
│
├── 00_System
├── 01_Knowledge
├── 02_Projects
├── 03_Resources
└── 99_Archive
```

### 5.1 `00_System`

KnowledgeOS system-level governance, navigation, release, versioning, and operational information.

### 5.2 `01_Knowledge`

Reusable Canonical Knowledge Objects, including Frameworks, Bibles, Standards, Registries, Prompts, Templates, References, and Decisions.

### 5.3 `02_Projects`

Project-specific implementations and integrations, including CozWeCare, OBK, KDS, and Personal.

### 5.4 `03_Resources`

Supporting resources that are not themselves necessarily Canonical Knowledge Objects.

### 5.5 `99_Archive`

Deprecated, historical, legacy, or superseded material. Archived material is not active canonical knowledge.

---

## 6. Classification Before Write

Before writing a document to GitHub, ChatGPT must determine:

1. What is this?
2. Who owns its authority?
3. Is it reusable across projects?
4. Is it project-specific?
5. Is it canonical?
6. Is it a new object or a revision of an existing object?
7. Where should it live?

Primary placement:

```text
Universal Knowledge → 01_Knowledge
Project Knowledge → 02_Projects
Supporting Resource → 03_Resources
Historical / Deprecated → 99_Archive
System Governance → 00_System
```

---

## 7. Write Request

A user may request creation, saving, updating, reviewing, publishing, archiving, or migration. ChatGPT must not assume that every save request means publication to `main`.

The requested operation must first be classified as:

- Draft
- Create
- Update
- Review
- Publish
- Archive
- Migrate

---

## 8. Canonical Placement Check

Before creating a new file, ChatGPT must determine whether an equivalent Knowledge Object already exists.

```text
Does an equivalent object exist?
        │
   ┌────┴────┐
   │         │
  YES        NO
   │         │
Update     Create
existing   new object
```

If an existing canonical object is found, updating or versioning that object is preferred over creating a competing duplicate.

---

## 9. Naming Convention

Canonical files should use stable, descriptive names. Where a Canonical Object ID exists, it should be incorporated into the filename or document metadata.

Recommended pattern:

```text
[CATEGORY]-[OBJECT-ID]-[SHORT-NAME].md
```

Version numbers should generally be stored in document metadata rather than repeatedly changing filenames.

---

## 10. Canonical Document Metadata

Canonical Knowledge Objects should contain metadata identifying their governance state.

Minimum recommended metadata:

```yaml
object_id:
object_name:
object_type:
domain:
status:
version:
authority:
created:
last_updated:
canonical_path:
```

Metadata must not contradict the authoritative registry.

---

## 11. Write Strategy

For existing documents, ChatGPT must retrieve the current version before replacing it. Blind overwriting is prohibited.

Preferred order:

```text
1. Read existing object
2. Understand current state
3. Determine intended change
4. Prepare complete new content
5. Validate
6. Write to branch
7. Review
8. Publish
```

---

## 12. Branch Strategy

The `main` branch represents the approved state. New significant work should occur on a dedicated branch.

Recommended patterns:

```text
knowledge/create/<object-name>
knowledge/update/<object-name>
knowledge/refactor/<object-name>
knowledge/archive/<object-name>
project/cozwecare/<change-name>
```

---

## 13. Commit Strategy

Each logical change should receive a meaningful commit message.

Recommended format:

```text
<action>: <object or scope>
```

Examples:

```text
create: CWC Brand Presenter Bible
update: CWC Canonical Asset Registry
refactor: KnowledgeOS navigation layer
archive: superseded CWC asset specification
```

---

## 14. Pull Request Strategy

For significant canonical changes:

```text
Working Branch
      ↓
Commit
      ↓
Pull Request
      ↓
Review
      ↓
Approval
      ↓
Merge
      ↓
main
```

Pull Requests should communicate what changed, why it changed, affected objects and paths, compatibility implications, whether canonical authority changed, and whether migration is required.

---

## 15. Review Gate

Before publication, evaluate:

- **Identity Gate** — Does the document have a clear identity?
- **Authority Gate** — Is the source of authority clear?
- **Placement Gate** — Is the document stored in the correct layer?
- **Duplication Gate** — Does an equivalent object already exist?
- **Consistency Gate** — Does it conflict with another canonical object?
- **Version Gate** — Is the version appropriate?
- **Governance Gate** — Does the change alter a canonical rule or authority boundary?
- **Completeness Gate** — Is it complete enough to publish?
- **Archive Gate** — If replacing an existing object, has the superseded state been handled correctly?

---

## 16. Canonical Publication

A document may be marked Canonical only when its identity and location are established, content passes validation, conflicts are resolved, version information is established, publication history is traceable, and the applicable review requirements have been satisfied.

```text
Draft
  ↓
Review Candidate
  ↓
Approved
  ↓
Published
  ↓
Canonical
```

---

## 17. Direct-to-Main Exception

Direct writes to `main` should be restricted to low-risk operational changes such as typo corrections, metadata corrections, and navigation fixes.

Changes affecting canonical authority, architecture, governance, registries, standards, bibles, object identity, lifecycle, or project-wide rules should use the branch/review workflow.

---

## 18. Update Existing Canonical Knowledge

When updating a canonical object:

```text
Read current version
       ↓
Identify requested change
       ↓
Preserve unchanged canonical content
       ↓
Apply controlled modification
       ↓
Increment version where required
       ↓
Record change
       ↓
Review
       ↓
Publish
```

The previous version must remain recoverable through Git history.

---

## 19. Supersession

When a new object replaces an old canonical object:

```text
Old Canonical
      ↓
Superseded
      ↓
Archive / Historical State
      ↓
New Canonical
```

The old object must not simply disappear. Its historical relationship to the replacement should be documented when appropriate.

---

## 20. Archive Policy

Archiving is not deletion. Retired canonical objects must preserve the historical artifact, identify why they were retired, identify their replacement where applicable, and be prevented from being interpreted as active canonical knowledge.

---

## 21. AI Write Safety Rule

ChatGPT must distinguish between:

```text
"I wrote this"
```

and:

```text
"This is authoritative."
```

AI-generated content must never become canonical solely because it was generated by ChatGPT. Human/project authority remains responsible for canonical acceptance.

---

## 22. No Silent Publication

ChatGPT must not silently publish a substantial change.

Before a consequential write, the intended action must be clear:

```text
Repository
Path
Operation
Target object
Branch
Publication state
```

---

## 23. Publication Levels

### Level 0 — Local Draft

Exists only in the current working context.

### Level 1 — Repository Draft

Written to GitHub but not recognized as canonical.

### Level 2 — Canonical Publication

Approved and merged into the authoritative `main` state.

---

## 24. Standard ChatGPT Commands

Recommended natural-language commands:

- **Create:** “Create this as a new Knowledge Object in KnowledgeOS.”
- **Save Draft:** “Save this as a repository draft in KnowledgeOS.”
- **Update:** “Update the existing Knowledge Object with these changes.”
- **Review:** “Prepare this change for KnowledgeOS review.”
- **Publish:** “Publish this approved Knowledge Object to KnowledgeOS.”
- **Archive:** “Archive the superseded Knowledge Object.”
- **Audit:** “Audit this Knowledge Object against the current KnowledgeOS structure.”

---

## 25. Recommended Default Workflow

```text
USER
  │
  ▼
ChatGPT creates / modifies content
  │
  ▼
Classification
  │
  ▼
Canonical Placement Check
  │
  ▼
Existing Object Check
  │
  ├── Existing → Update
  │
  └── New → Create
  │
  ▼
Validation
  │
  ▼
Feature / Knowledge Branch
  │
  ▼
Commit
  │
  ▼
Pull Request
  │
  ▼
Review
  │
  ▼
Merge
  │
  ▼
main
  │
  ▼
Canonical KnowledgeOS State
```

---

## 26. Governance Principle

The KnowledgeOS GitHub repository is not merely a file storage system.

> **GitHub preserves the state. KnowledgeOS governs the meaning.**

Git provides history, version control, branches, commits, review, rollback, and publication history.

KnowledgeOS provides classification, authority, canonical identity, placement, lifecycle, relationships, and governance.

These responsibilities must remain separate.

---

## 27. Canonical Workflow Statement

> **No Knowledge Object becomes canonical merely by being created, stored, or committed. Canonical status is established through identity, classification, placement, validation, review, and controlled publication.**

---

## 28. Adoption Status

**Workflow ID:** KOS-WPW-001  
**Version:** 1.0  
**Status:** Canonical / Locked  
**Implementation State:** Publication candidate  
**Target Repository:** `BillyProject2505/KnowledgeOS`  
**Target Layer:** `00_System`  
**Target Path:** `00_System/Governance/KOS-WPW-001-GitHub-Write-Publication-Workflow.md`
