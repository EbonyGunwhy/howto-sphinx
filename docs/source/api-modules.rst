Auto-generating the project API documentation
=================================================

``Sphinx`` comes with another handy tool (``sphinx-apidoc``) which can be used
to automatically generate the API documentation for all source or ``src``
modules of the project (assuming you have already been following some
`best practices <https://realpython.com/documenting-python-code/>`_ when it comes
to documenting your code).

The following steps demonstrate how to make use of this handy feature.

#. Open the ``conf.py`` file in an editor. At the top of the file,
   assign a system path for locating the project modules directory by
   including the following line of code:
	
   .. code-block:: python

         sys.path.insert(0, os.path.abspath(<relative_path_to_source_modules>))

   .. figure:: /images/api-modules_syspath.png
		
#. Run sphinx automatic API documentation to automatically generate an .rst file
   for each module located in the ``src`` folder. This also generates a ``modules.rst``
   file containing a list of all the ``src`` modules. ``-f`` forces override of any
   previously written .rst files with the same name.

   .. code-block:: python
         
         sphinx-apidoc -f -o source <relative_path_to_source_modules>

   .. figure:: /images/api-modules_modules.png

#. Open the ``modules.rst`` file and change the title to 'API documentation' or
   another title, as desired:
   
   .. figure:: /images/api-modules_moduletitle.png

   Then save the file.

#. Add a cross-reference to the ``modules.rst`` file in the toctree in
   the ``index.rst`` file:

   .. code-block:: rst
      
      .. toctree::
         :maxdepth: 5
         :caption: My contents are better than your contents:
         
         mynewsection
         modules

#. Update the html pages with any changes (``make html``):

   .. figure:: /images/api-modules_contents.png

   .. figure:: /images/api-modules_api.png

Edit the text within each .rst module by adding directives to alter
their output/behaviour. Some examples
`here <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_.
