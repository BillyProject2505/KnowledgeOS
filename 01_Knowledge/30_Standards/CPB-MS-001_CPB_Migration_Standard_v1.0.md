# CPB-MS-001 — CPB Migration Standard
Version: 1.0
Status: LOCKED
Classification: Canonical Standard

---

# 1. Purpose

The CPB Migration Standard (CPB-MS) defines the mandatory rules for migrating the Coz We Care Production Bible (CPB) from one version to another while preserving architectural integrity, production knowledge, and canonical consistency.

Its primary objective is to ensure that every migration can be performed safely across multiple ChatGPT conversations without depending on conversation memory.

---

# 2. Scope

This standard applies to all future migration activities involving the Coz We Care Production Bible.

It governs:

- Chapter migration
- Architecture migration
- Content migration
- Canonical validation
- Decision recording
- GitHub integration

---

# 3. Core Principle

> Conversations are temporary.
>
> Documentation is permanent.
>
> The Production Bible is the Single Source of Truth.

No production knowledge shall exist exclusively inside ChatGPT conversations.

---

# 4. Migration Rules

## Rule 1 — Architecture Freeze

Before migration begins, the CPB Architecture Refactoring Baseline must be approved and locked.

During migration, the architecture shall not be modified.

---

## Rule 2 — One Chapter per Conversation

Each ChatGPT conversation shall migrate only one chapter.

Example:

- Foundation
- Brand System
- Audience System

Multiple chapters shall never be migrated simultaneously.

---

## Rule 3 — Mandatory Context Header

Every migration conversation shall begin with the following context header.

```text
Project:
Coz We Care Production Bible v2

Architecture:
CPB Architecture Refactoring v2 (Locked)

Current Phase:
Content Migration

Current Chapter:
<Chapter Name>

Source:
CPB v1

Target:
CPB v2

Status:
Draft
```

This header provides the minimum canonical context required for migration.

---

## Rule 4 — Chapter Independence

Every chapter shall be understandable without reading another ChatGPT conversation.

Each chapter must clearly define:

- Purpose
- Scope
- Canonical Decisions
- Operational Rules

Dependencies shall be minimized.

---

## Rule 5 — No Hidden Decisions

All migration decisions shall be documented.

No decision may exist only inside ChatGPT memory.

Every decision shall be written into either:

- the Production Bible, or
- the official Decision Log.

---

## Rule 6 — Mandatory Decision Log

Every migration conversation shall end with a Decision Log.

Example:

```text
Migration Decisions

MD-001
...

MD-002
...

MD-003
...
```

All architectural and editorial decisions shall be recorded.

---

## Rule 7 — Chapter Completion Checklist

Before closing a migration conversation, the following checklist shall be completed.

- Architecture validated
- Content completed
- Rules validated
- Examples reviewed (if applicable)
- Checklist completed (if applicable)
- Canonical review passed
- Decision Log updated

A chapter shall not be considered complete until every required item has been satisfied.

---

## Rule 8 — Chapter Lock

After successful validation, the chapter status shall become:

```text
Status:
LOCKED
```

Locked chapters shall not be modified except through an approved Canonical Change process.

---

## Rule 9 — Migration Sequence

Migration shall follow the approved architecture order.

1. Foundation
2. Brand System
3. Audience System
4. Content Strategy
5. Content Architecture
6. Editorial System
7. Visual Design System
8. Production Workflow
9. Production Quality
10. Publication
11. Appendices

Earlier chapters establish the foundation for later chapters.

---

## Rule 10 — Canonical Validation

Before locking a chapter, the following questions shall be answered.

- Does the chapter follow the approved architecture?
- Does every knowledge object originate from an approved source?
- Is there any conceptual duplication?
- Has governance been separated from production knowledge?
- Does this chapter directly improve AI content production?

If any answer is "No", the chapter shall not be locked.

---

## Rule 11 — GitHub Commit Rule

Each completed chapter shall be committed independently.

Example:

```text
feat(cpb): complete Editorial System chapter
```

Large multi-chapter commits should be avoided.

---

## Rule 12 — Documentation over Conversation

No important information shall exist exclusively inside ChatGPT conversations.

All canonical knowledge shall be transferred immediately into official documentation.

The Production Bible and its supporting documents shall remain the only authoritative source.

---

## Rule 13 — Stateless Conversation Principle

Every new ChatGPT conversation shall be treated as stateless.

The AI shall never assume knowledge from previous conversations.

Instead, every migration shall rely exclusively on:

1. The current Production Bible.
2. The approved CPB Architecture Refactoring Baseline.
3. The official Decision Log.

Conversations are working sessions.

Documentation is canonical.

---

# 5. Definition of Done

A migration is complete only when:

- All migration rules have been satisfied.
- The chapter has passed Canonical Validation.
- The Decision Log has been updated.
- The chapter status is LOCKED.
- The chapter has been committed to GitHub.

Only then may migration proceed to the next chapter.

---

# 6. Canonical Statement

This document is the canonical migration standard for all future versions of the Coz We Care Production Bible.

It shall remain repository-agnostic and serve as the authoritative operational standard governing Production Bible migration.
