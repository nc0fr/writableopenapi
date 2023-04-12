# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Optional
from kind import Kind


@dataclass
class String(Kind):
    """
    A string.
    """

    format_: str = ""
    """
    The format of this string.
    """

    minimum_length: Optional[int] = None
    """
    The minimum length of this string.
    """

    maximum_length: Optional[int] = None
    """
    The maximum length of this string.
    """

    pattern: Optional[str] = None
    """
    The pattern of this string. (Regular expression)
    """


@dataclass
class Date(String):
    """
    A date as defined by RFC 3339, section 5.6.
    e.g. 2017-07-21
    """

    def __post_init__(self):
        self.format_ = "date"


@dataclass
class DateTime(String):
    """
    A date time as defined by RFC 3339, section 5.6.
    e.g. 2017-07-21T17:32:28Z
    """

    def __post_init__(self):
        self.format_ = "date-time"


@dataclass
class Password(String):
    """
    A hint to UIs to obscure input.
    e.g. hunter2
    """

    def __post_init__(self):
        self.format_ = "password"


@dataclass
class Byte(String):
    """
    Base64 encoded characters.
    e.g. U3dhZ2dlciByb2Nrcw==
    """

    def __post_init__(self):
        self.format_ = "byte"


@dataclass
class Binary(String):
    """
    Binary data, usually a file.
    e.g. <file contents>
    """

    def __post_init__(self):
        self.format_ = "binary"


@dataclass
class Email(String):
    """
    An email address.
    """

    def __post_init__(self):
        self.format_ = "email"


@dataclass
class UUID(String):
    """
    A UUID.
    """

    def __post_init__(self):
        self.format_ = "uuid"


@dataclass
class UUID3(String):
    """
    A UUID version 3.
    """

    def __post_init__(self):
        self.format_ = "uuid3"
        self.pattern = (
            r"^[0-9a-f]{8}-[0-9a-f]{4}-3[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}$"
        )


@dataclass
class UUID4(String):
    """
    A UUID version 4.
    """

    def __post_init__(self):
        self.format_ = "uuid4"
        self.pattern = (
            r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}$"
        )


@dataclass
class UUID5(String):
    """
    A UUID version 5.
    """

    def __post_init__(self):
        self.format_ = "uuid5"
        self.pattern = (
            r"^[0-9a-f]{8}-[0-9a-f]{4}-5[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}$"
        )


@dataclass
class URI(String):
    """
    A URI.
    """

    def __post_init__(self):
        self.format_ = "uri"


@dataclass
class Hostname(String):
    """
    A hostname.
    """

    def __post_init__(self):
        self.format_ = "hostname"
        self.pattern = r"^[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]$"


@dataclass
class IPv4(String):
    """
    An IPv4 address.
    """

    def __post_init__(self):
        self.format_ = "ipv4"
        self.pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"


@dataclass
class IPv6(String):
    """
    An IPv6 address.
    """

    def __post_init__(self):
        self.format_ = "ipv6"
        self.pattern = r"^[a-fA-F0-9:]+$"


@dataclass
class IRI(String):
    """
    An IRI.
    """

    def __post_init__(self):
        self.format_ = "iri"


@dataclass
class HexColor(String):
    """
    A hex color.
    """

    def __post_init__(self):
        self.format_ = "color"
        self.pattern = r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"


@dataclass
class RegEx(String):
    """
    A regular expression.
    """

    def __post_init__(self):
        self.format_ = "regex"
        self.pattern = r"^\/.*\/$"


@dataclass
class RGB(String):
    """
    An RGB color.
    """

    def __post_init__(self):
        self.format_ = "rgb"
        self.pattern = r"^rgb\(\d{1,3},\d{1,3},\d{1,3}\)$"


@dataclass
class RGBA(String):
    """
    An RGBA color.
    """

    def __post_init__(self):
        self.format_ = "rgba"
        self.pattern = r"^rgba\(\d{1,3},\d{1,3},\d{1,3},\d{1,3}\)$"


@dataclass
class HSL(String):
    """
    An HSL color.
    """

    def __post_init__(self):
        self.format_ = "hsl"
        self.pattern = r"^hsl\(\d{1,3},\d{1,3}%,\d{1,3}%\)$"


