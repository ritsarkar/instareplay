## 2025-01-20 - Dynamic ARIA Labels for List/Table Actions
**Learning:** Found a missing dynamic ARIA label in `DocumentTable.tsx`. Screen readers often announce generic labels like "Delete" for every item in a list or table, making it difficult to understand which item is being deleted without additional context.
**Action:** Always interpolate contextual identifiers (e.g., `aria-label="Delete ${doc.title}"`) when adding `aria-label` or `title` attributes to action buttons within lists or tables. Add `aria-hidden="true"` on internal icons to prevent redundant announcements.
