Auto-generating the project API documentation
=================================================

#. Open the ``conf.py`` file in an editor. At the top of the file,
   assign a system path for locating the project modules directory by
   including the following line of code:
	
   .. code-block:: python

         sys.path.insert(0, os.path.abspath(<relative_path_to_source_modules>))

   .. figure:: /images/api-modules_syspath.png
		
#. Run sphinx automatic API documentation to automatically generate an .rst file
   for each module located in the ``src`` folder. This also generates a modules.rst
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

#. Update html with any changes ``make html``

   .. figure:: /images/api-modules_contents.png

   .. figure:: /images/api-modules_api.png

