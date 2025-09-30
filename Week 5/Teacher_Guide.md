# Week 5 Teacher Guide: JavaScript Foundations with CodePen

This guide equips you to facilitate Week 5's introduction to JavaScript through an accessible, browser-based workflow. It complements the slide deck, demo starter, and student lab to deliver a cohesive experience that builds confidence with core JavaScript concepts while keeping solutions instructor-only.

---

## 1. Session Overview

- **Total time**: 90-minute lecture + 90-minute lab (adjust as needed for your schedule).
- **Arc**: Context → syntax foundations → live demo → guided lab → reflection.
- **Resources**: Slide deck (`Week5_JS_Basics.pptx`), demo starter (`Week5_JS_Demo_Starter.html`), student lab (`Week5_JS_CodePen_Lab.md`), this guide.

---

## 2. Instructor-Facing Learning Objectives

By the end of the week, students should be able to:

1. Explain what the JavaScript engine does inside the browser and how it collaborates with HTML/CSS.
2. Declare variables with `const` and `let`, manipulate strings/numbers/arrays, and trace simple control flow.
3. Use DOM APIs (`querySelector`, `textContent`, `classList`) to update the page in response to user interaction.
4. Attach event listeners that read input, make decisions, and render feedback to the UI.
5. Debug using the CodePen console and browser DevTools, including reading stack traces and using `console.log` strategically.
6. Share polished pens with naming conventions and reflective documentation.

---

## 3. Pre-Class Preparation Checklist

- **Dry-run the demo**: Open `Week5_JS_Demo_Starter.html` locally or paste into a CodePen pen. Practice the live coding sequence in the next section so the flow feels natural.
- **Verify student access**: Confirm that everyone has a CodePen account. Prepare a lightweight "Plan B" (e.g., jsbin, local HTML file) in case of access issues.
- **Review MDN references**: Bookmark key pages (variables, functions, DOM manipulation) to share quickly.
- **Plan formative checks**: Decide on quick cold-call questions or polls (e.g., "What value does this expression produce?").
- **Prepare visual aids**: Print or display the falsy value table and an event flow diagram if you expect visual learners to benefit.

---

## 4. Background Knowledge Refresher

### 4.1 Browser Execution Model

- JavaScript runs on a single-threaded event loop; emphasize that code executes top-to-bottom unless callbacks interrupt.
- The DOM is a live tree; updates mutate elements immediately, affecting layout and accessibility.
- Contrast `document.write` (legacy) versus modern DOM APIs.

### 4.2 Syntax & Data Types

- Primitives: string, number, boolean, null, undefined, bigint, symbol (mention the latter two only for completeness).
- Objects and arrays: highlight literal syntax, dot vs bracket notation, array iteration patterns.
- Template literals and string interpolation keep beginner code readable.

### 4.3 Event Handling Basics

- Common events for beginners: `click`, `input`, `change`, `submit` (with `preventDefault`).
- Walk through the anatomy of an event listener: target selection, handler definition, DOM updates.
- Introduce event bubbling at a high level to set expectations for future weeks.

### 4.4 Debugging Mindset

- Use `console.log` to trace values, but also demonstrate DevTools breakpoints for future growth.
- Encourage students to read error messages left-to-right: error type, message, file, line number.
- Normalize errors as part of the process; celebrate fixes publicly to model persistence.

---

## 5. Suggested Pacing Guide

| Phase | Time | Focus | Instructor Moves |
| --- | --- | --- | --- |
| Warm-Up | 10 min | JavaScript in everyday sites | Ask students to list JS-driven experiences (modals, forms). Preview learning objectives. |
| Concept Mini-Lecture | 25 min | Variables, types, functions | Use slides to introduce syntax; interleave live `console` demos. |
| Live Demo | 20 min | DOM + event handling | Start from `Week5_JS_Demo_Starter.html`; progressively enhance with JS. |
| Lab Launch | 10 min | Walkthrough of lab goals | Model forking the CodePen starter, naming conventions, and deliverables. |
| Lab Work Time | 55 min | Build interactive product spotlight | Circulate, answer questions, capture misconceptions for debrief. |
| Share & Reflect | 20 min | Peer review and debugging takeaways | Facilitate mini-presentations, use prompts from lab reflection section. |
| Wrap-Up | 10 min | Connect to next week | Summarize key patterns and preview asynchronous JS teaser. |

Adjust durations based on class length or pacing needs. If time runs short, capture the reflection asynchronously.

---

## 6. Live Demo Script & Solution Snippets

Use `Week5_JS_Demo_Starter.html` as the base (HTML scaffold + minimal styling). The live coding goal is to implement a feature spotlight toggler without revealing the lab's stretch goals.

### 6.1 Demo Steps

