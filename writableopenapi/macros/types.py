# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import re
from typing import Any, Dict, List, Optional, Union
from writableopenapi.openapi.v3_1 import ExternalDocumentation, Reference, Schema

_INT8_MIN = -128
_INT8_MAX = 127
_INT16_MIN = -32768
_INT16_MAX = 32767
_INT32_MIN = -2147483648
_INT32_MAX = 2147483647
_INT64_MIN = -9223372036854775808
_INT64_MAX = 9223372036854775807
_INT128_MIN = -170141183460469231731687303715884105728
_INT128_MAX = 170141183460469231731687303715884105727
_UINT8_MIN = 0
_UINT8_MAX = 255
_UINT16_MIN = 0
_UINT16_MAX = 65535
_UINT32_MIN = 0
_UINT32_MAX = 4294967295
_UINT64_MIN = 0
_UINT64_MAX = 18446744073709551615
_UINT128_MIN = 0
_UINT128_MAX = 340282366920938463463374607431768211455
"""
UNUSED DUE TO PRECISION ISSUES
_FLOAT_MIN = -340282346638528859811704183484516925440.0,
_FLOAT_MAX = 340282346638528859811704183484516925440.0,
_DOUBLE_MIN = -179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.0
_DOUBLE_MAX = 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.0
"""
_DATE_REGEX = r"^\d{4}-\d{2}-\d{2}$"
_DATETIME_REGEX = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,6})?Z$"
_TIME_REGEX = r"^\d{2}:\d{2}:\d{2}Z$"
_UUID_REGEX = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
_IPV4_REGEX = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
_IPV6_REGEX = r"^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"


