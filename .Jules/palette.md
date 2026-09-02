## 2024-09-02 - Dynamic ARIA labels for action buttons
**Learning:** Action buttons within tables or lists (like delete buttons) need specific context for screen reader users. A generic "Delete" label is insufficient when there are multiple delete buttons on the page.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label={\`Delete ${doc.title}\`}`) to provide better context.
