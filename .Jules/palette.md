## 2026-08-29 - Dynamic ARIA Labels in Tables
**Learning:** For action buttons inside lists or tables (like delete buttons), using generic labels like "Delete" lacks context for screen readers. It's critical to interpolate identifying information from the row (e.g., `Delete ${doc.title}`) into `aria-label` and `title` attributes so users know exactly what item they are acting upon.
**Action:** When adding action buttons to repeated elements (tables, lists, cards), always use the item's title or ID to create a dynamic, descriptive `aria-label` and `title`.
