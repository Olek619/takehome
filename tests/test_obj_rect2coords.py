import pytest
from functions import obj_rect2coords


@pytest.mark.parametrize("obj_definition, expected", [
    ({'top': 10, 'left': 20, 'width': 30, 'height': 40, 'scaleX': 1, 'scaleY': 1, 'angle': 0}, (10, 20, 30, 40, 0)),
    ({'top': 0, 'left': 0, 'width': 100, 'height': 100, 'scaleX': 2, 'scaleY': 2, 'angle': 90}, (0, 0, 200, 200, 90)),
    ({'top': -5, 'left': -5, 'width': 20, 'height': 20, 'scaleX': 0.5, 'scaleY': 0.5, 'angle': 45},
     (-5, -5, 10, 10, 45)),
    ({'top': 10, 'left': 20, 'width': -30, 'height': -40, 'scaleX': 1, 'scaleY': 1, 'angle': 30},
     (10, 20, -30, -40, 30)),
    ({'top': 10, 'left': 20, 'width': -10, 'height': -10, 'scaleX': 1, 'scaleY': -2, 'angle': 0}, (10, 20, -10, 20, 0)),
    ({'top': 1.2, 'left': 2.9, 'width': 10, 'height': 10, 'scaleX': 1, 'scaleY': 1, 'angle': 180}, (1, 2, 10, 10, 180)),
    ({'top': 1, 'left': 1, 'width': 10, 'height': 10, 'scaleX': 1, 'scaleY': 1, 'angle': 365}, (1, 1, 10, 10, 365)),
])
def test_obj_rect2coords(obj_definition, expected):
    assert obj_rect2coords(obj_definition) == expected


# Test for invalid input (missing keys)
def test_obj_rect2coords_invalid_input():
    with pytest.raises(KeyError):
        obj_rect2coords({'top': 10, 'left': 20, 'width': 30, 'height': 40, 'scaleX': 1, 'angle': 0})


# Test for invalid input (non-numeric values)
def test_obj_rect2coords_non_numeric_input():
    with pytest.raises(ValueError):
        obj_rect2coords({'top': 'abc', 'left': 20, 'width': 30, 'height': 40, 'scaleX': 1, 'scaleY': 1, 'angle': 0})


# Test for invalid input (negative width or height)
def test_obj_rect2coords_empty_dimension():
    with pytest.raises(ValueError):
        obj_rect2coords({'top': '', 'left': 20, 'width': -30, 'height': 40, 'scaleX': 1, 'scaleY': 1, 'angle': 0})
