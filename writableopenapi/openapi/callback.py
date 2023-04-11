# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Union
from specification_extension import SpecificationExtension
from path_item import PathItem
from reference import Reference


@dataclass
class Callback(SpecificationExtension):
    paths: Dict[str, Union[Reference, PathItem]] = {}

    def dump(self) -> Dict[str, Any]:
        """Dumps the callback into a dictionary."""
        data = self.extensions
        data.update({k: v.dump() for k, v in self.paths.items()})

        return data
