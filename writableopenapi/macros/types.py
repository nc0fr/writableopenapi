# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Dict, List, Optional, Union
from openapi import Schema, Reference


def integer(
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
    multiple_of: Optional[int] = None,
    exclusive_minimum: Optional[bool] = None,
    exclusive_maximum: Optional[bool] = None,
    format: Optional[str] = None,
    value: Optional[int] = None,
) -> Schema:
    """
    An integer.
    """
    return Schema(
        minimum=minimum,
        maximum=maximum,
        multiple_of=multiple_of,
        exclusive_minimum=exclusive_minimum,
        exclusive_maximum=exclusive_maximum,
        default=value,
        format=format,
    )


def int8(value: Optional[int] = None) -> Schema:
    """
    An int8.
    """
    return integer(
        minimum=-128,
        maximum=127,
        value=value,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="int8",
    )


def int16(value: Optional[int] = None) -> Schema:
    """
    An int16.
    """
    return integer(
        minimum=-32768,
        maximum=32767,
        value=value,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="int16",
    )


def int32(value: Optional[int] = None) -> Schema:
    """
    An int32.
    """
    return integer(
        minimum=-2147483648,
        maximum=2147483647,
        value=value,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="int32",
    )


def int64(value: Optional[int] = None) -> Schema:
    """
    An int64.
    """
    return integer(
        minimum=-9223372036854775808,
        maximum=9223372036854775807,
        value=value,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="int64",
    )


def int128(value: Optional[int] = None) -> Schema:
    """
    An int128.
    """
    return integer(
        minimum=-170141183460469231731687303715884105728,
        maximum=170141183460469231731687303715884105727,
        value=value,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="int128",
    )


def uint8(value: Optional[int] = None) -> Schema:
    """
    An uint8.
    """
    return integer(
        minimum=0,
        maximum=255,
        value=value,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="uint8",
    )


def uint16(value: Optional[int] = None) -> Schema:
    """
    An uint16.
    """
    return integer(
        minimum=0,
        maximum=65535,
        value=value,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="uint16",
    )


def uint32(value: Optional[int] = None) -> Schema:
    """
    An uint32.
    """
    return integer(
        minimum=0,
        maximum=4294967295,
        value=value,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="uint32",
    )


def uint64(value: Optional[int] = None) -> Schema:
    """
    An uint64.
    """
    return integer(
        minimum=0,
        maximum=18446744073709551615,
        value=value,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="uint64",
    )


def uint128(value: Optional[int] = None) -> Schema:
    """
    An uint128.
    """
    return integer(
        minimum=0,
        maximum=340282366920938463463374607431768211455,
        value=value,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="uint128",
    )


def number(
    minimum: Optional[Union[int, float]] = None,
    maximum: Optional[Union[int, float]] = None,
    multiple_of: Optional[Union[int, float]] = None,
    exclusive_minimum: Optional[bool] = None,
    exclusive_maximum: Optional[bool] = None,
    format: Optional[str] = None,
    value: Optional[Union[int, float]] = None,
) -> Schema:
    """
    A number.
    """
    return Schema(
        type="number",
        minimum=minimum,
        maximum=maximum,
        multiple_of=multiple_of,
        exclusive_minimum=exclusive_minimum,
        exclusive_maximum=exclusive_maximum,
        default=value,
        format=format,
    )


def floating(value: Optional[float] = None) -> Schema:
    """
    A float.
    """
    return number(
        value=value,
        exclusive_maximum=False,
        exclusive_minimum=False,
        minimum=-3.4028234663852886e38,
        maximum=3.4028234663852886e38,
        format="float",
    )


def double(value: Optional[float] = None) -> Schema:
    """
    A double.
    """
    return number(
        value=value,
        exclusive_maximum=False,
        exclusive_minimum=False,
        minimum=-1.7976931348623157e308,
        maximum=1.7976931348623157e308,
        format="double",
    )


def string(
    minimum_length: Optional[int] = None,
    maximum_length: Optional[int] = None,
    pattern: Optional[str] = None,
    format: Optional[str] = None,
    value: Optional[str] = None,
) -> Schema:
    """
    A string.
    """
    return Schema(
        type="string",
        min_length=minimum_length,
        max_length=maximum_length,
        pattern=pattern,
        default=value,
        format=format,
    )


