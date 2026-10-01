## 2024-10-01 - Dynamic ARIA labels for action buttons in lists/tables
**Learning:** Action buttons in lists or tables (e.g. Delete) need dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) to provide better context for screen reader users, rather than a generic "Delete".
**Action:** Always include item-specific context in `aria-label` and `title` attributes for icon-only action buttons within repeating elements like lists and tables.
