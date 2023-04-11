# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, fields
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
    allowEmptyValue: Optional[bool] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None
    schema: Optional[Union[Reference, Schema]] = None
    examples: Optional[Dict[str, Union[Reference, Example]]] = None
    example: Optional[Any] = None
    content: Optional[Dict[str, MediaType]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the parameter into a dictionary."""
        return {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
