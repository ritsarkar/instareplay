## 2026-09-18 - Dynamic ARIA labels for action buttons in lists
**Learning:** When adding ARIA labels to icon-only action buttons within lists or tables (like a delete button for a specific row), using static labels like 'Delete' lacks context for screen reader users.
**Action:** Always interpolate identifying information from the row data (e.g., `aria-label={\`Delete ${doc.title}\`}`) to provide precise context for action buttons.
