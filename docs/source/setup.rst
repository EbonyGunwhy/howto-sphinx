Project environment and setup
==============================

Environment and dependencies
------------------------------

A working Python environment is required to generate ``Sphinx`` documentation.
In this guide, ``conda`` virtual environments are used to manage the project
dependencies in isolation. The ``conda`` package manager may be downloaded
directly from `Anaconda's webpage <https://www.anaconda.com/download/>`_.
Feel free to create virtual environments using other tools, however please
remember to adjust the following anaconda-specific commands as necessary.

.. note::
	
	The following steps assume that commands are run from a Windows OS. If
	replicating from a different OS, please adapt commands to the appropriate 
	related invocation (`Some examples here <https://kinsta.com/blog/python-commands/>`_).

Installation
--------------


#. Open Git Bash in an interface of your choice and navigate to an empty project
   directory by inputting the following command:

   .. code-block:: rst

         cd <path_to_project_name>

#. Clone the target project from github

   .. code-block:: rst

         git clone -b <branch_name> https://github.com/<account_name>/<project_name>.git .

   Alternatively, download the whole archive locally as a zip file.
   `More details on cloning a repository here <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>`_.

#. From the project root directory, run the following command to create a separate virtual environment:

   .. code-block:: rst
         
         conda create --name <project_name> python=<version_of_choice>

   In these examples, Python v.3.7 was installed.

#. Activate the virtual environment

   .. code-block:: rst
			
         conda activate <project_name>

#. Create a ``requirements.txt`` file listing all the required packages to install, e.g.::
		
         pandas
         numpy
         statistics
         matplotlib
         scipy
         wezel
         sphinx

   .. figure:: /images/setup_requirements.png

#. Install the required packages

   .. code-block:: rst

         pip install -r requirements.txt
