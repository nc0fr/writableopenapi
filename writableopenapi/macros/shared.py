# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from abc import abstractmethod
from dataclasses import dataclass
from typing_extensions import override
from openapi import Schema, Response, Parameter, Example, RequestBody, Header, SecurityScheme, Link, Callback, PathItem, Reference


@dataclass
class Referencable:
    name: str
    """
    The name of this component.
    """

    @abstractmethod
    def ref(self) -> Reference:
        """
        The reference to this component.
        """
        raise NotImplementedError()


@dataclass
class ReferencableSchema(Referencable):
    """
    A shared schema.
    """

    schema: Schema
    """
    The schema.
    """

    @override
    def ref(self) -> Reference:
        return Reference(ref=f"#/components/schemas/{self.name}")


@dataclass
class ReferencableResponse(Referencable):
    """
    A shared response.
    """

    response: Response
    """
    The response.
    """

    @override
    def ref(self) -> Reference:
        return Reference(ref=f"#/components/responses/{self.name}")


@dataclass
class ReferencableParameter(Referencable):
    """
    A shared parameter.
    """

    parameter: Parameter
    """
    The parameter.
    """

    @override
    def ref(self) -> Reference:
        return Reference(ref=f"#/components/parameters/{self.name}")


@dataclass
class ReferencableRequestBody(Referencable):
    """
    A shared request body.
    """

    request_body: RequestBody
    """
    The request body.
    """

    @override
    def ref(self) -> Reference:
        return Reference(ref=f"#/components/requestBodies/{self.name}")


@dataclass
class ReferencableExample(Referencable):
    """
    A shared example.
    """

    example: Example
    """
    The example.
    """

    @override
    def ref(self) -> Reference:
        return Reference(ref=f"#/components/examples/{self.name}")


@dataclass
class ReferencableHeader(Referencable):
    """
    A shared header.
    """

    header: Header
    """
    The header.
    """

    @override
    def ref(self) -> Reference:
        return Reference(ref=f"#/components/headers/{self.name}")


@dataclass
class ReferencableSecurityScheme(Referencable):
    """
    A shared security scheme.
    """

    security_scheme: SecurityScheme
    """
    The security scheme.
    """

    @override
    def ref(self) -> Reference:
        return Reference(ref=f"#/components/securitySchemes/{self.name}")


@dataclass
class ReferencableLink(Referencable):
    """
    A shared link.
    """

    name: str
    """
    The name of this link.
    """

    link: Link
    """
    The link.
    """

    @override
    def ref(self) -> Reference:
        return Reference(ref=f"#/components/links/{self.name}")


@dataclass
class ReferencableCallback(Referencable):
    """
    A shared callback.
    """

    callback: Callback
    """
    The callback.
    """

    @override
    def ref(self) -> Reference:
        return Reference(ref=f"#/components/callbacks/{self.name}")


@dataclass
class ReferencablePathItem(Referencable):
    """
    A shared path item.
    """

    path_item: PathItem
    """
    The path item.
    """

    @override
    def ref(self) -> Reference:
        return Reference(ref=f"#/components/pathItems/{self.name}")
