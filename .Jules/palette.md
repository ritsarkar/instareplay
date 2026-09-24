## 2026-09-24 - Dynamic ARIA Labels in Lists
**Learning:** Action buttons in lists or tables (like "Delete" or "Edit") need dynamic ARIA labels (e.g., `aria-label="Delete ${doc.title}"`) to provide adequate context for screen reader users, rather than generic labels like "Delete".
**Action:** Always interpolate identifying information into ARIA labels for action buttons within lists or tables.
