## 2023-10-25 - Dynamic ARIA labels for list items
**Learning:** Icon-only action buttons within data lists (like delete buttons) lack context for screen readers when they don't include the item's identifying name, making it hard to know which item is being acted upon.
**Action:** Always interpolate identifying information (like document titles or user names) into the `aria-label` and `title` of action buttons in tables/lists (e.g., `aria-label="Delete ${doc.title}"`), and ensure `aria-hidden="true"` is on the icon.
