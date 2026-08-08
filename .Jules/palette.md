## 2023-10-25 - Dynamic ARIA Labels for List Items
**Learning:** Icon-only action buttons within mapped lists or tables need dynamic context to be accessible. A generic "Delete" label doesn't tell screen reader users *what* is being deleted when iterating through rows.
**Action:** When adding ARIA labels or titles to action buttons in lists, always interpolate identifying information from the loop context (e.g., `aria-label={"Delete " + doc.title}`) to provide clear context for screen reader users.
