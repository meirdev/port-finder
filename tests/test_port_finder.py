import socket

import pytest

from port_finder import PortFinderNotFoundError, port_finder


def test_port_finder():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 7980))

        assert port_finder(7980) == 7981


def test_port_finder_not_found():
    with pytest.raises(PortFinderNotFoundError):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(("127.0.0.1", 7980))

            assert port_finder(7980, 7980)


def test_port_invalid_range():
    with pytest.raises(ValueError):
        assert port_finder(-2)

    with pytest.raises(ValueError):
        assert port_finder(5000, 100_000)
