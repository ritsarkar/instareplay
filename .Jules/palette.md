
## 2026-09-17 - Dynamic ARIA labels in tables
**Learning:** When adding ARIA labels to action buttons inside lists or tables, static labels (like 'Delete') lack context for screen reader users.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information from the row (e.g., `aria-label="Delete ${doc.title}"`) to provide clear context.
