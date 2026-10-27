# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
# Custom website styling
from pathlib import Path

_custom_static = Path(__file__).resolve().parent / "_static"
_custom_static.mkdir(parents=True, exist_ok=True)

_custom_css = """
body {
    background: #f3f6fb;
    color: #283548;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 17px;
    line-height: 1.8;
    overflow-wrap: break-word;
}

div.body,
.wy-nav-content {
    background: #ffffff;
}

div.body,
.rst-content,
.bd-article {
    color: #283548;
    font-family: Arial, Helvetica, sans-serif;
}

h1 {
    color: #132c49;
    font-size: clamp(28px, 4vw, 40px);
    font-weight: 700;
    line-height: 1.3;
    margin-bottom: 26px;
    padding-bottom: 18px;
    border-bottom: 3px solid #1765ad;
}

h2 {
    color: #132c49;
    background: #eef5fc;
    font-size: clamp(23px, 3vw, 28px);
    line-height: 1.4;
    margin-top: 36px;
    margin-bottom: 18px;
    padding: 12px 16px;
    border-left: 4px solid #1765ad;
    border-radius: 0 8px 8px 0;
}

h3 {
    color: #193e65;
    font-size: 22px;
    line-height: 1.5;
    margin-top: 26px;
    margin-bottom: 12px;
}

p {
    margin-bottom: 20px;
    line-height: 1.85;
}

ul, ol {
    padding-left: 26px;
    margin-bottom: 24px;
}

li {
    margin-bottom: 10px;
}

li > p {
    margin-bottom: 10px;
}

a {
    color: #1765ad;
    text-underline-offset: 3px;
}

a:hover {
    color: #10487b;
}

a:focus-visible {
    outline: 3px solid #1765ad;
    outline-offset: 3px;
}

img {
    max-width: 100%;
    height: auto;
}

pre {
    overflow-x: auto;
    padding: 16px;
    background: #f5f7fa;
    border: 1px solid #dce5ef;
    border-radius: 8px;
}

@media (max-width: 767px) {
    body {
        font-size: 16px;
    }

    .wy-nav-content {
        padding: 24px 18px;
    }

    h2 {
        margin-top: 28px;
        padding: 10px 12px;
    }

    h3 {
        font-size: 20px;
    }
}
"""

(_custom_static / "custom.css").write_text(
    _custom_css, encoding="utf-8"
)

html_static_path = list(globals().get("html_static_path", []))
if "_static" not in html_static_path:
    html_static_path.append("_static")

html_css_files = list(globals().get("html_css_files", []))
if "custom.css" not in html_css_files:
    html_css_files.append("custom.css")
