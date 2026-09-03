
## 2024-05-18 - Add Dynamic ARIA Labels to Table Actions
**Learning:** In tables or lists with action buttons (e.g., delete buttons per row), static ARIA labels like `aria-label="Delete"` are insufficient for screen reader users as they do not provide context on *what* is being deleted.
**Action:** Always interpolate identifying row data (e.g., item name or title) into the `aria-label` and `title` attributes for action buttons within iterative lists or tables (e.g., `aria-label={\`Delete \${doc.title}\`}`).
