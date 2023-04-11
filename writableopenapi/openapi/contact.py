# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Dict, Optional
from specification_extension import SpecificationExtension


@dataclass
class Contact(SpecificationExtension):
    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[str] = None

    def dump(self) -> Dict[str, str]:
        data = self.extensions
        if self.name is not None:
            data["name"] = self.name
        if self.url is not None:
            data["url"] = self.url
        if self.email is not None:
            data["email"] = self.email

        return data
