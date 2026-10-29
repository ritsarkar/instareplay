## 2024-10-29 - Dynamic ARIA Labels for List Items
**Learning:** When using action buttons in lists or tables, static ARIA labels like "Delete" lack context. Hiding the internal icon from screen readers while interpolating identifying information into the button's ARIA label prevents redundant announcements.
**Action:** Use dynamic ARIA labels (e.g., `aria-label={"Delete " + item.title}`) for action buttons inside map functions, and apply `aria-hidden="true"` to the internal icon element.
