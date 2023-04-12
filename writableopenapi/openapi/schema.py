# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Self, Union

from discriminator import Discriminator
from external_documentation import ExternalDocumentation
from reference import Reference
from specification_extension import SpecificationExtension
from typing_extensions import override

from .xml import XML


@dataclass
class Schema(SpecificationExtension):
    title: Optional[str] = None
    multiple_of: Optional[float] = None
    maximum: Optional[float] = None
    exclusive_maximum: Optional[bool] = None
    minimum: Optional[float] = None
    exclusive_minimum: Optional[bool] = None
    max_length: Optional[int] = None
    min_length: Optional[int] = None
    pattern: Optional[str] = None
    max_items: Optional[int] = None
    min_items: Optional[int] = None
    unique_items: Optional[bool] = None
    max_properties: Optional[int] = None
    min_properties: Optional[int] = None
    required: Optional[List[str]] = None
    enum: Optional[List[Any]] = None
    type: Optional[Union[str, List[str]]] = None
    all_of: Optional[List[Union[Reference, "Schema"]]] = None
    one_of: Optional[List[Union[Reference, "Schema"]]] = None
    any_of: Optional[List[Union[Reference, "Schema"]]] = None
    not_: Optional[Union[Reference, "Schema"]] = None
    items: Optional[
        Union[Reference, "Schema", List[Union[Reference, "Schema"]]]
    ] = None
    properties: Optional[Dict[str, Union[Reference, "Schema"]]] = None
    additional_properties: Optional[Union[bool, Reference, "Schema"]] = None
    description: Optional[str] = None
    format: Optional[str] = None
    default: Optional[Any] = None
    nullable: Optional[bool] = None
    discriminator: Optional[Discriminator] = None
    read_only: Optional[bool] = None
    write_only: Optional[bool] = None
    xml: Optional[XML] = None
    external_docs: Optional[ExternalDocumentation] = None
    example: Optional[Any] = None
    deprecated: Optional[bool] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the schema into a dictionary."""
        data = self.extensions
        if self.title is not None:
            data["title"] = self.title
        if self.multiple_of is not None:
            data["multipleOf"] = self.multiple_of
        if self.maximum is not None:
            data["maximum"] = self.maximum
        if self.exclusive_maximum is not None:
            data["exclusiveMaximum"] = self.exclusive_maximum
        if self.minimum is not None:
            data["minimum"] = self.minimum
        if self.exclusive_minimum is not None:
            data["exclusiveMinimum"] = self.exclusive_minimum
        if self.max_length is not None:
            data["maxLength"] = self.max_length
        if self.min_length is not None:
            data["minLength"] = self.min_length
        if self.pattern is not None:
            data["pattern"] = self.pattern
        if self.max_items is not None:
            data["maxItems"] = self.max_items
        if self.min_items is not None:
            data["minItems"] = self.min_items
        if self.unique_items is not None:
            data["uniqueItems"] = self.unique_items
        if self.max_properties is not None:
            data["maxProperties"] = self.max_properties
        if self.min_properties is not None:
            data["minProperties"] = self.min_properties
        if self.required is not None:
            data["required"] = self.required
        if self.enum is not None:
            data["enum"] = self.enum
        if self.type is not None:
            data["type"] = self.type
        if self.all_of is not None:
            data["allOf"] = [v.dump() for v in self.all_of]
        if self.one_of is not None:
            data["oneOf"] = [v.dump() for v in self.one_of]
        if self.any_of is not None:
            data["anyOf"] = [v.dump() for v in self.any_of]
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
        if self.additional_properties is not None:
            if isinstance(self.additional_properties, bool):
                data["additionalProperties"] = self.additional_properties
            else:
                data["additionalProperties"] = self.additional_properties.dump()
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
        if self.read_only is not None:
            data["readOnly"] = self.read_only
        if self.write_only is not None:
            data["writeOnly"] = self.write_only
        if self.xml is not None:
            data["xml"] = self.xml.dump()
        if self.external_docs is not None:
            data["externalDocs"] = self.external_docs.dump()
        if self.example is not None:
            data["example"] = self.example
        if self.deprecated is not None:
            data["deprecated"] = self.deprecated
        return data
