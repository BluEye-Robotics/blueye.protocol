#!/usr/bin/env python3

__author__ = "Johannes Schrimpf"
__copyright__ = "Copyright (C) 2017 Blueye Robotics AS"
__license__ = "GPL3"
__version__ = "1.0"

import socket
import time
from .protocol import AppProtocol

info_test = print

class UdpClient:
    def __init__(self, port=2010, protocol_description=None):
        self._port = port
        self._ip = "0.0.0.0"
        self._sock = None

        self._sock = socket.socket(socket.AF_INET,
                                   socket.SOCK_DGRAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._ap = AppProtocol(protocol_description)
        self.bind()

    def __del__(self):
        self._sock.close()

    def bind(self):
        try:
            self._sock.bind((self._ip, self._port))
            #info_test("Bind address")
        except socket.error as e:
            info_test(str(e))
            return False
        return True

    def _get_raw_data(self):
        data_raw, addr = self._sock.recvfrom(1024)
        return data_raw

    def get_data(self, packet_type=None, timeout=None):
        start_time = time.time()
        while timeout is None or time.time() < start_time + timeout:
            raw_data = self._get_raw_data()
            data = self._ap.unpack_data(raw_data)
            if packet_type is None or data[1] == packet_type:
                return data
        return None

    def get_data_dict(self, packet_type=None, timeout=None):
        start_time = time.time()
        while timeout is None or time.time() < start_time + timeout:
            raw_data = self._get_raw_data()
            data = self._ap.unpack_data_dict(raw_data)
            if packet_type is None or data["command_type"] == packet_type:
                return data
        return None
