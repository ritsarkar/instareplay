## 2024-03-20 - Dynamic ARIA Labels in Lists
**Learning:** Icon-only action buttons within data tables or lists need dynamic ARIA labels (e.g. `aria-label={`Delete ${doc.title}`}`) to provide context for screen reader users, otherwise multiple "Delete" buttons on a page are indistinguishable. The internal icon should also have `aria-hidden="true"` to prevent redundant announcements.
**Action:** Always interpolate identifying information into ARIA labels for action buttons inside `.map()` loops.
