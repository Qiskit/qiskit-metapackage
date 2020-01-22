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

# Script for pushing the localized HTML documentation to the qiskit.org.

# Non-travis variables used by this script.
SOURCE_REPOSITORY="git@github.com:Qiskit/qiskit.git"
TARGET_DOC_DIR="documentation"
SOURCE_DOC_DIR="docs/_build/html"
SOURCE_DIR=`pwd`
TRANSLATION_LANG="ja_JP"

curl https://downloads.rclone.org/rclone-current-linux-amd64.deb -o rclone.deb
sudo apt-get install -y ./rclone.deb

RCLONE_CONFIG_PATH=$(rclone config file | tail -1)

set -e

pushd $SOURCE_DIR/docs

# Make translated document
# To parallelize a bash "for" loop, "&" is added after "tox" and before "done"
# https://unix.stackexchange.com/questions/103920/parallelize-a-bash-for-loop

for i in ${TRANSLATION_LANG[@]}; do
    echo $i;
    tox -etranslateddocs -- $i &
done
wait

popd

openssl aes-256-cbc -K $encrypted_rclone_key -iv $encrypted_rclone_iv -in tools/rclone.conf.enc -out $RCLONE_CONFIG_PATH -d

echo "Pushing built docs to website"
rclone sync ./docs/_build/html/locale IBMCOS:qiskit-org-website/documentation/locale