# BAKU Edit Tugas — QC System

**Status:** Active
**Version:** 2.1
**Authority:** Derived from `Operating_Model.md` v2.1, `Control_Matrix.md` v2.1, and `Master_Workflow.md` v2.1

## Purpose

Folder ini berisi quality-control artifacts yang digunakan untuk memverifikasi apakah hasil produksi memenuhi scope, applicable requirements, mandatory controls, dan Final QC gate.

## QC Principles

- QC verifies outcomes; it does not redefine normative controls.
- Use the control IDs defined in `Control_Matrix.md`.
- Record evidence proportional to risk and scope.
- Do not convert missing evidence directly into `FAIL` without applying MC-09 Evidence Sufficiency.
- Preserve `OPEN`, `WAITING_AUTHOR`, `WAITING_SOURCE`, and `ESCALATED` findings until properly resolved.
- Critical unresolved findings block delivery.

## QC Layer

```text
Operating_Model.md
        ↓
Control_Matrix.md
        ↓
Master_Workflow.md
        ↓
SOPs
        ↓
QC Artifacts
```

QC artifacts verify execution of the controls and SOPs. They must not become competing sources of normative rules.

## Planned QC Artifacts

- Intake QC
- Production/Human Review QC
- Academic Compliance QC
- Originality / AI Review QC
- Final QC

Artifacts should reference applicable control IDs rather than duplicate full control definitions.

## Status

QC artifact set is being built incrementally from the approved v2.1 Operating Model and SOP layer.
