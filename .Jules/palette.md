## 2024-03-24 - Dynamic ARIA Labels in Lists
**Learning:** For action buttons within lists or tables (like delete buttons), static ARIA labels like "Delete document" lack context when read by a screen reader navigating the list.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) to provide better context for screen reader users. Always apply `aria-hidden="true"` to the internal icon and include standard keyboard focus classes.
