## 2024-11-20 - [Dynamic ARIA Labels for Action Buttons]
**Learning:** Hardcoded ARIA labels on action buttons in lists/tables (e.g., "Delete") lack context, making it hard for screen reader users to know *what* they are deleting.
**Action:** Always use dynamic ARIA labels (e.g., `aria-label={`Delete ${item.name}`}`) and matching `title` attributes for row-level action buttons.
