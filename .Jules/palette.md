## 2024-07-27 - Dynamic ARIA labels for action buttons in lists/tables
**Learning:** Screen reader users can easily get confused by multiple identical action buttons (like "Delete") in a list or table without surrounding context.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label={`Delete ${doc.title}`}`) to provide better context for screen reader users.
