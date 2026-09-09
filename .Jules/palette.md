## 2024-05-18 - Dynamic ARIA Labels in Lists
**Learning:** Screen reader users lose context when all action buttons in a list just say 'Delete'. Without contextual information in the label, users tabbing through buttons won't know which item they are operating on.
**Action:** Always interpolate identifying information (like item title) into ARIA labels and titles for action buttons inside lists/tables.
