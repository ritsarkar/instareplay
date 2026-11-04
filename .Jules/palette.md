## 2024-05-24 - Dynamic ARIA labels in lists
**Learning:** Action buttons within lists (like a delete button for a specific row) need dynamic ARIA labels (e.g., "Delete [Item Name]") rather than generic labels like "Delete". This provides critical context for screen reader users so they know exactly which item the action applies to.
**Action:** When adding ARIA labels to action buttons inside map functions, interpolate identifying information like the item's title or name into the `aria-label` and `title` attributes.
