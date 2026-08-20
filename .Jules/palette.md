## 2024-08-20 - Dynamic ARIA Labels in Lists
**Learning:** Icon-only action buttons within iterative lists or tables lose their meaning for screen readers without specific context.
**Action:** Use dynamic ARIA labels (e.g., `aria-label={"Delete " + item.name}`) to inject the current item context into the action button.
