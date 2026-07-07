## 2024-07-07 - Dynamic ARIA Labels in Lists/Tables
**Learning:** For icon-only action buttons within lists or tables, static ARIA labels (e.g., "Delete") lack sufficient context for screen reader users to know *what* they are deleting.
**Action:** Always use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) to provide complete context for each list/table item.
