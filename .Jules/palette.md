## 2024-09-14 - Dynamic ARIA Labels in Lists
**Learning:** Action buttons within lists/tables need dynamic ARIA labels (interpolating identifying info like `doc.title`) to provide essential context for screen reader users, preventing a page full of ambiguous "Delete" announcements.
**Action:** Always interpolate unique identifying information (like item names or IDs) into `aria-label` and `title` attributes for repeated action buttons in mapped list or table components.
