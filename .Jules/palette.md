## 2024-01-20 - Dynamic ARIA Labels in Lists
**Learning:** Hardcoded "Delete" ARIA labels in tables or lists are ambiguous to screen reader users because they don't know *what* is being deleted without additional context.
**Action:** Always interpolate identifying information (like document title or item name) into the ARIA label and title attributes for icon-only action buttons within lists (e.g., `aria-label={\`Delete ${doc.title}\`}`).
