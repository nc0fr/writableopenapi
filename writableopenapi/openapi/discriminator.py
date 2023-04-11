# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional
from specification_extension import SpecificationExtension


@dataclass
class Discriminator(SpecificationExtension):
    property_name: str = ""
    mapping: Optional[Dict[str, str]] = None

    def dump(self) -> Dict[str, Any]:
        data = self.extensions
        data["propertyName"] = self.property_name
        if self.mapping is not None:
            data["mapping"] = self.mapping

        return data