1. **Inspect the scaffold**: Show semantic structure, placeholders, and empty `<script>` tag.
2. **Select DOM nodes**:
   ```javascript
   const highlightButton = document.querySelector('#highlightToggle');
   const statusMessage = document.querySelector('#statusMessage');
   ```
3. **Declare state**:
   ```javascript
   let isHighlighted = false;
   ```
4. **Attach event listener**:
   ```javascript
   highlightButton.addEventListener('click', () => {
     isHighlighted = !isHighlighted;
     statusMessage.textContent = isHighlighted
       ? 'Highlight mode is on — featured specs glow!'
       : 'Highlight mode is off.';
     document.body.classList.toggle('is-highlighted', isHighlighted);
   });
   ```
5. **Emphasize debugging**: Purposely mistype `textContent` then fix it after reading the console error.
6. **Invite extensions**: Ask what other interactions could build on this (e.g., cycling through products, persisting state).

### 6.2 Instructor-Only Solution Outline for Lab

Students will be asked to build a "Product Spotlight" pen with three main sections and interactive buttons. A reference solution is included below for grading and troubleshooting.

```html
<!-- Minimal HTML structure -->
<main class="spotlight">
  <header class="spotlight__header">
    <h1>Week 5 Product Spotlight</h1>
    <p id="statusMessage">Choose a feature to explore.</p>
  </header>
  <section class="spotlight__features">
    <article class="feature-card" data-feature="camera">
      <h2>Crystal Camera</h2>
      <p>Shoots vibrant photos in any lighting.</p>
      <button class="feature-button">See camera details</button>
    </article>
    <!-- Repeat for two more features -->
  </section>
  <aside class="spotlight__details" aria-live="polite">
    <h3 id="detailTitle">Feature details</h3>
    <p id="detailDescription">Select a feature to learn more.</p>
  </aside>
</main>
```

```css
:root {
  --accent: #2563eb;
  --accent-dark: #1d4ed8;
  --bg: #0f172a;
  --text: #e2e8f0;
}
body {
  font-family: "Inter", system-ui, sans-serif;
  background: var(--bg);
  color: var(--text);
  margin: 0;
  padding: 2rem;
}
.feature-card {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.4);
  border-radius: 1rem;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.feature-button {
  background: var(--accent);
  color: white;
  border: none;
  padding: 0.75rem 1rem;
  border-radius: 999px;
  cursor: pointer;
}
.feature-button:hover,
.feature-button:focus-visible {
  background: var(--accent-dark);
}
.is-active {
  outline: 3px solid var(--accent);
}
```

```javascript
const featureCards = document.querySelectorAll('.feature-card');
const detailTitle = document.querySelector('#detailTitle');
const detailDescription = document.querySelector('#detailDescription');

const featureCopy = {
  camera: {
    title: 'Camera Clarity',
    description: 'A 48MP sensor with adaptive HDR keeps details crisp in any light.'
  },
  battery: {
    title: 'Battery Endurance',
    description: 'Stream, scroll, and shoot for 20 hours thanks to smart power modes.'
  },
  audio: {
    title: 'Immersive Audio',
    description: 'Spatial sound and adaptive EQ tune output for every environment.'
  }
};

featureCards.forEach((card) => {
  const button = card.querySelector('.feature-button');
  const featureKey = card.dataset.feature;

  button.addEventListener('click', () => {
    featureCards.forEach((c) => c.classList.remove('is-active'));
    card.classList.add('is-active');

    const { title, description } = featureCopy[featureKey];
    detailTitle.textContent = title;
    detailDescription.textContent = description;
  });
});
```

Encourage students to personalize copy, colors, or additional features while preserving the interaction requirements listed in the lab. When grading, prioritize semantic structure, accessible interaction (focus states, `aria-live` on detail region), and code readability.

---

## 7. Teaching Strategies & Talking Points

### 7.1 Lower the Activation Energy

- Emphasize that JavaScript syntax builds on patterns they already know from Python (variables, conditionals) while pointing out differences (`let` vs `const`, semicolons optional but encouraged).
- Use analogies like "The DOM is the tree of LEGO bricks, and JavaScript is the hand rearranging them."

### 7.2 Model Debugging Behavior

- Verbally narrate your thought process when an error occurs during the demo.
- Encourage a "read the error, locate the line, inspect the state" routine.
- Highlight the power of `console.table` and `console.dir` for arrays/objects once students move beyond primitives.

### 7.3 Connect to Broader Web Development

- Show how the same DOM APIs underpin frameworks they may hear about (React, Vue).
- Mention bundlers and transpilers briefly but reassure that this course sticks to vanilla JS for clarity.

---

## 8. Common Misconceptions & Rescue Plans

