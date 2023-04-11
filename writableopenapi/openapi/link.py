# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional
from specification_extension import SpecificationExtension
from server import Server


@dataclass
class Link(SpecificationExtension):
    operationRef: Optional[str] = None
    operationId: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    requestBody: Optional[Any] = None
    description: Optional[str] = None
    server: Optional[Server] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the link into a dictionary."""
        data = self.extensions
        if self.operationRef is not None:
            data["operationRef"] = self.operationRef
        if self.operationId is not None:
            data["operationId"] = self.operationId
        if self.parameters is not None:
            data["parameters"] = self.parameters
        if self.requestBody is not None:
            data["requestBody"] = self.requestBody
        if self.description is not None:
            data["description"] = self.description

        return data
