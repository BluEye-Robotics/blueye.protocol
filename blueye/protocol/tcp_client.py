#!/usr/bin/env python3
import logging
import socket
import threading

from blueye.protocol.exceptions import (MismatchedReply, NoConnectionToDrone,
                                        ResponseTimeout, SocketNotConnected)


class TcpClientBase(threading.Thread):
    """A base level TcpClient for communicating with the Blueye Pioneer

    TcpClientBase should not be instantiated on its own. Instead protocol version classes inherit
    the functionality from TcpClientBase, and the combined functionality of a protocol version
    class and TcpClientBase are exposed in the top level class TcpClient.

    TcpClientBase -> TcpclientV1(or other protocol versions) -> TcpClient.

    Example of how to connect to a drone, and toggle the lights
    Example:
    >>> import time
    >>> import blueye.protocol
    >>> tc = blueye.protocol.TcpClient(maxConnectRetries=3)
    >>> tc.set_lights(10, 10)
    >>> time.sleep(3)
    >>> tc.set_lights(0, 0)
    """

    def __init__(
        self,
        port=2011,
        ip="192.168.1.101",
        maxConnectRetries=0,
        autoConnect=True,
        logger=None,
    ):
        threading.Thread.__init__(self)
        self._ip = ip
        self._port = port

        if logger is None:
            # If no logger has been passed we'll use the module logger
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = logger

        self._sock = None
        self.socket_lock = threading.Lock()

        self._exit_flag = threading.Event()
        self.daemon = True

        if autoConnect is True:
            self.connect(maxConnectRetries)
            self.start()

    def run(self):
        """Keep the TCP connection to the drone alive by sending watchdog commands.
        """
        i = 0
        WATCHDOG_DELAY = 1
        while not self._exit_flag.wait(timeout=WATCHDOG_DELAY):
            self.watchdog(i)
            i += 1

    def connect(self, max_retries=0):
        """Connect the TcpClient to the drone

        Args:
            max_retries(int): Make max_retries attempt at connecting to the drone before failing
        """
        attempts = 0
        while attempts <= max_retries:
            try:
                # Creating a new socket for each attempt, as a broken socket should not be reused.
                self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self._sock.settimeout(1.0)
                self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self._sock.connect((self._ip, self._port))
            except socket.timeout:
                self._sock.close()
                attempts += 1
                continue
            break
        else:
            self.logger.error(
                f"Attempted {attempts} time{'' if attempts == 1 else 's'}, "
                "but was unable to connect to drone.")
            raise NoConnectionToDrone(self._ip, self._port)

    def stop(self):
        """Stop the watchdog thread started by run()
        """
        self._exit_flag.set()

    def send_msg(self, msg):
        """Send a binary message to the drone

        Args:
            msg (bytes): The message to be sent
        """
        if self._sock is None:
            raise SocketNotConnected
        self.logger.debug(f"Sent message: {msg}")
        self._sock.send(msg)

    def receive_msg(self, size=1):
        """Receive a binary message from the drone

        Args:
           receive_size (int): The expected byte count of the reply

        Returns:
            reply (bytes): The reply from the drone
        """
        try:
            reply = self._sock.recv(size)
            self.logger.debug(f"Received message: {reply}")
            return reply
        except socket.timeout as e:
            self.logger.warning("Timed out while waiting for message reply")
            raise ResponseTimeout from e

    def send_and_receive(self, msg, expects_reply=True, receive_size=1):
        """Send a binary message and return the drones reply

        Messages that have a reply in the form of data or a ack from the drone
        should be sent using this method to ensure messages send are correctly
        matched up to their replies

        Args:
            msg (bytes): The message to be sent
            expects_reply (bool): True if the message has a expected reply
            receive_size (int): The byte count of the expected reply

        Returns:
            reply (bytes): The reply from the drone
        """
        with self.socket_lock:
            self.send_msg(msg)
            if expects_reply:
                reply = self.receive_msg(receive_size)
                return reply
            return 0

    def check_reply(self, reply, expected_reply):
        """ Check that reply matched expected reply, raise exception if not

        Args:
            reply (str): The reply from the drone
            expected_reply (str): The expected reply from the drone
        """
        if not reply == expected_reply:
            raise MismatchedReply(expected_reply, reply)


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # test examples in docstrings if module run as main
