SETUP (PROJECT ENVIRONMENT & SPHINX)
=====================================================================

1. Open visual studio
2. Navigate to empty project directory

.. code-block:: rst
	
	cd Documents/GIT/QIB-Sheffield/project_name

3. Clone project from github 

.. code-block:: rst
	
	git clone -b branch_name https://github.com/account_name/project_name.git .

4. Create virtual environment

.. code-block:: rst
	
	conda create --name project_name python=3.7

5. Activate virtual environment

.. code-block:: rst
	
	conda activate project_name

6. Create requirements.txt file with list of required packages to install::

	numpy
	pandas
	statistics
	matplotlib
	scipy
	wezel
	sphinx

7. Install required packages

.. code-block:: rst
	
	pip install -r requirements.txt

8. Create documentation folder

.. code-block:: rst
	
	mkdir docs

9. Navigate to documentation folder

.. code-block:: rst
	
	cd docs

10. Run Sphinx quickstart 

.. code-block:: rst
	
	sphinx-quickstart
	
Options for sphinx-quickstart::
		
 	i. Separate source and build directories (y)
 	ii. Project name (project_name)
 	iii. Author name (QIB-Sheffield)
	iv. Project release/version (1.0)
	v. Project language (en)