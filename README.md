# nostalgialab.sk

Landing page for Nostalgia Lab, built with [Pelican](https://getpelican.com) and deployed to GitHub Pages.

## Local development

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pelican -lr        # http://localhost:8000, rebuilds on save
```

## Layout

- `content/pages/home.md` – landing page hero: title and intro text (rendered as `index.html`)
- `content/landing.toml` – the remaining landing page sections (spotlights, features, contact)
- `content/pages/*.md` – any other page; rendered with the theme's generic page layout and listed in the header nav
- `content/images/` – images, copied as-is
- `content/extra/` – `CNAME` and `robots.txt`, copied to the site root
- `themes/nostalgialab/` – the theme, adapted from Hyperspace by Pixelarity. `THEME_COLOR` in `pelicanconf.py` picks the purple, blue or green variant. `sass/` holds the original sources for reference; the compiled CSS in `static/css/` is what the site uses.
- `plugins/landing.py` – loads `landing.toml` into the templates
- `pelicanconf.py` – settings for local builds
- `publishconf.py` – production settings, used by CI
- `.github/workflows/pages.yml` – builds and deploys on every push to `main`

## Deployment

Pushing to `main` builds the site with `publishconf.py` and publishes it to GitHub Pages.
In the repo's **Settings → Pages**, the source must be set to **GitHub Actions**.
