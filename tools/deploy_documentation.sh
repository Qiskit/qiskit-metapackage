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
SOURCE_REPOSITORY="https://github.com/Qiskit/qiskit.git"
TARGET_DOC_DIR="documentation/locale/"
SOURCE_DOC_DIR="docs/_build/html/locale"
SOURCE_DIR=`pwd`
TRANSLATION_LANG="ja de pt"

curl https://downloads.rclone.org/rclone-current-linux-amd64.deb -o rclone.deb
sudo apt-get install -y ./rclone.deb

RCLONE_CONFIG_PATH=$(rclone config file | tail -1)

set -e

# Clone the sources files and po files to $SOURCE_DIR/docs_source
git clone --depth=1 $SOURCE_REPOSITORY docs_source
cp -r docs_source/docs/. $SOURCE_DIR/docs/

pushd $SOURCE_DIR/docs

# Make translated document
sudo apt-get install parallel
parallel sphinx-build -b html -D language={} . _build/html/local/{} ::: $TRANSLATION_LANG

popd

openssl aes-256-cbc -K $encrypted_rclone_key -iv $encrypted_rclone_iv -in tools/rclone.conf.enc -out $RCLONE_CONFIG_PATH -d

echo "Pushing built docs to website"
rclone sync ./docs/_build/html/locale IBMCOS:qiskit-org-website/documentation/locale
