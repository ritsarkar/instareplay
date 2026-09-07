## 2024-05-15 - Dynamic ARIA Labels in Lists
**Learning:** When adding action buttons (like Delete or Edit) to items in a list or table, using a static 'aria-label' is insufficient because screen reader users lose the context of which item the button affects. Dynamic ARIA labels that interpolate identifying information (like the item's title) provide much better context.
**Action:** Always use dynamic data (e.g., `aria-label={\`Delete ${item.name}\`}`) when creating action buttons within mapped lists or data tables.