| Misconception | Instructor Prompt | Quick Fix |
| --- | --- | --- |
| `const` means immutable object | Clarify that bindings are constant, but object properties can change | Demonstrate modifying object property after `const` declaration |
| Forgetting parentheses when calling functions | Ask, "What does JavaScript think this value is?" | Show difference between `handleClick` and `handleClick()` |
| Querying elements before DOM loads | Ask where the script tag lives | Suggest placing script at end of `<body>` or using `defer` |
| Multiple buttons toggling incorrect content | Encourage logging the dataset key being used | Use `data-*` attributes and ensure closures capture the right value |

---

## 9. Assessment & Grading Guidance

- **Formative checks**: Quick console challenges ("Predict the output") before the lab.
- **Lab rubric** (aligns with student handout): semantics, styling, interactivity, reflection.
- **Feedback cadence**: Respond to pens within 48 hours; use targeted comments like "Great use of `classList.toggle`—consider adding a focus outline.".
- **Gradebook note**: Tag submissions as "Week5_JS_Lab" to simplify sorting.

---

## 10. Extensions & Advanced Topics

- **Performance peek**: Use `performance.now()` around a loop to illustrate measurement.
- **Event delegation**: Refactor the solution to attach one listener to the parent container and rely on `event.target.matches('.feature-button')`.
- **State persistence**: Save the last-selected feature to `localStorage` and restore on load.
- **Asynchronous teaser**: Fetch a JSON snippet (pre-hosted) and hydrate the feature copy dynamically; this sets up next week's async focus.

Document which extensions you cover so future iterations can build on your adjustments.

---

## 11. Post-Class Follow-Up

- Aggregate reflection answers and surface patterns in the next session (e.g., "Most of you debugged by reading console errors first—keep that habit!").
- Capture anonymized screenshots or GIFs of standout pens to inspire upcoming cohorts.
- Note any recurring bugs to address in the README or lab instructions for next term.
- Preview the next week: asynchronous JavaScript basics, fetch requests, and connecting to APIs.

---

## 12. Slide-by-Slide Script (Week5_JS_Basics.pptx)

Use the following language as a baseline. Adapt phrasing, but ensure each bullet receives explicit coverage.

### Slide 1 – Week 5: JavaScript Foundations with CodePen
"Welcome back to CST1100. This week we dive into JavaScript—the language that brings the web to life. We'll work entirely in the browser so everyone can focus on core ideas without setup friction."

### Slide 2 – Agenda
"Today's arc moves from where JavaScript fits in the web stack, through fundamental syntax, into DOM manipulation, debugging, and lab expectations."

### Slide 3 – Why JavaScript Matters
"JavaScript runs in every modern browser. It's how we listen for clicks, validate forms, fetch data, and animate user interfaces."

### Slide 4 – JavaScript in the Browser
"Browsers bundle a rendering engine for HTML/CSS and a JavaScript engine. Our code runs line by line on a single thread, reacting to events through the event loop."

### Slide 5 – Language Building Blocks
"We'll focus on variables, primitive types, objects, arrays, conditionals, and functions—enough to structure logic and react to user input."

### Slide 6 – Declaring & Using Variables
"Use `const` for values that never get reassigned and `let` when you know the value will change. We'll avoid `var` to prevent hoisting surprises."

### Slide 7 – Functions & Scope
"Functions bundle reusable behavior. Pay attention to block scope with `let`/`const`; closures capture values for event handlers."

### Slide 8 – DOM Refresher
"The DOM is the browser's tree of our HTML. JavaScript selects nodes, reads properties, and writes new content or classes."

### Slide 9 – Event-Driven Thinking
"We listen for events—like `click`—and run functions when they fire. We'll look at handler anatomy and prevent common pitfalls."

### Slide 10 – Live Demo Roadmap
"During the demo we'll query elements, store a bit of state, and update the UI. Watch for the pattern: select → listen → update."

### Slide 11 – Debugging Toolkit
"Use `console.log` to inspect variables, but also see how DevTools breakpoints let you pause and step through code. Errors are guideposts, not failures." 

### Slide 12 – Lab Preview
"Your CodePen lab asks you to build a product spotlight with semantic HTML, custom styling, and interactive buttons that update detail text." 

### Slide 13 – Success Criteria
"We'll grade on structure, styling, interactivity, and reflection. Focus on clarity and accessibility over flashy visuals." 

### Slide 14 – Stretch Ideas
"If you finish early, try adding a dark mode toggle, persisting the last selection, or animating transitions." 

### Slide 15 – Wrap-Up & Next Steps
"Document what debugging techniques helped you today, and get ready for next week's asynchronous JavaScript and API fetches." 

Update this script with notes from your actual delivery to build a reusable teaching archive.

