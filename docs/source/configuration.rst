conf.py file
==============

After running the sphinx-quickstart command shown on the previous page,
a default conf.py file is generated and may be found within the
``docs/source/`` directory.This file contains the majority of configuration
settings needed for customising how the Sphinx documentation is built. Some
common options for customising this file are shown below.

Choosing a theme
------------------

Choose a theme for your documentation. A number of `pre-existing themes are
provided by Sphinx <https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes>`_:

.. code-block:: python
      
      html_theme = 'classic'


Extensions
------------

Add extensions for Sphinx autodocumentation generation with ``autodoc``
and parsing of NumPy and Google style docstrings with ``napoleon``:

.. code-block:: python
      
      extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

Or for including a button to allow users to directly view the raw code
within the documentation:

.. code-block:: python
      
      extensions = ['sphinx.ext.viewcode']

.. figure:: /images/configuration_viewcode1.png

.. figure:: /images/configuration_viewcode2.png

Another handy extension is ``intersphinx``, which generates links to documentation
for other packages (e.g., ``numpy``) used in the project.

.. code-block:: python
      
      extensions = ['sphinx.ext.intersphinx']

Extensions configuration
---------------------------

The behaviour and output of certain extensions can also be customised:

.. figure:: /images/configuration_intersphinx.png

After all edits have been made to the ``conf.py`` file, save the file
and then re-build the html pages using the ``make html`` command.