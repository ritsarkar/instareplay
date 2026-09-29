
## 2026-09-29 - Accessibility for Dynamic List Buttons
**Learning:** When dealing with action buttons within a list of items (like a table of documents), static `aria-label`s like "Delete" are insufficient for screen readers as they lack context of *what* is being deleted.
**Action:** Use dynamic string interpolation for `aria-label` and `title` attributes on action buttons (e.g., `` aria-label={`Delete ${doc.title}`} ``) to provide full context to assistive technologies.
