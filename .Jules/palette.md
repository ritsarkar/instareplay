## 2024-03-05 - Dynamic ARIA labels for list items
**Learning:** Action buttons within lists/tables benefit significantly from dynamic ARIA labels that interpolate identifying information (like document titles) rather than generic labels like "Delete". This provides critical context for screen reader users when navigating tabular data.
**Action:** Always interpolate unique row identifiers (titles, names, IDs) into ARIA labels and tooltips for row-level action buttons.
