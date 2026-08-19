## 2024-08-19 - [Dynamic ARIA labels for list actions]
**Learning:** When adding action buttons to list or table items, using dynamic ARIA labels (e.g., \`aria-label={\`Delete ${doc.title}\`}\`) provides critical context for screen reader users compared to a generic "Delete" label.
**Action:** Always interpolate identifying information into ARIA labels and titles for action buttons within iterative lists.
