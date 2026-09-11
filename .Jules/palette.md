
## 2024-05-18 - Dynamic ARIA labels in tables
**Learning:** Adding static ARIA labels like `aria-label="Delete"` to icon-only buttons inside lists or tables causes screen readers to read "Delete, Delete, Delete" without providing context on *what* is being deleted.
**Action:** Always interpolate identifying information (e.g., `aria-label={\`Delete \${item.name}\`}`) into the ARIA label and `title` attributes for action buttons within repeating data structures to provide proper context.
