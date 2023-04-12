# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional

from specification_extension import SpecificationExtension


@dataclass
class XML(SpecificationExtension):
    name: Optional[str] = None
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    attribute: Optional[bool] = None
    wrapped: Optional[bool] = None

    def dump(self) -> Dict[str, Any]:
        data = self.extensions
        if self.name is not None:
            data["name"] = self.name
        if self.namespace is not None:
            data["namespace"] = self.namespace
        if self.prefix is not None:
            data["prefix"] = self.prefix
        if self.attribute is not None:
            data["attribute"] = self.attribute
        if self.wrapped is not None:
            data["wrapped"] = self.wrapped

        return data
