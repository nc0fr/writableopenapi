# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing_extensions import override
from into import IntoSchema, IntoResponse, IntoParameter, IntoRequestBody, IntoExample, IntoHeader, IntoSecurityScheme, IntoLink, IntoCallback, IntoPathItem, IntoReference
from openapi import Schema, Response, Parameter, Example, RequestBody, Header, SecurityScheme, Link, Callback, PathItem, Reference


@dataclass
class SharedSchema(IntoSchema, IntoReference):
    """
    A shared schema.
    """

    name: str
    """
    The name of this schema.
    """

    schema: IntoSchema
    """
    The schema.
    """

    @override
    def into_schema(self) -> Schema:
        return self.schema.into_schema()

    @override
    def into_reference(self) -> Reference:
        return Reference(ref=f"#/components/schemas/{self.name}")


@dataclass
class SharedResponse(IntoResponse, IntoReference):
    """
    A shared response.
    """

    name: str
    """
    The name of this response.
    """

    response: IntoResponse
    """
    The response.
    """

    @override
    def into_response(self) -> Response:
        return self.response.into_response()

    @override
    def into_reference(self) -> Reference:
        return Reference(ref=f"#/components/responses/{self.name}")


@dataclass
class SharedParameter(IntoParameter, IntoReference):
    """
    A shared parameter.
    """

    name: str
    """
    The name of this parameter.
    """

    parameter: IntoParameter
    """
    The parameter.
    """

    @override
    def into_parameter(self) -> Parameter:
        return self.parameter.into_parameter()

    @override
    def into_reference(self) -> Reference:
        return Reference(ref=f"#/components/parameters/{self.name}")


@dataclass
class SharedRequestBody(IntoRequestBody, IntoReference):
    """
    A shared request body.
    """

    name: str
    """
    The name of this request body.
    """

    request_body: IntoRequestBody
    """
    The request body.
    """

    @override
    def into_request_body(self) -> RequestBody:
        return self.request_body.into_request_body()

    @override
    def into_reference(self) -> Reference:
        return Reference(ref=f"#/components/requestBodies/{self.name}")


@dataclass
class SharedExample(IntoExample, IntoReference):
    """
    A shared example.
    """

    name: str
    """
    The name of this example.
    """

    example: IntoExample
    """
    The example.
    """

    @override
    def into_example(self) -> Example:
        return self.example.into_example()

    @override
    def into_reference(self) -> Reference:
        return Reference(ref=f"#/components/examples/{self.name}")


@dataclass
class SharedHeader(IntoHeader, IntoReference):
    """
    A shared header.
    """

    name: str
    """
    The name of this header.
    """

    header: IntoHeader
    """
    The header.
    """

    @override
    def into_header(self) -> Header:
        return self.header.into_header()

    @override
    def into_reference(self) -> Reference:
        return Reference(ref=f"#/components/headers/{self.name}")


@dataclass
class SharedSecurityScheme(IntoSecurityScheme, IntoReference):
    """
    A shared security scheme.
    """

    name: str
    """
    The name of this security scheme.
    """

    security_scheme: IntoSecurityScheme
    """
    The security scheme.
    """

    @override
    def into_security_scheme(self) -> SecurityScheme:
        return self.security_scheme.into_security_scheme()

    @override
    def into_reference(self) -> Reference:
        return Reference(ref=f"#/components/securitySchemes/{self.name}")


@dataclass
class SharedLink(IntoLink, IntoReference):
    """
    A shared link.
    """

    name: str
    """
    The name of this link.
    """

    link: IntoLink
    """
    The link.
    """

    @override
    def into_link(self) -> Link:
        return self.link.into_link()

    @override
    def into_reference(self) -> Reference:
        return Reference(ref=f"#/components/links/{self.name}")


@dataclass
class SharedCallback(IntoCallback, IntoReference):
    """
    A shared callback.
    """

    name: str
    """
    The name of this callback.
    """

    callback: IntoCallback
    """
    The callback.
    """

    @override
    def into_callback(self) -> Callback:
        return self.callback.into_callback()

    @override
    def into_reference(self) -> Reference:
        return Reference(ref=f"#/components/callbacks/{self.name}")


@dataclass
class SharedPathItem(IntoPathItem, IntoReference):
    """
    A shared path item.
    """

    name: str
    """
    The name of this path item.
    """

    path_item: IntoPathItem
    """
    The path item.
    """

    @override
    def into_path_item(self) -> PathItem:
        return self.path_item.into_path_item()

    @override
    def into_reference(self) -> Reference:
        return Reference(ref=f"#/components/pathItems/{self.name}")
