"""Pelican settings for the production build (used by GitHub Actions).

Build with:  pelican content -s publishconf.py
"""

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: E402,F403

SITEURL = "https://nostalgialab.sk"
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True
