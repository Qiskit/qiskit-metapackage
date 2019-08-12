How to write docs for Qiskit
============================

You can simplify docs into several categories.

* **Concept**: Explanations of the software architecture and potential use cases.
* **Task**: "How-to" that explains the steps to complete a procedure, like installing Qiskit.
* **Reference**: Detailed description or definition, such as the default values for a function.

Depending on what you're documenting, you can have a file that combines a *Description* section
with a *Task*, a *Task* with *Reference* material, or files that only contain the steps to complete
 a *Task*.

Writing and Merging PR's
------------------------

  #. Fork or clone the `Qiskit/qiskit` repo to your local machine.

  #. Make a new branch for your updates or edits.

  #. If you're writing a new topic, pick a template for your work: Description, reference, or task.

  #. Make a pull request to the `Qiskit/master` branch and link to any issues that the PR fixes.

  #. Request a review from a docs-squad member.

Formatting and Style
--------------------

`.rst` files are restructured text files that we build into docs using Sphinx.

You can see the comprehensive style syntax on the
`Restructured Text (reST) and Sphinx CheatSheet
<http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`__
page. We've included the basics here as well as any need-to-know info about formatting.

Linting and Character Limits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**There is a 100 character limit per line**. If you exceed 100 characters, the build will fail and
you will need to reformat your content.

Bullets and numbering steps
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can format bullets and numbered lists with `*`, numbers, or `#.` ::

  * This is a bulleted list.
  * It has two items, the second
    item uses two lines. (note the indentation)

  1. This is a numbered list.
  2. It has two items too.

  #. This is a numbered list.
  #. It has two items too.


If you're writing a series of steps for a task or process, make sure to use the `#.` formatting, or
`1.`, `2.`, etc. Do not use `Step 1.`, `Step 2`, etc, because it can make translation and
automating some content management activities more difficult.

Hyperlinks
^^^^^^^^^^

To create links to internal or external resources, use the external hyperlink formatting::

 `Website Title or section name <URL of resource`_

Images and figures
^^^^^^^^^^^^^^^^^^

When you add images and figures to Qiskit, you can specify the height/width in pixels, otherwise
it will default to the size of the file.::

  .. image:: ../images/file_name.png
      :width: 200px
      :align: center
      :height: 100px
      :alt: Image description

Accessibility
'''''''''''''

Qiskit is an inclusive community, and we want to make sure that everyone can use the documentation.
Alt-text, captions, and figure descriptions are necessary for people who use screen readers and
anyone with lower bandwidth internet speeds.

Please make sure that you caption any tables or figures and use the alt-text tags when you add
images or visualizations to the Qiskit docs.

Code Examples
^^^^^^^^^^^^^

You can include both `code examples
<http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html#inserting-code-and-literal-blocks>`__
using Sphinx.

The basic syntax for code is by adding `::` to the end of the line preceding the code.::

  Add :: to the end of your line::

You can also add specific language examples, such as HTML or Python with `code-block`.::

  .. code-block:: html

     <h1>code block example</h1>

Math Examples
^^^^^^^^^^^^^
You can also add `math equations <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html#maths-and-equations-with-latex>`__
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
See `Tables <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html#tables>`__ for more information.

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
