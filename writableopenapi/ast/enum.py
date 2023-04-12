# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from kind import Kind
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Enum(Kind):
    """
    An enumeration.
    """

    values: List[Kind] = []
    """
    The values of this enumeration.
    """

    default: Optional[Kind] = None
    """
    The default value of this enumeration.
    """
