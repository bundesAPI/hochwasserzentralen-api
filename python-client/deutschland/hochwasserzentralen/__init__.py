# flake8: noqa

"""
    hochwasserzentrale.de API

    Das Länderübergreifendes Hochwasserportal (LHP) bietet auf https://www.hochwasserzentralen.de über die hier dokumentierte API Informationen zur Hochwassersituation in Deutschland an. Betreiber des LHP sind das Bayerische Landesamt für Umwelt (LfU) und die Landesanstalt für Umwelt Baden-Württemberg (LUBW). Die Urheberrechte an den veröffentlichten Daten liegen nach [Auskunft der Betreiber](https://www.hochwasserzentralen.de/impressum) bei der für das jeweilige Bundesland zuständigen Hochwasserzentrale bzw. beim jeweiligen Pegelbetreiber.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


__version__ = "0.1.0"

# import ApiClient
from deutschland.hochwasserzentralen.api_client import ApiClient

# import Configuration
from deutschland.hochwasserzentralen.configuration import Configuration

# import exceptions
from deutschland.hochwasserzentralen.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)