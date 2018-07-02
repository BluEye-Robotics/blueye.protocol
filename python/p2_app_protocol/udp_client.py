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
    def __init__(self, port=2010):
        self._port = port
        self._ip = "0.0.0.0"
        self._sock = None

        self._sock = socket.socket(socket.AF_INET,
                                   socket.SOCK_DGRAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._ap = AppProtocol()
        self.bind()

    def __del__(self):
        self._sock.close()

    def bind(self):
        try:
            self._sock.bind((self._ip, self._port))
            #info_test("Bind address")
        except socket.error as e:
            info_test(str(e))
            info_test("Please ensure you are in the address range 192.168.1.x")
            return False
        return True

    def _get_raw_data(self):
        data_raw, addr = self._sock.recvfrom(1024)
        return data_raw

    def _get_data(self, packet_type=None, timeout=None):
        start_time = time.time()
        while timeout is None or time.time() < start_time + timeout:
            raw_data = self._get_raw_data()
            data = self._ap.unpack_data(raw_data)
            if packet_type is None or data[1] == packet_type:
                return data
        return None



    """
    def get_data(self, num_packets):
        data = []
        for n in range(num_packets):
            data_raw, addr = self._sock.recvfrom(1024)
            protocol_version = data_raw[0]
            struct_str = get_struct_info(protocol_version)['struct_str']
            struct_size = get_struct_info(protocol_version)['struct_size']
            field_names = get_struct_info(protocol_version)['field_names']
            info_test("received message with length %s" % len(data_raw))
            if len(data_raw) != struct_size:
                info_test("Wrong length - struct: %d data %d" % (struct_size, len(data_raw)))
                return None
            data.append(dict(zip(field_names, struct.unpack(struct_str, data_raw))))
            for key in data[-1].keys():
                print(key, data[-1][key])
            print("\n")
        return data
    """