## 2024-11-09 - Dynamic ARIA labels in data lists
**Learning:** Hardcoded ARIA labels like 'Delete document' on repetitive list items fail to provide adequate context for screen reader users when multiple instances exist on the page.
**Action:** When adding ARIA labels or titles to action buttons within iterative lists or tables (like map functions), always interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) to provide specific context.
