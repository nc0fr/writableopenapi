# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from specification_extension import SpecificationExtension
from callback import Callback
from external_documentation import ExternalDocumentation
from parameter import Parameter
from reference import Reference
from request_body import RequestBody
from response import Response
from server import Server


@dataclass
class Operation(SpecificationExtension):
    tags: Optional[List[str]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None
    operationId: Optional[str] = None
    parameters: Optional[List[Union[Reference, Parameter]]] = None
    requestBody: Optional[Union[Reference, RequestBody]] = None
    responses: Dict[str, Union[Reference, Response]] = {}
    callbacks: Optional[Dict[str, Union[Reference, Callback]]] = None
    deprecated: Optional[bool] = None
    security: Optional[List[Dict[str, List[str]]]] = None
    servers: Optional[List[Server]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the operation into a dictionary."""
        data = self.extensions
        if self.tags is not None:
            data["tags"] = self.tags
        if self.summary is not None:
            data["summary"] = self.summary
        if self.description is not None:
            data["description"] = self.description
        if self.externalDocs is not None:
            data["externalDocs"] = self.externalDocs.dump()
        if self.operationId is not None:
            data["operationId"] = self.operationId
        if self.parameters is not None:
            data["parameters"] = [
                parameter.dump() for parameter in self.parameters
            ]
        if self.requestBody is not None:
            data["requestBody"] = self.requestBody.dump()
        data["responses"] = {
            response: response.dump()
            for response, response in self.responses.items()
        }
        if self.callbacks is not None:
            data["callbacks"] = {
                callback: callback.dump()
                for callback, callback in self.callbacks.items()
            }
        if self.deprecated is not None:
            data["deprecated"] = self.deprecated
        if self.security is not None:
            data["security"] = self.security
        if self.servers is not None:
            data["servers"] = [server.dump() for server in self.servers]

        return data
