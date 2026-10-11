## 2024-10-10 - Add dynamic ARIA labels to list item action buttons
**Learning:** Action buttons inside lists (like delete or edit buttons) need dynamic ARIA labels that include the item's identifying information (e.g., the title) so screen reader users have proper context about what item they are modifying.
**Action:** Always interpolate identifying data when setting `aria-label` and `title` attributes on icon-only action buttons within mapped lists.
