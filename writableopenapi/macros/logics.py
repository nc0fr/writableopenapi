# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from writableopenapi.openapi import Schema


def one_of(*one_of: Schema) -> Schema:
    """
    A one of.
    """
    return Schema(one_of=[s for s in one_of])


def any_of(*any_of: Schema) -> Schema:
    """
    An any of.
    """
    return Schema(any_of=[s for s in any_of])


def all_of(*all_of: Schema) -> Schema:
    """
    An all of.
    """
    return Schema(all_of=[s for s in all_of])


def not_(not_: Schema) -> Schema:
    """
    A not.
    """
    return Schema(not_=not_)
