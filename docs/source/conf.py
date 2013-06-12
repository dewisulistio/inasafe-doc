# -*- coding: utf-8 -*-
#
# QGIS Workshop documentation build configuration file, created by
# sphinx-quickstart on Fri Jul  1 14:40:42 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('../..'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
              'sphinx.ext.coverage', 'sphinx.ext.viewcode',
              'sphinx.ext.pngmath']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['../templates']


# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toc tree document. Changed by Tim from index to contents so we can
# have our own front page
master_doc = 'contents'

# General information about the project.
project = u'InaSAFE Documentation Project'
copyright = u'2013, InaSAFE project'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.2'
# The full version, including alpha/beta/rc tags.
release = '1.2.0'

# The language for content auto generated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = en

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['buildout', 'build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

rst_prolog = """
.. role:: disclaimer
.. |updatedisclaimer| replace:: :disclaimer:`DISCLAIMER: This section of the documentation needs updating.`
"""

rst_epilog = """
.. |project_name| replace:: InaSAFE
.. |AIFDR| replace:: AIFDR
"""


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'sphinxdoc'
#html_theme = 'linfiniti-sphinx-theme'
#html_theme = 'basic'
#html_theme = 'sphinxdoc'
html_theme = 'inasafe-theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['../themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
html_short_title = 'InaSAFE Docs'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the /static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicon.ico'

# Add any paths that contain custom /static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin /static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}
html_sidebars = {
    'index': ['inasafe-base.html'],
    'contents': ['globaltoc.html', 'searchbox.html'],
    'general/**': ['localtoc.html', 'searchbox.html'],
    'tutorial-docs/**': ['localtoc.html', 'searchbox.html'],
    'user-docs/**': ['localtoc.html', 'searchbox.html'],
    'developer-docs/**': ['localtoc.html', 'searchbox.html'],
    'api-docs/**': ['localtoc.html', 'searchbox.html'],
    'road-map/**': ['localtoc.html', 'searchbox.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {'index': 'index.html'}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'InaSAFEUserGuide'


# show 'build with Sphinx', defaults to True
html_show_sphinx = False

# show copyright notice, defaults to True
html_show_copyright = False

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('contents',
     'InaSAFE-Documentation.tex',
     u'InaSAFE Documentation',
     u'InaSAFE Project',
     'manual')]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '../../icon.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
latex_preamble = (
    '% Added by Tim\n'
    '\\usepackage{wallpaper}\n'
    '\\LRCornerWallPaper{1}{InaSAFE_footer.png}\n')

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# -- Options for PDF output ----------------------------------------------------

# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author).
pdf_documents = [
    ('user-docs/index',
     u'InaSAFE-User-Guide',
     u'InaSAFE User Guide',
     u'InaSAFE Project'),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx', 'kerning', 'a4']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
# Enabled by Tim
pdf_compressed = True

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path=['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']
# Language to be used for hyphenation support
#pdf_language="en_EN"

# If false, no index is generated.
#pdf_use_index = True

# If false, no modindex is generated.
#pdf_use_modindex = True

# If false, no coverpage is generated.
#pdf_use_coverpage = True

locale_dirs = ['../i18n']

# create 1 po file per rst file instead of one po file per module
gettext_compact = False
