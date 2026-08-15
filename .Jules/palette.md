## 2024-08-15 - Action Buttons in Tables
**Learning:** Icon-only action buttons within list items or table rows (like delete buttons) need dynamic context in their ARIA labels (e.g., `Delete ${item.title}`) so screen reader users know exactly which item the action applies to, rather than hearing a generic "Delete" multiple times.
**Action:** Always interpolate identifying information into `aria-label` and `title` attributes for action buttons in repetitive structures.
