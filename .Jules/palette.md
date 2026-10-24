## 2024-10-24 - Dynamic ARIA labels for action buttons in lists
**Learning:** When adding ARIA labels to icon-only action buttons (like Delete) inside dynamic lists or tables, static labels (like `aria-label="Delete"`) are insufficient as screen readers won't know *what* is being deleted without additional context.
**Action:** Always interpolate identifying information into the ARIA label (e.g., `aria-label={\`Delete ${doc.title}\`}`) to give screen reader users explicit context for the action.
