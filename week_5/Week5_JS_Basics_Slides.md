% Week 5: JavaScript Foundations with CodePen
% CST1100 Intro to Computing
% Week 5 Session

# Agenda

- Situate JavaScript in the web stack
- Review syntax foundations and mental models
- Explore DOM access and event handling patterns
- Practice debugging with DevTools & console
- Preview the CodePen lab deliverables

::: notes
Welcome students, outline the hour, and connect to last week. Emphasize that today pairs conceptual understanding with hands-on experimentation in CodePen.
:::

# Why JavaScript Matters

- Runs in every modern browser without installs
- Powers interactivity, validation, animation, and data flow
- Bridges design intent and user experience expectations
- Connects front-end UI to APIs and back-end services

::: notes
Highlight everyday experiences where JS plays a role—form validation, live search, dashboards. Reinforce that JS complements HTML/CSS rather than replacing them.
:::

# JavaScript in the Browser

- Rendering engine handles HTML/CSS; JS engine executes scripts
- Single-threaded execution loop reacts to events
- DOM updates happen instantly; the tree stays live
- Blocking code freezes the UI—keep handlers lightweight

::: notes
Use a slide diagram or the whiteboard to sketch the call stack and event loop. Mention names (V8, SpiderMonkey) to demystify, but reassure students we will stay at fundamentals.
:::

# Language Building Blocks

- Declare values with `const` (fixed) or `let` (mutable)
- Primitive types: string, number, boolean, null, undefined
- Objects and arrays group related data
- Template literals make string interpolation clean

::: notes
Relate to Python: variables, lists, dictionaries. Explain why `var` is deprecated in introductory code. Show a quick example of a template literal vs string concatenation.
:::

# Functions & Scope

- Functions encapsulate reusable behavior
- Parameters accept input; `return` passes values back
- Block scope controls variable visibility
- Closures capture surrounding variables for later use

::: notes
Demo a simple function in the browser console. Point out how event handlers rely on closures to remember references, foreshadowing the lab.
:::

# Control Flow Essentials

- `if / else` handles decisions
- Comparison operators (`===`, `>`, `<`) evaluate conditions
- Logical operators (`&&`, `||`, `!`) combine checks
- `for` and `for...of` loops iterate over arrays

::: notes
Walk through predicting the result of a short snippet. Encourage students to mentally trace boolean expressions before testing in the console.
:::

# DOM Refresher

- HTML becomes a node tree (Document Object Model)
- `document.querySelector` grabs the first matching element
- `textContent`, `innerHTML`, `classList` update structure & styling
- Attribute methods (`setAttribute`, `dataset`) add metadata

::: notes
Open DevTools Elements panel and show how selecting a node highlights it in the DOM. Emphasize the difference between writing HTML and mutating it with JS.
:::

# Event-Driven Thinking

- Events describe user actions or system changes
- Listen with `addEventListener('click', handler)`
- Handlers receive an event object for context
- Keep handlers focused: read, decide, update

::: notes
Break down the anatomy of an event listener. Mention common mistakes—forgetting parentheses, referencing stale variables—and how to avoid them.
:::

# Live Demo Roadmap

- Select DOM nodes required for interaction
- Track UI state with a boolean or string
- Update text and classes inside the handler
- Mirror each change with a console log for verification

::: notes
Preview what students should watch for in the live coding segment. Invite them to spot the select → listen → update pattern.
:::

# Debugging Toolkit

- `console.log`, `console.table`, `console.error` for visibility
- Read error messages: type, description, file, line number
- Breakpoints in DevTools pause code to inspect values
- Refresh frequently to ensure a clean state

::: notes
Normalize debugging as a collaborative habit. Share a quick story of a past bug to humanize troubleshooting.
:::

# Lab Preview

- Build a "Product Spotlight" pen from the provided starter
- Semantic HTML boxes in hero, features, and detail areas
- CSS variables define theme and responsive layout
- Buttons update detail copy without page reloads

::: notes
Walk through a screenshot or the starter pen so students understand deliverables. Clarify naming and submission expectations.
:::

# Success Criteria

- Accessible structure and focus management
- Consistent styling with tokens and responsive rules
- Event handlers update content reliably
- Reflection explains debugging insights and next steps

::: notes
Connect the rubric to daily practice. Encourage students to test with keyboard navigation and screen readers if possible.
:::

# Stretch Ideas

- Surprise button cycles through features automatically
- Dark mode toggle swaps CSS variable values
- Transition animations polish detail updates
- Persist last selection with `localStorage`

::: notes
Motivate fast finishers. Remind the class these are optional but demonstrate how small additions reinforce learning.
:::

# Wrap-Up & Next Steps

- Summarize the select → listen → update rhythm
- Celebrate debugging wins and shared strategies
- Preview asynchronous JavaScript and fetch APIs next week
- Encourage students to recreate the pen locally as practice

::: notes
End with energy. Invite questions, then transition into lab time or logistics.
:::

