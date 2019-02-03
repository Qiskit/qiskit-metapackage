#!/usr/bin/env python3

with open('AUTHORS', 'r') as authors_file:
    authors = list(sorted([x.strip() for x in authors_file]))

with open('Qiskit.bib', 'w') as fd:
    fd.write("@misc{ Qiskit,\n")
    fd.write('       author = {%s},\n' % ' and '.join(authors))
    fd.write('       title = {Qiskit: the Quantum Information Science Kit},\n')
    fd.write('       year = {2019},\n}\n')
