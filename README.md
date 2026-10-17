# Eve's Portfolio

A responsive, single-page portfolio made with HTML, CSS, JavaScript, and a small Flask app. The supplied `Evee.png` is served from the project root as the profile image.

## Run locally

1. Create and activate a virtual environment.
2. Install the dependency with `pip install -r requirements.txt`.
3. Start the site with `python app.py`.
4. Open `http://127.0.0.1:5000`.

## Host on GitHub Pages

This project is ready to publish as a static GitHub Pages site.

1. Push the repository to GitHub.
2. In the repository settings, open Pages.
3. Set the source to GitHub Actions.
4. The workflow in `.github/workflows/pages.yml` will deploy the site automatically when changes are pushed to `main`.

The website root includes a static `index.html`, `static/`, and `Evee.png`, which GitHub Pages can serve directly.

The contact action opens a pre-addressed email in the visitor's mail app; it does not store or send messages through a server. Update the text in `index.html` or `templates/index.html` as Eve's details change.
