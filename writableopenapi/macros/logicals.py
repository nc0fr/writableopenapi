# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import List
from openapi import Schema
from typing_extensions import override
from into import IntoSchema


@dataclass
class OneOf(IntoSchema):
    """
    A one of.
    """

    one_of: List[IntoSchema]
    """
    The one of.
    """

    @override
    def into_schema(self) -> Schema:
        return Schema(one_of=[s.into_schema() for s in self.one_of])


@dataclass
class AnyOf(IntoSchema):
    """
    An any of.
    """

    any_of: List[IntoSchema]
    """
    The any of.
    """

    @override
    def into_schema(self) -> Schema:
        return Schema(any_of=[s.into_schema() for s in self.any_of])


@dataclass
class AllOf(IntoSchema):
    """
    An all of.
    """

    all_of: List[IntoSchema]
    """
    The all of.
    """

    @override
    def into_schema(self) -> Schema:
        return Schema(all_of=[s.into_schema() for s in self.all_of])


@dataclass
class Not(IntoSchema):
    """
    A not.
    """

    not_: IntoSchema
    """
    The not.
    """

    @override
    def into_schema(self) -> Schema:
        return Schema(not_=self.not_.into_schema())


@dataclass
class Any(IntoSchema):
    """
    An any.
    """

    nullable: bool = False

    @override
    def into_schema(self) -> Schema:
        return Schema(
            nullable=self.nullable,
        )
