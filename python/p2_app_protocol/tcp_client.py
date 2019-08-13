#!/usr/bin/env python3

__author__ = "Johannes Schrimpf"
__copyright__ = "Copyright (C) 2017 Blueye Robotics AS"
__license__ = "LGPL-3"
__version__ = "1.0"

import socket
import time
import threading

from .tcp_protocol_class import TcpCommands

class TcpClient(threading.Thread, TcpCommands):
    def __init__(self, port=2011, ip="192.168.1.101"):
        threading.Thread.__init__(self)
        self._ip = ip
        self._port = port

        self._sock = None
        self._stop_thread = False
        self.daemon = False

        self.write_lock = threading.Lock()

    def __del__(self):
        if self._sock is not None:
            self._sock.close()

    def run(self):
        while not self._stop_thread:
            # keep drone from disconnecting by pinging
            self.ping()
            time.sleep(0.5)

    def connect(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((self._ip, self._port))
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def stop(self):
        self._stop_thread = True
        self.join()

    def send_msg(self, msg):
        """Send a binary message to the drone

        Args:
            msg (bytes): The message to be sent
        """
        if self._sock is None:
            raise(IOError("Can not send message: No connection!"))
        with self.write_lock:
            print(f"Sent message: {msg}")
            self._sock.send(msg)

    def receive_msg(self):
        reply = self._sock.recv(1)
        print(f"Reply: {reply}")
        return reply

    def check_reply(self, reply, expected_reply):
        if not reply == expected_reply:
                raise ValueError(f"Unexpected reply from drone, expected: {expected_reply}, but got: {reply}")


if __name__ == "__main__":
    tc = TcpClient()
    tc.start()
    tc.connect()
    time.sleep(3)
    tc.stop()