def date(value: Optional[str] = None) -> Schema:
    """
    A date as defined by RFC 3339, section 5.6.
    e.g. 2017-07-21
    """
    return string(
        minimum_length=10,
        maximum_length=10,
        pattern=r"^\d{4}-\d{2}-\d{2}$",
        format="date",
        value=value,
    )


def datetime(value: Optional[str] = None) -> Schema:
    """
    A date time as defined by RFC 3339, section 5.6.
    e.g. 2017-07-21T17:32:28Z
    """
    return string(
        minimum_length=20,
        maximum_length=20,
        pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$",
        format="date-time",
        value=value,
    )


def time(value: Optional[str] = None) -> Schema:
    """
    A time as defined by RFC 3339, section 5.6.
    e.g. 17:32:28Z
    """
    return string(
        minimum_length=8,
        maximum_length=8,
        pattern=r"^\d{2}:\d{2}:\d{2}Z$",
        format="time",
        value=value,
    )


def password(value: Optional[str] = None) -> Schema:
    """
    A password.
    """
    return string(format="password", value=value)


def byte(value: Optional[str] = None) -> Schema:
    """
    A byte.
    """
    return string(format="byte", value=value)


def binary(value: Optional[str] = None) -> Schema:
    """
    A binary.
    """
    return string(format="binary", value=value)


def email(value: Optional[str] = None) -> Schema:
    """
    An email.
    """
    return string(format="email", value=value)


def uuid(value: Optional[str] = None) -> Schema:
    """
    A UUID.
    """
    return string(
        minimum_length=36,
        maximum_length=36,
        pattern=r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
        format="uuid",
        value=value,
    )


def uri(value: Optional[str] = None) -> Schema:
    """
    A URI.
    """
    return string(format="uri", value=value)


def hostname(value: Optional[str] = None) -> Schema:
    """
    A hostname.
    """
    return string(format="hostname", value=value)


def ipv4(value: Optional[str] = None) -> Schema:
    """
    An IPv4.
    """
    return string(
        format="ipv4",
        value=value,
        pattern=r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
        minimum_length=7,
        maximum_length=15,
    )


def ipv6(value: Optional[str] = None) -> Schema:
    """
    An IPv6.
    """
    return string(
        format="ipv6",
        value=value,
        pattern=r"^[0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){7}$",
        minimum_length=2,
        maximum_length=39,
    )


def boolean(value: Optional[bool] = None) -> Schema:
    """
    A boolean.
    """
    return Schema(type="boolean", default=value)


def null(value: Optional[None] = None) -> Schema:
    """
    A null.
    """
    return Schema(type="null", default=value)


def array(
    items: Union[Schema, Reference],
    minimum_length: Optional[int] = None,
    maximum_length: Optional[int] = None,
    unique_items: Optional[bool] = None,
    value: Optional[List[Union[Schema, Reference]]] = None,
) -> Schema:
    """
    An array.
    """
    return Schema(
        type="array",
        items=items,
        min_items=minimum_length,
        max_items=maximum_length,
        unique_items=unique_items,
        default=value,
    )


def object(
    properties: Dict[str, Union[Schema, Reference]],
    required: Optional[List[str]] = None,
    minimum_length: Optional[int] = None,
    maximum_length: Optional[int] = None,
    value: Optional[Dict[str, Union[Schema, Reference]]] = None,
) -> Schema:
    """
    An object.
    """
    return Schema(
        type="object",
        properties={k: v for k, v in properties.items()},
        required=required,
        min_properties=minimum_length,
        max_properties=maximum_length,
        default=value,
    )


def enum(
    values: List[str], default: Optional[str] = None, nullable: bool = False
) -> Schema:
    """
    An enum.
    """
    return Schema(
        type="string",
        enum=values,
        default=default,
        nullable=nullable,
    )


def any(nullable: bool = False) -> Schema:
    """
    Any type.
    """
    return Schema(nullable=nullable)
