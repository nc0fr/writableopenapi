# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
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
        data = self.extensions
        if self.contentType is not None:
            data["contentType"] = self.contentType
        if self.headers is not None:
            data["headers"] = {k: v.dump() for k, v in self.headers.items()}
        if self.style is not None:
            data["style"] = self.style
        if self.explode is not None:
            data["explode"] = self.explode
        if self.allowReserved is not None:
            data["allowReserved"] = self.allowReserved

        return data
