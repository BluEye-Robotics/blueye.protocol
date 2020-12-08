class TCPClientException(Exception):
    """Generic exception related to the TCPClient"""


class SocketNotConnected(TCPClientException):
    """Raised when trying to use a socket that is not connected"""


class ResponseTimeout(TCPClientException):
    """Raised when the socket timed out waiting for response to a message"""


class MismatchedReply(TCPClientException, ValueError):
    """Raised when the TCP Client receives an unexpected reply from the drone"""

    def __init__(self, expected_reply, actual_reply):
        self.expected_reply = expected_reply
        self.actual_reply = actual_reply
        TCPClientException.__init__(self, ("Unexpected reply from drone, expected: " +
                                           f"{expected_reply}, but got: {actual_reply}"))


class NoConnectionToDrone(TCPClientException):
    """Raised if the TCP Client is unable to establish a connection to the drone"""

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        TCPClientException.__init__(self, f"Unable to connect to drone at {ip}:{port}")
