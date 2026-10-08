## 2024-10-25 - Dynamic ARIA labels for action buttons in lists
**Learning:** Icon-only action buttons (like Delete/Edit) inside lists or tables often lack context for screen reader users when simply labelled 'Delete'. Adding dynamic data to the label and title provides essential context.
**Action:** When adding ARIA labels to icon-only buttons within iterated data (lists, tables), always use dynamic labels that interpolate identifying information, such as `aria-label={"Delete " + doc.title}`.
