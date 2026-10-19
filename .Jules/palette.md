## 2024-10-19 - Dynamic ARIA Labels for List Actions
**Learning:** For action buttons within lists or tables, static ARIA labels are insufficient for screen reader users. They need context to know *which* item the action applies to.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information from the list item (e.g., `aria-label={"Delete " + doc.title}`) to provide better context.
