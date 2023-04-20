# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, field
from typing import Any, Dict, Union, Optional, List, Union, Self


@dataclass
class SpecificationExtension:
    extensions: Dict[str, Any] = field(default_factory=dict)
    """Additional properties, names should be prefixed with `x-`."""

    def dump(self) -> Dict[str, Any]:
        return self.extensions


@dataclass
class Callback(SpecificationExtension):
    paths: Dict[str, Union["Reference", "PathItem"]] = field(
        default_factory=dict
    )

    def dump(self) -> Dict[str, Any]:
        """Dumps the callback into a dictionary."""
        data = self.extensions
        data.update({k: v.dump() for k, v in self.paths.items()})

        return data


@dataclass
class Components(SpecificationExtension):
    schemas: Optional[Dict[str, Union["Reference", "Schema"]]] = None
    responses: Optional[Dict[str, Union["Reference", "Response"]]] = None
    parameters: Optional[Dict[str, Union["Reference", "Parameter"]]] = None
    examples: Optional[Dict[str, Union["Reference", "Example"]]] = None
    request_bodies: Optional[
        Dict[str, Union["Reference", "RequestBody"]]
    ] = None
    headers: Optional[Dict[str, Union["Reference", "Header"]]] = None
    security_schemes: Optional[
        Dict[str, Union["Reference", "SecurityScheme"]]
    ] = None
    links: Optional[Dict[str, Union["Reference", "Link"]]] = None
    callbacks: Optional[Dict[str, Union["Reference", "Callback"]]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the components into a dictionary."""
        data = self.extensions
        if self.schemas is not None:
            data["schemas"] = {k: v.dump() for k, v in self.schemas.items()}
        if self.responses is not None:
            data["responses"] = {k: v.dump() for k, v in self.responses.items()}
        if self.parameters is not None:
            data["parameters"] = {
                k: v.dump() for k, v in self.parameters.items()
            }
        if self.examples is not None:
            data["examples"] = {k: v.dump() for k, v in self.examples.items()}
        if self.request_bodies is not None:
            data["requestBodies"] = {
                k: v.dump() for k, v in self.request_bodies.items()
            }
        if self.headers is not None:
            data["headers"] = {k: v.dump() for k, v in self.headers.items()}
        if self.security_schemes is not None:
            data["securitySchemes"] = {
                k: v.dump() for k, v in self.security_schemes.items()
            }
        if self.links is not None:
            data["links"] = {k: v.dump() for k, v in self.links.items()}
        if self.callbacks is not None:
            data["callbacks"] = {k: v.dump() for k, v in self.callbacks.items()}

        return data


@dataclass
class Contact(SpecificationExtension):
    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[str] = None

    def dump(self) -> Dict[str, str]:
        data = self.extensions
        if self.name is not None:
            data["name"] = self.name
        if self.url is not None:
            data["url"] = self.url
        if self.email is not None:
            data["email"] = self.email

        return data


@dataclass
class Discriminator(SpecificationExtension):
    property_name: str = ""
    mapping: Optional[Dict[str, str]] = None

    def dump(self) -> Dict[str, Any]:
        data = self.extensions
        data["propertyName"] = self.property_name
        if self.mapping is not None:
            data["mapping"] = self.mapping

        return data


@dataclass
class Encoding(SpecificationExtension):
    content_type: Optional[str] = None
    headers: Optional[Dict[str, Union["Reference", "Header"]]] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allow_reserved: Optional[bool] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the encoding into a dictionary."""
        data = self.extensions
        if self.content_type is not None:
            data["contentType"] = self.content_type
        if self.headers is not None:
            data["headers"] = {k: v.dump() for k, v in self.headers.items()}
        if self.style is not None:
            data["style"] = self.style
        if self.explode is not None:
            data["explode"] = self.explode
        if self.allow_reserved is not None:
            data["allowReserved"] = self.allow_reserved

        return data


@dataclass
class Example(SpecificationExtension):
    summary: Optional[str] = None
    description: Optional[str] = None
    value: Optional[Any] = None
    external_value: Optional[str] = None

    def __post_init__(self):
        if self.value is not None and self.external_value is not None:
            raise ValueError(
                "Example cannot have both a value and an external value."
            )

    def dump(self) -> Dict[str, Any]:
        """Dumps the example into a dictionary."""
        data = self.extensions
        if self.summary is not None:
            data["summary"] = self.summary
        if self.description is not None:
            data["description"] = self.description
        if self.value is not None:
            data["value"] = str(self.value)
        if self.external_value is not None:
            data["externalValue"] = self.external_value

        return data


@dataclass
class ExternalDocumentation(SpecificationExtension):
    description: Optional[str] = None
    url: str = ""

    def dump(self) -> Dict[str, str]:
        data = self.extensions
        if self.description is not None:
            data["description"] = self.description
        data["url"] = self.url

        return data


@dataclass
class Header(SpecificationExtension):
    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    allow_empty_value: Optional[bool] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allow_reserved: Optional[bool] = None
    schema: Optional["Schema"] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, "Example"]] = None
    content: Optional[Dict[str, "MediaType"]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the header into a dictionary."""
        data = self.extensions
        if self.description is not None:
            data["description"] = self.description
        if self.required is not None:
            data["required"] = self.required
        if self.deprecated is not None:
            data["deprecated"] = self.deprecated
        if self.allow_empty_value is not None:
            data["allowEmptyValue"] = self.allow_empty_value
        if self.style is not None:
            data["style"] = self.style
        if self.explode is not None:
            data["explode"] = self.explode
        if self.allow_reserved is not None:
            data["allowReserved"] = self.allow_reserved
        if self.schema is not None:
            data["schema"] = self.schema.dump()
        if self.example is not None:
            data["example"] = self.example.__str__()
        if self.examples is not None:
            data["examples"] = {k: v.dump() for k, v in self.examples.items()}
        if self.content is not None:
            data["content"] = {k: v.dump() for k, v in self.content.items()}

        return data


@dataclass
class Info(SpecificationExtension):
    title: str = ""
    description: Optional[str] = None
    terms_of_service: Optional[str] = None
    contact: Optional["Contact"] = None
    license: Optional["License"] = None
    version: str = ""

    def dump(self) -> Dict[str, str]:
        data = self.extensions
        data["title"] = self.title
        if self.description is not None:
            data["description"] = self.description
        if self.terms_of_service is not None:
            data["termsOfService"] = self.terms_of_service
        if self.contact is not None:
            data["contact"] = self.contact.dump()
        if self.license is not None:
            data["license"] = self.license.dump()
        data["version"] = self.version

        return data


@dataclass
class License(SpecificationExtension):
    name: str = ""
    url: Optional[str] = None
    identifier: Optional[str] = None

    def __post_init__(self):
        if self.identifier is not None and self.url is not None:
            raise ValueError("License can't have both identifier and url.")

    def dump(self) -> Dict[str, str]:
        data = self.extensions
        data["name"] = self.name
        if self.url is not None:
            data["url"] = self.url
        if self.identifier is not None:
            data["identifier"] = self.identifier

        return data


@dataclass
class Link(SpecificationExtension):
    operation_ref: Optional[str] = None
    operation_id: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    request_body: Optional[Any] = None
    description: Optional[str] = None
    server: Optional["Server"] = None

    def __post_init__(self):
        if self.operation_ref is not None and self.operation_id is not None:
            raise ValueError(
                "Link can't have both operation_ref and operation_id."
            )

    def dump(self) -> Dict[str, Any]:
        """Dumps the link into a dictionary."""
        data = self.extensions
        if self.operation_ref is not None:
            data["operationRef"] = self.operation_ref
        if self.operation_id is not None:
            data["operationId"] = self.operation_id
        if self.parameters is not None:
            data["parameters"] = self.parameters
        if self.request_body is not None:
            data["requestBody"] = self.request_body
        if self.description is not None:
            data["description"] = self.description

        return data


@dataclass
class MediaType(SpecificationExtension):
    schema: Optional[Union["Reference", "Schema"]] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, Union["Reference", "Example"]]] = None
    encoding: Optional[Dict[str, "Encoding"]] = None

    def __post_init__(self):
        if self.examples is not None and self.example is not None:
            raise ValueError("MediaType can't have both examples and example.")

    def dump(self) -> Dict[str, Any]:
        """Dumps the media type into a dictionary."""
        data = self.extensions
        if self.schema is not None:
            data["schema"] = self.schema.dump()
        if self.example is not None:
            data["example"] = self.example.__str__()
        if self.examples is not None:
            data["examples"] = {k: v.dump() for k, v in self.examples.items()}
        if self.encoding is not None:
            data["encoding"] = {k: v.dump() for k, v in self.encoding.items()}

        return data


@dataclass
class OAuthFlow(SpecificationExtension):
    authorization_url: Optional[str] = None
    token_url: Optional[str] = None
    refresh_url: Optional[str] = None
    scopes: Dict[str, str] = field(default_factory=dict)

    def dump(self) -> Dict[str, Any]:
        """Dumps the OAuth flow into a dictionary."""
        data = self.extensions
        if self.authorization_url is not None:
            data["authorizationUrl"] = self.authorization_url
        if self.token_url is not None:
            data["tokenUrl"] = self.token_url
        if self.refresh_url is not None:
            data["refreshUrl"] = self.refresh_url
        if self.scopes is not None:
            data["scopes"] = self.scopes

        return data


@dataclass
class OAuthFlows(SpecificationExtension):
    implicit: Optional["OAuthFlow"] = None
    password: Optional["OAuthFlow"] = None
    client_credentials: Optional["OAuthFlow"] = None
    authorization_code: Optional["OAuthFlow"] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the OAuth flows into a dictionary."""
        data = self.extensions
        if self.implicit is not None:
            data["implicit"] = self.implicit.dump()
        if self.password is not None:
            data["password"] = self.password.dump()
        if self.client_credentials is not None:
            data["clientCredentials"] = self.client_credentials.dump()
        if self.authorization_code is not None:
            data["authorizationCode"] = self.authorization_code.dump()

        return data


@dataclass
class OpenAPI(SpecificationExtension):
    openapi: str = "3.1.0"
    info: "Info" = field(default_factory=Info)
    servers: Optional[List["Server"]] = None
    paths: Dict[str, "PathItem"] = field(default_factory=dict)
    components: Optional["Components"] = None
    security: Optional[List["SecurityRequirement"]] = None
    tags: Optional[List["Tag"]] = None
    external_docs: Optional["ExternalDocumentation"] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the OpenAPI specification into a dictionary."""
        data = self.extensions
        data["openapi"] = self.openapi
        data["info"] = self.info.dump()
        if self.servers is not None:
            data["servers"] = [server.dump() for server in self.servers]
        data["paths"] = {
            path: path_item.dump() for path, path_item in self.paths.items()
        }
        if self.components is not None:
            data["components"] = self.components.dump()
        if self.security is not None:
            data["security"] = [security.dump() for security in self.security]
        if self.tags is not None:
            data["tags"] = [tag.dump() for tag in self.tags]
        if self.external_docs is not None:
            data["externalDocs"] = self.external_docs.dump()

        return data


@dataclass
class Operation(SpecificationExtension):
    tags: Optional[List[str]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    external_docs: Optional["ExternalDocumentation"] = None
    operation_id: Optional[str] = None
    parameters: Optional[List[Union["Reference", "Parameter"]]] = None
    request_body: Optional[Union["Reference", "RequestBody"]] = None
    responses: Dict[str, Union["Reference", "Response"]] = field(
        default_factory=dict
    )
    callbacks: Optional[Dict[str, Union["Reference", "Callback"]]] = None
    deprecated: Optional[bool] = None
    security: Optional[List[Dict[str, List[str]]]] = None
    servers: Optional[List["Server"]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the operation into a dictionary."""
        data = self.extensions
        if self.tags is not None:
            data["tags"] = self.tags
        if self.summary is not None:
            data["summary"] = self.summary
        if self.description is not None:
            data["description"] = self.description
        if self.external_docs is not None:
            data["externalDocs"] = self.external_docs.dump()
        if self.operation_id is not None:
            data["operationId"] = self.operation_id
        if self.parameters is not None:
            data["parameters"] = [
                parameter.dump() for parameter in self.parameters
            ]
        if self.request_body is not None:
            data["requestBody"] = self.request_body.dump()
        data["responses"] = {k: v.dump() for k, v in self.responses.items()}
        if self.callbacks is not None:
            data["callbacks"] = {k: v.dump() for k, v in self.callbacks.items()}
        if self.deprecated is not None:
            data["deprecated"] = self.deprecated
        if self.security is not None:
            data["security"] = self.security
        if self.servers is not None:
            data["servers"] = [server.dump() for server in self.servers]

        return data


@dataclass
class Parameter(SpecificationExtension):
    name: str = ""
    in_: str = ""
    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    allow_empty_value: Optional[bool] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allow_reserved: Optional[bool] = None
    schema: Optional[Union["Reference", "Schema"]] = None
    examples: Optional[Dict[str, Union["Reference", "Example"]]] = None
    example: Optional[Any] = None
    content: Optional[Dict[str, "MediaType"]] = None

    def __post_init__(self) -> None:
        if self.example is not None and self.examples is not None:
            raise ValueError(
                "Parameter cannot have both example and examples defined."
            )

    def dump(self) -> Dict[str, Any]:
        """Dumps the parameter into a dictionary."""
        data = self.extensions
        if self.name is not None:
            data["name"] = self.name
        if self.in_ is not None:
            data["in"] = self.in_
        if self.description is not None:
            data["description"] = self.description
        if self.required is not None:
            data["required"] = self.required
        if self.deprecated is not None:
            data["deprecated"] = self.deprecated
        if self.allow_empty_value is not None:
            data["allowEmptyValue"] = self.allow_empty_value
        if self.style is not None:
            data["style"] = self.style
        if self.explode is not None:
            data["explode"] = self.explode
        if self.allow_reserved is not None:
            data["allowReserved"] = self.allow_reserved
        if self.schema is not None:
            data["schema"] = self.schema.dump()
        if self.examples is not None:
            data["examples"] = {k: v.dump() for k, v in self.examples.items()}
        if self.example is not None:
            data["example"] = str(self.example)
        if self.content is not None:
            data["content"] = {k: v.dump() for k, v in self.content.items()}

        return data


@dataclass
class PathItem(SpecificationExtension):
    summary: Optional[str] = None
    description: Optional[str] = None
    get: Optional["Operation"] = None
    put: Optional["Operation"] = None
    post: Optional["Operation"] = None
    delete: Optional["Operation"] = None
    options: Optional["Operation"] = None
    head: Optional["Operation"] = None
    patch: Optional["Operation"] = None
    trace: Optional["Operation"] = None
    servers: Optional[List["Server"]] = None
    parameters: Optional[List[Union["Reference", "Parameter"]]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the path item into a dictionary."""
        data = self.extensions
        if self.summary is not None:
            data["summary"] = self.summary
        if self.description is not None:
            data["description"] = self.description
        if self.get is not None:
            data["get"] = self.get.dump()
        if self.put is not None:
            data["put"] = self.put.dump()
        if self.post is not None:
            data["post"] = self.post.dump()
        if self.delete is not None:
            data["delete"] = self.delete.dump()
        if self.options is not None:
            data["options"] = self.options.dump()
        if self.head is not None:
            data["head"] = self.head.dump()
        if self.patch is not None:
            data["patch"] = self.patch.dump()
        if self.trace is not None:
            data["trace"] = self.trace.dump()
        if self.servers is not None:
            data["servers"] = [server.dump() for server in self.servers]
        if self.parameters is not None:
            data["parameters"] = [
                parameter.dump() for parameter in self.parameters
            ]

        return data


@dataclass
class Paths(SpecificationExtension):
    paths: Dict[str, "PathItem"] = field(default_factory=dict)

    def dump(self) -> Dict[str, Any]:
        """Dumps the paths into a dictionary."""
        data = self.extensions
        data.update({k: v.dump() for k, v in self.paths.items()})
        return data


@dataclass
class Reference(SpecificationExtension):
    ref: str = ""

    def dump(self) -> Dict[str, Any]:
        data = self.extensions
        data["$ref"] = self.ref

        return data


@dataclass
class RequestBody(SpecificationExtension):
    description: Optional[str] = None
    content: Dict[str, "MediaType"] = field(default_factory=dict)
    required: Optional[bool] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the request body into a dictionary."""
        data = self.extensions
        if self.description is not None:
            data["description"] = self.description
        if self.content is not None:
            data["content"] = {k: v.dump() for k, v in self.content.items()}
        if self.required is not None:
            data["required"] = self.required

        return data


@dataclass
class Response(SpecificationExtension):
    description: str = ""
    headers: Optional[Dict[str, Union["Reference", "Header"]]] = None
    content: Optional[Dict[str, "MediaType"]] = None
    links: Optional[Dict[str, Union["Reference", "Link"]]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the response into a dictionary."""
        data = self.extensions
        data["description"] = self.description
        if self.headers is not None:
            data["headers"] = {k: v.dump() for k, v in self.headers.items()}
        if self.content is not None:
            data["content"] = {k: v.dump() for k, v in self.content.items()}
        if self.links is not None:
            data["links"] = {k: v.dump() for k, v in self.links.items()}
        return data


@dataclass
class Responses(SpecificationExtension):
    responses: Dict[str, Union["Reference", "Response"]] = field(
        default_factory=dict
    )

    def dump(self) -> Dict[str, Any]:
        """Dumps the responses into a dictionary."""
        data = self.extensions
        data["responses"] = {k: v.dump() for k, v in self.responses.items()}
        return data


@dataclass
class Schema(SpecificationExtension):
    title: Optional[str] = None
    multiple_of: Optional[float] = None
    maximum: Optional[float] = None
    exclusive_maximum: Optional[bool] = None
    minimum: Optional[float] = None
    exclusive_minimum: Optional[bool] = None
    max_length: Optional[int] = None
    min_length: Optional[int] = None
    pattern: Optional[str] = None
    max_items: Optional[int] = None
    min_items: Optional[int] = None
    unique_items: Optional[bool] = None
    max_properties: Optional[int] = None
    min_properties: Optional[int] = None
    required: Optional[List[str]] = None
    enum: Optional[List[Any]] = None
    type: Optional[Union[str, List[str]]] = None
    all_of: Optional[List[Union["Reference", Self]]] = None
    one_of: Optional[List[Union["Reference", Self]]] = None
    any_of: Optional[List[Union["Reference", Self]]] = None
    not_: Optional[Union["Reference", Self]] = None
    items: Optional[
        Union["Reference", Self, List[Union["Reference", Self]]]
    ] = None
    properties: Optional[Dict[str, Union["Reference", Self]]] = None
    additional_properties: Optional[Union[bool, "Reference", Self]] = None
    description: Optional[str] = None
    format: Optional[str] = None
    default: Optional[Any] = None
    nullable: Optional[bool] = None
    discriminator: Optional["Discriminator"] = None
    read_only: Optional[bool] = None
    write_only: Optional[bool] = None
    xml: Optional["XML"] = None
    external_docs: Optional["ExternalDocumentation"] = None
    example: Optional[Any] = None
    deprecated: Optional[bool] = None

    def __post_init__(self) -> None:
        """Post init hook."""
        if self.read_only is not None and self.write_only is not None:
            raise ValueError("Cannot be both read-only and write-only.")

    def dump(self) -> Dict[str, Any]:
        """Dumps the schema into a dictionary."""
        data = self.extensions
        if self.title is not None:
            data["title"] = self.title
        if self.multiple_of is not None:
            data["multipleOf"] = self.multiple_of
        if self.maximum is not None:
            data["maximum"] = self.maximum
        if self.exclusive_maximum is not None:
            data["exclusiveMaximum"] = self.exclusive_maximum
        if self.minimum is not None:
            data["minimum"] = self.minimum
        if self.exclusive_minimum is not None:
            data["exclusiveMinimum"] = self.exclusive_minimum
        if self.max_length is not None:
            data["maxLength"] = self.max_length
        if self.min_length is not None:
            data["minLength"] = self.min_length
        if self.pattern is not None:
            data["pattern"] = self.pattern
        if self.max_items is not None:
            data["maxItems"] = self.max_items
        if self.min_items is not None:
            data["minItems"] = self.min_items
        if self.unique_items is not None:
            data["uniqueItems"] = self.unique_items
        if self.max_properties is not None:
            data["maxProperties"] = self.max_properties
        if self.min_properties is not None:
            data["minProperties"] = self.min_properties
        if self.required is not None:
            data["required"] = self.required
        if self.enum is not None:
            data["enum"] = self.enum
        if self.type is not None:
            data["type"] = self.type
        if self.all_of is not None:
            data["allOf"] = [v.dump() for v in self.all_of]
        if self.one_of is not None:
            data["oneOf"] = [v.dump() for v in self.one_of]
        if self.any_of is not None:
            data["anyOf"] = [v.dump() for v in self.any_of]
        if self.not_ is not None:
            data["not"] = self.not_.dump()
        if self.items is not None:
            if isinstance(self.items, list):
                data["items"] = [v.dump() for v in self.items]
            else:
                data["items"] = self.items.dump()
        if self.properties is not None:
            data["properties"] = {
                k: v.dump() for k, v in self.properties.items()
            }
        if self.additional_properties is not None:
            if isinstance(self.additional_properties, bool):
                data["additionalProperties"] = self.additional_properties
            else:
                data["additionalProperties"] = self.additional_properties.dump()
        if self.description is not None:
            data["description"] = self.description
        if self.format is not None:
            data["format"] = self.format
        if self.default is not None:
            data["default"] = self.default
        if self.nullable is not None:
            data["nullable"] = self.nullable
        if self.discriminator is not None:
            data["discriminator"] = self.discriminator.dump()
        if self.read_only is not None:
            data["readOnly"] = self.read_only
        if self.write_only is not None:
            data["writeOnly"] = self.write_only
        if self.xml is not None:
            data["xml"] = self.xml.dump()
        if self.external_docs is not None:
            data["externalDocs"] = self.external_docs.dump()
        if self.example is not None:
            data["example"] = self.example
        if self.deprecated is not None:
            data["deprecated"] = self.deprecated
        return data


@dataclass
class SecurityRequirement(SpecificationExtension):
    security_requirement: Dict[str, List[str]] = field(default_factory=dict)

    def dump(self) -> Dict[str, Any]:
        """Dumps the security requirement into a dictionary."""
        return {**self.extensions, **self.security_requirement}


@dataclass
class SecurityScheme(SpecificationExtension):
    type: str = ""
    description: Optional[str] = None
    name: Optional[str] = None
    in_: Optional[str] = None
    scheme: Optional[str] = None
    bearer_format: Optional[str] = None
    flows: Optional["OAuthFlows"] = None
    open_id_connect_url: Optional[str] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the security scheme into a dictionary."""
        data = self.extensions
        data["type"] = self.type
        if self.description is not None:
            data["description"] = self.description
        if self.name is not None:
            data["name"] = self.name
        if self.in_ is not None:
            data["in"] = self.in_
        if self.scheme is not None:
            data["scheme"] = self.scheme
        if self.bearer_format is not None:
            data["bearerFormat"] = self.bearer_format
        if self.flows is not None:
            data["flows"] = self.flows.dump()
        if self.open_id_connect_url is not None:
            data["openIdConnectUrl"] = self.open_id_connect_url

        return data


@dataclass
class ServerVariable(SpecificationExtension):
    enum: Optional[List[str]] = None
    default: str = ""
    description: Optional[str] = None

    def dump(self) -> Dict[str, Any]:
        data = self.extensions
        if self.enum is not None:
            data["enum"] = self.enum
        data["default"] = self.default
        if self.description is not None:
            data["description"] = self.description

        return data


@dataclass
class Server(SpecificationExtension):
    url: str = ""
    description: Optional[str] = None
    variables: Optional[Dict[str, "ServerVariable"]] = None

    def dump(self) -> Dict[str, Any]:
        data = self.extensions
        data["url"] = self.url
        if self.description is not None:
            data["description"] = self.description
        if self.variables is not None:
            data["variables"] = {k: v.dump() for k, v in self.variables.items()}

        return data


@dataclass
class Tag(SpecificationExtension):
    name: str = ""
    description: Optional[str] = None
    external_docs: Optional["ExternalDocumentation"] = None

    def dump(self) -> Dict[str, Any]:
        data = self.extensions
        data["name"] = self.name
        if self.description is not None:
            data["description"] = self.description
        if self.external_docs is not None:
            data["externalDocs"] = self.external_docs.dump()

        return data


@dataclass
class XML(SpecificationExtension):
    name: Optional[str] = None
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    attribute: Optional[bool] = None
    wrapped: Optional[bool] = None

    def dump(self) -> Dict[str, Any]:
        data = self.extensions
        if self.name is not None:
            data["name"] = self.name
        if self.namespace is not None:
            data["namespace"] = self.namespace
        if self.prefix is not None:
            data["prefix"] = self.prefix
        if self.attribute is not None:
            data["attribute"] = self.attribute
        if self.wrapped is not None:
            data["wrapped"] = self.wrapped

        return data
