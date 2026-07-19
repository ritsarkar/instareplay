## 2024-05-24 - Dynamic ARIA Labels in Lists
**Learning:** Screen reader users lose context in data tables or lists when identical action buttons (like "Delete") only have static ARIA labels. They hear "Delete button" multiple times without knowing *what* is being deleted.
**Action:** Always interpolate identifying information into ARIA labels and titles for list/table actions (e.g. `aria-label="Delete ${item.name}"`). Apply `aria-hidden="true"` to any internal icons to prevent redundant announcements.
