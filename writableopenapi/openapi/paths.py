# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, fields
from typing import Any, Dict
from specification_extension import SpecificationExtension
from path_item import PathItem


@dataclass
class Paths(SpecificationExtension):
    paths: Dict[str, PathItem] = {}

    def dump(self) -> Dict[str, Any]:
        """Dumps the paths into a dictionary."""
        return {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
