BUILD (SPHINX HTML pages)
==================================================================================

1. Run sphinx html build to generate html pages for project documentation

.. code-block:: rst
	
	make html

2. Run sphinx automatic API documentation to generate .rst files for each module located in src folder. This generates a modules.rst file containing list of all modules to include.
-f forces override of any previously written .rst files with same name

.. code-block:: rst
	
	sphinx-apidoc -f -o source ../src
	
3. Add reference to modules.rst file to the toctree in index.rst:

.. code-block:: rst

   	.. toctree::
	   :maxdepth: 5
	   :caption: Contents:
	   
	   modules

4. Edit titles of .rst files at top of page under headings separator (===) to desired output display in toctree
5. Add/Edit features of .rst file .. automodule:: directives. These can also be adjusted in conf.py file to set values for all .rst files:
	i. Recursively generate documentation for all members of target module

	.. code-block:: rst
		
		.. automodule::
			:members:

	ii. Generate documentation for members not having docstrings

	.. code-block:: rst
		
		.. automodule::
			:undoc-members:

	iii. Generate documentation for all members inherited from base classes
	
	.. code-block:: rst
		
		.. automodule::
			:show-inheritance:

	iv. Generate documentation for __special__ members 
	
	.. code-block:: rst
		
		.. automodule::
			:special-members: __init__, __name__

6. Update html with any changes (make html)