#!/usr/bin/env python3
from pylatexenc.latexencode import utf8tolatex

with open('../AUTHORS', 'r') as authors_file:
    authors = list([utf8tolatex(x.rstrip()) for x in authors_file])

with open('../Qiskit.bib', 'w') as fd:
    fd.write("@misc{ Qiskit,\n")
    fd.write('       author = {%s},\n' % ' and '.join(authors))
    fd.write('       title = {Qiskit: An Open-source Framework for Quantum Computing},\n')
    fd.write('       year = {2019},\n')
    fd.write('       doi = {10.5281/zenodo.2562110}\n}')
