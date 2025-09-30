# Week 4 Day 2 Lab: Building a Modern Web Page in CodePen

## Lab Overview

This 90-minute lab asks students to synthesize the "modern web" lecture by creating an interactive landing page in [CodePen](https://codepen.io/). Students will practice structuring content with semantic HTML, applying layout and visual design with CSS, and wiring interactivity with JavaScript. The lab mirrors professional front-end workflows while keeping tooling lightweight and entirely browser-based.

## Learning Targets

By the end of the lab, students should be able to:

1. Outline a web page with semantic HTML elements (header, main, section, footer).
2. Style the page using reusable CSS classes, Flexbox, and responsive adjustments.
3. Manipulate the DOM with JavaScript to handle user events and update content in real time.
4. Explain how CodePen approximates local development by bundling HTML, CSS, and JS panes.
5. Package and share work using CodePen links and GitHub Gists (optional extension).

## Prerequisites & Setup

- Confirm each student has a free CodePen account (sign up via email, GitHub, or Google).
- Share the starter pen link (create once and post in LMS/Slack): `https://codepen.io/pen?template=YOUR_STARTER_ID`.
- Starter HTML should include meaningful placeholder content blocks and comments guiding the activity.
- Provide a reference sheet (PDF or slide) that lists common HTML tags, Flexbox utilities, and DOM methods from class.

## Lab Flow & Timing

| Phase | Time | Focus | Instructor Moves |
| --- | --- | --- | --- |
| Kickoff | 10 min | Demo CodePen interface & starter pen | Showcase HTML/CSS/JS panes, describe Save/Fork, introduce output panel & console. |
| Build the Skeleton | 20 min | Semantic layout | Students replace placeholder divs with header/nav/main/section/footer. Instructor circulates to review structure. |
| Style & Layout | 25 min | Flexbox layout + design tokens | Encourage class to define CSS variables, add responsive breakpoints, and experiment with layout helpers. |
| Add Interactivity | 20 min | DOM events and state | Students implement a call-to-action button that toggles a feature panel or updates live stats via JavaScript. |
| Share & Reflect | 15 min | Presentations & feedback | Volunteers project their pens, highlight design and code decisions, classmates give "Glow/Grow" feedback, capture reflections in LMS. |

## Detailed Student Tasks

### 1. Fork the Starter Pen

- Click the shared template link and choose **Fork** to create a personal working copy.
- Rename the pen using the format `Week4D2_FirstLast_ModernWeb` for easy identification.
- In **Settings → HTML**, check the box to add `<!DOCTYPE html>` if it is missing.

### 2. Structure the Page with Semantic HTML

- Replace generic `<div>` wrappers with meaningful elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`).
- Add a hero section with a heading (`<h1>`), supporting paragraph, and primary call-to-action button.
- Create a features section with at least three cards. Each card needs a heading, description, and icon placeholder (use emoji or inline SVG).
- Include a testimonial or quote section using `<blockquote>` and `<cite>`.
- End with a footer containing contact info and a "Back to top" anchor link.

### 3. Apply CSS for Layout & Visual Hierarchy

- Define CSS variables for colors, fonts, and spacing at the top using the `:root` selector.
- Implement a global reset (`* { box-sizing: border-box; }` plus margin/padding zero) to normalize styles.
- Use Flexbox to arrange the feature cards. Aim for responsive behavior that stacks on narrow screens.
- Style the CTA button with hover/focus states. Use `:focus-visible` to ensure keyboard accessibility.
- Add media queries (recommended breakpoints: 768px and 1024px) to adjust typography and layout.

### 4. Introduce JavaScript Interactivity

- Query the CTA button via `document.querySelector` and attach a `click` event listener.
- Update the DOM when users click. Suggested interactions:
  - Toggle a class that reveals a hidden details panel.
  - Rotate through an array of feature highlights, updating text content dynamically.
  - Increment a live counter that simulates sign-ups or downloads.
- Log helpful messages to the console for debugging and ask students to verify results using the CodePen console tab.
- Bonus: Use `localStorage` to remember whether the details panel was opened and restore the state on page reload.

### 5. Reflect & Share

- Click **Save** and ensure the pen is public (default for free accounts).
- Copy the pen URL into the LMS discussion or shared spreadsheet.
- Answer the reflection prompt: *"How did CSS and JavaScript work together to change the user experience on your page?"*

## Instructor Tips

- Model incremental saves and how to roll back using CodePen's **History** (Pro feature) or manual copy/paste.
- Encourage students to scaffold JS logic with pseudo-code comments before writing functions.
- Suggest using MDN Web Docs for quick syntax checks and property explanations.
- Highlight accessibility considerations, such as `aria-expanded` when toggling visibility and contrasting color choices.
- Pair faster finishers with peers who need help, or assign an extension (below).

## Extensions & Differentiation

- **Design Challenge**: Experiment with more advanced Flexbox patterns (e.g., wrapping rows, alignment tweaks) for the testimonials section.
- **API Integration**: Fetch JSON from a public API (e.g., quote or cat facts) and render results in the DOM.
- **GitHub Gist Export**: Demonstrate how to export the pen to GitHub Gist and clone locally for continued work.
- **Dark Mode Toggle**: Add a button that switches CSS variables to a dark theme and persists preference in `localStorage`.

## Assessment Options

| Criteria | Emerging | Proficient | Advanced |
| --- | --- | --- | --- |
| HTML Semantics | Uses generic tags with some structure | Applies appropriate semantic elements | Semantic structure plus accessibility attributes (aria, alt) |
| CSS Layout | Minimal styling, limited layout control | Implements cohesive color/typography and responsive layout | Employs advanced layout (e.g., nested Flexbox), transitions, or custom components |
| JavaScript Interaction | Static page, no event handling | Functional interaction responding to user input | State management, persistence, or API integration |
| Reflection | Brief or incomplete response | Clearly describes CSS/JS collaboration | Offers insights on debugging or future improvements |

## Cleanup & Follow-Up

- Export notable student pens as PDFs or screenshots for next week's showcase.
- Encourage students to recreate the project locally with VS Code + Live Server to compare workflows.
- Post a curated list of exemplary pens and annotate what each does well (structure, design, interactivity).
- Tease the next session: connecting the front-end to Supabase or another database service introduced later in the course.
