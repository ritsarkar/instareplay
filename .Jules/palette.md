## 2025-02-24 - Dynamic ARIA Labels in Lists
**Learning:** Icon-only action buttons within lists or tables need dynamic ARIA labels that interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`). Static labels like "Delete document" lack context when a screen reader reads through a list of items.
**Action:** Always include item-specific context in `aria-label` and `title` attributes for action buttons in mapped components.
