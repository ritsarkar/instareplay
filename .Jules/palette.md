## 2026-10-09 - Dynamic ARIA labels for action buttons in lists
**Learning:** When dealing with lists or tables that have action buttons (like delete or edit) on each row, it is crucial to use dynamic ARIA labels (e.g., `aria-label="Delete ${doc.title}"`) rather than static ones (`aria-label="Delete"`). This provides critical context for screen reader users so they know *which* item they are acting upon, avoiding ambiguity.
**Action:** Always interpolate identifying information (like title or name) into ARIA labels and titles for action buttons inside map functions or lists.
