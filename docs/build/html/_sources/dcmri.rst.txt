QUICK OVERVIEW OF 'HOW-TO' STEPS:
============================================================================================================
COMMIT #1 "Initial Sphinx documentation build"
- Run basic build without modifying index.rst/conf.py files (sphinx-quickstart, make html)
- Check sphinx build
- Push to Github
- Sync with RTDs
- Check RTDS build
COMMIT #2. "Sphinx docs customisation via conf.py file"
- Assign system path ('../../src')
- Add sphinx_rtd_theme to requirements.txt file & pip install again
- Add extensions (autodoc, autosummary, napoleon, viewcode, intersphinx, sphinx_rtd_theme)
- Configure extensions (intersphinx_mapping, autosummary_generate)
- Run sphinx apidoc from docs folder (sphinx-apidoc -f -o source ../src)
- Re-build html pages (make html)
- Check sphinx build
- Push to Github
- Sync with RTDs
- Check RTDs build
COMMIT #3. "Add contents for module API documentation"
- Add API doc modules to table of contents tree (toctree)
- Change title 'src' to 'API documentation' in modules.rst
- Re-build html pages (make html)
- Check sphinx build
- Push to Github
- Sync with RTDs
- Check RTDs build
COMMIT #4. "Link to README in sphinx docs & add parser for markdown (.md) files"
- Add myst-parser to requirements.txt file & pip install again
- Add myst_parser extension to conf.py file
- Create readme.rst file linking to README.md in dbdicom parent folder
- Enable .md suffix in conf.py file
- Re-build html pages (make html)
- Check sphinx build
- Push to Github
- Sync with RTDs
- Check RTDs build
COMMIT #5."Customisation"
- Welcome page:
	- Insert text about dbdicom
	- Add warning box for 'work in progress'
	- Add Sheffield logo to sidebar
- conf.py:
	- update intersphinx mappings (matplotlib, nilabel, pandas, pydicom)
	- update extensions (pip install sphinx-copybutton, sphinx-remove-toctrees; extension = sphinx_copybutton, sphinx_remove_toctrees)