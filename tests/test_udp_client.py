#!/usr/bin/env python3
import json
import socket
import struct
import threading
import time
import unittest
import pytest
from unittest.mock import *

from blueye.protocol import UdpClient

UDP_PORT = 32011

fake_json = json.loads("""
[
    {
        "version": "2",
        "messages": [
            {
                "name": "telemetry",
                "message_type": "1",
                "fields":[
                    {"description": "", "dtype": "<u1", "field_name": "u1-2-v", "unit": ""},
                    {"description": "", "dtype": "<u1", "field_name": "u1-2-t", "unit": ""},
                    {"description": "", "dtype": "<i1", "field_name": "i1-2", "unit": ""},
                    {"description": "", "dtype": "<u2", "field_name": "u2-2", "unit": ""},
                    {"description": "", "dtype": "<i2", "field_name": "i2-2", "unit": ""},
                    {"description": "", "dtype": "<u4", "field_name": "u4-2", "unit": ""},
                    {"description": "", "dtype": "<i4", "field_name": "i4-2", "unit": ""},
                    {"description": "", "dtype": "<u8", "field_name": "u8-2", "unit": ""},
                    {"description": "", "dtype": "<i8", "field_name": "i8-2", "unit": ""},
                    {"description": "", "dtype": "<f4", "field_name": "f4-2", "unit": ""},
                    {"description": "", "dtype": "<f8", "field_name": "f8-2-a", "unit": ""},
                    {"description": "", "dtype": "<f8", "field_name": "f8-2-b", "unit": ""}
                ]
            },
            {
                "name": "telemetry",
                "message_type": "2",
                "fields":[
                    {"description": "", "dtype": "<u1", "field_name": "u1-2-v", "unit": ""},
                    {"description": "", "dtype": "<u1", "field_name": "u1-2-t", "unit": ""},
                    {"description": "", "dtype": "<i1", "field_name": "i1-2", "unit": ""}
                ]
            },
            {
                "name": "telemetry",
                "message_type": "3",
                "fields":[
                    {"description": "", "dtype": "<u1", "field_name": "u1-2-v", "unit": ""},
                    {"description": "", "dtype": "<u1", "field_name": "u1-2-t", "unit": ""},
                    {"description": "", "dtype": "<i2", "field_name": "i1-2", "unit": ""}
                ]
            }
        ]
    }
]
""")


class UDPServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self._stop_loop = False
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._addr = ("127.0.0.1", UDP_PORT)
        self._msg2 = struct.pack("<BBb", 2, 2, 2)
        self._msg3 = struct.pack("<BBh", 2, 3, 3)
        self.start()

    def __del__(self):
        self._socket.close()

    def stop_thread(self):
        self._stop_loop = True
        self.join()

    def run(self):
        for n in range(3):
            if self._stop_loop:
                continue
            self._socket.sendto(self._msg2, self._addr)
            time.sleep(0.01)
        while not self._stop_loop:
            self._socket.sendto(self._msg3, self._addr)
            time.sleep(0.01)


class TestUdpClient(unittest.TestCase):
    def setUp(self):
        pass

    @pytest.mark.timeout(1)
    def test_get_raw_data(self):
        us = UDPServer()
        uc = UdpClient(protocol_description=fake_json, port=UDP_PORT, drone_ip="127.0.0.1")
        data = uc._get_raw_data()
        us.stop_thread()
        self.assertEqual(data, struct.pack("<BBb", 2, 2, 2))

    @pytest.mark.timeout(1)
    def test_get_data(self):
        us = UDPServer()
        uc = UdpClient(protocol_description=fake_json, port=UDP_PORT, drone_ip="127.0.0.1")
        data = uc.get_data()
        us.stop_thread()
        self.assertEqual(data, (2, 2, 2))

    @pytest.mark.timeout(1)
    def test_get_data_t3(self):
        us = UDPServer()
        uc = UdpClient(protocol_description=fake_json, port=UDP_PORT, drone_ip="127.0.0.1")
        data = uc.get_data(packet_type=3)
        us.stop_thread()
        self.assertEqual(data, (2, 3, 3))

    @pytest.mark.timeout(1)
    def test_get_data_dict(self):
        us = UDPServer()
        uc = UdpClient(protocol_description=fake_json, port=UDP_PORT, drone_ip="127.0.0.1")
        data = uc.get_data_dict()
        us.stop_thread()
        self.assertEqual(data, {'u1-2-v': 2, 'u1-2-t': 2, 'i1-2': 2})


if __name__ == '__main__':
    unittest.main()
