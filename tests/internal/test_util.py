import pytest

from userhub_sdk._internal import constants, util


@pytest.mark.parametrize(
    ("body", "expected"),
    [
        ("", ""),
        (" ", ""),
        ("ok", ": ok"),
        ("one  two\nthree  ", ": one two three"),
        (
            "x" * constants.SUMMARIZE_BODY_LENGTH,
            ": " + ("x" * constants.SUMMARIZE_BODY_LENGTH),
        ),
        (
            "x" * (constants.SUMMARIZE_BODY_LENGTH + 1),
            ": " + ("x" * constants.SUMMARIZE_BODY_LENGTH) + "...",
        ),
    ],
)
def test_summarize_body(body: str, expected: str):
    assert util.summarize_body(body) == expected
