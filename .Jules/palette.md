## 2024-10-24 - Dynamic ARIA Labels in Lists
**Learning:** For action buttons within lists or tables, using generic labels like "Delete" lacks context for screen reader users when multiple identical buttons exist on a page.
**Action:** Always use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label={`Delete ${doc.title}`}`) to provide better context for screen reader users.
