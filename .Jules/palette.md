## 2026-09-16 - Dynamic ARIA Labels in Lists
**Learning:** When adding ARIA labels to repetitive action buttons within lists or tables (like "Delete" or "Edit"), static labels are insufficient and create a frustrating screen reader experience by lacking context.
**Action:** Always interpolate identifying data (e.g., `aria-label={\`Delete ${doc.title}\`}`) to provide distinct, contextual labels for every row.
