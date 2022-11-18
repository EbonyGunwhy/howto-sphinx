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

After updating the ``html_theme``, save the changes to the ``conf.py`` file,
run the command ``make html`` again, and open the ``build/index.html`` file
again to check the theme output. Experiment in this way with different themes
to find one for the project.

To use a theme not provided by Sphinx, for example the
`ReadTheDocs <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_ theme, the
theme first needs to be installed like a regular Python package. To do this, add
the name of the package to the ``requirements.txt`` file, navigate to the project
root directory (``cd ..``) and re-run the command:

| ``pip install -r requirements.txt``.

.. figure:: /images/conf_sphinxrtd.png

This theme is now (almost) ready to be used as a ``html_theme`` option, however
we need to add it to the list of ``extensions`` in the ``conf.py`` file, first.

Extensions
------------

Add any Sphinx extension module names here, as strings. They can be
extensions coming with Sphinx (named ``sphinx.ext.*``) external packages (such as
the ``sphinx_rtd_theme``), or custom-made ones.

Two important extensions coming from Sphinx that should be added first are:

* ``autodoc``: for Sphinx autodocumentation generation

* ``napoleon``: for parsing of NumPy and Google style docstrings:

.. code-block:: python
      
      extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

Another nice extension is ``viewcode`` which generates a button on the html
pages which allows users to directly view the raw code within the documentation:

.. code-block:: python
      
      extensions = ['sphinx.ext.viewcode']

.. figure:: /images/configuration_viewcode1.png

The user may now view the raw code by clicking on the ``[source]`` button.

.. figure:: /images/configuration_viewcode2.png

One more handy extension is ``intersphinx`` , which generates links to
documentation for other packages which already have their own documentation
(e.g., ``NumPy``) used in the project.

.. code-block:: python
      
      extensions = ['sphinx.ext.intersphinx']

`More info here <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_.

*Extensions configuration*
+++++++++++++++++++++++++++

The behaviour and output of certain extensions can also be customised. For
instance, the specific packages which ``intersphinx`` should generate
cross-references for need to specified explicitly in the ``conf.py`` file:

.. figure:: /images/configuration_intersphinx.png

Some more popular/useful extensions and their usage may be found
`here <https://sphinx-intro-tutorial.readthedocs.io/en/latest/sphinx_extensions.html>`_.

After all edits have been made to the ``conf.py`` file, save the file
and then re-build the html pages using the ``make html`` command to view the
updated html pages.
