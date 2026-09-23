## 2024-05-24 - Dynamic ARIA labels for icon-only action buttons in lists
**Learning:** Icon-only buttons within lists (like delete buttons in a document table) lack context for screen readers when they only say "Delete".
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) to provide better context, set `type="button"`, and apply `aria-hidden="true"` to the internal icon to prevent redundant announcements.
