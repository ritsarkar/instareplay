## 2024-07-06 - Dynamic ARIA Labels in Lists
**Learning:** When using icon-only action buttons inside loops (like a Document Table), static ARIA labels (e.g. "Delete") create a poor screen reader experience because users lose context of *what* is being deleted.
**Action:** Always interpolate identifying row data into the ARIA label and title (e.g. `aria-label={"Delete " + doc.title}`) to provide crucial context.
