# This code is part of Qiskit.
#
# (C) Copyright IBM 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

.PHONY: doc autodoc autodoc_qiskit autodoc_aqua autodoc_chemistry clean

# Define the paths where the different packages are placed. If present in an
# environment variable with the same name (ie. "PATH_QISKIT=/a/b/c make doc"),
# the environment variable value will take precedence.
PATH_QISKIT ?= $(shell pip show qiskit-terra | grep Location | sed 's/Location: //')

autodoc_qiskit:
ifneq ($(PATH_QISKIT), )
	sphinx-apidoc --output docs/autodoc --separate --implicit-namespaces --private --module-first -d 16 \
		$(PATH_QISKIT)/qiskit
endif

autodoc: autodoc_qiskit
ifneq ($(PATH_TERRA), )
	rm -f docs/autodoc/modules.rst
endif

doc: autodoc
	make -C docs html
	rm -rf docs/_build/html/_static/font
	find docs/_build/html/_static/material-design-lite-1.3.0 -type f ! \
		\( -name 'material.blue-indigo.min.css' -o -name 'LICENSE' \) -delete

clean:
	make -C docs clean
	rm -rf docs/autodoc
