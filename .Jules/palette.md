## 2024-05-15 - Dynamic ARIA labels for action buttons in lists
**Learning:** Hardcoded ARIA labels like "Delete" for list items lack context for screen reader users and make it impossible to distinguish which item is being acted upon.
**Action:** Use string interpolation with item identifying information (e.g. `aria-label={\`Delete ${doc.title}\`}`) and apply this dynamically to title attributes as well to ensure clarity for all assistive technologies.
