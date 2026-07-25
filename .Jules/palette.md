## 2024-07-25 - Dynamic ARIA labels for action buttons in lists/tables
**Learning:** Using generic ARIA labels like "Delete" for action buttons in lists or tables lacks context for screen reader users, making it difficult to know which specific item is being targeted.
**Action:** Always use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) to provide better context for screen reader users when dealing with list items.
