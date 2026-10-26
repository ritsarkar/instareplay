## 2025-02-20 - Dynamic ARIA Labels in Lists
**Learning:** When using action buttons inside maps/lists (like deleting a document), generic ARIA labels like "Delete" are insufficient for screen reader users as they lose context of *which* item is being acted upon.
**Action:** Always interpolate identifying information into ARIA labels for list items (e.g., `aria-label={\`Delete ${item.name}\`}`).
