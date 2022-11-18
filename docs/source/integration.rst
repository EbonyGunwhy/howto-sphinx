Continuous integration with GitHub
=====================================

.. caution::

  This page is currently undergoing development.

#. Create folder path from top-level of repo: ``.github/workflows``

#. Navigate to ``workflows`` and create a ``.yaml`` file

#. name the action.yaml file in first line of script, e.g.,

   .. code-block:: yaml
		
         name: Docs

#. (optional) Input a 'run-name', i.e., text describing the action that was performed, e.g.,

   .. code-block:: yaml
		
         run-name: ${{ github.actor }} has pushed changes which update the Docs

#. Define mode of action trigger, e.g.,

   .. code-block:: yaml
		
         on: [push, pull_request, workflow_dispatch]

#. Define a list of jobs to perform, e.g.,

   .. code-block:: yaml
		
         jobs:
				  docs:

#. Specify the OS which the job should run on, e.g.,

   .. code-block:: yaml
		
         runs-on: ubuntu-latest

#. Outline the steps of the job, e.g.,

   .. code-block:: yml

         steps:

#. Name the step, e.g.,

   .. code-block:: yaml

         - name: Install Python 3.7

#. Assign an action to perfom at step, e.g.,

   .. code-block:: yaml
		
         uses: actions/setup-python@v4

#. (optional) Provide any additional arguments for the action, e.g.,

   .. code-block:: yaml
		
         with:
		        python-version: '3.7'

#. Repeat steps 9-11 for each action step required

#. Add optional command line arguments inbetween or in tandem with action steps, e.g.,

   .. code-block:: yaml
		
         - run: echo "Beginning action"
				 - name: Install Python 3.7
				 uses: actions/setup-python@v4
				 with:
				 python-version: '3.7'
				 run:  my_python_script.py
