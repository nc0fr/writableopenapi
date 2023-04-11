# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, fields
from typing import Any, Dict, Optional, Union
from specification_extension import SpecificationExtension
from callback import Callback
from example import Example
from header import Header
from link import Link
from parameter import Parameter
from reference import Reference
from request_body import RequestBody
from response import Response
from schema import Schema
from security_scheme import SecurityScheme


@dataclass
class Components(SpecificationExtension):
    schemas: Optional[Dict[str, Union[Reference, Schema]]] = None
    responses: Optional[Dict[str, Union[Reference, Response]]] = None
    parameters: Optional[Dict[str, Union[Reference, Parameter]]] = None
    examples: Optional[Dict[str, Union[Reference, Example]]] = None
    requestBodies: Optional[Dict[str, Union[Reference, RequestBody]]] = None
    headers: Optional[Dict[str, Union[Reference, Header]]] = None
    securitySchemes: Optional[
        Dict[str, Union[Reference, SecurityScheme]]
    ] = None
    links: Optional[Dict[str, Union[Reference, Link]]] = None
    callbacks: Optional[Dict[str, Union[Reference, Callback]]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the components into a dictionary."""
        return {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
