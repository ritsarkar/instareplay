## 2024-10-10 - Dynamic ARIA Labels for Action Buttons
**Learning:** For action buttons inside tables or lists (e.g., delete buttons), static ARIA labels like "Delete" are insufficiently descriptive for screen reader users, making it difficult to know which item will be deleted.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information, such as `aria-label={"Delete ${doc.title}"}`, to provide better context for screen reader users.
