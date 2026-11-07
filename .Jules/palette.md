## 2024-05-24 - Dynamic ARIA labels for lists
**Learning:** For action buttons within lists or tables, static ARIA labels (like "Delete") are insufficient for screen reader users as they don't provide context about *what* is being deleted when multiple buttons exist on the page.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) to provide better context and improve accessibility.
