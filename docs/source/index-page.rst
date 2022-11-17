index.rst file
===============

In addition to the ``conf.py`` file, an ``index.rst`` is also created after
running the sphinx-quickstart command and may be found within the
``docs/source/`` directory. This is file is a restructured text file and
contains everything that will be displayed on the project's index or 'welcome'
page. Edit the top of the file as desired. This text will be displayed on the
welcome page of the website. A brief guide on formatting rst files may be found
`here <>`_, and a more in-depth guide `here <>`_. 

Some more common options for customising this file are shown below.

Creating a table of contents (i.e., toctree)
----------------------------------------------
 
.. code-block:: rst
   
   .. toctree::

#. Customise directive features on new indented line directly underneath directive (:features:), e.g.:

   .. code-block:: rst

         ..toctree::
            :caption: Contents:

