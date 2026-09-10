## 2024-05-24 - Dynamic ARIA Labels in Action Button Lists
**Learning:** For action buttons inside dynamically mapped lists or tables, static ARIA labels (e.g., "Delete") are insufficient for screen readers as they result in a list of identical "Delete Button" announcements. Users cannot determine which item an action is associated with.
**Action:** When implementing action buttons in mapped lists, always use dynamic values from the mapped object (e.g., ``aria-label={`Delete ${item.title}`}``) for the `aria-label` and `title` attributes to provide specific context.
