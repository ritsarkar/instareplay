## 2024-08-10 - Dynamic ARIA Labels for Table Actions
**Learning:** Icon-only action buttons within tables or lists (like a delete trash can) often lack context for screen reader users when multiple identical actions exist on the page. Generic labels like "Delete" are ambiguous.
**Action:** Always interpolate identifying information into ARIA labels and titles for row-specific actions (e.g., `aria-label="Delete ${doc.title}"`) and add `aria-hidden="true"` to the internal icon to prevent redundant announcements. Also, ensure standard keyboard focus states are present.
