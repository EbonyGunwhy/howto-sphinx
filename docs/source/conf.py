# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'howto-sphinx'
copyright = '2022, Ebony Gunwhy'
author = 'Ebony Gunwhy'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones
extensions = ['sphinx.ext.viewcode', # viewing source code
                'sphinx_rtd_theme', # ReadTheDocs theme
                'sphinx_copybutton', # copy button for code blocks
                ]

# Add any paths that contain templates here, relative to this directory
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
#html_theme = 'insegel'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css"
html_static_path = ['_static']

# The suffix(es) of source filenames.
#source_suffix = ['.rst', '.md']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'images/sheffield-logo.jpg'