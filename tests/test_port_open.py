from functions import is_port_open


def test_port_open():
    ip = "www.google.com"
    port = 80
    assert is_port_open(ip, port) == True


def test_port_closed():
    ip = "www.google.com"
    port = 81
    assert is_port_open(ip, port) == False


def test_port_unreachable():
    ip = "nonexistent.example.com"
    port = 80
    assert is_port_open(ip, port) == False


def test_port_incorret_ip():
    ip = "257.168.0.1"
    port = 80
    assert is_port_open(ip, port) == False



def test_negative_port_number():
    ip = "www.google.com"
    port = -1
    assert is_port_open(ip, port) == False


def test_large_port_number():
    ip = "www.google.com"
    port = 65536
    assert is_port_open(ip, port) == False


def test_non_integer_port_number():
    ip = "www.google.com"
    port = "not_a_port"
    assert is_port_open(ip, port) == False


def test_non_bool_port_number():
    ip = "www.google.com"
    port = True
    assert is_port_open(ip, port) == False


def test_non_float_port_number():
    ip = "www.google.com"
    port = 1.12
    assert is_port_open(ip, port) == False
