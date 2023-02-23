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

import dataclasses
from dataclasses import dataclass
from typing import Dict, List, Optional
from unittest import TestCase
from unittest.mock import Mock

from docs.custom_extensions import add_qiskit_deprecation


@dataclass(frozen=True)
class DeprecationMetadataEntry:
    """Emulates the type from Terra's deprecation.py."""

    msg: str
    since: str
    pending: bool


@dataclass(frozen=True)
class DeprecationMetadata:
    """Emulates the type from Terra's deprecation.py."""

    func_deprecation: Optional[DeprecationMetadataEntry]
    args_deprecations: Dict[str, DeprecationMetadataEntry]


class CustomExtensionsTest(TestCase):
    def test_add_qiskit_deprecation(self) -> None:
        """Test that we correctly insert the deprecation directive at the right location.

        These test cases were manually created by adding this simplified version of the extension in
        the `qiskit-ibmq-provider` repo to its `conf.py` (any Qiskit repo will do):

            def add_qiskit_deprecation(app, what, name, obj, options, lines):
                if not hasattr(obj, "__qiskit_deprecation__"):
                    return
                directive = [".. deprecated:: 1.2", "  HERE"]
                print("BEFORE")
                print(lines)
                # INSTRUCTIONS: change this line to insert where you want the directive.
                lines.extend(directive)
                print("AFTER")
                print(lines)

            def setup(app):
                app.connect('autodoc-process-docstring', add_qiskit_deprecation)

        Then, add `__qiskit_deprecation = True` to some function, and generate the docs. Ensure that
        no Sphinx warnings were created, and visually review the generated docs to make sure the
        directive is rendered properly. If valid, then use the `BEFORE` and `AFTER` to determine
        the `original` and `expected` arguments for this test. Change the docstring and/or type
        hints to generate new edge cases.
        """
        def assert_deprecation(
            *,
            metadata: Optional[DeprecationMetadata],
            original: List[str],
            expected: List[str],
        ) -> None:
            func = Mock()
            if metadata:
                func.__qiskit_deprecation__ = metadata

            add_qiskit_deprecation(
                app=Mock(),
                what="function",
                name="my_func",
                obj=func,
                options=Mock(),
                lines=original,
            )
            self.assertEqual(original, expected)

        assert_deprecation(metadata=None, original=["line 1"], expected=["line 1"])
        assert_deprecation(
            metadata=DeprecationMetadata(func_deprecation=None, args_deprecations={}),
            original=["line 1"],
            expected=["line 1"],
        )

        # Test deprecations of the function.
        entry = DeprecationMetadataEntry("Deprecated!", since="9.999", pending=False)
        metadata = DeprecationMetadata(func_deprecation=entry, args_deprecations={})
        assert_deprecation(
            metadata=metadata,
            original=[],
            expected=[".. deprecated:: 9.999", "  Deprecated!"],
        )
        assert_deprecation(
            metadata=metadata,
            original=[
                "No args/return sections.",
                "",
            ],
            expected=[
                "No args/return sections.",
                "",
                ".. deprecated:: 9.999",
                "  Deprecated!",
            ],
        )
        assert_deprecation(
            metadata=metadata,
            original=[
                "Paragraph 1, line 1.",
                "Line 2.",
                "",
                "Paragraph 2.",
                "",
                "",
            ],
            expected=[
                "Paragraph 1, line 1.",
                "Line 2.",
                "",
                "Paragraph 2.",
                "",
                "",
                ".. deprecated:: 9.999",
                "  Deprecated!",
            ],
        )
        assert_deprecation(
            metadata=metadata,
            original=[
                "A list.",
                "  * element 1",
                "  * element 2",
                "    continued",
                "",
            ],
            expected=[
                "A list.",
                "  * element 1",
                "  * element 2",
                "    continued",
                "",
                ".. deprecated:: 9.999",
                "  Deprecated!",
            ],
        )
        # Check that we correctly insert the directive in-between the function description
        # and metadata args. See
        # https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#info-field-lists.
        for metadata_line in [
            ":param foo:",
            ":parameter foo:",
            ":arg foo:",
            ":argument foo:",
            ":key foo:",
            ":keyword foo:",
            ":type foo:",
            ":raise ValueError:",
            ":raises ValueError:",
            ":except ValueError:",
            ":exception ValueError:",
            ":return: blah",
            ":returns: blah",
            ":rtype: blah",
        ]:
            assert_deprecation(
                metadata=metadata,
                original=["", metadata_line],
                expected=[".. deprecated:: 9.999", "  Deprecated!", "", metadata_line],
            )
            assert_deprecation(
                metadata=metadata,
                # For some metadata configurations, like only having the return type, we can expect
                # two blank lines between the docstring and metadata.
                original=[
                    "Docstring.",
                    "",
                    "",
                    metadata_line,
                ],
                expected=[
                    "Docstring.",
                    "",
                    ".. deprecated:: 9.999",
                    "  Deprecated!",
                    "",
                    metadata_line,
                ],
            )
            assert_deprecation(
                metadata=metadata,
                # For some metadata configurations, like only having the param type, there will
                # only be one blank line between the docstring and metadata.
                original=[
                    "Docstring.",
                    "",
                    metadata_line,
                    "",
                ],
                expected=[
                    "Docstring.",
                    "",
                    ".. deprecated:: 9.999",
                    "  Deprecated!",
                    "",
                    metadata_line,
                    "",
                ],
            )

        # Test deprecated arguments.
        metadata = DeprecationMetadata(func_deprecation=None, args_deprecations={"my_arg": entry})

        # Test both a deprecated function and arguments.
        pass

        # Pending should add `_pending` to the version string.
        pending_entry = dataclasses.replace(entry, pending=True)
        assert_deprecation(
            # TODO: add args
            metadata=DeprecationMetadata(func_deprecation=pending_entry, args_deprecations={}),
            original=[],
            expected=[".. deprecated:: 9.999_pending", "  Deprecated!"]
        )
