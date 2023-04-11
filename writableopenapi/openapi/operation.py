# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, fields
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
        return {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
