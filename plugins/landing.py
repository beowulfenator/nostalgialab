"""Feeds content/landing.toml to the templates as LANDING, and adds a
`markdown` Jinja filter for rendering its text fields.

Runs on every generator init, so `pelican -lr` picks up edits to the TOML
file without a restart.
"""

import tomllib
from pathlib import Path

from markdown import Markdown
from pelican import signals


def setup(generator):
    settings = generator.settings
    path = Path(settings["PATH"]) / settings.get("LANDING_FILE", "landing.toml")
    with path.open("rb") as f:
        generator.context["LANDING"] = tomllib.load(f)

    md_settings = settings.get("MARKDOWN", {})
    generator.env.filters["markdown"] = lambda text: Markdown(**md_settings).convert(text or "")


def register():
    signals.generator_init.connect(setup)
