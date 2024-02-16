import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class EmptyResponse:
    """
    Empty response.
    """

    @staticmethod
    def __json_encode__() -> Dict[str, Any]:
        return {}

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "EmptyResponse":
        return EmptyResponse()
