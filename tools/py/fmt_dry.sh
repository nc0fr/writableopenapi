#!/usr/bin/env sh
# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


# Dry run of yapf (does not write to files).
# This is used in CI check for instance.

yapf -d -r -p -vv --style=google --recur writableopenapi writableopenapitests