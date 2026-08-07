
## 2024-08-07 - Add Dynamic ARIA Labels for Icon Buttons in Tables
**Learning:** Icon-only buttons (like delete or edit) inside data tables/lists are confusing for screen reader users without dynamic ARIA labels. A static label like "Delete document" is insufficient when there are multiple instances in a list, making it ambiguous which row is targeted.
**Action:** Always interpolate identifying data (e.g., `doc.title`) into `aria-label` and `title` attributes (e.g., `Delete ${doc.title}`) for list-based action buttons to ensure exact targeting context.
