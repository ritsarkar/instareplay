## 2024-10-15 - Dynamic ARIA Labels in Lists
**Learning:** When using action buttons inside lists or tables, static ARIA labels (like "Delete") don't provide enough context for screen reader users on which item is being deleted.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) to provide specific context.
