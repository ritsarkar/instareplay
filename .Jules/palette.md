## 2024-05-15 - Icon-only Buttons A11y
**Learning:** Found multiple instances where interactive, icon-only actions (like delete buttons) lack essential ARIA attributes, causing poor screen reader experiences.
**Action:** Always verify icon-only buttons include `aria-label`, `title`, explicit `type="button"`, and apply `aria-hidden="true"` to the inner SVG/icon component to prevent redundant screen reader announcements.
