## 2024-05-22 - Missing ARIA Labels on Icon-Only Buttons
**Learning:** Found an accessibility issue pattern: several icon-only buttons across the app (like `Trash2`, `X`, and `Bell`) are missing accessible names (`aria-label`) and visual hints (`title`), which impacts screen readers and usability.
**Action:** Always verify that buttons containing only icons have `aria-label` and `title` attributes, and that the inner icons have `aria-hidden="true"`.
