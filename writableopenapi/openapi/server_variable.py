# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, fields
from typing import Any, Dict, List, Optional
from specification_extension import SpecificationExtension


@dataclass
class ServerVariable(SpecificationExtension):
    enum: Optional[List[str]] = None
    default: str = ""
    description: Optional[str] = None

    def dump(self) -> Dict[str, Any]:
        return {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
