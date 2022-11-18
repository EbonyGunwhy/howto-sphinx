Getting started with Sphinx
==============================

Create a documentation folder
--------------------------------

Create a new folder for storing all files related to documentation by running
the following command:

.. code-block:: rst
      
      mkdir docs

``sphinx-quickstart``
-----------------------

Sphinx comes with a handy 'quickstart' feature, which is a script that generates
default source and build directories, along with a configuration file ``conf.py``
for easily compiling the Sphinx documentation for your project.

To use this feature, navigate to inside the newly created documentation folder:

.. code-block:: rst
      
      cd docs

Now run the Sphinx quickstart command:

.. code-block:: rst
      
      sphinx-quickstart
	
A list of options for customising some of the ``sphinx-quickstart`` features
should now pop up on the screen. Please answer these options according to your
own preferences.

The first of these options asks whether seperate ``source`` and ``build`` 
directories should be created for the documentation. For ``dcmri``'s 
documentation yes was chosen:

Now input a name for your project:

Provide the project author name(s):

Provide the project release/version:

And finally, choose a language for the project language:

``Sphinx`` should now start compiling the project. Once completed
the project documentation folder ``docs`` should now look like this:


Build a basic html
---------------------

To get a feel for how Sphinx works and what the project documentation
could look like, run the following command to build a basic html:

.. code-block:: rst
      
      make html

This should create a basic and uncustomised html page which looks like
like this:

To check this, open the index.html which was created in the ``docs\build``
directory:


The following sections demonstrate how to populate this plain html with
documentation for the project.



.. toctree::
   :hidden:
   :maxdepth: 5
   :caption: Contents:

   configuration
   index-page
   api-modules
   md-readme