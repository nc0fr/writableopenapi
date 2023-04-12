# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional

from server_variable import ServerVariable
from specification_extension import SpecificationExtension


@dataclass
class Server(SpecificationExtension):
    url: str = ""
    description: Optional[str] = None
    variables: Optional[Dict[str, ServerVariable]] = None

    def dump(self) -> Dict[str, Any]:
        data = self.extensions
        data["url"] = self.url
        if self.description is not None:
            data["description"] = self.description
        if self.variables is not None:
            data["variables"] = {k: v.dump() for k, v in self.variables.items()}

        return data
