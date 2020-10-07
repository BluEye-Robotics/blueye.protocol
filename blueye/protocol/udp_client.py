#!/usr/bin/env python3

import logging
import socket
import time
import platform

from blueye.protocol import AppProtocol


class UdpClient:
    def __init__(self, port=2010, protocol_description=None, logger=None):
        self._port = port
        self._ip = "0.0.0.0"

        if logger is None:
            # If no logger has been passed we'll use the module logger
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = logger

        self._sock = None

        self._sock = socket.socket(socket.AF_INET,
                                   socket.SOCK_DGRAM)
        # To able to run multiple UdpClients on MacOS one needs to set
        # SO_REUSEPORT, however on Windows that option does not exist,
        # so we use SO_REUSEADDR for Windows and Linux.
        if platform.system() == "Darwin":
            self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        else:
            self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._ap = AppProtocol(protocol_description)
        self.bind()

    def __del__(self):
        self.logger.debug("Closing UDP socket")
        self._sock.close()

    def bind(self):
        self.logger.debug(f"Binding UDP socket to {self._ip}:{self._port}")
        self._sock.bind((self._ip, self._port))

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
