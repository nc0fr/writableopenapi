# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, fields
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
        return {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