@dataclass
class HSLA(String):
    """
    An HSLA color.
    """

    def __post_init__(self):
        self.format_ = "hsla"
        self.pattern = r"^hsla\(\d{1,3},\d{1,3}%,\d{1,3}%,\d{1,3}\)$"


@dataclass
class HSV(String):
    """
    An HSV color.
    """

    def __post_init__(self):
        self.format_ = "hsv"
        self.pattern = r"^hsv\(\d{1,3},\d{1,3}%,\d{1,3}%\)$"


@dataclass
class HSVA(String):
    """
    An HSVA color.
    """

    def __post_init__(self):
        self.format_ = "hsva"
        self.pattern = r"^hsva\(\d{1,3},\d{1,3}%,\d{1,3}%,\d{1,3}\)$"


@dataclass
class CreditCard(String):
    """
    A credit card number.
    """

    def __post_init__(self):
        self.format_ = "credit-card"
        self.pattern = r"^[0-9]{13,16}$"


@dataclass
class ISBN(String):
    """
    An ISBN.
    """

    def __post_init__(self):
        self.format_ = "isbn"
        self.pattern = r"^(?:ISBN(?:-13)?:?●)?(?=[0-9X]{10}$|(?=(?:[0-9]+[-●]){3})[-●0-9X]{13}$)97[89][-●]?(?:[0-9]+[-●]){2}[0-9]+[0-9X]$"


@dataclass
class ISBN10(String):
    """
    An ISBN-10.
    """

    def __post_init__(self):
        self.format_ = "isbn10"
        self.pattern = r"^(?:ISBN(?:-10)?:?●)?(?=[0-9X]{10}$|(?=(?:[0-9]+[-●]){3})[-●0-9X]{13}$)97[89][-●]?(?:[0-9]+[-●]){2}[0-9]+[0-9X]$"


@dataclass
class ISBN13(String):
    """
    An ISBN-13.
    """

    def __post_init__(self):
        self.format_ = "isbn13"
        self.pattern = r"^(?:ISBN(?:-13)?:?●)?(?=[0-9X]{10}$|(?=(?:[0-9]+[-●]){3})[-●0-9X]{13}$)97[89][-●]?(?:[0-9]+[-●]){2}[0-9]+[0-9X]$"


@dataclass
class JSONSchema:
    """
    A JSON Schema.
    """

    def __post_init__(self):
        self.format_ = "json-schema"


@dataclass
class CIDR(String):
    """
    A CIDR.
    """

    def __post_init__(self):
        self.format_ = "cidr"
        self.pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\/(3[0-2]|[12]?[0-9])$"


@dataclass
class CIDRv4(String):
    """
    A CIDRv4.
    """

    def __post_init__(self):
        self.format_ = "cidrv4"
        self.pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\/(3[0-2]|[12]?[0-9])$"


@dataclass
class CIDRv6(String):
    """
    A CIDRv6.
    """

    def __post_init__(self):
        self.format_ = "cidrv6"
        self.pattern = r"^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}\/(12[0-8]|1[01][0-9]|[1-9]?[0-9])$"


@dataclass
class MAC(String):
    """
    A MAC address.
    """

    def __post_init__(self):
        self.format_ = "mac-address"
        self.pattern = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"


@dataclass
class MIME(String):
    """
    A MIME type.
    """

    def __post_init__(self):
        self.format_ = "mime"
        self.pattern = r"^[a-z]+\/[a-z0-9\-\+]+$"


@dataclass
class City(String):
    """
    A city.
    """

    def __post_init__(self):
        self.format_ = "city"
        self.pattern = r"^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$"


@dataclass
class Country(String):
    """
    A country.
    """

    def __post_init__(self):
        self.format_ = "country"
        self.pattern = r"^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$"


@dataclass
class CountryCode(String):
    """
    A country code.
    """

    def __post_init__(self):
        self.format_ = "country-code"
        self.pattern = r"^[a-zA-Z]{2}$"


@dataclass
class Currency(String):
    """
    A currency.
    """

    def __post_init__(self):
        self.format_ = "currency"
        self.pattern = r"^[a-zA-Z]{3}$"


@dataclass
class Language(String):

    """
    A language.
    """

    def __post_init__(self):
        self.format_ = "language"
        self.pattern = r"^[a-zA-Z]{2}$"
