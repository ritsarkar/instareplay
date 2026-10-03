## 2024-05-18 - Dynamic ARIA Labels for Action Buttons
**Learning:** Action buttons in lists or tables (like Delete or Edit) without context are unhelpful for screen reader users, resulting in repetitive "Delete" announcements that aren't tied to the specific item.
**Action:** Always interpolate identifying information into ARIA labels and titles for action buttons inside iterative mapping elements (e.g., `aria-label={`Delete ${doc.title}`}`).
