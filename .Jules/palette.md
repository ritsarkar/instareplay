## 2024-10-21 - Dynamic ARIA Labels for Action Buttons
**Learning:** Generic action buttons (like a trash icon) inside lists or tables lack context for screen reader users when announced repeatedly as just "Delete". Adding dynamic `aria-label` attributes that interpolate the identifying information (e.g., `aria-label="Delete ${doc.title}"`) significantly improves context.
**Action:** Always interpolate identifying row data into ARIA labels for action buttons in lists and tables.
