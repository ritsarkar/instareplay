## 2024-09-04 - Dynamic ARIA labels and focus states for icon-only buttons
**Learning:** When using icon-only buttons inside lists or tables, static aria-labels can be ambiguous for screen readers. Additionally, icon-only buttons often lack visual boundaries making custom focus classes necessary.
**Action:** Use string interpolation to inject dynamic context into `aria-label` and `title` attributes (e.g., `aria-label={\`Delete ${doc.title}\`}`). Add specific focus outline classes to ensure keyboard navigability, and apply `aria-hidden="true"` to the internal icon element.
