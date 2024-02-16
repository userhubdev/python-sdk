import dataclasses
from typing import Any as TypingAny, Dict, Optional


@dataclasses.dataclass
class Any:
    """
    Contains an arbitrary serialized message along with a @type that describes the type of the serialized message.
    """

    #: The type of the serialized message.
    object_type: Optional[str] = None

    def __json_encode__(self) -> Dict[str, TypingAny]:
        data: Dict[str, TypingAny] = {}

        if self.object_type is not None:
            data["@type"] = self.object_type

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, TypingAny]) -> Optional["TypingAny"]:
        if data is None:
            data = {}

        kwargs = {}

        if data.get("@type") is not None:
            kwargs["object_type"] = data["@type"]

        return Any(**kwargs)
