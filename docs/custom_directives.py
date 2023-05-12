# This code is part of Qiskit.
#
# (C) Copyright IBM 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import re

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList


class IncludeDirective(Directive):
    """Include source file without docstring at the top of file.

    Implementation just replaces the first docstring found in file
    with '' once.

    Example usage:

    .. includenodoc:: /beginner/examples_tensor/two_layer_net_tensor.py

    """

    # defines the parameter the directive expects
    # directives.unchanged means you get the raw value from RST
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = False
    add_index = False

    docstring_pattern = r'"""(?P<docstring>(?:.|[\r\n])*?)"""\n'
    docstring_regex = re.compile(docstring_pattern)

    def run(self):
        document = self.state.document
        env = document.settings.env
        rel_filename, filename = env.relfn2path(self.arguments[0])

        try:
            text = open(filename).read()
            text_no_docstring = self.docstring_regex.sub("", text, count=1)

            code_block = nodes.literal_block(text=text_no_docstring)
            return [code_block]
        except FileNotFoundError as e:
            print(e)
            return []


class CustomCalloutItemDirective(Directive):
    option_spec = {
        "header": directives.unchanged,
        "description": directives.unchanged,
        "button_link": directives.unchanged,
        "button_text": directives.unchanged,
    }

    def run(self):
        try:
            if "description" in self.options:
                description = self.options["description"]
            else:
                description = ""

            if "header" in self.options:
                header = self.options["header"]
            else:
                raise ValueError("header not doc found")

            if "button_link" in self.options:
                button_link = self.options["button_link"]
            else:
                button_link = ""

            if "button_text" in self.options:
                button_text = self.options["button_text"]
            else:
                button_text = ""

        except FileNotFoundError as e:
            print(e)
            return []
        except ValueError as e:
            print(e)
            raise
            return []

        callout_rst = CALLOUT_TEMPLATE.format(
            description=description, header=header, button_link=button_link, button_text=button_text
        )
        callout_list = StringList(callout_rst.split("\n"))
        callout = nodes.paragraph()
        self.state.nested_parse(callout_list, self.content_offset, callout)
        return [callout]


CALLOUT_TEMPLATE = """
.. raw:: html

    <div class="col-md-6">
        <div class="text-container">
            <h3>{header}</h3>
            <p class="body-paragraph">{description}</p>
            <a class="btn with-right-arrow callout-button" href="{button_link}">{button_text}</a>
        </div>
    </div>
"""
