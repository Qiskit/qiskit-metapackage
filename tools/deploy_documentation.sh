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
SOURCE_REPOSITORY="git@github.com:Qiskit/qiskit.git"
TARGET_REPOSITORY="git@github.com:Qiskit/qiskit.org.git"
TARGET_DOC_DIR="documentation/locale/"
SOURCE_DOC_DIR="docs/_build/html/locale"
SOURCE_DIR=`pwd`
TRANSLATION_LANG=("ja" "de" "pt")

# Setup the deploy key.
# https://gist.github.com/qoomon/c57b0dc866221d91704ffef25d41adcf
set -e
openssl aes-256-cbc -K $encrypted_19594d4cf7cb_key -iv $encrypted_19594d4cf7cb_iv -in tools/github_deploy_key.enc -out github_deploy_key -d
chmod 600 github_deploy_key
eval $(ssh-agent -s)
ssh-add github_deploy_key

# Clone the sources files and po files to $SOURCE_DIR/docs_source
git clone $SOURCE_REPOSITORY docs_source
cp -r docs_source/docs/. $SOURCE_DIR/docs/

cd $SOURCE_DIR/docs

# Make translated document
# make -e SPHINXOPTS="-Dlanguage='ja'" html
for i in "${TRANSLATION_LANG[@]}"; do
   echo $i;
   sphinx-build -b html -D language=$i . _build/html/locale/$i
done

# Clone the landing page repository.
cd ..
git clone --depth 1 $TARGET_REPOSITORY tmp
cd tmp
git config user.name "Qiskit Autodeploy"
git config user.email "qiskit@qiskit.org"

# Selectively delete files from the dir, for preserving versions and languages.
for i in "${TRANSLATION_LANG[@]}"; do
    echo $i;
    git rm -rf --ignore-unmatch $TARGET_DOC_DIR/$i/*.html \
        $TARGET_DOC_DIR/$i/_* \
        $TARGET_DOC_DIR/$i/apidoc \
        $TARGET_DOC_DIR/$i/api \
        $TARGET_DOC_DIR/$i/.doctrees
    # Remove .doctrees from newly build files
    rm -rf $SOURCE_DIR/$SOURCE_DOC_DIR/$i/.doctrees
done


# Copy the new rendered files and add them to the commit.
cp -r $SOURCE_DIR/$SOURCE_DOC_DIR/* $TARGET_DOC_DIR/
git add $TARGET_DOC_DIR

# Commit and push the changes.
git commit -m "Automated translated documentation update from meta-qiskit" -m "Commit: $TRAVIS_COMMIT" -m "Travis build: https://travis-ci.com/$TRAVIS_REPO_SLUG/builds/$TRAVIS_BUILD_ID"
git push --quiet
