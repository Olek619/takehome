import pytest

from functions import hex2bgr


@pytest.mark.parametrize("obj_definition, expected", [
    ("#FF0000", (0, 0, 255)),
    ("#00FF00", (0, 255, 0)),
    ("#0000FF", (255, 0, 0)),
    ("#FFFFFF", (255, 255, 255)),
    ("#000000", (0, 0, 0)),
    ("#02FA12", (18, 250, 2)),
])
def test_hex2bgr(obj_definition, expected):
    assert hex2bgr(obj_definition) == expected


def test_obj_hex2bgr_invalid_char():
    with pytest.raises(ValueError):
        hex2bgr("#ZZZZZZ")


def test_obj_hex2bgr_invalid_incomplete_color():
    with pytest.raises(ValueError):
        hex2bgr("#FF00")


def test_obj_hex2bgr_invalid_int():
    with pytest.raises(AttributeError):
        hex2bgr(1)


def test_obj_hex2bgr_invalid_bool():
    with pytest.raises(AttributeError):
        hex2bgr(True)


def test_obj_hex2bgr_invalid_float():
    with pytest.raises(AttributeError):
        hex2bgr(1.123)


def test_obj_hex2bgr_invalid_complex():
    with pytest.raises(AttributeError):
        hex2bgr(2 + 3j)

