# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, fields
from typing import Any, Dict, List, Optional, Union
from specification_extension import SpecificationExtension
from reference import Reference
from discriminator import Discriminator
from .xml import XML
from external_documentation import ExternalDocumentation


@dataclass
class Schema(SpecificationExtension):
    title: Optional[str] = None
    multipleOf: Optional[float] = None
    maximum: Optional[float] = None
    exclusiveMaximum: Optional[float] = None
    minimum: Optional[float] = None
    exclusiveMinimum: Optional[float] = None
    maxLength: Optional[int] = None
    minLength: Optional[int] = None
    pattern: Optional[str] = None
    maxItems: Optional[int] = None
    minItems: Optional[int] = None
    uniqueItems: Optional[bool] = None
    maxProperties: Optional[int] = None
    minProperties: Optional[int] = None
    required: Optional[List[str]] = None
    enum: Optional[List[Any]] = None
    type: Optional[Union[str, List[str]]] = None
    allOf: Optional[List[Union[Reference, "Schema"]]] = None
    oneOf: Optional[List[Union[Reference, "Schema"]]] = None
    anyOf: Optional[List[Union[Reference, "Schema"]]] = None
    not_: Optional[Union[Reference, "Schema"]] = None
    items: Optional[
        Union[Reference, "Schema", List[Union[Reference, "Schema"]]]
    ] = None
    properties: Optional[Dict[str, Union[Reference, "Schema"]]] = None
    additionalProperties: Optional[Union[bool, Reference, "Schema"]] = None
    description: Optional[str] = None
    format: Optional[str] = None
    default: Optional[Any] = None
    nullable: Optional[bool] = None
    discriminator: Optional[Discriminator] = None
    readOnly: Optional[bool] = None
    writeOnly: Optional[bool] = None
    xml: Optional[XML] = None
    externalDocs: Optional[ExternalDocumentation] = None
    example: Optional[Any] = None
    deprecated: Optional[bool] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the schema into a dictionary."""
        return {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
