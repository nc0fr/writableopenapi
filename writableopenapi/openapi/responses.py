# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Union
from specification_extension import SpecificationExtension
from reference import Reference
from response import Response


@dataclass
class Responses(SpecificationExtension):
    responses: Dict[str, Union[Reference, Response]] = {}

    def dump(self) -> Dict[str, Any]:
        """Dumps the responses into a dictionary."""
        data = self.extensions
        data["responses"] = {k: v.dump() for k, v in self.responses.items()}
        return data
