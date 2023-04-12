# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from openapi import Schema, Response, Parameter, Example, RequestBody, Header, SecurityScheme, Link, Callback, PathItem, Reference


class IntoSchema:
    """
    An object that can be converted into a schema.
    """

    def into_schema(self) -> Schema:
        """
        Convert this object into a schema.
        """
        raise NotImplementedError()


class IntoResponse:
    """
    An object that can be converted into a response.
    """

    def into_response(self) -> Response:
        """
        Convert this object into a response.
        """
        raise NotImplementedError()


class IntoParameter:
    """
    An object that can be converted into a parameter.
    """

    def into_parameter(self) -> Parameter:
        """
        Convert this object into a parameter.
        """
        raise NotImplementedError()


class IntoRequestBody:
    """
    An object that can be converted into a request body.
    """

    def into_request_body(self) -> RequestBody:
        """
        Convert this object into a request body.
        """
        raise NotImplementedError()


class IntoExample:
    """
    An object that can be converted into an example.
    """

    def into_example(self) -> Example:
        """
        Convert this object into an example.
        """
        raise NotImplementedError()


class IntoHeader:
    """
    An object that can be converted into a header.
    """

    def into_header(self) -> Header:
        """
        Convert this object into a header.
        """
        raise NotImplementedError()


class IntoSecurityScheme:
    """
    An object that can be converted into a security scheme.
    """

    def into_security_scheme(self) -> SecurityScheme:
        """
        Convert this object into a security scheme.
        """
        raise NotImplementedError()


class IntoLink:
    """
    An object that can be converted into a link.
    """

    def into_link(self) -> Link:
        """
        Convert this object into a link.
        """
        raise NotImplementedError()


class IntoCallback:
    """
    An object that can be converted into a callback.
    """

    def into_callback(self) -> Callback:
        """
        Convert this object into a callback.
        """
        raise NotImplementedError()


class IntoPathItem:
    """
    An object that can be converted into a path item.
    """

    def into_path_item(self) -> PathItem:
        """
        Convert this object into a path item.
        """
        raise NotImplementedError()


class IntoReference:
    """
    An object that can be converted into a reference.
    """

    def into_reference(self) -> Reference:
        """
        Convert this object into a reference.
        """
        raise NotImplementedError()
