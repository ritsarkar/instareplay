## 2025-03-01 - Dynamic ARIA labels for List Action Buttons
**Learning:** For action buttons within dynamic lists or tables (like deleting a specific document), a static aria-label (e.g., "Delete") provides insufficient context for screen reader users. The label needs to interpolate identifying information.
**Action:** Always use dynamic interpolation (e.g., `aria-label={"Delete " + item.title}`) for list-based action buttons to ensure context is preserved for accessibility.
