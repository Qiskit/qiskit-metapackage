# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

.PHONY: doc autodoc clean

SITE_PACKAGES := $(shell pip show qiskit | grep Location | sed 's/Location: //')

autodoc:
ifneq ($(SITE_PACKAGES), )
	sphinx-apidoc --output doc/autodoc --separate --implicit-namespaces --module-first -d 16 \
		$(SITE_PACKAGES)/qiskit
endif

doc: autodoc
	make -C doc html

clean:
	make -C doc clean
	rm -rf doc/autodoc
