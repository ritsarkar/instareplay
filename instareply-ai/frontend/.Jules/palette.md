## 2024-09-02 - [Dynamic ARIA labels in tables]
**Learning:** Icon-only buttons inside lists or tables lack context for screen reader users when they only have generic labels like "Delete".
**Action:** Always use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) for action buttons within lists or tables to provide better context.