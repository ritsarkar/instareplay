## 2024-05-18 - Dynamic ARIA labels for Data Tables
**Learning:** For action buttons within lists or tables (like DocumentTable), static ARIA labels (e.g., "Delete") are insufficient. Users need context on *what* they are deleting.
**Action:** Always interpolate identifying information into ARIA labels and titles for row-level actions (e.g., `aria-label={`Delete ${doc.title}`}`).
