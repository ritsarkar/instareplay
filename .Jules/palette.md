## 2026-08-12 - Dynamic ARIA labels for List Actions
**Learning:** For action buttons inside iterative lists or tables (like deleting a specific document), static ARIA labels like "Delete document" are insufficient for screen readers because they lack context when navigating out of flow. Dynamic ARIA labels that interpolate identifying data (e.g., `Delete ${doc.title}`) provide critical context.
**Action:** When adding accessibility to action buttons in maps/lists, always use dynamic data from the iteratee to create unique, descriptive ARIA labels and native titles.
