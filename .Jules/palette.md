## 2024-05-24 - [Dynamic ARIA labels for list items]
**Learning:** Action buttons within lists or tables require dynamic ARIA labels to provide screen reader users with sufficient context (e.g., including the document title).
**Action:** Always interpolate identifying information (e.g. `aria-label="Delete ${item.name}"`) when rendering repeating action buttons.
