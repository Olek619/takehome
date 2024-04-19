from functions import obj_rect2coords, compute_affine


def test_obj_rect2coords_positive():
    obj_definition = {'top': 5, 'left': 10, 'width': 15, 'height': 20, 'scaleX': 2, 'scaleY': 3.5, 'angle': 90}
    expected_result = (5, 10, 30, 70, 90)
    result = obj_rect2coords(obj_definition)
    assert result == expected_result


def test_obj_rect2coords_zero():
    obj_definition = {'top': 0, 'left': 0, 'width': 1, 'height': 1, 'scaleX': 0, 'scaleY': 0, 'angle': 0}
    expected_result = (0, 0, 0, 0, 0)
    result = obj_rect2coords(obj_definition)
    assert result == expected_result


def test_obj_rect2coords_negative():
    obj_definition = {'top': -1, 'left': -2, 'width': -3, 'height': -4, 'scaleX': -2, 'scaleY': 2,
                      'angle': -66}
    expected_result = (-1, -2, 6, -8, -66)
    result = obj_rect2coords(obj_definition)
    assert result == expected_result


def test_obj_rect2coords_string():
    obj_definition = {'top': '1', 'left': '2', 'width': -3, 'height': -4, 'scaleX': 2, 'scaleY': 2,
                      'angle': -66}
    expected_result = (1, 2, -6, -8, -66)
    result = obj_rect2coords(obj_definition)
    assert result == expected_result


def test_obj_rect2coords_bool():
    obj_definition = {'top': True, 'left': False, 'width': -3, 'height': -4, 'scaleX': -1.5, 'scaleY': 2.0,
                      'angle': -66}
    expected_result = (1, 0, 4, -8, -66)
    result = obj_rect2coords(obj_definition)
    assert result == expected_result
