# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Dict, Optional

from contact import Contact
from license import License
from specification_extension import SpecificationExtension


@dataclass
class Info(SpecificationExtension):
    title: str = ""
    description: Optional[str] = None
    terms_of_service: Optional[str] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
    version: str = ""

    def dump(self) -> Dict[str, str]:
        data = self.extensions
        data["title"] = self.title
        if self.description is not None:
            data["description"] = self.description
        if self.terms_of_service is not None:
            data["termsOfService"] = self.terms_of_service
        if self.contact is not None:
            data["contact"] = self.contact.dump()
        if self.license is not None:
            data["license"] = self.license.dump()
        data["version"] = self.version

        return data
