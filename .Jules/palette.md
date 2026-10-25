## 2024-10-25 - Dynamic ARIA Labels in Lists
**Learning:** Icon-only action buttons inside mapped lists or tables require dynamic, interpolated context (like `aria-label={"Delete ${item.name}"}`) to provide meaningful announcements for screen readers, as static labels (like "Delete") fail to differentiate which item is being acted upon.
**Action:** Always interpolate identifying item information into `aria-label` and `title` attributes when rendering action buttons within iterations.
