DEPLOY ONLINE (GITHUB & READTHEDOCS)
=======================================================================
A. PUSHING TO GITHUB BRANCH
-----------------------------------------------------------------------------------------------------------
1. Check status of ignored/uncommited (untracked) files (git status)
2. Add/edit .gitignore file to include files/folders which should not be pushed to github repository::

	src/__pycache__/
	docs/build/
	virtual_environment.txt

3. Create a branch for committing files to

.. code-block:: git
	
	git checkout -b branch_name

4. Add files to github staging area

.. code-block:: git
	
	git add -A

5. Commit staged files to github

.. code-block:: git
	
	git commit -m"First commit"

6. Push commited files to online github repository

.. code-block:: git
	
	git push origin branch_name

B. SYNCING TO READTHEDOCS
-----------------------------------------------------------------------------------------------------------
1. Create an account (option to link to github account) on readthedocs.org
2. At top right of page click on drop down box next to account name and go to:
 'My Projects -> Import a Project -> Import manually'
3. Input github repository name, url, and branch and click 'Next'
4. Click 'Build version' and wait for build to complete