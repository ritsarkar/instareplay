## 2024-10-26 - Dynamic ARIA Labels in Lists
**Learning:** Adding static ARIA labels like 'Delete' to action buttons in tables/lists doesn't provide enough context for screen reader users when multiple rows exist.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label={`Delete ${doc.title}`}`) to provide precise context for action buttons within repeatable components.
