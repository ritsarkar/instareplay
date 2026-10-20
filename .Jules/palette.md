## 2023-10-24 - Dynamic ARIA labels for list actions
**Learning:** Icon-only buttons inside lists/tables need specific context, otherwise a screen reader will just announce "Delete, button" multiple times.
**Action:** When adding aria-labels to list item actions, interpolate identifying info (e.g., `aria-label={"Delete " + doc.title}`) to provide better context for screen reader users. Also add `type="button"`, `aria-hidden="true"` to the icon, and keyboard `focus-visible` states.
