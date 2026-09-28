## 2024-05-22 - Dynamic ARIA Labels for List Action Buttons
**Learning:** Icon-only action buttons inside data tables and lists (like a delete button in a mapped row) need dynamic, interpolated ARIA labels (e.g., `aria-label={"Delete " + item.title}`) so screen reader users know exactly *which* item they are acting upon, rather than hearing "Delete" redundantly for every row.
**Action:** Always interpolate unique identifying row information into the `aria-label` and `title` attributes for icon-only action buttons in mapped lists.
