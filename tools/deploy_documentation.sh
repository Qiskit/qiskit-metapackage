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
set -e

curl https://downloads.rclone.org/rclone-current-linux-amd64.deb -o rclone.deb
sudo apt-get install -y ./rclone.deb

RCLONE_CONFIG_PATH=$(rclone config file | tail -1)

# Build the documentation.
tox -edocs -- -j auto

echo "show current dir: "
pwd

# Push to qiskit.org website
openssl aes-256-cbc -K $encrypted_rclone_key -iv $encrypted_rclone_iv -in tools/rclone.conf.enc -out $RCLONE_CONFIG_PATH -d
echo "Pushing built docs to website"
rclone sync --progress --exclude-from ./tools/other-builds.txt ./docs/_build/html IBMCOS:qiskit-org-web-resources/documentation
