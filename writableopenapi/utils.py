# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import json
import yaml
from writableopenapi.openapi.v3_1 import OpenAPI


def into_json(api: OpenAPI) -> str:
    """Convert OpenAPI object into JSON string."""
    return json.dumps(api.dump(), indent=2, sort_keys=True)


def into_yaml(api: OpenAPI) -> str:
    """Convert OpenAPI object into YAML string."""
    return yaml.dump(api.dump(), indent=2, sort_keys=True)


def write_file(content: str, filename: str) -> None:
    """Write OpenAPI object into file."""
    with open(filename, "w") as file:
        file.write(content)
