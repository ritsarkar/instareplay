## 2024-08-25 - Dynamic ARIA Labels in Tables
**Learning:** When using action buttons (like delete or edit) within list items or table rows, generic ARIA labels like 'Delete' are insufficient for screen reader users as they lack context of *what* is being deleted.
**Action:** Always interpolate identifying information (e.g., row title or item name) into the `aria-label` and `title` attributes (e.g., `aria-label={\`Delete ${doc.title}\`}`) to provide full context.
