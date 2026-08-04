## 2024-08-04 - Dynamic ARIA Labels in Lists
**Learning:** Icon-only buttons within iterated lists (like tables) need dynamic ARIA labels (e.g., `aria-label="Delete ${doc.title}"`) to give screen reader users context. Without this, a screen reader user simply hears "Delete" repeatedly without knowing what they are deleting.
**Action:** Always interpolate identifying information into ARIA labels and titles for action buttons inside lists or tables.
