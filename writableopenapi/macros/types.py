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
class Int8(Int):
    """
    An int8.
    """

    def __post_init__(self):
        self.format_ = "int8"
        self.maximum = 127
        self.minimum = -128
        self.exclusive_maximum = False
        self.exclusive_minimum = False


@dataclass
class Int16(Int):
    """
    An int16.
    """

    def __post_init__(self):
        self.format_ = "int16"
        self.maximum = 32767
        self.minimum = -32768
        self.exclusive_maximum = False
        self.exclusive_minimum = False


@dataclass
class Int32(Int):
    """
    An int32.
    """

    def __post_init__(self):
        self.format_ = "int32"
        self.maximum = 2147483647
        self.minimum = -2147483648
        self.exclusive_maximum = False
        self.exclusive_minimum = False


@dataclass
class Int64(Int):
    """
    An int64.
    """

    def __post_init__(self):
        self.format_ = "int64"
        self.maximum = 9223372036854775807
        self.minimum = -9223372036854775808
        self.exclusive_maximum = False
        self.exclusive_minimum = False


@dataclass
class Int128(Int):
    """
    An int128.
    """

    def __post_init__(self):
        self.format_ = "int128"
        self.maximum = 170141183460469231731687303715884105727
        self.minimum = -170141183460469231731687303715884105728
        self.exclusive_maximum = False
        self.exclusive_minimum = False


@dataclass
class UInt8(Int):
    """
    An uint8.
    """

    def __post_init__(self):
        self.format_ = "uint8"
        self.maximum = 255
        self.minimum = 0
        self.exclusive_maximum = False
        self.exclusive_minimum = False


@dataclass
class UInt16(Int):
    """
    An uint16.
    """

    def __post_init__(self):
        self.format_ = "uint16"
        self.maximum = 65535
        self.minimum = 0
        self.exclusive_maximum = False
        self.exclusive_minimum = False


@dataclass
class UInt32(Int):
    """
    An uint32.
    """

    def __post_init__(self):
        self.format_ = "uint32"
        self.maximum = 4294967295
        self.minimum = 0
        self.exclusive_maximum = False
        self.exclusive_minimum = False


@dataclass
class UInt64(Int):
    """
    An uint64.
    """

    def __post_init__(self):
        self.format_ = "uint64"
        self.maximum = 18446744073709551615
        self.minimum = 0
        self.exclusive_maximum = False
        self.exclusive_minimum = False


@dataclass
class UInt128(Int):
    """
    An uint128.
    """

    def __post_init__(self):
        self.format_ = "uint128"
        self.maximum = 340282366920938463463374607431768211455
        self.minimum = 0
        self.exclusive_maximum = False
        self.exclusive_minimum = False


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

    def __post_init__(self):
        self.format_ = "float"


@dataclass
class Double(Number):
    """
    A double.
    """

    def __post_init__(self):
        self.format_ = "double"


@dataclass
class String(IntoSchema):
    """
    A string.
    """

    format_: str = ""
    """
    The format of this string.
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
            format=self.format_,
        )


@dataclass
class Date(String):
    """
    A date as defined by RFC 3339, section 5.6.
    e.g. 2017-07-21
    """

    def __post_init__(self):
        self.format_ = "date"
        self.pattern = r"^\d{4}-\d{2}-\d{2}$"


@dataclass
class DateTime(String):
    """
    A date time as defined by RFC 3339, section 5.6.
    e.g. 2017-07-21T17:32:28Z
    """

    def __post_init__(self):
        self.format_ = "date-time"
        self.pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$"


@dataclass
class Password(String):
    """
    A password.
    """

    def __post_init__(self):
        self.format_ = "password"


@dataclass
class Byte(String):
    """
    A byte.
    """

    def __post_init__(self):
        self.format_ = "byte"


@dataclass
class Binary(String):
    """
    A binary.
    """

    def __post_init__(self):
        self.format_ = "binary"


@dataclass
class Email(String):
    """
    An email.
    """

    def __post_init__(self):
        self.format_ = "email"


@dataclass
class UUID(String):
    """
    A UUID.
    """

    def __post_init__(self):
        self.format_ = "uuid"
        self.pattern = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"


@dataclass
class URI(String):
    """
    A URI.
    """

    def __post_init__(self):
        self.format_ = "uri"


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
