Auto-generating the project API documentation
=================================================

#. Assign system path for locating project module directory
	
   .. code-block:: python

         sys.path.insert(0, os.path.abspath(<relative_path_to_source_modules>))

		
#. Run sphinx apidoc from docs folder

   Run sphinx automatic API documentation to generate .rst files for each module
   located in src folder. This generates a modules.rst file containing list of all
   modules to include. ``-f`` forces override of any previously written .rst files
   with the same name.

   .. code-block:: python
         
         sphinx-apidoc -f -o source <relative_path_to_source_modules>

#. Add reference to modules.rst file to the toctree in index.rst:

   .. code-block:: rst
      
      .. toctree::
	   :maxdepth: 5
	   :caption: Contents:
	   
	   modules

#. Edit titles of .rst files at top of page under headings separator 
   ``=====`` to desired output display in toctree

#. Add/Edit features of .rst file .. automodule:: directives. These can also
   be adjusted in conf.py file to set values for all .rst files:

   #. Recursively generate documentation for all members of target module
      
      .. code-block:: rst
            
            .. automodule::
                  :members:

   #. Generate documentation for members not having docstrings

      .. code-block:: rst
            
            .. automodule::
                  :undoc-members:

   #. Generate documentation for all members inherited from base classes
	
      .. code-block:: rst
            
            .. automodule::
                  :show-inheritance:

   #. Generate documentation for __special__ members 
   
      .. code-block:: rst
            
            .. automodule::
                  :special-members: __init__, __name__

#. Update html with any changes ``make html``