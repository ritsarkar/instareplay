## 2025-08-14 - Dynamic ARIA labels for action buttons within lists or tables
**Learning:** For action buttons like 'Delete' or 'Edit' within lists or tables where there are multiple identical buttons, using a static ARIA label like "Delete" is not sufficient for screen reader users as they won't know which item they are acting upon.
**Action:** Always interpolate identifying information into the ARIA label and title (e.g., `aria-label="Delete ${doc.title}"`) to provide better context for screen reader users. Also hide purely decorative icons within these buttons using `aria-hidden="true"`.
