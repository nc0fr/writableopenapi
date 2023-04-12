# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from kind import Kind
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class OneOf(Kind):
    """
    Values that may be one of several kinds.
    """

    kinds: List[Kind] = []
    """
    The kinds that this value may be.
    """


@dataclass
class AnyOf(Kind):
    """
    Values that may be any of several kinds.
    """

    kinds: List[Kind] = []
    """
    The kinds that this value may be.
    """


@dataclass
class AllOf(Kind):
    """
    Values that must be all of several kinds.
    """

    kinds: List[Kind] = []
    """
    The kinds that this value must be.
    """


@dataclass
class Not(Kind):
    """
    Values that must not be a certain kind.
    """

    kind: Optional[Kind] = None
    """
    The kind that this value must not be.
    """
