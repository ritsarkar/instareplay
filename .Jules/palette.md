## 2026-07-04 - Dynamic ARIA Labels in Lists
**Learning:** Using generic ARIA labels (like "Delete") on action buttons within lists or tables fails to provide enough context for screen reader users, making it unclear which item is being acted upon.
**Action:** Always interpolate identifying information into ARIA labels and titles for action buttons inside iterative structures (e.g., `aria-label={"Delete " + doc.title}`).
