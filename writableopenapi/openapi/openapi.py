# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, fields
from typing import Any, Dict, List, Optional
from specification_extension import SpecificationExtension
from components import Components
from external_documentation import ExternalDocumentation
from info import Info
from path_item import PathItem
from server import Server
from tag import Tag


@dataclass
class OpenAPI(SpecificationExtension):
    openapi: str = "3.0.0"
    info: Info = Info()
    servers: Optional[List[Server]] = None
    paths: Dict[str, PathItem] = {}
    components: Optional[Components] = None
    security: Optional[List[Dict[str, List[str]]]] = None
    tags: Optional[List[Tag]] = None
    externalDocs: Optional[ExternalDocumentation] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the OpenAPI specification into a dictionary."""
        return {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
