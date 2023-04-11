# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
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
        data = self.extensions
        if self.title is not None:
            data["title"] = self.title
        if self.multipleOf is not None:
            data["multipleOf"] = self.multipleOf
        if self.maximum is not None:
            data["maximum"] = self.maximum
        if self.exclusiveMaximum is not None:
            data["exclusiveMaximum"] = self.exclusiveMaximum
        if self.minimum is not None:
            data["minimum"] = self.minimum
        if self.exclusiveMinimum is not None:
            data["exclusiveMinimum"] = self.exclusiveMinimum
        if self.maxLength is not None:
            data["maxLength"] = self.maxLength
        if self.minLength is not None:
            data["minLength"] = self.minLength
        if self.pattern is not None:
            data["pattern"] = self.pattern
        if self.maxItems is not None:
            data["maxItems"] = self.maxItems
        if self.minItems is not None:
            data["minItems"] = self.minItems
        if self.uniqueItems is not None:
            data["uniqueItems"] = self.uniqueItems
        if self.maxProperties is not None:
            data["maxProperties"] = self.maxProperties
        if self.minProperties is not None:
            data["minProperties"] = self.minProperties
        if self.required is not None:
            data["required"] = self.required
        if self.enum is not None:
            data["enum"] = self.enum
        if self.type is not None:
            data["type"] = self.type
        if self.allOf is not None:
            data["allOf"] = [v.dump() for v in self.allOf]
        if self.oneOf is not None:
            data["oneOf"] = [v.dump() for v in self.oneOf]
        if self.anyOf is not None:
            data["anyOf"] = [v.dump() for v in self.anyOf]
        if self.not_ is not None:
            data["not"] = self.not_.dump()
        if self.items is not None:
            if isinstance(self.items, list):
                data["items"] = [v.dump() for v in self.items]
            else:
                data["items"] = self.items.dump()
        if self.properties is not None:
            data["properties"] = {
                k: v.dump() for k, v in self.properties.items()
            }
        if self.additionalProperties is not None:
            if isinstance(self.additionalProperties, bool):
                data["additionalProperties"] = self.additionalProperties
            else:
                data["additionalProperties"] = self.additionalProperties.dump()
        if self.description is not None:
            data["description"] = self.description
        if self.format is not None:
            data["format"] = self.format
        if self.default is not None:
            data["default"] = self.default
        if self.nullable is not None:
            data["nullable"] = self.nullable
        if self.discriminator is not None:
            data["discriminator"] = self.discriminator.dump()
        if self.readOnly is not None:
            data["readOnly"] = self.readOnly
        if self.writeOnly is not None:
            data["writeOnly"] = self.writeOnly
        if self.xml is not None:
            data["xml"] = self.xml.dump()
        if self.externalDocs is not None:
            data["externalDocs"] = self.externalDocs.dump()
        if self.example is not None:
            data["example"] = self.example
        if self.deprecated is not None:
            data["deprecated"] = self.deprecated
        return data
