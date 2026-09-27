## 2026-09-27 - Dynamic ARIA Labels in Lists
**Learning:** When adding actions (like delete) to items within lists or tables, static ARIA labels like 'Delete' are insufficient for screen reader users as they lack context. Using dynamic labels that interpolate identifying information (e.g., `aria-label=Delete ${doc.title}`) provides necessary context.
**Action:** Always include specific identifying content from the row/list item when adding ARIA labels or titles to action buttons in collections.
