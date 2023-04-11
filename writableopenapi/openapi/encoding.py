# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, fields
from typing import Any, Dict, Optional, Union
from specification_extension import SpecificationExtension
from header import Header
from reference import Reference


@dataclass
class Encoding(SpecificationExtension):
    contentType: Optional[str] = None
    headers: Optional[Dict[str, Union[Reference, Header]]] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the encoding into a dictionary."""
        return {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