def integer(
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
    multiple_of: Optional[int] = None,
    exclusive_minimum: Optional[bool] = None,
    exclusive_maximum: Optional[bool] = None,
    format: Optional[str] = None,
    example: Optional[int] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    deprecated: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[int] = None,
) -> Schema:
    """
    An integer.
    """

    if minimum is not None and maximum is not None and minimum > maximum:
        raise ValueError("Minimum must be less than maximum")

    if minimum is not None and example is not None and example < minimum:
        raise ValueError("Example must be greater than minimum")

    if maximum is not None and example is not None and example > maximum:
        raise ValueError("Example must be less than maximum")

    if minimum is not None and default is not None and default < minimum:
        raise ValueError("Default must be greater than minimum")

    if maximum is not None and default is not None and default > maximum:
        raise ValueError("Default must be less than maximum")

    if (
        multiple_of is not None
        and default is not None
        and default % multiple_of != 0
    ):
        raise ValueError("Default must be a multiple of multiple_of")

    if (
        multiple_of is not None
        and example is not None
        and example % multiple_of != 0
    ):
        raise ValueError("Example must be a multiple of multiple_of")

    return Schema(
        minimum=minimum,
        maximum=maximum,
        multiple_of=multiple_of,
        exclusive_minimum=exclusive_minimum,
        exclusive_maximum=exclusive_maximum,
        example=example,
        format=format,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        type="integer",
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def int8(
    example: Optional[int] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[int] = None,
) -> Schema:
    """
    An int8.
    """

    if example is not None and (example > _INT8_MAX or example < _INT8_MIN):
        raise ValueError(f"Example must be between {_INT8_MIN} and {_INT8_MAX}")

    return integer(
        minimum=_INT8_MIN,
        maximum=_INT8_MAX,
        example=example,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="int8",
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def int16(
    example: Optional[int] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[int] = None,
) -> Schema:
    """
    An int16.
    """

    if example is not None and (example > _INT16_MAX or example < _INT16_MIN):
        raise ValueError(
            f"Example must be between {_INT16_MIN} and {_INT16_MAX}"
        )

    if default is not None and (default > _INT16_MAX or default < _INT16_MIN):
        raise ValueError(
            f"Default must be between {_INT16_MIN} and {_INT16_MAX}"
        )

    return integer(
        minimum=_INT16_MIN,
        maximum=_INT16_MAX,
        example=example,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="int16",
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def int32(
    example: Optional[int] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[int] = None,
) -> Schema:
    """
    An int32.
    """

    if example is not None and (example > _INT32_MAX or example < _INT32_MIN):
        raise ValueError(
            f"Example must be between {_INT32_MIN} and {_INT32_MAX}"
        )

    if default is not None and (default > _INT32_MAX or default < _INT32_MIN):
        raise ValueError(
            f"Default must be between {_INT32_MIN} and {_INT32_MAX}"
        )

    return integer(
        minimum=_INT32_MIN,
        maximum=_INT32_MAX,
        example=example,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="int32",
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def int64(
    example: Optional[int] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[int] = None,
) -> Schema:
    """
    An int64.
    """

    if example is not None and (example > _INT64_MAX or example < _INT64_MIN):
        raise ValueError(
            f"Example must be between {_INT64_MIN} and {_INT64_MAX}"
        )

    if default is not None and (default > _INT64_MAX or default < _INT64_MIN):
        raise ValueError(
            f"Default must be between {_INT64_MIN} and {_INT64_MAX}"
        )

    return integer(
        minimum=_INT64_MIN,
        maximum=_INT64_MAX,
        example=example,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="int64",
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def int128(
    example: Optional[int] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[int] = None,
) -> Schema:
    """
    An int128.
    """

    if example is not None and (example > _INT128_MAX or example < _INT128_MIN):
        raise ValueError(
            f"Example must be between {_INT128_MIN} and {_INT128_MAX}"
        )

    if default is not None and (default > _INT128_MAX or default < _INT128_MIN):
        raise ValueError(
            f"Default must be between {_INT128_MIN} and {_INT128_MAX}"
        )

    return integer(
        minimum=_INT128_MIN,
        maximum=_INT128_MAX,
        example=example,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="int128",
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def uint8(
    example: Optional[int] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[int] = None,
) -> Schema:
    """
    An uint8.
    """

    if example is not None and (example > _UINT8_MAX or example < _UINT8_MIN):
        raise ValueError(
            f"Example must be between {_UINT8_MIN} and {_UINT8_MAX}"
        )

    if default is not None and (default > _UINT8_MAX or default < _UINT8_MIN):
        raise ValueError(
            f"Default must be between {_UINT8_MIN} and {_UINT8_MAX}"
        )

    return integer(
        minimum=_UINT8_MIN,
        maximum=_UINT8_MAX,
        example=example,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="uint8",
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def uint16(
    example: Optional[int] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[int] = None,
) -> Schema:
    """
    An uint16.
    """

    if example is not None and (example > _UINT16_MAX or example < _UINT16_MIN):
        raise ValueError(
            f"Example must be between {_UINT16_MIN} and {_UINT16_MAX}"
        )

    if default is not None and (default > _UINT16_MAX or default < _UINT16_MIN):
        raise ValueError(
            f"Default must be between {_UINT16_MIN} and {_UINT16_MAX}"
        )

    return integer(
        minimum=_UINT16_MIN,
        maximum=_UINT16_MAX,
        example=example,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="uint16",
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def uint32(
    example: Optional[int] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[int] = None,
) -> Schema:
    """
    An uint32.
    """

    if example is not None and (example > _UINT32_MAX or example < _UINT32_MIN):
        raise ValueError(
            f"Example must be between {_UINT32_MIN} and {_UINT32_MAX}"
        )

    if default is not None and (default > _UINT32_MAX or default < _UINT32_MIN):
        raise ValueError(
            f"Default must be between {_UINT32_MIN} and {_UINT32_MAX}"
        )

    return integer(
        minimum=_UINT32_MIN,
        maximum=_UINT32_MAX,
        example=example,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="uint32",
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def uint64(
    example: Optional[int] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[int] = None,
) -> Schema:
    """
    An uint64.
    """

    if example is not None and (example > _UINT64_MAX or example < _UINT64_MIN):
        raise ValueError(
            f"Example must be between {_UINT64_MIN} and {_UINT64_MAX}"
        )

    if default is not None and (default > _UINT64_MAX or default < _UINT64_MIN):
        raise ValueError(
            f"Default must be between {_UINT64_MIN} and {_UINT64_MAX}"
        )

    return integer(
        minimum=_UINT64_MIN,
        maximum=_UINT64_MAX,
        example=example,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="uint64",
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def uint128(
    example: Optional[int] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[int] = None,
) -> Schema:
    """
    An uint128.
    """

    if example is not None and (
        example > _UINT128_MAX or example < _UINT128_MIN
    ):
        raise ValueError(
            f"Example must be between {_UINT128_MIN} and {_UINT128_MAX}"
        )

    if default is not None and (
        default > _UINT128_MAX or default < _UINT128_MIN
    ):
        raise ValueError(
            f"Default must be between {_UINT128_MIN} and {_UINT128_MAX}"
        )

    return integer(
        minimum=_UINT128_MIN,
        maximum=_UINT128_MAX,
        example=example,
        exclusive_maximum=False,
        exclusive_minimum=False,
        format="uint128",
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def number(
    minimum: Optional[Union[int, float]] = None,
    maximum: Optional[Union[int, float]] = None,
    multiple_of: Optional[Union[int, float]] = None,
    exclusive_minimum: Optional[bool] = None,
    exclusive_maximum: Optional[bool] = None,
    format: Optional[str] = None,
    example: Optional[Union[int, float]] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    deprecated: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[Union[int, float]] = None,
) -> Schema:
    """
    A number.
    """

    # no check for example, default, minimum, maximum, multiple_of
    # due to float precision issues

    return Schema(
        type="number",
        minimum=minimum,
        maximum=maximum,
        multiple_of=multiple_of,
        exclusive_minimum=exclusive_minimum,
        exclusive_maximum=exclusive_maximum,
        example=example,
        format=format,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def floating(
    example: Optional[float] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[float] = None,
) -> Schema:
    """
    A float.
    """

    return number(
        example=example,
        exclusive_maximum=False,
        exclusive_minimum=False,
        minimum=-3.4028234663852886e38,
        maximum=3.4028234663852886e38,
        format="float",
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def double(
    example: Optional[float] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[float] = None,
) -> Schema:
    """
    A double.
    """
    return number(
        example=example,
        exclusive_maximum=False,
        exclusive_minimum=False,
        minimum=-1.7976931348623157e308,
        maximum=1.7976931348623157e308,
        format="double",
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def string(
    minimum_length: Optional[int] = None,
    maximum_length: Optional[int] = None,
    pattern: Optional[str] = None,
    format: Optional[str] = None,
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    deprecated: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    A string.
    """

    if example is not None and (
        minimum_length is not None and len(example) < minimum_length
    ):
        raise ValueError(
            f"Example must be at least {minimum_length} characters long"
        )

    if example is not None and (
        maximum_length is not None and len(example) > maximum_length
    ):
        raise ValueError(
            f"Example must be at most {maximum_length} characters long"
        )

    if default is not None and (
        minimum_length is not None and len(default) < minimum_length
    ):
        raise ValueError(
            f"Default must be at least {minimum_length} characters long"
        )

    if default is not None and (
        maximum_length is not None and len(default) > maximum_length
    ):
        raise ValueError(
            f"Default must be at most {maximum_length} characters long"
        )

    if (
        example is not None
        and pattern is not None
        and not re.match(pattern, example)
    ):
        raise ValueError(f"Example must match pattern {pattern}")

    if (
        default is not None
        and pattern is not None
        and not re.match(pattern, default)
    ):
        raise ValueError(f"Default must match pattern {pattern}")

    if (
        minimum_length is not None
        and maximum_length is not None
        and minimum_length > maximum_length
    ):
        raise ValueError(f"Minimum length must be less than maximum length")

    if minimum_length is not None and minimum_length < 0:
        raise ValueError(f"Minimum length must be greater than 0")

    if maximum_length is not None and maximum_length < 0:
        raise ValueError(f"Maximum length must be greater than 0")

    return Schema(
        type="string",
        min_length=minimum_length,
        max_length=maximum_length,
        pattern=pattern,
        example=example,
        format=format,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def date(
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    A date as defined by RFC 3339, section 5.6.
    e.g. 2017-07-21
    """

    if example is not None and not re.match(_DATE_REGEX, example):
        raise ValueError("Example must be a valid date string")

    if default is not None and not re.match(_DATE_REGEX, default):
        raise ValueError("Default must be a valid date string")

    return string(
        minimum_length=10,
        maximum_length=10,
        pattern=_DATE_REGEX,
        format="date",
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def datetime(
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    A date time as defined by RFC 3339, section 5.6.
    e.g. 2017-07-21T17:32:28Z
    """

    if example is not None and not re.match(_DATETIME_REGEX, example):
        raise ValueError("Example must be a valid date time string")

    if default is not None and not re.match(_DATETIME_REGEX, default):
        raise ValueError("Default must be a valid date time string")

    return string(
        minimum_length=20,
        maximum_length=20,
        pattern=_DATETIME_REGEX,
        format="date-time",
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def time(
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    A time as defined by RFC 3339, section 5.6.
    e.g. 17:32:28Z
    """

    if example is not None and not re.match(_TIME_REGEX, example):
        raise ValueError("Example must be a valid time string")

    if default is not None and not re.match(_TIME_REGEX, default):
        raise ValueError("Default must be a valid time string")

    return string(
        minimum_length=8,
        maximum_length=8,
        pattern=_TIME_REGEX,
        format="time",
        example=example,
        description=description,
        external_docs=external_docs,
        nullable=nullable,
        deprecated=deprecated,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def password(
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    A password.
    """

    return string(
        format="password",
        external_docs=external_docs,
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def byte(
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    A byte.
    """

    return string(
        format="byte",
        external_docs=external_docs,
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def binary(
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    A binary.
    """

    return string(
        format="binary",
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def email(
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    An email.
    """
    return string(
        format="email",
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def uuid(
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    A UUID.
    """

    if example is not None and not re.match(_UUID_REGEX, example):
        raise ValueError("Example must be a valid UUID string")

    if default is not None and not re.match(_UUID_REGEX, default):
        raise ValueError("Default must be a valid UUID string")

    return string(
        minimum_length=36,
        maximum_length=36,
        pattern=_UUID_REGEX,
        format="uuid",
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def uri(
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    A URI.
    """
    return string(
        format="uri",
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def hostname(
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    A hostname.
    """
    return string(
        format="hostname",
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def ipv4(
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    An IPv4.
    """

    if example is not None and not re.match(_IPV4_REGEX, example):
        raise ValueError("Example must be a valid IPv4 string")

    if default is not None and not re.match(_IPV4_REGEX, default):
        raise ValueError("Default must be a valid IPv4 string")

    return string(
        format="ipv4",
        example=example,
        pattern=_IPV4_REGEX,
        minimum_length=7,
        maximum_length=15,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def ipv6(
    example: Optional[str] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    deprecated: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[str] = None,
) -> Schema:
    """
    An IPv6.
    """

    if example is not None and not re.match(_IPV6_REGEX, example):
        raise ValueError("Example must be a valid IPv6 string")

    if default is not None and not re.match(_IPV6_REGEX, default):
        raise ValueError("Default must be a valid IPv6 string")

    return string(
        format="ipv6",
        example=example,
        pattern=_IPV6_REGEX,
        minimum_length=2,
        maximum_length=39,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def boolean(
    example: Optional[bool] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[bool] = None,
) -> Schema:
    """
    A boolean.
    """

    return Schema(
        type="boolean",
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def null(
    example: Optional[None] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    deprecated: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
) -> Schema:
    """
    A null.
    """
    return Schema(
        type="null",
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
    )


def array(
    items: Union[Schema, Reference],
    minimum_length: Optional[int] = None,
    maximum_length: Optional[int] = None,
    unique_items: Optional[bool] = None,
    example: Optional[List[Union[Schema, Reference]]] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    deprecated: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[List[Union[Schema, Reference]]] = None,
) -> Schema:
    """
    An array.
    """

    if minimum_length is not None and minimum_length < 0:
        raise ValueError("Minimum length must be greater than or equal to 0")

    if maximum_length is not None and maximum_length < 0:
        raise ValueError("Maximum length must be greater than or equal to 0")

    if (
        minimum_length is not None
        and maximum_length is not None
        and minimum_length > maximum_length
    ):
        raise ValueError(
            "Minimum length must be less than or equal to maximum length"
        )

    if (
        example is not None
        and minimum_length is not None
        and len(example) < minimum_length
    ):
        raise ValueError(
            "Example must be greater than or equal to minimum length"
        )

    if (
        example is not None
        and maximum_length is not None
        and len(example) > maximum_length
    ):
        raise ValueError("Example must be less than or equal to maximum length")

    if (
        default is not None
        and minimum_length is not None
        and len(default) < minimum_length
    ):
        raise ValueError(
            "Default must be greater than or equal to minimum length"
        )

    if (
        default is not None
        and maximum_length is not None
        and len(default) > maximum_length
    ):
        raise ValueError("Default must be less than or equal to maximum length")

    return Schema(
        type="array",
        items=items,
        min_items=minimum_length,
        max_items=maximum_length,
        unique_items=unique_items,
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def object(
    properties: Dict[str, Union[Schema, Reference]],
    required: Optional[List[str]] = None,
    minimum_properties: Optional[int] = None,
    maximum_properties: Optional[int] = None,
    example: Optional[Dict[str, Union[Schema, Reference]]] = None,
    description: Optional[str] = None,
    nullable: bool = False,
    deprecated: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[Dict[str, Union[Schema, Reference]]] = None,
) -> Schema:
    """
    An object.
    """

    if minimum_properties is not None and minimum_properties < 0:
        raise ValueError("Minimum length must be greater than or equal to 0")

    if maximum_properties is not None and maximum_properties < 0:
        raise ValueError("Maximum length must be greater than or equal to 0")

    if (
        minimum_properties is not None
        and maximum_properties is not None
        and minimum_properties > maximum_properties
    ):
        raise ValueError(
            "Minimum length must be less than or equal to maximum length"
        )

    return Schema(
        type="object",
        properties={k: v for k, v in properties.items()},
        required=required,
        min_properties=minimum_properties,
        max_properties=maximum_properties,
        example=example,
        description=description,
        nullable=nullable,
        deprecated=deprecated,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
    )


def string_enum(
    variants: List[str],
    default: Optional[str] = None,
    nullable: bool = False,
    description: Optional[str] = None,
    deprecated: bool = False,
    example: Optional[str] = None,
    external_docs: Optional[ExternalDocumentation] = None,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
) -> Schema:
    """
    An string enum.
    """
    return Schema(
        type="string",
        enum=variants,
        default=default,
        nullable=nullable,
        description=description,
        deprecated=deprecated,
        example=example,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
    )


def number_enum(
    variants: List[Union[int, float]],
    default: Optional[Union[int, float]] = None,
    nullable: bool = False,
    description: Optional[str] = None,
    deprecated: bool = False,
    example: Optional[Union[int, float]] = None,
    external_docs: Optional[ExternalDocumentation] = None,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
) -> Schema:
    """
    An number enum.
    """
    return Schema(
        type="number",
        enum=variants,
        default=default,
        nullable=nullable,
        description=description,
        deprecated=deprecated,
        example=example,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
    )


def integer_enum(
    variants: List[int],
    default: Optional[int] = None,
    nullable: bool = False,
    description: Optional[str] = None,
    deprecated: bool = False,
    example: Optional[Union[int, float]] = None,
    external_docs: Optional[ExternalDocumentation] = None,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
) -> Schema:
    """
    An integer enum.
    """
    return Schema(
        type="integer",
        enum=variants,
        default=default,
        nullable=nullable,
        description=description,
        deprecated=deprecated,
        example=example,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
    )


def boolean_enum(
    variants: List[bool],
    default: Optional[bool] = None,
    nullable: bool = False,
    deprecated: bool = False,
    description: Optional[str] = None,
    example: Optional[Union[int, float]] = None,
    external_docs: Optional[ExternalDocumentation] = None,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
) -> Schema:
    """
    An boolean enum.
    """
    return Schema(
        type="boolean",
        enum=variants,
        default=default,
        nullable=nullable,
        deprecated=deprecated,
        description=description,
        example=example,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
    )


def any(
    description: Optional[str] = None,
    nullable: bool = False,
    external_docs: Optional[ExternalDocumentation] = None,
    deprecated: bool = False,
    title: Optional[str] = None,
    read_only: bool = False,
    write_only: bool = False,
    default: Optional[Any] = None,
    example: Optional[Any] = None,
) -> Schema:
    """
    Any type.
    """
    return Schema(
        nullable=nullable,
        deprecated=deprecated,
        description=description,
        external_docs=external_docs,
        title=title,
        read_only=read_only,
        write_only=write_only,
        default=default,
        example=example,
    )
