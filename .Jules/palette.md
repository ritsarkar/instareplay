## 2026-10-31 - Dynamic ARIA labels for Icon-Only Action Buttons
**Learning:** Adding static ARIA labels (e.g. 'Delete') to icon-only buttons in lists or tables is insufficient, as it doesn't give screen readers context of *what* is being deleted.
**Action:** Use dynamic ARIA labels and titles that interpolate identifying context, like `aria-label="Delete ${item.title}"`, and remember to add `aria-hidden="true"` to the icon to avoid redundant announcements.
