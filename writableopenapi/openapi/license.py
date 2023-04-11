# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Dict, Optional
from specification_extension import SpecificationExtension


@dataclass
class License(SpecificationExtension):
    name: str = ""
    url: Optional[str] = None
    identifier: Optional[str] = None

    def dump(self) -> Dict[str, str]:
        data = self.extensions
        data["name"] = self.name
        if self.url is not None:
            data["url"] = self.url
        if self.identifier is not None:
            data["identifier"] = self.identifier

        return data
