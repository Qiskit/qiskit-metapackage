#!/bin/bash

DOC_SOURCE_PATH=$1

REPO_PATH=`mktemp -d`

git clone --depth 1 https://github.com/Qiskit/qiskit-tutorial.git $REPO_PATH

cp -r $REPO_PATH/qiskit/basics/* $DOC_SOURCE_PATH/terra/qiskit-tutorials/qiskit/basics/.
cp -r $REPO_PATH/qiskit/terra/* $DOC_SOURCE_PATH/terra/qiskit-tutorials/qiskit/terra/.

rm -rf $REPO_PATH
