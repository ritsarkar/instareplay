## 2026-06-17 - Focus Outline Anti-Pattern
**Learning:** Found multiple instances where `focus:outline-none` was used without a corresponding fallback focus style (like `focus-visible:ring-2`), effectively breaking keyboard navigation for accessibility. Using `focus:outline-none` also hides the default focus indicator from screen readers.
**Action:** Always pair `focus:outline-none` with `focus-visible` utility classes to ensure keyboard focus states remain visible to users relying on keyboard navigation without disrupting mouse clicks.
