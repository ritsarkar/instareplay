## 2026-06-28 - Topbar Keyboard Accessibility
**Learning:** The Topbar buttons (notifications and user menu) previously used `focus:ring` which caused unsightly focus rings when clicked with a mouse. Also, the user menu lacked padding to offset the ring properly.
**Action:** Use `focus-visible:ring` instead of `focus:ring` for all interactive elements to show focus rings ONLY during keyboard navigation. Ensure proper padding (`p-1 -mr-1`) and border radius (`rounded-lg`) so the ring wraps the element beautifully.
