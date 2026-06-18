## 2024-03-24 - Screen Reader Compatibility for Lucide Icons
**Learning:** Found an accessibility issue pattern specific to this app's components: icon-only buttons using `lucide-react` icons (e.g., `<Trash2>`, `<X>`, `<Bell>`) lack context for screen readers. Screen readers may try to announce the SVG details unhelpfully.
**Action:** When adding icon-only buttons, always implement `aria-label` and `title` on the `<button>` itself, and add `aria-hidden="true"` to the inner Lucide icon component to prevent redundant and confusing screen reader announcements.
