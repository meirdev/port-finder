import socket

LOCALHOST = "127.0.0.1"

HIGHEST_PORT = 65535


class PortFinderNotFoundError(Exception):
    pass


def port_finder(start: int, end: int = HIGHEST_PORT, host: str = LOCALHOST) -> int:
    if start < 0:
        raise ValueError("start must be greater than 0")

    if end > HIGHEST_PORT:
        raise ValueError(f"end must be less than {HIGHEST_PORT}")

    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind((host, port))
            except socket.error:
                pass
            else:
                return port

    raise PortFinderNotFoundError("No open port found in the given range.")
