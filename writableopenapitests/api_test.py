# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from ..writableopenapi.macros.shared import *
from ..writableopenapi.macros.types import *
from ..writableopenapi.openapi.v3_1 import *
from ..writableopenapi.utils import into_json, into_yaml, write_file


shared_callback = ReferencableCallback(
    name="callback",
    callback=Callback(
        extensions={
            "x-foo": "bar",
        },
        paths={
            "/pet/findByStatus": PathItem(
                get=Operation(
                    operation_id="findPetsByStatus",
                    parameters=[
                        Parameter(
                            name="status",
                            in_="query",
                            description="Status values that need to be considered for filter",
                            required=True,
                            schema=enum(
                                nullable=False,
                                values=["available", "pending", "sold"],
                                default="available",
                            ),
                        ),
                    ],
                    responses={
                        "200": Response(
                            description="successful operation",
                        ),
                    },
                ),
                post=Operation(
                    operation_id="updatePetWithForm",
                    parameters=[
                        Parameter(
                            name="petId",
                            in_="path",
                            description="ID of pet that needs to be updated",
                            required=True,
                            schema=string(minimum_length=1, maximum_length=100),
                        ),
                    ],
                    responses={
                        "405": Response(
                            description="Invalid input",
                        ),
                    },
                ),
            ),
        },
    ),
)
shared_example = ReferencableExample(
    name="example",
    example=Example(
        value={
            "id": 0,
            "category": {
                "id": 0,
                "name": "string",
            },
            "name": "doggie",
            "photoUrls": [
                "string",
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string",
                },
            ],
            "status": "available",
        },
        summary="An example of a pet",
        description="This is an example of a pet",
        extensions={
            "x-foo": "bar",
        },
    ),
)
shared_header = ReferencableHeader(
    name="header",
    header=Header(
        description="The number of allowed requests in the current period",
        required=True,
        deprecated=True,
        allow_empty_value=True,
        style="simple",
        explode=False,
        allow_reserved=True,
        schema=integer(),
        example=42,
        examples={
            "example1": Example(
                value=42,
                summary="An example of a header",
                description="This is an example of a header",
                extensions={
                    "x-foo": "bar",
                },
            ),
        },
        extensions={
            "x-foo": "bar",
        },
    ),
)
shared_link = ReferencableLink(
    name="link",
    link=Link(
        operation_ref="#/components/operations/putPet",
        parameters={
            "petId": "value1",
            "status": "value2",
        },
        request_body="value3",
        description="A link to the callback",
        server=Server(
            url="http://petstore.swagger.io/v1",
            description="My server",
        ),
    ),
)
shared_parameter = ReferencableParameter(
    name="parameter",
    parameter=Parameter(
        name="petId",
        in_="path",
        description="ID of pet to return",
        required=True,
        deprecated=True,
        allow_empty_value=True,
        style="simple",
        explode=False,
        allow_reserved=True,
        schema=uuid(),
    ),
)
shared_schema = ReferencableSchema(
    name="schema",
    schema=Schema(
        type="object",
        properties={
            "id": uuid(),
            "name": string(),
            "tag": string(),
        },
    ),
)
shared_request_body = ReferencableRequestBody(
    name="request_body",
    request_body=RequestBody(
        description="user to add to the system",
        content={
            "application/json": MediaType(
                schema=shared_schema.ref(),
            )
        },
        required=True,
    ),
)
shared_response = ReferencableResponse(
    name="response",
    response=Response(
        description="A complex object array response",
        content={
            "application/json": MediaType(
                schema=array(
                    items=shared_schema.ref(),
                    minimum_length=1,
                    maximum_length=100,
                ),
            )
        },
        headers={
            "X-Rate-Limit-Limit": shared_header.ref(),
            "X-Rate-Limit-Remaining": shared_header.ref(),
            "X-Rate-Limit-Reset": Header(
                description="The number of allowed requests in the current period",
                required=True,
                deprecated=True,
                allow_empty_value=True,
                style="simple",
                explode=False,
                allow_reserved=True,
                schema=integer(),
            ),
        },
    ),
)
shared_security_scheme = ReferencableSecurityScheme(
    name="security_scheme",
    security_scheme=SecurityScheme(
        type="http",
        scheme="basic",
        bearer_format="JWT",
        flows=OAuthFlows(
            implicit=OAuthFlow(
                authorization_url="http://example.com/api/oauth/dialog",
                refresh_url="http://example.com/api/oauth/token",
                scopes={
                    "write:pets": "modify pets in your account",
                    "read:pets": "read your pets",
                },
            ),
            password=OAuthFlow(
                authorization_url="http://example.com/api/oauth/dialog",
                refresh_url="http://example.com/api/oauth/token",
                scopes={
                    "write:pets": "modify pets in your account",
                    "read:pets": "read your pets",
                },
            ),
            client_credentials=OAuthFlow(
                authorization_url="http://example.com/api/oauth/dialog",
                refresh_url="http://example.com/api/oauth/token",
                scopes={
                    "write:pets": "modify pets in your account",
                    "read:pets": "read your pets",
                },
            ),
            authorization_code=OAuthFlow(
                authorization_url="http://example.com/api/oauth/dialog",
                refresh_url="http://example.com/api/oauth/token",
                scopes={
                    "write:pets": "modify pets in your account",
                    "read:pets": "read your pets",
                },
            ),
        ),
    ),
)


