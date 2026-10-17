## 2024-11-20 - [Enhanced Icon-only Delete Button Accessibility]
**Learning:** Found that the DocumentTable's delete action button lacked accessible labeling and keyboard focus states, making it difficult to use for non-mouse users.
**Action:** Implemented standard dynamic `aria-label` and native tooltips, while specifically using Tailwind's `focus-visible` classes to ensure visible focus states only appear during keyboard navigation.
