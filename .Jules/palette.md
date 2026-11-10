## 2026-11-10 - Dynamic ARIA labels for action buttons
**Learning:** Hardcoded ARIA labels like "Delete document" in tables or lists are insufficiently descriptive for screen reader users when multiple similar actions exist on a page.
**Action:** Always interpolate identifying information (e.g., `aria-label={`Delete ${doc.title}`}`) into ARIA labels and titles for action buttons inside map functions to provide clear context.
