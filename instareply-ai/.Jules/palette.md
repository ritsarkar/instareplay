## 2024-05-15 - Dynamic ARIA Labels in Lists
**Learning:** For action buttons within lists or tables, static ARIA labels like "Delete" aren't specific enough for screen reader users when multiple identical actions exist.
**Action:** Always use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) to provide clear context for what item is being acted upon.
