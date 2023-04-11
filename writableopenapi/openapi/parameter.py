# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional, Union
from specification_extension import SpecificationExtension
from example import Example
from reference import Reference
from schema import Schema
from media_type import MediaType


@dataclass
class Parameter(SpecificationExtension):
    name: str = ""
    in_: str = ""
    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    allow_empty_value: Optional[bool] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allow_reserved: Optional[bool] = None
    schema: Optional[Union[Reference, Schema]] = None
    examples: Optional[Dict[str, Union[Reference, Example]]] = None
    example: Optional[Any] = None
    content: Optional[Dict[str, MediaType]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the parameter into a dictionary."""
        data = self.extensions
        if self.name is not None:
            data["name"] = self.name
        if self.in_ is not None:
            data["in"] = self.in_
        if self.description is not None:
            data["description"] = self.description
        if self.required is not None:
            data["required"] = self.required
        if self.deprecated is not None:
            data["deprecated"] = self.deprecated
        if self.allow_empty_value is not None:
            data["allowEmptyValue"] = self.allow_empty_value
        if self.style is not None:
            data["style"] = self.style
        if self.explode is not None:
            data["explode"] = self.explode
        if self.allow_reserved is not None:
            data["allowReserved"] = self.allow_reserved
        if self.schema is not None:
            data["schema"] = self.schema.dump()
        if self.examples is not None:
            data["examples"] = {k: v.dump() for k, v in self.examples.items()}
        if self.example is not None:
            data["example"] = str(self.example)
        if self.content is not None:
            data["content"] = {k: v.dump() for k, v in self.content.items()}

        return data
