## 2024-08-03 - [Accessibility] Dynamic ARIA labels for list items
**Learning:** When using action buttons within lists or tables, static ARIA labels (like "Delete") lack context for screen reader users navigating by interactive elements. Using dynamic labels that incorporate row data (e.g., `aria-label="Delete ${doc.title}"`) provides critical context without cluttering the visual UI.
**Action:** Always interpolate identifying information into ARIA labels and titles for action buttons inside iterative components (tables, lists, cards) across the application.
