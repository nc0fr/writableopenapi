# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from components import Components
from external_documentation import ExternalDocumentation
from info import Info
from path_item import PathItem
from security_requirement import SecurityRequirement
from server import Server
from specification_extension import SpecificationExtension
from tag import Tag


@dataclass
class OpenAPI(SpecificationExtension):
    openapi: str = "3.0.0"
    info: Info = Info()
    servers: Optional[List[Server]] = None
    paths: Dict[str, PathItem] = {}
    components: Optional[Components] = None
    security: Optional[List[SecurityRequirement]] = None
    tags: Optional[List[Tag]] = None
    external_docs: Optional[ExternalDocumentation] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the OpenAPI specification into a dictionary."""
        data = self.extensions
        data["openapi"] = self.openapi
        data["info"] = self.info.dump()
        if self.servers is not None:
            data["servers"] = [server.dump() for server in self.servers]
        data["paths"] = {
            path: path_item.dump() for path, path_item in self.paths.items()
        }
        if self.components is not None:
            data["components"] = self.components.dump()
        if self.security is not None:
            data["security"] = self.security
        if self.tags is not None:
            data["tags"] = [tag.dump() for tag in self.tags]
        if self.external_docs is not None:
            data["externalDocs"] = self.external_docs.dump()

        return data
