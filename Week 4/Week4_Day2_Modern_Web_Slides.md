% Week 4 Day 2: Modern Web Foundations
% CST1100 Intro to Computing
% Day 2 - Modern Website Development

# Session Roadmap

- Situate the web within the client-server model
- Demonstrate the browser's role and developer tooling
- Relate DOM structure to HTML semantics and CSS styling
- Show how JavaScript powers interactivity and data flow
- Map publishing paths: hosting, servers, and GitHub collaboration

# Learning Objectives

- Explain how the web delivers documents over HTTP/HTTPS
- Describe what a web browser does under the hood
- Define the Document Object Model and its relationship to HTML
- Differentiate the responsibilities of HTML, CSS, and JavaScript
- Outline options for hosting projects and tracking changes with GitHub

# What Is the Web?

- Global network of linked documents and applications delivered via the internet
- Built on open standards (HTTP/S, URLs, HTML, CSS, JavaScript)
- Client-server architecture: clients request resources from servers
- Stateless protocol: each request stands alone, so state is managed on top (cookies, local storage, back-end sessions)

# Request-Response Cycle

1. User enters URL or clicks link, browser resolves domain via DNS
2. Browser sends HTTP(S) request to the server's IP address
3. Server responds with status code, headers, and payload (HTML, JSON, images)
4. Browser parses the response, builds the DOM, applies CSS, and executes JavaScript
5. Additional requests fetch assets (stylesheets, scripts, fonts, APIs)

# Web Browsers as Runtime Environments

- Rendering engine translates HTML/CSS into pixels (Blink, WebKit, Gecko)
- JavaScript engine executes scripts (V8, SpiderMonkey, JavaScriptCore)
- Networking stack handles HTTP, caching, and security policies
- Developer tools expose DOM inspection, network timing, console, performance, and storage
- Browser differences persist: test across Chrome, Firefox, Safari, Edge

# Document Object Model (DOM)

- Tree representation of HTML nodes after the browser parses markup
- Nodes include elements, attributes, and text; hierarchy informs layout and accessibility
- DOM updates dynamically when scripts modify elements or when data is fetched
- DOM APIs (querySelector, appendChild, classList) let JavaScript read and alter content
- Semantic HTML produces predictable DOM structures for assistive technologies

# HTML: Structure & Semantics

- HyperText Markup Language defines the document skeleton
- Use semantic tags (header, nav, main, article, section, footer) for meaning
- Elements describe content types: headings, paragraphs, lists, links, media
- Attributes add metadata (alt, aria-label, data-*) to support context and accessibility
- Valid, well-nested HTML ensures consistent DOM and easier styling

# CSS: Presentation & Layout

- Cascading Style Sheets control visual design, from colors to responsive layout
- Selectors target elements via tags, classes, ids, attributes, pseudo-classes
- Cascade and specificity resolve conflicts; source order and !important affect outcomes
- Modern layout system: Flexbox handles alignment, spacing, and responsive wrapping
- Media queries adapt experiences across devices, supporting inclusive design

# JavaScript: Behavior & Data

- Adds interactivity, handles events, and manipulates the DOM in real time
- Communicates with servers via fetch/XHR for dynamic data (AJAX)
- Stores state in memory, localStorage, sessionStorage, or IndexedDB
- Frameworks (React, Vue, Svelte) abstract DOM updates but rest on core JS APIs
- Progressive enhancement keeps pages usable even if scripts fail

# Putting It Together

- HTML provides structure, CSS styles it, JavaScript layers interactions
- Browser combines the DOM and CSSOM into a render tree
- Repaints and reflows occur when layout changes; optimize to avoid jank
- Component thinking: group markup, styles, and behaviors for reuse
- Accessibility and performance start with clean markup and measured scripting

# Web Servers & Hosting

- Servers store files or applications and respond to HTTP requests
- Static hosting (GitHub Pages, Netlify, Vercel) serves pre-built HTML/CSS/JS
- Dynamic hosting (Node, Python, Ruby, PHP) generates responses per request
- Content delivery networks (CDNs) cache assets geographically for speed
- HTTPS certificates encrypt traffic; automate via Let's Encrypt or platform tooling

# Version Control & GitHub

- Git tracks changes, enabling branching, merging, and history review
- GitHub hosts repositories, issues, pull requests, and actions pipelines
- Collaborators clone, commit, push, and merge through pull requests
- Pages and Actions deploy static sites directly from the repository
- Adopt good practices: descriptive commits, README onboarding, .gitignore hygiene

# Deploying a Web Project

- Local development: edit files and preview in browser or dev server
- Version control: commit changes and push to a shared repository
- Automated build: lint, test, and bundle assets when tooling requires it
- Deployment: hosting platform pulls latest code and publishes the site
- Monitoring: track uptime, performance, and user feedback for iteration

# CodePen Lab Preview

- Use CodePen to experiment with HTML, CSS, and JavaScript side by side
- Remix starter pens to understand structure and styling relationships
- Live preview accelerates debugging and visual learning
- Share pens via links for peer review and instructor feedback
- Document takeaways in the reflection prompt

# Wrap-Up & Next Steps

- Review how browser, languages, and hosting align in the web stack
- Preview upcoming focus: connecting front-end code to APIs and databases
- Encourage students to bookmark MDN Web Docs for ongoing reference
- Assign reflection: describe one insight and one question about modern web development
