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

# Script for generating translatable files and pushing the HTML documentation to qiskit.org.

# Non-travis variables used by this script.
SOURCE_REPOSITORY="git@github.com:Qiskit/qiskit.git"
SOURCE_DOC_DIR="docs/_build/html"
SOURCE_DIR=`pwd`
SOURCE_LANG='en'

DOC_DIR_PO="docs/locale"

curl https://downloads.rclone.org/rclone-current-linux-amd64.deb -o rclone.deb
sudo apt-get install -y ./rclone.deb

RCLONE_CONFIG_PATH=$(rclone config file | tail -1)

# Build the documentation.
tox -edocs -- -D content_prefix=documentation

pushd docs

# Extract document's translatable messages into pot files and generate po files
# https://sphinx-intl.readthedocs.io/en/master/quickstart.html
tox -egettext -- -D language=$SOURCE_LANG

echo "Setup ssh keys"
set -e
# Add poBranch push key to ssh-agent
openssl enc -aes-256-cbc -d -in ../tools/github_poBranch_update_key.enc -out github_poBranch_deploy_key -K $encrypted_deploy_po_branch_key -iv $encrypted_deploy_po_branch_iv
chmod 600 github_poBranch_deploy_key
eval $(ssh-agent -s)
ssh-add github_poBranch_deploy_key

popd

git config user.name "Qiskit Autodeploy"
git config user.email "qiskit@qiskit.org"

echo "git rm -rf for the translation po files"
git rm -rf --ignore-unmatch $DOC_DIR_PO/$SOURCE_LANG/LC_MESSAGES/*.po \
	$DOC_DIR_PO/$SOURCE_LANG/LC_MESSAGES/api \
	$DOC_DIR_PO/$SOURCE_LANG/LC_MESSAGES/apidoc \
	$DOC_DIR_PO/$SOURCE_LANG/LC_MESSAGES/theme \
	$DOC_DIR_PO/$SOURCE_LANG/LC_MESSAGES/_*

# Remove api/ and apidoc/ to avoid confusion while translating
rm -rf $SOURCE_DIR/$DOC_DIR_PO/en/LC_MESSAGES/api/ \
	$SOURCE_DIR/$DOC_DIR_PO/en/LC_MESSAGES/apidoc/ \
	$SOURCE_DIR/$DOC_DIR_PO/en/LC_MESSAGES/stubs/ \
	$SOURCE_DIR/$DOC_DIR_PO/en/LC_MESSAGES/theme/

# Copy the new rendered files and add them to the commit.
echo "copy directory"
cp -r $SOURCE_DIR/$DOC_DIR_PO/ docs/

echo "add to po files to target dir"
git add $DOC_DIR_PO

# Commit and push the changes.
git commit -m "Automated documentation update to add .po files from meta-qiskit" -m "[skip travis]" -m "Commit: $TRAVIS_COMMIT" -m "Travis build: https://travis-ci.com/$TRAVIS_REPO_SLUG/builds/$TRAVIS_BUILD_ID"
echo "git push"
git push --quiet origin master
echo "********** End of pushing po to working repo! *************"


# Push to qiskit.org website
openssl aes-256-cbc -K $encrypted_rclone_key -iv $encrypted_rclone_iv -in tools/rclone.conf.enc -out $RCLONE_CONFIG_PATH -d
echo "Pushing built docs to website"
rclone sync --exclude 'locale/**' ./docs/_build/html IBMCOS:qiskit-org-website/documentation
