# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, fields
from typing import Dict, Optional
from specification_extension import SpecificationExtension


@dataclass
class License(SpecificationExtension):
    name: str = ""
    url: Optional[str] = None
    identifier: Optional[str] = None

    def dump(self) -> Dict[str, str]:
        return {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
