# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

.PHONY: doc autodoc autodoc_qiskit autodoc_aqua autodoc_chemistry clean

# Define the paths where the different packages are placed. If present in an
# environment variable with the same name (ie. "PATH_QISKIT=/a/b/c make doc"),
# the environment variable value will take precedence.
PATH_QISKIT ?= $(shell pip show qiskit-terra | grep Location | sed 's/Location: //')
PATH_AQUA ?= $(shell pip show qiskit-aqua | grep Location | sed 's/Location: //')
PATH_CHEMISTRY ?= $(shell pip show qiskit-chemistry | grep Location | sed 's/Location: //')

autodoc_qiskit:
ifneq ($(PATH_QISKIT), )
	sphinx-apidoc --output docs/autodoc --separate --implicit-namespaces --module-first -d 16 \
		$(PATH_QISKIT)/qiskit
endif

autodoc_aqua:
ifneq ($(PATH_AQUA), )
	sphinx-apidoc --output docs/autodoc --separate --implicit-namespaces --module-first -d 16 \
		$(PATH_QISKIT)/qiskit_aqua
endif

autodoc_chemistry:
ifneq ($(PATH_CHEMISTRY), )
	sphinx-apidoc --output docs/autodoc --separate --implicit-namespaces --module-first -d 16 \
		$(PATH_CHEMISTRY)/qiskit_chemistry
endif

autodoc: autodoc_qiskit autodoc_aqua autodoc_chemistry
ifneq ($(PATH_TERRA) $(PATH_AQUA) $(PATH_CHEMISTRY), )
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
