#!/usr/bin/env python3
from __future__ import print_function

__author__ = "Johannes Schrimpf"
__copyright__ = "Copyright (C) 2017 Blueye Robotics AS"
__license__ = "GPL3"
__version__ = "1.0"

import socket
import time
import threading

from drone_commands import LightCommand
info_test = print

class TcpClient(threading.Thread):
    def __init__(self, port=2011, ip="192.168.1.101"):
        threading.Thread.__init__(self)
        self._ip = ip
        self._port = port

        self._sock = None
        self._stop_thread = False
        self.daemon = False

    def __del__(self):
        if self._sock is not None:
            self._sock.close()

    def run(self):
        while not self._stop_thread:
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
            print("Can not send message: No connection!")
            return False
        self._sock.send(msg)

    def ping(self):
        self.send_msg(b"p")
        data = self._sock.recv(1)
        if not data == b"P":
            print("Ping error")
            return False
        return True

    def send_light_cmd(self, light_command):
        self.send_msg(light_command.to_binary)


if __name__ == "__main__":
    tc = TcpClient()
    tc.start()
    tc.connect()
    time.sleep(3)
    tc.stop()

