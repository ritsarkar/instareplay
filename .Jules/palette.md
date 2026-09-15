## 2026-09-15 - Dynamic ARIA labels for table action buttons
**Learning:** Action buttons inside list or table rows (like 'Delete') need dynamic ARIA labels (e.g., `aria-label="Delete ${doc.title}"`) so screen reader users know exactly which item the action applies to.
**Action:** Always interpolate identifying information into ARIA labels for iterative UI components.
