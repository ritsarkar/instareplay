## 2026-08-06 - Context-Specific ARIA Labels for Action Buttons
**Learning:** For action buttons within lists or tables (like delete or edit buttons), a generic ARIA label (e.g., 'Delete') does not provide enough context for screen reader users traversing the list.
**Action:** Always interpolate identifying information into the ARIA label and title for list item actions, for example: `aria-label={"Delete " + doc.title}` to provide clear, actionable context.
