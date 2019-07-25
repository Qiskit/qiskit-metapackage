How to write docs for Qiskit
============================

You can simplify docs into several categories.

* Description
* Reference
* Task

Writing and Merging PR's
------------------------

#. Fork or clone the `Qiskit/qiskit` repo to your local machine.

#. Make a new branch for your updates or edits. If you name your branch with the issue or feature
that you're working on, it is easier for reviewers to keep track of your work.

#. If you're writing a new topic, pick a template for your work: Description, reference, or task.

#. Make a pull request to the `Qiskit/master` branch and include a short description of your changes
as well as link to any issues that the PR fixes.

#. Request a review from a docs-squad member.

Formatting and Style
--------------------

`.rst` files are restructured text files that we build into docs using Sphinx.

You can see the comprehensive style syntax on the `Restructured Text (reST) and Sphinx CheatSheet
 <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_
  page. We've included the basics here as well as any need-to-know info about formatting.

Linting and Character Limits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**There is a 100 character limit per line**. If you exceed 100 characters, the build will fail and
you will need to reformat your content.

Bullets and numbering steps
^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you're writing a series of steps for a task or process, make sure to use the `#.` formatting, or
`1.`, `2.`, etc. Do not use `Step 1.`, `Step 2`, etc.

Hyperlinks
^^^^^^^^^^



Code Examples
^^^^^^^^^^^^^

You can include both `code examples
<http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html#inserting-code-and-literal-blocks>`_
using Sphinx.

The basic syntax for code is by adding `::` to the end of the line preceding the code.::

  Add :: to the end of your line::

You can also add specific language examples, such as HTML or Python with `code-block`.::

.. code-block:: html
  <h1>Header Example</h1>

Math Examples
^^^^^^^^^^^^^
You can also add `math equations <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html#maths-and-equations-with-latex>`_
by using laTex.::

.. math::
  `\alpha > \beta`

Headers
^^^^^^^

Header formatting with Sphinx is very flexible, however, we want to be consistent in our formatting.

Headers and titles are noted within Sphinx by adding a line of symbols in the following line.::

  Title
  =====

  Header 1
  --------

  Header 2
  ^^^^^^^^

  Header 3
  ''''''''


Table formatting
^^^^^^^^^^^^^^^^

There are some special considerations for tables because Sphinx supports both html and laTex.
See `Tables
<http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html#tables`_
 for more information.

You can use the following table example to start building tables.::

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+
