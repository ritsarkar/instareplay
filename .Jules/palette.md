## 2024-05-19 - Dynamic ARIA Labels in Action Lists
**Learning:** For icon-only action buttons within data tables/lists (like the delete button in DocumentTable), a static `aria-label="Delete"` lacks sufficient context for screen reader users to know *which* item is being deleted.
**Action:** Always interpolate contextual data into ARIA labels and titles (e.g., `aria-label={\`Delete ${doc.title}\`}`) and ensure the icon itself has `aria-hidden="true"` to prevent redundant announcements.
