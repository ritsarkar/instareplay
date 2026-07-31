
## 2023-10-27 - Dynamic ARIA Labels in Lists
**Learning:** Using generic ARIA labels like `aria-label="Delete"` on icon-only buttons within a list or table provides insufficient context for screen reader users, who will just hear "Delete, button" multiple times.
**Action:** When implementing icon-only action buttons in repeated items (like tables or lists), always use dynamic string interpolation to include identifying information in the `aria-label` and `title` (e.g., ``aria-label={`Delete ${doc.title}`}``).
