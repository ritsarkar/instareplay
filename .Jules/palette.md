
## 2023-10-27 - Action Buttons Context
**Learning:** Icon-only action buttons within lists or tables need dynamic ARIA labels (e.g., `Delete ${doc.title}`) rather than static ones (e.g., `Delete document`) to provide specific context for screen reader users and maintain keyboard accessibility with proper focus rings.
**Action:** Always interpolate identifying data (like title or ID) into ARIA labels and title attributes for repeated action buttons in map functions. Additionally, hide the purely visual inner icon using `aria-hidden="true"`.
