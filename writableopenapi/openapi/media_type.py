# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional, Union
from specification_extension import SpecificationExtension
from reference import Reference
from schema import Schema
from example import Example
from encoding import Encoding


@dataclass
class MediaType(SpecificationExtension):
    schema: Optional[Union[Reference, Schema]] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, Union[Reference, Example]]] = None
    encoding: Optional[Dict[str, Encoding]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the media type into a dictionary."""
        data = self.extensions
        if self.schema is not None:
            data["schema"] = self.schema.dump()
        if self.example is not None:
            data["example"] = self.example.__str__()
        if self.examples is not None:
            data["examples"] = {k: v.dump() for k, v in self.examples.items()}
        if self.encoding is not None:
            data["encoding"] = {k: v.dump() for k, v in self.encoding.items()}

        return data