default_external_doc = ExternalDocumentation(
    description="Find out more about our store",
    url="http://example.com",
)

api = OpenAPI(
    openapi="3.1.0",
    info=Info(
        title="My API",
        description="My API description",
        terms_of_service="http://example.com/terms/",
        contact=Contact(
            name="API Support",
            url="http://www.example.com/support",
        ),
        license=License(
            name="Apache 2.0",
            url="http://www.apache.org/licenses/LICENSE-2.0.html",
        ),
        version="1.0.0",
    ),
    servers=[
        Server(
            url="http://petstore.swagger.io/v1",
            description="My server",
            variables={
                "username": ServerVariable(
                    default="demo",
                    description="This value is assigned by the service",
                    enum=["demo", "admin"],
                ),
                "password": ServerVariable(
                    default="demo",
                    description="This value is assigned by the service",
                    enum=["demo", "admin"],
                ),
            },
        )
    ],
    paths={
        "/pets": PathItem(
            delete=Operation(
                operation_id="deletePets",
                tags=["pets"],
                summary="Deletes all pets",
                description="",
                parameters=[
                    shared_parameter.ref(),
                ],
                responses={
                    "200": shared_response.ref(),
                    "400": shared_response.ref(),
                },
                deprecated=False,
            ),
            head=Operation(
                operation_id="getPets",
                tags=["pets"],
                summary="Find pets by status",
                description="Multiple status values can be provided with comma separated strings",
                parameters=[
                    shared_parameter.ref(),
                ],
                responses={
                    "200": shared_response.ref(),
                    "400": shared_response.ref(),
                },
                deprecated=False,
            ),
        ),
        "/pets/{petId}": PathItem(
            get=Operation(
                operation_id="getPetById",
                tags=["pets"],
                summary="Find pet by ID",
                description="Returns a single pet",
                parameters=[
                    shared_parameter.ref(),
                    Parameter(
                        name="status",
                        in_="query",
                        description="Status values that need to be considered for filter",
                        required=True,
                        deprecated=True,
                        allow_empty_value=True,
                        style="simple",
                        explode=False,
                        allow_reserved=True,
                        schema=string(),
                    ),
                ],
                responses={
                    "200": shared_response.ref(),
                    "400": shared_response.ref(),
                    "404": shared_response.ref(),
                },
                deprecated=True,
            ),
        ),
    },
    components=Components(
        callbacks={
            shared_callback.name: shared_callback.callback,
        },
        examples={
            shared_example.name: shared_example.example,
        },
        headers={
            shared_header.name: shared_header.header,
        },
        links={
            shared_link.name: shared_link.link,
        },
        parameters={
            shared_parameter.name: shared_parameter.parameter,
        },
        request_bodies={
            shared_request_body.name: shared_request_body.request_body,
        },
        responses={
            shared_response.name: shared_response.response,
        },
        schemas={
            shared_schema.name: shared_schema.schema,
        },
        security_schemes={
            shared_security_scheme.name: shared_security_scheme.security_scheme,
        },
        extensions={
            "x-foo": "bar",
        },
    ),
    security=[
        SecurityRequirement(
            security_requirement={
                "petstore_auth": ["write:pets", "read:pets"],
            }
        ),
        SecurityRequirement(
            security_requirement={
                "api_key": [],
            }
        ),
    ],
    tags=[
        Tag(
            name="pet",
            description="Everything about your Pets",
            external_docs=default_external_doc,
            extensions={
                "x-foo": "bar",
            },
        ),
        Tag(
            name="store",
            description="Access to Petstore orders",
            external_docs=default_external_doc,
            extensions={
                "x-foo": "bar",
            },
        ),
    ],
    external_docs=default_external_doc,
    extensions={
        "x-foo": "bar",
    },
)

api_json = into_json(api)
api_yaml = into_yaml(api)

write_file(api_json, "openapi.json")
write_file(api_yaml, "openapi.yaml")
