## 2024-08-28 - Dynamic ARIA Labels for List Actions
**Learning:** When using icon-only action buttons inside lists or tables, static ARIA labels (e.g., "Delete") lack context for screen reader users, who hear "Delete, button, Delete, button" without knowing what item will be deleted.
**Action:** Always interpolate identifying information into ARIA labels and titles for list items (e.g., `aria-label={"Delete " + doc.title}`) to provide crucial context.
