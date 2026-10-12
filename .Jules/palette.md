## 2024-10-12 - Dynamic ARIA labels for list items
**Learning:** For action buttons inside tables or lists, generic ARIA labels like "Delete" are insufficient for screen reader context.
**Action:** Always interpolate identifying information into ARIA labels and titles (e.g., `aria-label={"Delete ${doc.title}"}`) to provide necessary context.
