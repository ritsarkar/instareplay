## 2024-07-13 - Add dynamic ARIA labels to table action buttons
**Learning:** Icon-only action buttons in tables or lists are ambiguous to screen reader users if they share identical generic labels (e.g., "Delete"). Dynamic ARIA labels that include the item's identifying information (like the document title) are necessary to provide context.
**Action:** When implementing action buttons for list items, interpolate unique row data (e.g., `aria-label="Delete ${doc.title}"`) and add explicit keyboard focus indicators to ensure users navigating by tab can easily locate their focus.
