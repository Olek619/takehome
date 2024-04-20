from functions import is_port_open


def test_port_open():
    ip = "192.168.0.1"
    port = 80
    assert is_port_open(ip, port) == True


def test_port_closed():
    ip = "192.168.0.1"
    port = 81
    assert is_port_open(ip, port) == False


def test_port_unreachable():
    ip = "277.168.0.1"
    port = 80
    assert is_port_open(ip, port) == False


def test_negative_port_number():
    ip = "192.168.0.1"
    port = -1
    assert is_port_open(ip, port) == False


def test_large_port_number():
    ip = "192.168.0.1"
    port = 65536
    assert is_port_open(ip, port) == False


def test_non_integer_port_number():
    ip = "192.168.0.1"
    port = "not_a_port"
    assert is_port_open(ip, port) == False


def test_non_bool_port_number():
    ip = "192.168.0.1"
    port = True
    assert is_port_open(ip, port) == False


def test_non_float_port_number():
    ip = "192.168.0.1"
    port = 1.12
    assert is_port_open(ip, port) == False
