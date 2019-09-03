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
SOURCE_LANG='en'
TRANSLATION_LANG='ja'

SOURCE_REPOSITORY="git@github.com:Qiskit/qiskit.git"
TARGET_BRANCH_PO="poBranch"
DOC_DIR_PO="docs/locale"

# Build the documentation.
make doc

echo "show current dir: "
pwd

cd docs

# Extract document's translatable messages into pot files
# https://sphinx-intl.readthedocs.io/en/master/quickstart.html
echo "Extract document's translatable messages into pot files: "
sphinx-build -b gettext -D language=$TRANSLATION_LANG . _build/gettext

# Setup / Update po files
echo "Setup / Update po files"
sphinx-intl update -p _build/gettext -l en

echo "Setup ssh keys"
pwd
set -e
# Add poBranch push key to ssh-agent
openssl enc -aes-256-cbc -d -in ../tools/github_poBranch_update_key.enc -out github_poBranch_deploy_key -K $encrypted_deploy_po_branch_key -iv $encrypted_deploy_po_branch_iv
chmod 600 github_poBranch_deploy_key
eval $(ssh-agent -s)
ssh-add github_poBranch_deploy_key

# Clone to the working repository for .po and pot files
cd ..
pwd
echo "git clone for working repo"
git clone --depth 1 $SOURCE_REPOSITORY temp --single-branch --branch $TARGET_BRANCH_PO
cd temp
git branch
git config user.name "Qiskit Autodeploy"
git config user.email "qiskit@qiskit.org"

echo "git rm -rf for the translation po files"
# git rm -rf --ignore-unmatch $DOC_DIR_2/$TRANSLATION_LANG/**/*.po # Remove old po files
git rm -rf --ignore-unmatch $DOC_DIR_PO/$SOURCE_LANG/LC_MESSAGES/*.po \
	$DOC_DIR_PO/$SOURCE_LANG/LC_MESSAGES/api \
	$DOC_DIR_PO/$SOURCE_LANG/LC_MESSAGES/apidoc \
	$DOC_DIR_PO/$SOURCE_LANG/LC_MESSAGES/_*

# Copy the new rendered files and add them to the commit.
echo "copy directory"
cp -r $SOURCE_DIR/$DOC_DIR_PO/ docs/

# git checkout translationDocs
echo "add to po files to target dir"
git add $DOC_DIR_PO

# Commit and push the changes.
git commit -m "Automated documentation update to add .po files from meta-qiskit" -m "Commit: $TRAVIS_COMMIT" -m "Travis build: https://travis-ci.com/$TRAVIS_REPO_SLUG/builds/$TRAVIS_BUILD_ID"
echo "git push"
git push --quiet origin $TARGET_BRANCH_PO
echo "********** End of pushing po to working repo! *************"
# Delete keys
ssh-add -D

# Add qiskit.org push key to ssh-agent
openssl aes-256-cbc -K $encrypted_19594d4cf7cb_key -iv $encrypted_19594d4cf7cb_iv -in ../tools/github_deploy_key.enc -out github_deploy_key -d
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
    $TARGET_DOC_DIR/apidoc \
    $TARGET_DOC_DIR/api

# Copy the new rendered files and add them to the commit.
mkdir -p $TARGET_DOC_DIR
cp -r $SOURCE_DIR/$SOURCE_DOC_DIR/* $TARGET_DOC_DIR/
git add $TARGET_DOC_DIR

# Commit and push the changes.
git commit -m "Automated documentation update from meta-qiskit" -m "Commit: $TRAVIS_COMMIT" -m "Travis build: https://travis-ci.com/$TRAVIS_REPO_SLUG/builds/$TRAVIS_BUILD_ID"
git push --quiet
