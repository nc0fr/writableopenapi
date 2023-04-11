# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional
from specification_extension import SpecificationExtension


@dataclass
class OAuthFlow(SpecificationExtension):
    authorizationUrl: Optional[str] = None
    tokenUrl: Optional[str] = None
    refreshUrl: Optional[str] = None
    scopes: Dict[str, str] = {}

    def dump(self) -> Dict[str, Any]:
        """Dumps the OAuth flow into a dictionary."""
        data = self.extensions
        if self.authorizationUrl is not None:
            data["authorizationUrl"] = self.authorizationUrl
        if self.tokenUrl is not None:
            data["tokenUrl"] = self.tokenUrl
        if self.refreshUrl is not None:
            data["refreshUrl"] = self.refreshUrl
        if self.scopes is not None:
            data["scopes"] = self.scopes

        return data
