# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional
from specification_extension import SpecificationExtension


@dataclass
class Example(SpecificationExtension):
    summary: Optional[str] = None
    description: Optional[str] = None
    value: Optional[Any] = None
    externalValue: Optional[str] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the example into a dictionary."""
        data = self.extensions
        if self.summary is not None:
            data["summary"] = self.summary
        if self.description is not None:
            data["description"] = self.description
        if self.value is not None:
            data["value"] = self.value.__str__()
        if self.externalValue is not None:
            data["externalValue"] = self.externalValue

        return data
