import pytest

from functions import bgr2hex


@pytest.mark.parametrize("obj_definition, expected", [
    ((0, 0, 255), "#FF0000"),
    ((0, 255, 0), "#00FF00"),
    ((255, 0, 0), "#0000FF"),
    ((255, 255, 255), "#FFFFFF"),
    ((0, 0, 0), "#000000"),
    ((18, 250, 2), "#02FA12"),
])
def test_hex2bgr(obj_definition, expected):
    assert bgr2hex(obj_definition) == expected


# I'm expecting an error her
@pytest.mark.parametrize("obj_definition, expected", [
    ((0, 0, 894034), "#DA4520000"),
    ((0, 632912, 0), "#009A85000"),
    ((412123, 0, 0), "#0000649DB"),
])
def test_hex2bgr(obj_definition, expected):
    assert bgr2hex(obj_definition) == expected


def test_obj_hex2bgr_invalid_char():
    with pytest.raises(TypeError):
        bgr2hex((0.0))


def test_obj_hex2bgr_invalid_incomplete_color():
    with pytest.raises(TypeError):
        bgr2hex("#FF00")


def test_obj_hex2bgr_invalid_int():
    with pytest.raises(TypeError):
        bgr2hex(True)


def test_obj_hex2bgr_invalid_complex():
    with pytest.raises(TypeError):
        bgr2hex(2 + 3j)
