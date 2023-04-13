# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional

from external_documentation import ExternalDocumentation
from specification_extension import SpecificationExtension


@dataclass
class Tag(SpecificationExtension):
    name: str = ""
    description: Optional[str] = None
    external_docs: Optional[ExternalDocumentation] = None

    def dump(self) -> Dict[str, Any]:
        data = self.extensions
        data["name"] = self.name
        if self.description is not None:
            data["description"] = self.description
        if self.external_docs is not None:
            data["externalDocs"] = self.external_docs.dump()

        return data
