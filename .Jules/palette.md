## 2026-08-11 - Dynamic ARIA Labels for Action Buttons
**Learning:** Icon-only buttons within lists or tables need dynamic context. A generic "Delete" label is not enough for screen reader users when there are multiple identical buttons in a list.
**Action:** Use string interpolation for `aria-label` and `title` attributes (e.g., `aria-label={"Delete ${doc.title}"}`) to provide necessary context for screen reader users, along with adding proper focus states and `aria-hidden="true"` to the inner icons.
