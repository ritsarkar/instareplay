## 2024-10-18 - DocumentTable Accessibility
**Learning:** Found an icon-only delete button in the Knowledge Document table lacking aria-label, title, and keyboard navigation support.
**Action:** Always add aria-labels with dynamic context (e.g., `Delete ${doc.title}`) to icon-only action buttons in tables.
## 2024-10-18 - UploadZone Accessibility
**Learning:** Found an icon-only close button in the UploadZone modal lacking aria-label, title, and keyboard navigation support.
**Action:** Always add aria-labels (e.g., 'Close modal') to icon-only action buttons in modals.
