## 2024-05-15 - Dynamic ARIA labels for list items
**Learning:** For list or table items containing action buttons, standard aria-labels (like "Delete") fail to provide enough context for screen reader users, making it unclear which item is being affected.
**Action:** Always interpolate identifying information into ARIA labels and titles (e.g., `aria-label={\`Delete ${doc.title}\`}`) when dealing with repeatable actions in a list/table view.
