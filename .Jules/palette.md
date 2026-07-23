## 2024-07-23 - Dynamic ARIA Labels in Lists
**Learning:** For icon-only action buttons within a list or table (like a delete button for a document), a generic `aria-label="Delete"` is insufficient and confusing when multiple identical buttons are read by screen readers.
**Action:** Always interpolate identifying information into the `aria-label` and `title` (e.g., ``aria-label={`Delete ${doc.title}`}``) to provide explicit context about what item will be affected.
