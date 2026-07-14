## 2024-03-20 - Dynamic ARIA Labels in Lists
**Learning:** For action buttons inside iterating lists or tables (like deleting a specific item), static ARIA labels are insufficient. Screen readers will announce "Delete" repeatedly without context.
**Action:** Always interpolate identifying information into ARIA labels and titles for list item actions (e.g., `aria-label="Delete ${item.name}"`).
