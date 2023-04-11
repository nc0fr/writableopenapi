# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional
from specification_extension import SpecificationExtension
from media_type import MediaType


@dataclass
class RequestBody(SpecificationExtension):
    description: Optional[str] = None
    content: Dict[str, MediaType] = {}
    required: Optional[bool] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the request body into a dictionary."""
        data = self.extensions
        if self.description is not None:
            data["description"] = self.description
        if self.content is not None:
            data["content"] = {k: v.dump() for k, v in self.content.items()}
        if self.required is not None:
            data["required"] = self.required

        return data
