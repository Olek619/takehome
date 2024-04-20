import numpy as np
import pytest

from functions import compute_affine


@pytest.fixture
def valid_input():
    obj_definition = {'top': 10, 'left': 10, 'width': 20, 'height': 20, 'scaleX': 1, 'scaleY': 1, 'angle': 45}
    dsize = (200, 200)
    frame_affine_matrix = np.eye(3)
    return obj_definition, dsize, frame_affine_matrix


def test_valid_input(valid_input):
    obj_definition, dsize, frame_affine_matrix = valid_input
    result = compute_affine(obj_definition, dsize, frame_affine_matrix)
    assert isinstance(result, np.ndarray)


@pytest.mark.parametrize("scaleX, scaleY", [(2, 1.5), (1, 2), (0.5, 0.5)])
def test_scaling(valid_input, scaleX, scaleY):
    obj_definition, dsize, frame_affine_matrix = valid_input
    obj_definition['scaleX'] = scaleX
    obj_definition['scaleY'] = scaleY
    result = compute_affine(obj_definition, dsize, frame_affine_matrix)
    assert isinstance(result, np.ndarray)


@pytest.mark.parametrize("dsize", [(100, 100), (300, 300), (500, 200)])
def test_different_dsize(valid_input, dsize):
    obj_definition, _, frame_affine_matrix = valid_input
    result = compute_affine(obj_definition, dsize, frame_affine_matrix)
    assert isinstance(result, np.ndarray)


@pytest.mark.parametrize("frame_affine_matrix", [np.eye(3), np.zeros((3, 3)), np.ones((3, 3))])
def test_different_frame_affine_matrix(valid_input, frame_affine_matrix):
    obj_definition, dsize, _ = valid_input
    result = compute_affine(obj_definition, dsize, frame_affine_matrix)
    assert isinstance(result, np.ndarray)


def test_non_numeric_frame_affine_matrix(valid_input):
    obj_definition, dsize, _ = valid_input
    frame_affine_matrix = np.array([[1, 'a', 0], [0, 1, 0], [0, 0, 1]])
    with pytest.raises(TypeError):
        compute_affine(obj_definition, dsize, frame_affine_matrix)


def test_invalid_shape_frame_affine_matrix(valid_input):
    obj_definition, dsize, _ = valid_input
    frame_affine_matrix = np.zeros((2, 2))
    with pytest.raises(ValueError):
        compute_affine(obj_definition, dsize, frame_affine_matrix)


@pytest.mark.parametrize("missing_key", ['top', 'left', 'width', 'height', 'angle'])
def test_missing_keys(valid_input, missing_key):
    obj_definition, dsize, frame_affine_matrix = valid_input
    del obj_definition[missing_key]
    with pytest.raises(KeyError):
        compute_affine(obj_definition, dsize, frame_affine_matrix)

