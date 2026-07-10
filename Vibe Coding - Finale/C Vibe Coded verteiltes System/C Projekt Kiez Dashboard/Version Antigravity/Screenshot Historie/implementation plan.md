mplementation Plan - Kiez-Dashboard Stage 1
Implement a responsive, modern urban dashboard ("Stitch Kiez-Dashboard") in index.html and style.css using TailwindCSS (via CDN) and the design tokens from the "Modern Urban Folk" design system.

User Review Required
IMPORTANT

The tiles initially represent styled HTML placeholders with icons and mockup data matching the four themes defined in the project description.
The sidebar settings panel features interactive switches to show/hide tiles, control dark mode, and save layout configurations to localStorage.
Proposed Changes
We will create two new files in the version directory:

index.html - The core markup, dashboard layout, and Vanilla JS logic.
style.css - Custom classes, animations, fonts, and dark mode overrides.
Dashboard Component
[NEW] 
index.html
The page will implement:

Header: Search bar for Zip code and City, Geolocation API button, Settings button, logo, and user profile image.
Sidebar: Dashboard Settings including toggles for each tile's visibility, a Dark Mode switch, and a "Save Layout" button.
Main Canvas: A 12-column grid containing:
Weather Widget (with daily and 3-day forecast details).
Relax & Wellness Tile (spas, wellness pools).
Nerd & Gaming Tile (boardgame cafes, hobby stores).
Food & Travel Tile (Thai/Vietnamese restaurant search highlights).
Tech & Work Tile (coworking hubs, laptop-friendly cafes).
Interactive JavaScript:
SortableJS integration to drag-and-drop tiles.
State management (localStorage) for tile visibility and ordering.
Active Location state: typing a PLZ/City updates the display text across all widgets.
Geolocation detection simulator.
Dark mode state toggling.
[NEW] 
style.css
Imports google fonts: Outfit (headings) and Inter (body text).
Tailored color styling using CSS custom variables matching DESIGN.md.
Customized toggle transitions, drag-and-drop ghost styles, and dotted "stitch" border dividers.
Verification Plan
Automated / Manual Verification
Verify responsiveness on mobile, tablet, and desktop viewports.
Confirm card visibility checkboxes successfully hide/show matching dashboard cards.
Check drag-and-drop functionality using SortableJS.
Toggle Dark Mode and verify colors adapt nicely according to the Stitch design specifications.
Check the location initialization updates local widget contexts.