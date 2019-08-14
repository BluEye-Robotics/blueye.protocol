class TCPClientException(Exception):
    """Generic exception related to the TCPClient"""


class SocketNotConnected(TCPClientException):
    """Raised when trying to use a socket that is not connected"""


class ResponseTimeout(TCPClientException):
    """Raised when the socket timed out waiting for response to a message"""
