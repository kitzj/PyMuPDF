# -*- coding: utf-8 -*-
#
import re
import sys
import os
import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("."))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = "4.2.0"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = ["sphinx.ext.autodoc", "sphinx.ext.coverage", "sphinx.ext.ifconfig"]
extensions = []
# rst2pdf is not available on OpenBSD.
if hasattr(os, "uname") and os.uname()[0] != "OpenBSD":
    extensions.append("rst2pdf.pdfbuilder")

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
root_doc = "index"

# General information about the project.
project = "PyMuPDF"
thisday = datetime.date.today()
copyright = "2015-" + str(thisday.year) + ", Artifex"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
_path = os.path.abspath(f'{__file__}/../../fitz/version.i')
with open(_path) as f:
    for line in f:
        match = re.search('VersionBind = "([0-9][.][0-9]+[.][0-9]+(rc[0-9]+)?)"', line)
        if match:
            release = match.group(1)
            print(f'{__file__}: setting version from {_path}: {release}')
            break
    else:
        raise Exception(f'Failed to find `VersionBind = ...` in {_path}')

# The short X.Y version
version = release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "build"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "any"

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
keep_warnings = False

# Localization vars

gettext_uuid = True

gettext_compact = False

locale_dirs = ["locales"]



# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "furo"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "canonical_url": "",
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": None,
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.


# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/PyMuPDF.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_theme_options = {
    "light_logo": "pymupdf-sidebar-logo-dark.png",
    "dark_logo": "pymupdf-sidebar-logo-light.png",
}

# A list of CSS files. The entry must be a filename string or a tuple containing
# the filename string and the attributes dictionary. The filename must be
# relative to the html_static_path, or a full URI
html_css_files = ["custom.css"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%d. %b %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = False

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True
html_sourcelink_suffix = ".rst"
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = ""

# This is the file name suffix for HTML files (e.g. ".xhtml").
html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "PyMuPDF"


# -- Options for LaTeX output ---------------------------------------------
latex_engine = "platex"
latex_use_xindy = False
latex_elements = {
    # "fontpkg": r"\usepackage[sfdefault]{ClearSans} \usepackage[T1]{fontenc}"
}
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [("index", "PyMuPDF.tex", "PyMuPDF Documentation", "Artifex", "manual")]
# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "images/pymupdf-logo.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = True
# latex_use_xindy = True
# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = True

# -- Options for PDF output --------------------------------------------------
# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author).

pdf_documents = [("index", "PyMuPDF", "PyMuPDF Manual", "Artifex")]

# A comma-separated list of custom stylesheets. Example:
# pdf_stylesheets = ["sphinx", "bahnschrift", "a4"]

# Create a compressed PDF
pdf_compressed = True

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path=['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']

# Language to be used for hyphenation support
pdf_language = "en_US"

# If false, no index is generated.
pdf_use_index = True

# If false, no modindex is generated.
pdf_use_modindex = True

# If false, no coverpage is generated.
pdf_use_coverpage = True

pdf_break_level = 2

pdf_verbosity = 0
pdf_invariant = True
