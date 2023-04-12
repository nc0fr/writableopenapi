# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Union, Optional
from kind import Kind


@dataclass
class Number(Kind):
    format_: str = ""
    """
    The format of this number.
    """

    is_float: bool = False
    """
    Whether this number is a float.
    """

    is_64: bool = False
    """
    Whether this number is a 64-bit number.
    """

    minimum: Optional[Union[int, float]] = None
    """
    The minimum value of this number.
    """

    maximum: Optional[Union[int, float]] = None
    """
    The maximum value of this number.
    """

    exclusive_minimum: bool = False
    """
    Whether the minimum value is exclusive.
    """

    exclusive_maximum: bool = False
    """
    Whether the maximum value is exclusive.
    """

    multiple_of: Optional[Union[int, float]] = None
    """
    The multiple of value of this number.
    """


@dataclass
class Integer(Number):
    """
    An integer number.
    """

    def __post_init__(self):
        self.is_float = False


@dataclass
class Float(Number):
    """
    A floating number.
    """

    def __post_init__(self):
        self.is_float = True
        self.is_64 = False
        self.format_ = "float"


@dataclass
class Double(Number):
    """
    A double precision floating number.
    """

    def __post_init__(self):
        self.is_64 = True
        self.format_ = "double"
        self.is_float = True


@dataclass
class Int32(Integer):
    """
    A 32-bit integer number.
    """

    def __post_init__(self):
        self.format_ = "int32"
        self.is_64 = False


@dataclass
class Int64(Integer):
    """
    A 64-bit integer number.
    """

    def __post_init__(self):
        self.format_ = "int64"
        self.is_64 = True
