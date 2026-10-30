## 2024-10-30 - Dynamic ARIA Labels in Lists
**Learning:** When using action buttons in lists or tables, static ARIA labels (like "Delete") are insufficient. Screen reader users need context about *what* they are acting on.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) to provide better context.
