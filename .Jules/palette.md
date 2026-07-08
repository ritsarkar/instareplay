## 2024-07-08 - Accessible action buttons in tables
**Learning:** Icon-only action buttons (like delete or edit) inside data tables or lists lack context for screen reader users if they only have static "Delete" labels.
**Action:** Always use dynamic `aria-label` and `title` attributes that interpolate the identifying information from the row (e.g., `aria-label={\`Delete ${doc.title}\`}`) to provide specific context. Ensure `type="button"` and focus classes are applied.
