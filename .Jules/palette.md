## 2026-09-30 - Dynamic ARIA labels for action buttons
**Learning:** Adding static ARIA labels to action buttons within lists or tables (like "Delete") lacks context for screen reader users when multiple similar buttons exist.
**Action:** Always interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) into ARIA labels and titles for action buttons inside iterative collections to provide better context.
