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
TARGET_DOC_DIR="documentation"
SOURCE_DOC_DIR="docs/_build/html"
SOURCE_DIR=`pwd`

# Build the documentation.
make doc

# Setup the deploy key.
# https://gist.github.com/qoomon/c57b0dc866221d91704ffef25d41adcf
set -e
openssl aes-256-cbc -K $encrypted_19594d4cf7cb_key -iv $encrypted_19594d4cf7cb_iv \
     -in tools/github_deploy_key.enc -out github_deploy_key -d
chmod 600 github_deploy_key
eval $(ssh-agent -s)
ssh-add github_deploy_key

# Clone the landing page repository.
cd ..
git clone --depth 1 $TARGET_REPOSITORY tmp
cd tmp
git config user.name "Qiskit Autodeploy"
git config user.email "qiskit@qiskit.org"

# Selectively delete files from the dir, for preserving versions and languages.
git rm -rf --ignore-unmatch $TARGET_DOC_DIR/*.html \
    $TARGET_DOC_DIR/_* \
    $TARGET_DOC_DIR/aer \
    $TARGET_DOC_DIR/autodoc \
    $TARGET_DOC_DIR/aqua \
    $TARGET_DOC_DIR/terra \
    $TARGET_DOC_DIR/ignis

# Copy the new rendered files and add them to the commit.
mkdir -p $TARGET_DOC_DIR
cp -r $SOURCE_DIR/$SOURCE_DOC_DIR/* $TARGET_DOC_DIR/
git add $TARGET_DOC_DIR

# Commit and push the changes.
git commit -m "Automated documentation update from meta-qiskit" -m "Commit: $TRAVIS_COMMIT" -m "Travis build: https://travis-ci.com/$TRAVIS_REPO_SLUG/builds/$TRAVIS_BUILD_ID"
git push --quiet
