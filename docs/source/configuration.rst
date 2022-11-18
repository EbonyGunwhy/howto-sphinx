conf.py file
==============

After running the sphinx-quickstart command shown on the previous page,
a default conf.py file is generated and may be found within the
``docs/source/`` directory.This file contains the majority of configuration
settings needed for customising how the Sphinx documentation is built. Some
common options for customising this file are shown below.

Choosing a theme
------------------

Set theme to ReadTheDocs style:

.. code-block:: python
      
      html_theme = 'sphinx_rtd_theme'


Extensions
------------

Add extensions for Sphinx autodocumentation generation with ``autodoc``
and parsing of NumPy and Google style docstrings with ``napoleon``:

.. code-block:: python
      
      extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

Or for viewing code:

.. code-block:: python
      
      extensions = ['sphinx.ext.viewcode']

Configure extension settings:

e.g., ``intersphinx_mapping``, ``autosummary_generate``

After all edits have been made to the ``conf.py`` file, save the file
and then re-build the html pages using the ``make html`` command.