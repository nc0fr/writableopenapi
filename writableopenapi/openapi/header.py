# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, fields
from typing import Any, Dict, Optional
from specification_extension import SpecificationExtension
from schema import Schema
from example import Example
from media_type import MediaType


@dataclass
class Header(SpecificationExtension):
    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    allowEmptyValue: Optional[bool] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None
    schema: Optional[Schema] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, Example]] = None
    content: Optional[Dict[str, MediaType]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the header into a dictionary."""
        return {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
