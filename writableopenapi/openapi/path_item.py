# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

from operation import Operation
from parameter import Parameter
from reference import Reference
from server import Server
from specification_extension import SpecificationExtension


@dataclass
class PathItem(SpecificationExtension):
    summary: Optional[str] = None
    description: Optional[str] = None
    get: Optional[Operation] = None
    put: Optional[Operation] = None
    post: Optional[Operation] = None
    delete: Optional[Operation] = None
    options: Optional[Operation] = None
    head: Optional[Operation] = None
    patch: Optional[Operation] = None
    trace: Optional[Operation] = None
    servers: Optional[List[Server]] = None
    parameters: Optional[List[Union[Reference, Parameter]]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the path item into a dictionary."""
        data = self.extensions
        if self.summary is not None:
            data["summary"] = self.summary
        if self.description is not None:
            data["description"] = self.description
        if self.get is not None:
            data["get"] = self.get.dump()
        if self.put is not None:
            data["put"] = self.put.dump()
        if self.post is not None:
            data["post"] = self.post.dump()
        if self.delete is not None:
            data["delete"] = self.delete.dump()
        if self.options is not None:
            data["options"] = self.options.dump()
        if self.head is not None:
            data["head"] = self.head.dump()
        if self.patch is not None:
            data["patch"] = self.patch.dump()
        if self.trace is not None:
            data["trace"] = self.trace.dump()
        if self.servers is not None:
            data["servers"] = [server.dump() for server in self.servers]
        if self.parameters is not None:
            data["parameters"] = [
                parameter.dump() for parameter in self.parameters
            ]

        return data
