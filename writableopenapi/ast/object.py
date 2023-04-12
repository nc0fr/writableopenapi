# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from kind import Kind
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Object(Kind):
    """
    An object.
    """

    properties: Dict[str, Kind] = {}
    """
    The properties of this object.
    """

    required: List[str] = []
    """
    The required properties of this object.
    """

    min_properties: Optional[int] = None
    """
    The minimum number of properties in this object.
    """

    max_properties: Optional[int] = None
    """
    The maximum number of properties in this object.
    """

    additional_properties: Optional[Kind] = None
    """
    The additional properties of this object.
    """
