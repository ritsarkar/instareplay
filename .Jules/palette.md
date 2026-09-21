## 2026-09-21 - Dynamic ARIA Labels for Action Buttons
**Learning:** Adding static ARIA labels like 'Delete' to action buttons within lists or tables lacks context for screen reader users, making it difficult to know which item will be deleted.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label={\`Delete ${doc.title}\`}`) to provide better context for screen reader users.
