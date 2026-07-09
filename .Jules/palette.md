## 2023-10-27 - Added ARIA Label and Focus State to Document Table Delete Button
**Learning:** The DocumentTable component used icon-only buttons for document deletion, lacking accessible names for screen readers and visible focus indicators for keyboard navigation.
**Action:** Replaced the plain button with an accessible version, utilizing dynamic `aria-label` and `title` based on document titles, adding `aria-hidden="true"` to the internal icon, and utilizing Tailwind `focus-visible` utility classes for clear keyboard focus.
