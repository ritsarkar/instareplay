## 2026-07-29 - Dynamic ARIA labels for list actions
**Learning:** When adding actions (like delete) to items within a list or table, static labels like 'Delete' are insufficient for screen readers because they lack context. Users won't know *what* they are deleting.
**Action:** Always interpolate identifying information into ARIA labels and titles for action buttons in collections (e.g. `aria-label={\"Delete \${item.title}\"}`).
