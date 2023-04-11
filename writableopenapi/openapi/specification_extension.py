# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class SpecificationExtension:
    extensions: Dict[str, Any] = {}
    """Additional properties, names should be prefixed with `x-`."""

    def dump(self) -> Dict[str, Any]:
        return self.extensions
