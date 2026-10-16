## 2024-10-16 - Dynamic ARIA labels in Lists and Tables
**Learning:** Adding static `aria-label="Delete"` to icon-only action buttons inside mapped lists or tables creates poor accessibility experiences, as screen reader users hear identical generic announcements for multiple distinct items.
**Action:** Always use dynamic ARIA labels and titles that interpolate identifying information (e.g., `aria-label="Delete ${doc.title}"`) to provide better context for screen reader users navigating iterative UI structures.
