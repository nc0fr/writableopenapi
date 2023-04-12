# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from kind import Kind
from dataclasses import dataclass
from typing import Optional


@dataclass
class Array(Kind):
    """
    An array.
    """

    items: Kind
    """
    The items of this array.
    """

    min_items: Optional[int] = None
    """
    The minimum number of items in this array.
    """

    max_items: Optional[int] = None
    """
    The maximum number of items in this array.
    """

    unique_items: bool = False
    """
    Whether the items in this array must be unique.
    """
