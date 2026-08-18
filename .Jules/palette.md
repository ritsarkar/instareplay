## 2024-05-18 - Dynamic ARIA Labels in Lists
**Learning:** Icon-only action buttons inside tables or lists (like "Delete") are confusing for screen readers when they simply announce "Delete" without context.
**Action:** Always interpolate identifying information into ARIA labels and titles for list items, such as `aria-label={"Delete " + item.title}`, to give screen reader users context about what they are affecting.
