# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional
from specification_extension import SpecificationExtension
from oauth_flows import OAuthFlows


@dataclass
class SecurityScheme(SpecificationExtension):
    type: str = ""
    description: Optional[str] = None
    name: Optional[str] = None
    in_: Optional[str] = None
    scheme: Optional[str] = None
    bearerFormat: Optional[str] = None
    flows: Optional[OAuthFlows] = None
    openIdConnectUrl: Optional[str] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the security scheme into a dictionary."""
        data = self.extensions
        data["type"] = self.type
        if self.description is not None:
            data["description"] = self.description
        if self.name is not None:
            data["name"] = self.name
        if self.in_ is not None:
            data["in"] = self.in_
        if self.scheme is not None:
            data["scheme"] = self.scheme
        if self.bearerFormat is not None:
            data["bearerFormat"] = self.bearerFormat
        if self.flows is not None:
            data["flows"] = self.flows.dump()
        if self.openIdConnectUrl is not None:
            data["openIdConnectUrl"] = self.openIdConnectUrl

        return data
