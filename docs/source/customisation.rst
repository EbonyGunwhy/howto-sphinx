.. _my-reference-label:

Working with restructured text files
=======================================

Bold
	
.. code-block:: rst
	
	**text**

Italics 
	
.. code-block:: rst
	
	*text*

Bullets 
	
.. code-block:: rst
	
	* text

Numbered list

Like this:

.. code-block:: rst

	1. Item 1
	2. Item 2

or like this, gives the same output:

.. code-block:: rst

	#. Item 1
	#. Item 2

Separate headings

.. code-block::

	MAIN HEADING
	===============

	Sub-heading
	--------------

	Sub-sub-heading
	++++++++++++++++

Edit/add directives (.. directive::), e.g.:

* Insert a figure

  .. code-block:: rst
		
		.. figure:: /images/sheffield-logo.jpg

* Insert an inline image, such as a button icon

  .. code-block:: rst
		
		.. |button_name| image:: /images/buttons/button_name.png

* Include table of contents

  .. code-block:: rst
		
		.. toctree::

* Add a note box

  .. code-block:: rst
		
		.. note:: This is a note box.

* Add a warning box

  .. code-block:: rst
		
		.. warning:: This is a warning box.

* Add customised text box

  .. code-block:: rst
		
		.. admonition:: Customised text box

Customise directive features on newly indented line directly underneath 
directive (:features:), e.g.:

.. code-block:: rst
	
	..toctree::
		:maxdepth: 5
	  :caption: Contents:

.. code-block:: rst
	
	.. figure:: /images/sheffield-logo.jpg
		:align: right

Display text on newly indented line underneath directive with space
separating lines, e.g.:

.. code-block:: rst
	
	.. admonition:: Customised text box
		
		This is a customised text box.

.. code-block:: rst
	
	.. figure:: /images/sheffield-logo.jpg
		:align: right
			
		University of Sheffield logo
