# Week 5 Lab: JavaScript Foundations in CodePen

## Lab Overview

In this 90-minute lab you will create an interactive "Product Spotlight" page using [CodePen](https://codepen.io/). The project reinforces the JavaScript fundamentals introduced in lecture—variables, DOM selection, event handling, and state updates—while keeping tooling entirely browser-based. By the end, you will publish a polished pen demonstrating beginner-friendly JavaScript applied to a realistic web UI challenge.

## Learning Goals

By completing this lab you will be able to:

1. Structure a small web page with semantic HTML sections and accessible labeling.
2. Apply CSS variables and Flexbox utilities to define layout, spacing, and brand-inspired styling.
3. Use JavaScript to manage simple state, respond to button clicks, and update DOM content without reloading.
4. Employ the browser console to trace values, interpret errors, and verify your logic.
5. Document your process and reflect on debugging strategies in a short write-up.

## Timeline & Milestones

| Phase | Suggested Time | Goal |
| --- | --- | --- |
| Fork & Rename | 5 min | Duplicate the starter pen and adopt the class naming convention. |
| Structure & Content | 20 min | Replace placeholder markup with semantic sections and meaningful copy. |
| Style & Layout | 25 min | Introduce CSS variables, layout rules, and responsive tweaks. |
| Interactivity | 30 min | Implement button-driven interactions and verify updates via console logs. |
| Polish & Reflection | 10 min | Test keyboard/mouse behavior, finalize copy, and complete the reflection prompt. |

## Prerequisites

- Access to a CodePen account (free tier is sufficient).
- Starter pen shared by your instructor; open the link and click **Fork**.
- Familiarity with Week 5 lecture topics: variables, DOM APIs, event listeners, and debugging basics.

## Part 1 – Fork the Starter & Configure Settings

1. Open the starter pen link provided in class and sign in to CodePen.
2. Click **Fork** to create your own copy. Rename the pen using `Week5_ProductSpotlight_FirstLast`.
3. In **Settings → HTML**, ensure `<!DOCTYPE html>` is enabled and set the language attribute `lang="en"`.
4. In **Settings → JavaScript**, turn on **Auto Save** so changes persist while you work.

## Part 2 – Build Semantic Structure

1. Replace placeholder `<div>` elements with semantic tags: `<header>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>` as appropriate.
2. Write a concise hero section with a heading, supporting paragraph, and call-to-action button.
3. Create three feature cards inside a `<section>`; each card needs a title, description, and button for more details.
4. Add an `<aside>` with a heading and paragraph to display feature details that will change via JavaScript.
5. Ensure every button has clear text (no vague "Click here" labels) and add `aria-live="polite"` to the detail paragraph so screen readers announce updates.

## Part 3 – Style with CSS Tokens & Layout

1. Define at least three CSS variables (`--bg`, `--accent`, `--text`) inside `:root` and apply them throughout your styles.
2. Apply a global reset (`box-sizing`, `margin`, `padding`) to create consistent spacing.
3. Use Flexbox or CSS Grid to lay out the feature cards side by side on wide screens and stacked on small screens.
4. Configure focus states for interactive elements using `:focus-visible` to ensure keyboard accessibility.
5. Create a tablet breakpoint (around 768px) that adjusts typography and spacing for readability.

## Part 4 – Add JavaScript Interactivity

1. Use `document.querySelector` / `querySelectorAll` to capture references to the feature buttons and detail area.
2. Store copy for each feature (title and description) inside an object or array so you can look it up when a button is clicked.
3. Attach `click` event listeners to each button. When a button fires:
   - Update the detail heading and paragraph text.
   - Toggle a CSS class to highlight the active feature card.
   - Log a helpful message to the console to confirm the event fired correctly.
4. Keep track of the currently active feature using a variable so you can provide custom feedback (e.g., change button text or disable it).
5. Test in the CodePen preview and console. Fix any errors before moving on.

## Part 5 – Optional Enhancements

Choose one enhancement if time permits:

- Add a "Surprise Me" button that cycles through the features automatically.
- Include a toggle that switches to a dark mode by swapping CSS variables.
- Animate the detail panel with a CSS transition when the text updates.
- Persist the last-selected feature using `localStorage` so the page remembers the user's choice when refreshed.

Document any enhancement you attempt in your reflection.

## Reflection Prompt

Add a short paragraph (4–6 sentences) at the bottom of the HTML that answers:

- Which debugging technique helped you resolve an issue today?
- How did JavaScript, CSS, and HTML collaborate to produce the final interaction?
- If you had another hour, what improvement would you tackle next?

Wrap the reflection in a `<section>` with an `id="reflection"` and style it so it is clearly visible but secondary to the main UI.

## Submission Checklist

- [ ] Pen name follows `Week5_ProductSpotlight_FirstLast` convention.
- [ ] Semantic HTML sections and accessible labels are in place.
- [ ] CSS variables, responsive layout, and focus states are implemented.
- [ ] Buttons update the detail area dynamically without page refresh.
- [ ] Console shows clear logs without errors when interactions fire.
- [ ] Reflection section is complete and includes answers to all prompts.
- [ ] Pen is set to **Public** and link is shared in the LMS submission space.

## Deliverables

- Submit the public CodePen URL in the LMS assignment.
- Upload a PDF screenshot of your final pen (optional but recommended for quick reference).
- Include any additional notes for the instructor if you deviated from the base requirements.

## Evaluation Rubric

| Criterion | Emerging (1) | Proficient (2) | Advanced (3) |
| --- | --- | --- | --- |
| HTML Structure | Mostly generic containers, missing semantic cues | Clear use of semantic tags and accessible labels | Semantic structure plus thoughtful metadata (aria, alt, landmarks) |
| CSS Implementation | Limited styling, minimal responsive behavior | Cohesive color system, responsive layout, focus states | Adds animations, dark mode, or additional polish while maintaining clarity |
| JavaScript Interactivity | Buttons do not update content or contain errors | Buttons update content reliably and highlight the active card | Adds enhancements (surprise mode, persistence, transitions) with clean code |
| Debugging & Reflection | Reflection is incomplete or lacks insights | Reflects on debugging and collaboration between HTML/CSS/JS | Provides detailed debugging narrative and plans future improvements |

## Support & Resources

- MDN Web Docs: [JavaScript First Steps](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps)
- MDN Web Docs: [Manipulating Documents](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
- Inclusive Components: [Accessible Toggle Buttons](https://inclusive-components.design/toggle-button/)
- CodePen Help: [Working with Pens](https://blog.codepen.io/documentation/pens/)

Good luck! Focus on clarity, accessibility, and readable code. Celebrate the small wins—each DOM update you implement builds crucial intuition for larger projects.

