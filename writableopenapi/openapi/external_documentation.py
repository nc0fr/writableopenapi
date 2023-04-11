# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Dict, Optional
from specification_extension import SpecificationExtension


@dataclass
class ExternalDocumentation(SpecificationExtension):
    description: Optional[str] = None
    url: str = ""

    def dump(self) -> Dict[str, str]:
        data = self.extensions
        if self.description is not None:
            data["description"] = self.description
        data["url"] = self.url

        return data
