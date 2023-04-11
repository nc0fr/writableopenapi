# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional, Union
from specification_extension import SpecificationExtension
from header import Header
from link import Link
from media_type import MediaType
from reference import Reference


@dataclass
class Response(SpecificationExtension):
    description: str = ""
    headers: Optional[Dict[str, Union[Reference, Header]]] = None
    content: Optional[Dict[str, MediaType]] = None
    links: Optional[Dict[str, Union[Reference, Link]]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the response into a dictionary."""
        data = self.extensions
        data["description"] = self.description
        if self.headers is not None:
            data["headers"] = {k: v.dump() for k, v in self.headers.items()}
        if self.content is not None:
            data["content"] = {k: v.dump() for k, v in self.content.items()}
        if self.links is not None:
            data["links"] = {k: v.dump() for k, v in self.links.items()}
        return data
