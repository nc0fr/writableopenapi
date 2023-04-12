# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional

from server import Server
from specification_extension import SpecificationExtension


@dataclass
class Link(SpecificationExtension):
    operation_ref: Optional[str] = None
    operation_id: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    request_body: Optional[Any] = None
    description: Optional[str] = None
    server: Optional[Server] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the link into a dictionary."""
        data = self.extensions
        if self.operation_ref is not None:
            data["operationRef"] = self.operation_ref
        if self.operation_id is not None:
            data["operationId"] = self.operation_id
        if self.parameters is not None:
            data["parameters"] = self.parameters
        if self.request_body is not None:
            data["requestBody"] = self.request_body
        if self.description is not None:
            data["description"] = self.description

        return data
