# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys

# sys.path.insert(0, os.path.abspath('.'))
import sphinx_fontawesome
# -- Project information -----------------------------------------------------

project = 'Loïc VH'
copyright = '2020, Loïc Van Hoorebeeck'
author = 'Loïc Van Hoorebeeck'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''



# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx_fontawesome',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'alabaster'

html_css_files = [
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css',
]

html_theme_options = {
#        'show_fossasia_logo': 'false',
#        'nosidebar': 'true', 
        # 'html_favicon': 'TODO',
            
}
html_show_sphinx = False

html_sidebars = {
       '**': [
                'about.html',
                'navigation.html',
       #         'globaltoc.html',
      #        'sourcelink.html',
       ],
    #   'using/windows': ['windowssidebar.html'],
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
DEFAULT_LANG = "en"

NAVIGATION_LINKS = {
        DEFAULT_LANG: (
                    ("cv.rst", "Cv"),
                ),
}


#html_sidebars = {
#            '**': [
#                                 # located at _templates/
#                                 'foo.html',
#                            ]
#            }

# Alternative navigation links. Works the same way NAVIGATION_LINKS does,
# although themes may not always support them. (translatable)
# (Bootstrap 4: right-side of navbar, Bootblog 4: right side of title)
NAVIGATION_ALT_LINKS = {
    DEFAULT_LANG: {}
}


# Name of the theme to use.
THEME = "bootstrap4"

# Primary color of your theme. This will be used to customize your theme.
# Must be a HEX value.
THEME_COLOR = '#5670d4'

# Theme configuration. Fully theme-dependent. (translatable)
# Examples below are for bootblog4.
# bootblog4 supports: featured_large featured_small featured_on_mobile
#                     featured_large_image_on_mobile featured_strip_html sidebar
# bootstrap4 supports: navbar_light (defaults to False)
THEME_CONFIG = {
    DEFAULT_LANG: {
        # Show the latest featured post in a large box, with the previewimage as its background.
        'featured_large': False,
        # Show the first (remaining) two featured posts in small boxes.
        'featured_small': False,
        # Show featured posts on mobile.
        'featured_on_mobile': True,
        # Show image in `featured_large` on mobile.
        # `featured_small` displays them only on desktop.
        'featured_large_image_on_mobile': True,
        # Strip HTML from featured post text.
        'featured_strip_html': False,
        # Contents of the sidebar, If empty, the sidebar is not displayed.
        'sidebar': ''
    }
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'loicvhdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'loicvh.tex', 'loicvh Documentation',
     'Loïc Van Hoorebeeck', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'loicvh', 'loicvh Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'loicvh', 'loicvh Documentation',
     author, 'loicvh', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------
