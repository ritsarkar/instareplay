## 2024-05-15 - Dynamic ARIA Labels in Lists
**Learning:** Hardcoded ARIA labels like `aria-label="Delete"` are insufficient in lists or tables, as screen reader users hear multiple identical "Delete" actions without context of what is being deleted.
**Action:** Always interpolate identifying information (like the item title or ID) into ARIA labels and titles for action buttons inside iterative maps (e.g., `aria-label={"Delete ${item.title}"}`).
