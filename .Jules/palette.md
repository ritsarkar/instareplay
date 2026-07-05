## 2024-07-05 - Dynamic ARIA Labels in Lists/Tables
**Learning:** When adding ARIA labels to action buttons within iterables (like lists or tables), using static labels (e.g., "Delete") creates a poor screen reader experience because users hear "Delete, Delete, Delete" without knowing what they are deleting.
**Action:** Always interpolate identifying information from the item into the `aria-label` and `title` attributes for buttons in iterables (e.g., ``aria-label={`Delete ${item.title}`}``). Add `aria-hidden="true"` to internal icons and explicit `type="button"`.
