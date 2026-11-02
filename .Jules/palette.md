## 2023-10-27 - Dynamic ARIA Labels in Lists
**Learning:** Hardcoded ARIA labels on repeated elements (like "Delete" buttons in a list or table) fail to provide sufficient context for screen reader users, making it impossible to know *which* item is being targeted without navigating backwards.
**Action:** Always interpolate identifying information into ARIA labels for actions within mapped arrays/tables (e.g., `aria-label={"Delete " + doc.title}`).
