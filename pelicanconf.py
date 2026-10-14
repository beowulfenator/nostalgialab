"""Pelican settings for local development.

Build locally with:  pelican -lr   (serves at http://localhost:8000 and rebuilds on change)
"""

from datetime import date

AUTHOR = "Nostalgia Lab"
SITENAME = "Nostalgia Lab"
SITEURL = ""  # empty for local dev; set in publishconf.py

PATH = "content"
TIMEZONE = "Europe/Bratislava"
DEFAULT_LANG = "sk"

# --- Landing page setup ------------------------------------------------------
# The landing page is content/pages/home.md, saved as index.html (see its
# "Save_as" metadata). Pelican's own article index is moved out of the way so
# it doesn't clash; it's there if you add a blog later.
INDEX_SAVE_AS = "blog/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Turn off blog machinery we don't need yet. Re-enable when you add posts.
ARCHIVES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- Static files -------------------------------------------------------------
# Everything in content/images is copied as-is. content/extra/CNAME ends up at
# the site root so GitHub Pages keeps the custom domain.
STATIC_PATHS = ["images", "extra/CNAME", "extra/robots.txt"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/robots.txt": {"path": "robots.txt"},
}

# --- Theme --------------------------------------------------------------------
# Hyperspace (Pixelarity), adapted. The landing page sections below the hero
# are read from content/landing.toml by plugins/landing.py.
THEME = "themes/nostalgialab"
THEME_COLOR = "blue"  # purple, blue or green
CURRENT_YEAR = date.today().year

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["landing"]
LANDING_FILE = "landing.toml"  # relative to PATH

# --- Operator details (shown in the footer) -----------------------------------
# Required on the website by § 3a of the Slovak Commercial Code (business name,
# place of business, IČO, register and entry number). DIČ, VAT status, contact
# and the supervisory authority come from the e-commerce act (22/2004 Z. z.).
# Fields left as None are not shown.
OPERATOR = {
    "name": "Kostiantyn Syrotkin",
    "address": "Agátová 3460/7F, 841 01 Bratislava-Dúbravka",
    "ico": "57 867 062",
    "dic": "3122610689",  # 10-digit DIČ from the tax office's registration certificate
    "ic_dph": None,  # e.g. "SK1234567890" if registered for VAT
    "vat_payer": False,  # True = VAT payer; False shows "Nie je platiteľ DPH"
    "register": "Živnostenskom registri Okresného úradu Bratislava, č. 110-371090",
    "email": "hello@nostalgialab.sk",  # TODO: confirm
    "phone": None,  # e.g. "+421 900 000 000"
    "authority": "Slovenská obchodná inšpekcia, Bajkalská 21/A, 827 99 Bratislava",
}

DISPLAY_PAGES_ON_MENU = True  # other pages appear in the header nav
LINKS = ()
SOCIAL = ()

RELATIVE_URLS = True
