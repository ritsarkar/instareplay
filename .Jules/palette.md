## 2024-07-16 - Dynamic ARIA Labels for List Action Buttons
**Learning:** Icon-only action buttons within a list or table (like "Delete") are confusing for screen reader users when multiple instances exist on a single page, as they all read generically (e.g., "Delete button").
**Action:** Always interpolate identifying information (e.g., `aria-label={"Delete " + item.name}`) into the ARIA labels and title attributes for action buttons mapped over arrays, and apply `aria-hidden="true"` to the internal decorative icon.
