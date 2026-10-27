## 2023-10-27 - [Dynamic ARIA labels for action buttons in lists/tables]
**Learning:** Hardcoded ARIA labels like "Delete document" in tables with multiple rows create a poor screen reader experience because users cannot distinguish which item the button deletes.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label={`Delete ${doc.title}`}`) for action buttons within loops or tables.
