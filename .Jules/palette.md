## 2026-06-10 - Upload Zone Keyboard Accessibility
**Learning:** Interactive divs containing nested buttons create invalid HTML and confuse screen readers, a common issue when building complex clickable areas like dropzones.
**Action:** Always convert interactive wrapper divs to `role="button"` with `tabIndex={0}` and `onKeyDown` handlers, and change nested visual 'buttons' to `<span>` elements styled to look like buttons.
