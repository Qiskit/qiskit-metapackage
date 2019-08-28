#!/bin/bash

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# Script for pushing the documentation to the qiskit.org repository.

# Non-travis variables used by this script.
TARGET_REPOSITORY="git@github.com:Qiskit/qiskit.org.git"
TARGET_DOC_DIR="documentation/locale/"
SOURCE_DOC_DIR="docs/_build/html/locale"
SOURCE_DIR=`pwd`
TRANSLATION_LANG='ja'

# Build api .rst files
make autodoc

# Setup the deploy key.
# https://gist.github.com/qoomon/c57b0dc866221d91704ffef25d41adcf
set -e
openssl aes-256-cbc -K $encrypted_19594d4cf7cb_key -iv $encrypted_19594d4cf7cb_iv -in tools/github_deploy_key.enc -out github_deploy_key -d
chmod 600 github_deploy_key
eval $(ssh-agent -s)
ssh-add github_deploy_key

# Clone the sources files and po files to $SOURCE_DIR/docs_source
git clone $SOURCE_REPOSITORY docs_source
mkdir -p docs_source/docs/api && cp -r $SOURCE_DIR/docs/api/. docs_source/docs/api
git clone $SOURCE_REPOSITORY -b translationDocs $SOURCE_DIR/translations
mkdir -p $SOURCE_DIR/translations/docs/locale && cp -r docs_source/docs/. $SOURCE_DIR/translations/docs/locale

cd $SOURCE_DIR/translations/docs

# Make translated document
# make -e SPHINXOPTS="-Dlanguage='ja'" html
sphinx-build -b html -D language=$TRANSLATION_LANG . _build/html/locale/$TRANSLATION_LANG

# Clone the landing page repository.
cd ..
git clone --depth 1 $TARGET_REPOSITORY tmp
cd tmp
git config user.name "Qiskit Autodeploy"
git config user.email "qiskit@qiskit.org"

# Selectively delete files from the dir, for preserving versions and languages.
git rm -rf --ignore-unmatch $TARGET_DOC_DIR/TRANSLATION_LANG/*.html \
    $TARGET_DOC_DIR/TRANSLATION_LANG/_* \
    $TARGET_DOC_DIR/TRANSLATION_LANG/apidoc \
    $TARGET_DOC_DIR/TRANSLATION_LANG/api

# Copy the new rendered files and add them to the commit.

cp -r $SOURCE_DIR/$SOURCE_DOC_DIR/* $TARGET_DOC_DIR/
git add $TARGET_DOC_DIR

# Commit and push the changes.
git commit -m "Automated translated documentation update from meta-qiskit" -m "Commit: $TRAVIS_COMMIT" -m "Travis build: https://travis-ci.com/$TRAVIS_REPO_SLUG/builds/$TRAVIS_BUILD_ID"
git push --quiet
