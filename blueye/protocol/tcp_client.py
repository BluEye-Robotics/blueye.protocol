#!/usr/bin/env python3
import logging
import socket
import threading
import time

from blueye.protocol.exceptions import (MismatchedReply, NoConnectionToDrone,
                                        ResponseTimeout, SocketNotConnected)


class TcpClientBase(threading.Thread):
    def __init__(self, port=2011, ip="192.168.1.101", maxConnectRetries=0, autoConnect=True):
        threading.Thread.__init__(self)
        self._ip = ip
        self._port = port

        self._sock = None
        self._stop_thread = False
        self.daemon = False
        self.logger = logging.getLogger()
        self.socket_lock = threading.Lock()
        if autoConnect is True:
            self.connect(maxConnectRetries)
            self.start()

    def __del__(self):
        if self._sock is not None:
            self._sock.close()

    def run(self):
        """
        Keeps the TCP connection to the drone alive by sending watchdog commands.
        """
        i = 0
        while not self._stop_thread:
            self.watchdog(i)
            i += 1
            time.sleep(1)

    def connect(self, max_retries=0):
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
            self.logger.error(f"Attempted {max_retries} times, but was unable to connect to drone.")
            raise NoConnectionToDrone(self._ip, self._port)

    def stop(self):
        self._stop_thread = True
        self.join()

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
        try:
            reply = self._sock.recv(size)
            self.logger.debug(f"Reply: {reply}")
            return reply
        except socket.timeout as e:
            self.logger.warning("Timed out while waiting for message reply")
            raise ResponseTimeout from e

    def send_and_receive(self, msg, expects_reply=True, receive_size=1):
        with self.socket_lock:
            self.send_msg(msg)
            if expects_reply:
                reply = self.receive_msg(receive_size)
                return reply
            return 0

    def check_reply(self, reply, expected_reply):
        if not reply == expected_reply:
            raise MismatchedReply(expected_reply, reply)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    tc = TcpClient(maxConnectRetries=3)
    time.sleep(3)
    tc.stop()
