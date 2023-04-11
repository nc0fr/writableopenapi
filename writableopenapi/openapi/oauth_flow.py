# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional
from specification_extension import SpecificationExtension


@dataclass
class OAuthFlow(SpecificationExtension):
    authorization_url: Optional[str] = None
    token_url: Optional[str] = None
    refresh_url: Optional[str] = None
    scopes: Dict[str, str] = {}

    def dump(self) -> Dict[str, Any]:
        """Dumps the OAuth flow into a dictionary."""
        data = self.extensions
        if self.authorization_url is not None:
            data["authorizationUrl"] = self.authorization_url
        if self.token_url is not None:
            data["tokenUrl"] = self.token_url
        if self.refresh_url is not None:
            data["refreshUrl"] = self.refresh_url
        if self.scopes is not None:
            data["scopes"] = self.scopes

        return data
