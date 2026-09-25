## 2025-02-25 - Initial Learnings
**Learning:** Understanding frontend components.
**Action:** Proceed to fix minor UX/a11y issues.

## 2025-02-25 - Dynamic ARIA Labels for List Actions
**Learning:** For action buttons within lists or tables, static ARIA labels like "Delete" lack context. Using dynamic ARIA labels (e.g., `aria-label={"Delete " + doc.title}`) provides necessary identifying information for screen reader users, making the action's target clear.
**Action:** Always interpolate contextual identifying information into ARIA labels and titles for repeatable UI actions in lists/tables.
