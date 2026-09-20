## 2024-11-20 - Dynamic ARIA labels in mapped tables
**Learning:** When adding ARIA labels to action buttons inside lists or tables, static labels like "Delete document" lack context when a screen reader navigates through multiple identical items.
**Action:** Always use dynamic interpolation (e.g. `` aria-label={`Delete ${doc.title}`} ``) to provide specific context for screen reader users and tooltip hover states.
