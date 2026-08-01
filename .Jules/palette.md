
## 2024-05-18 - Dynamic ARIA Labels for List Actions
**Learning:** Action buttons (like delete, edit) in list/table views often lack context for screen readers when they are just icon-only (e.g., "Delete" repeated 10 times).
**Action:** When implementing action buttons in lists, always interpolate the item's identifying name into the `aria-label` and `title` (e.g., `aria-label={\`Delete ${doc.title}\`}`) to provide specific context for assistive technologies and tooltips.
