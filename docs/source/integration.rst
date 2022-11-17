Continuous integration with GitHub
=====================================

#. Create folder path from top-level of repo: ``.github/workflows``

#. Navigate to 'workflows' and create a ``.yaml`` file

#. name the action.yaml file in first line of script, e.g.,

   .. code-block:: yaml

      name: Docs

#. (optional) Input a 'run-name', i.e., text describing the action that was performed, e.g.,

	run-name: ${{ github.actor }} has pushed changes which update the Docs

#. Define mode of action trigger, e.g.,

	on: [push, pull_request, workflow_dispatch]

#. Define a list of jobs to perform, e.g.,

	jobs:
	  docs:

#. Specify the OS which the job should run on, e.g.,

	runs-on: ubuntu-latest

#. Outline the steps of the job, e.g.,

	steps:

#. Name the step, e.g.,

	  - name: Install Python 3.7

#. Assign an action to perfom at step, e.g.,

	    uses: actions/setup-python@v4

#. (optional) Provide any additional arguments for the action, e.g.,
	    
	    with:
		python-version: '3.7'

#. Repeat steps 9-11 for each action step required

#. Add optional command line arguments inbetween or in tandem with action steps, e.g.,

	- run: echo "Beginning action"
	- name: Install Python 3.7
	  uses: actions/setup-python@v4
	  with:
		python-version: '3.7'
	  run:  my_python_script.py
