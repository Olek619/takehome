import numpy as np

from functions import draw_edge_locs


def test_draw_edge_locs_valid():
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    edge_locs = [(10, 10), (20, 20), (30, 30)]
    color = (255, 0, 0)
    result = draw_edge_locs(frame, edge_locs, color)
    assert isinstance(result, np.ndarray)


def test_draw_edge_locs_empty_edge_locs():
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    result = draw_edge_locs(frame)
    assert isinstance(result, np.ndarray)


def test_draw_edge_locs_custom_color():
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    edge_locs = [(10, 10), (20, 20), (30, 30)]
    color = (0, 255, 0)
    result = draw_edge_locs(frame, edge_locs, color)
    assert isinstance(result, np.ndarray)
