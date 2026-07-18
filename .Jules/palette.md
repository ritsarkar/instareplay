## 2026-07-18 - Dynamic ARIA labels for list actions
**Learning:** When adding ARIA labels to icon-only action buttons within a list or table (like a delete button for a specific row), static labels like 'Delete' lack context for screen reader users, making it difficult to distinguish which item the action applies to.
**Action:** Always interpolate identifying information from the row data into the ARIA label and title (e.g., `aria-label={\"Delete \" + doc.title}`) to provide precise context, and pair this with `aria-hidden=\"true\"` on the internal icon.
