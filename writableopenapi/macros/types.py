# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Dict, List, Optional
from openapi import Schema
from typing_extensions import override
from into import IntoSchema


@dataclass
class Int(IntoSchema):
    """
    An integer.
    """

    minimum: Optional[int] = None
    """
    The minimum value of this integer.
    """

    maximum: Optional[int] = None
    """
    The maximum value of this integer.
    """

    multiple_of: Optional[int] = None
    """
    The multiple of this integer.
    """

    exclusive_minimum: Optional[int] = None
    """
    The exclusive minimum value of this integer.
    """

    exclusive_maximum: Optional[int] = None
    """
    The exclusive maximum value of this integer.
    """

    @override
    def into_schema(self) -> Schema:
        return Schema(
            type="integer",
            minimum=self.minimum,
            maximum=self.maximum,
            multiple_of=self.multiple_of,
            exclusive_minimum=self.exclusive_minimum,
            exclusive_maximum=self.exclusive_maximum,
        )


@dataclass
class Int32(Int):
    """
    An int32.
    """

    @override
    def into_schema(self) -> Schema:
        schema = super().into_schema()
        schema.format = "int32"
        return schema


@dataclass
class Int64(Int):
    """
    An int64.
    """

    @override
    def into_schema(self) -> Schema:
        schema = super().into_schema()
        schema.format = "int64"
        return schema


@dataclass
class Number(IntoSchema):
    """
    A number.
    """

    minimum: Optional[float] = None
    """
    The minimum value of this number.
    """

    maximum: Optional[float] = None
    """
    The maximum value of this number.
    """

    multiple_of: Optional[float] = None
    """
    The multiple of this number.
    """

    exclusive_minimum: Optional[float] = None
    """
    The exclusive minimum value of this number.
    """

    exclusive_maximum: Optional[float] = None
    """
    The exclusive maximum value of this number.
    """

    @override
    def into_schema(self) -> Schema:
        return Schema(
            type="number",
            minimum=self.minimum,
            maximum=self.maximum,
            multiple_of=self.multiple_of,
            exclusive_minimum=self.exclusive_minimum,
            exclusive_maximum=self.exclusive_maximum,
        )


@dataclass
class Float(Number):
    """
    A float.
    """

    @override
    def into_schema(self) -> Schema:
        schema = super().into_schema()
        schema.format = "float"
        return schema


@dataclass
class Double(Number):
    """
    A double.
    """

    @override
    def into_schema(self) -> Schema:
        schema = super().into_schema()
        schema.format = "double"
        return schema


@dataclass
class String(IntoSchema):
    """
    A string.
    """

    minimum_length: Optional[int] = None
    """
    The minimum length of this string.
    """

    maximum_length: Optional[int] = None
    """
    The maximum length of this string.
    """

    pattern: Optional[str] = None
    """
    The pattern of this string.
    """

    @override
    def into_schema(self) -> Schema:
        return Schema(
            type="string",
            min_length=self.minimum_length,
            max_length=self.maximum_length,
            pattern=self.pattern,
        )


@dataclass
class Date(String):
    """
    A date as defined by RFC 3339, section 5.6.
    e.g. 2017-07-21
    """

    @override
    def into_schema(self) -> Schema:
        schema = super().into_schema()
        schema.format = "date"
        schema.pattern = r"^\d{4}-\d{2}-\d{2}$"
        return schema


@dataclass
class DateTime(String):
    """
    A date time as defined by RFC 3339, section 5.6.
    e.g. 2017-07-21T17:32:28Z
    """

    @override
    def into_schema(self) -> Schema:
        schema = super().into_schema()
        schema.format = "date-time"
        schema.pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$"
        return schema


@dataclass
class Password(String):
    """
    A password.
    """

    @override
    def into_schema(self) -> Schema:
        schema = super().into_schema()
        schema.format = "password"
        return schema


@dataclass
class Byte(String):
    """
    A byte.
    """

    @override
    def into_schema(self) -> Schema:
        schema = super().into_schema()
        schema.format = "byte"
        return schema


@dataclass
class Binary(String):
    """
    A binary.
    """

    @override
    def into_schema(self) -> Schema:
        schema = super().into_schema()
        schema.format = "binary"
        return schema


@dataclass
class Email(String):
    """
    An email.
    """

    @override
    def into_schema(self) -> Schema:
        schema = super().into_schema()
        schema.format = "email"
        return schema


@dataclass
class UUID(String):
    """
    A UUID.
    """

    @override
    def into_schema(self) -> Schema:
        schema = super().into_schema()
        schema.format = "uuid"
        return schema


@dataclass
class URI(String):
    """
    A URI.
    """

    @override
    def into_schema(self) -> Schema:
        schema = super().into_schema()
        schema.format = "uri"
        return schema


@dataclass
class Boolean(IntoSchema):
    """
    A boolean.
    """

    @override
    def into_schema(self) -> Schema:
        return Schema(type="boolean")


@dataclass
class Null(IntoSchema):
    """
    A null.
    """

    @override
    def into_schema(self) -> Schema:
        return Schema(type="null")


@dataclass
class Array(IntoSchema):
    """
    An array.
    """

    items: IntoSchema
    """
    The items of this array.
    """

    minimum_length: Optional[int] = None
    """
    The minimum length of this array.
    """

    maximum_length: Optional[int] = None
    """
    The maximum length of this array.
    """

    unique_items: Optional[bool] = None

    @override
    def into_schema(self) -> Schema:
        return Schema(
            type="array",
            items=self.items.into_schema(),
            min_items=self.minimum_length,
            max_items=self.maximum_length,
            unique_items=self.unique_items,
        )


@dataclass
class Object(IntoSchema):
    """
    An object.
    """

    properties: Dict[str, IntoSchema]
    """
    The properties of this object.
    """

    required: Optional[List[str]] = None
    """
    The required properties of this object.
    """

    minimum_length: Optional[int] = None
    """
    The minimum length of this object.
    """

    maximum_length: Optional[int] = None
    """
    The maximum length of this object.
    """

    @override
    def into_schema(self) -> Schema:
        return Schema(
            type="object",
            properties={k: v.into_schema() for k, v in self.properties.items()},
            required=self.required,
            min_properties=self.minimum_length,
            max_properties=self.maximum_length,
        )


@dataclass
class Enum(IntoSchema):
    """
    An enum.
    """

    values: List[IntoSchema]
    """
    The values of this enum.
    """

    default: Optional[IntoSchema] = None
    """
    The default value of this enum.
    """

    nullable: bool = False

    @override
    def into_schema(self) -> Schema:
        return Schema(
            type="string",
            enum=self.values,
            default=self.default,
            nullable=self.nullable,
        )
