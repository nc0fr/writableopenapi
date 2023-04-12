# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from kind import Kind
from dataclasses import dataclass


@dataclass
class Null(Kind):
    """
    A null.
    """

    pass
