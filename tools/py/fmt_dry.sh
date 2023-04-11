#!/usr/bin/env sh
# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


# Dry run of yapf (does not write to files).
# This is used in CI check for instance.

python -m pyink -l 80 -t py311 --safe -v --diff --color writableopenapi writableopenapitests
