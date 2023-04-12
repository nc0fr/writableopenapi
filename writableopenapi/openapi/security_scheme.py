# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional

from oauth_flows import OAuthFlows
from specification_extension import SpecificationExtension


@dataclass
class SecurityScheme(SpecificationExtension):
    type: str = ""
    description: Optional[str] = None
    name: Optional[str] = None
    in_: Optional[str] = None
    scheme: Optional[str] = None
    bearer_format: Optional[str] = None
    flows: Optional[OAuthFlows] = None
    open_id_connect_url: Optional[str] = None

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
        if self.bearer_format is not None:
            data["bearerFormat"] = self.bearer_format
        if self.flows is not None:
            data["flows"] = self.flows.dump()
        if self.open_id_connect_url is not None:
            data["openIdConnectUrl"] = self.open_id_connect_url

        return data
