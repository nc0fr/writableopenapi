# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from specification_extension import SpecificationExtension


@dataclass
class ServerVariable(SpecificationExtension):
    enum: Optional[List[str]] = None
    default: str = ""
    description: Optional[str] = None

    def dump(self) -> Dict[str, Any]:
        data = self.extensions
        if self.enum is not None:
            data["enum"] = self.enum
        data["default"] = self.default
        if self.description is not None:
            data["description"] = self.description

        return data
