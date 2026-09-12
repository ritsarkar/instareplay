## 2026-09-12 - Dynamic ARIA Labels for Icon Buttons in Tables
**Learning:** Table action buttons with plain "Delete" ARIA labels cause ambiguity for screen reader users when multiple rows exist. A button without type="button" may inadvertently act as a submit button in forms.
**Action:** Use string interpolation to include identifying context in the aria-label and title (e.g., `aria-label="Delete ${doc.title}"`), and always explicitly set type="button" for icon-only action buttons.
