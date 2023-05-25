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

# Script for pushing the stable documentation.
set -e

if [ $# -ne 1 ]; then
    echo "Usage: $(basename "$0") <tag>" >&2 && exit 1
fi

curl https://downloads.rclone.org/rclone-current-linux-amd64.deb -o rclone.deb
sudo apt-get install -y ./rclone.deb

RCLONE_CONFIG_PATH=$(rclone config file | tail -1)

echo "show current dir: "
pwd
CURRENT_TAG=$1
echo "Got tag $CURRENT_TAG"
IFS=. read -ra VERSION <<< "$CURRENT_TAG"
STABLE_VERSION="${VERSION[0]}.${VERSION[1]}"
echo "Building for stable version $STABLE_VERSION"

# Build the documentation.
tox -edocs -- -D docs_url_prefix=documentation/stable/"$STABLE_VERSION" -j auto

# Push to qiskit.org website
openssl aes-256-cbc -K $encrypted_rclone_key -iv $encrypted_rclone_iv -in tools/rclone.conf.enc -out $RCLONE_CONFIG_PATH -d
echo "Pushing built docs to stable site"
rclone sync --progress ./docs/_build/html IBMCOS:qiskit-org-web-resources/documentation/stable/"$STABLE_VERSION"
