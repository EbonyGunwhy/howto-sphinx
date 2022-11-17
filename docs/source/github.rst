Pushing to GitHub
===========================

#. Check status of ignored/uncommited (untracked) files
   
   .. code-block:: rst

         git status

#. Add/edit .gitignore file to include files/folders which should not be pushed to github repository::

         src/__pycache__/
         docs/build/
         virtual_environment.txt

#. Create a branch for committing files to

   .. code-block:: git
	
         git checkout -b <branch_name>

#. Add files to github staging area

   .. code-block:: git
	
         git add -A

#. Commit staged files to GitHub

   .. code-block:: git
	
         git commit -m"First commit"

#. Push commited files to online github repository

   .. code-block:: git
	
         git push origin <branch_name>

