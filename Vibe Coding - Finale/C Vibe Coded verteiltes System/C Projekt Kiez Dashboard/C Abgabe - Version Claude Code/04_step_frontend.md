# Step 4: Frontend Module

## Task
Read `00_architecture.md` for context. Navigate into the `/frontend` directory and build the user interface.

## Requirements
1.  Create an `index.html` file.
2.  Include TailwindCSS via CDN for styling.
3.  Build a simple UI with an input field for a zip code and a "Load Dashboard" button.
4.  Create an `app.js` file.
5.  Write a function that fetches data from `http://localhost:3000/gateway/dashboard-data?zip=...` when the button is clicked.
6.  Render the returned JSON data into clean CSS-Grid cards on the screen.