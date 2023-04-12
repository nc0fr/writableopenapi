# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional, Union

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
from specification_extension import SpecificationExtension


@dataclass
class Components(SpecificationExtension):
    schemas: Optional[Dict[str, Union[Reference, Schema]]] = None
    responses: Optional[Dict[str, Union[Reference, Response]]] = None
    parameters: Optional[Dict[str, Union[Reference, Parameter]]] = None
    examples: Optional[Dict[str, Union[Reference, Example]]] = None
    request_bodies: Optional[Dict[str, Union[Reference, RequestBody]]] = None
    headers: Optional[Dict[str, Union[Reference, Header]]] = None
    security_schemes: Optional[
        Dict[str, Union[Reference, SecurityScheme]]
    ] = None
    links: Optional[Dict[str, Union[Reference, Link]]] = None
    callbacks: Optional[Dict[str, Union[Reference, Callback]]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the components into a dictionary."""
        data = self.extensions
        if self.schemas is not None:
            data["schemas"] = {k: v.dump() for k, v in self.schemas.items()}
        if self.responses is not None:
            data["responses"] = {k: v.dump() for k, v in self.responses.items()}
        if self.parameters is not None:
            data["parameters"] = {
                k: v.dump() for k, v in self.parameters.items()
            }
        if self.examples is not None:
            data["examples"] = {k: v.dump() for k, v in self.examples.items()}
        if self.request_bodies is not None:
            data["requestBodies"] = {
                k: v.dump() for k, v in self.request_bodies.items()
            }
        if self.headers is not None:
            data["headers"] = {k: v.dump() for k, v in self.headers.items()}
        if self.security_schemes is not None:
            data["securitySchemes"] = {
                k: v.dump() for k, v in self.security_schemes.items()
            }
        if self.links is not None:
            data["links"] = {k: v.dump() for k, v in self.links.items()}
        if self.callbacks is not None:
            data["callbacks"] = {k: v.dump() for k, v in self.callbacks.items()}

        return data
