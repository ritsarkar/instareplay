## 2026-11-08 - Accessible action buttons with dynamic context
**Learning:** For delete buttons inside dynamic lists/tables (like DocumentTable), generic `aria-label="Delete"` is insufficient for screen readers as they lose context of *what* is being deleted.
**Action:** Always interpolate the item's identifying name into both `aria-label` and `title` attributes (e.g., `` `Delete ${doc.title}` ``) on list item action buttons to provide clear context for assistive technologies.
