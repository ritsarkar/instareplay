## 2024-05-14 - Dynamic ARIA Labels for List Actions
**Learning:** For action buttons within mapping functions rendering lists or tables (e.g., delete buttons per document row), a static label like "Delete" is insufficient for screen readers, as they won't know *which* item is being deleted if navigating outside table semantics.
**Action:** Always interpolate identifying information into ARIA labels and titles (e.g., `aria-label={\`Delete ${doc.title}\`}`) to provide clear context for screen reader users when implementing action items in lists.
