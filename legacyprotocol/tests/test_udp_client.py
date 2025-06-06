#!/usr/bin/env python3
import json
import struct
import pytest
from unittest.mock import Mock

from blueye.legacyprotocol import UdpClient

UDP_PORT = 32011

fake_json = json.loads(
    """
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
"""
)


@pytest.fixture
def udp_client():
    client = UdpClient(
        protocol_description=fake_json, port=UDP_PORT, drone_ip="127.0.0.1"
    )
    client._sock = Mock()
    recvfrom_side_effect = [
        (struct.pack("<BBb", 2, 2, 2), ("127.0.0.1", UDP_PORT)),
        (struct.pack("<BBh", 2, 3, 3), ("127.0.0.1", UDP_PORT)),
    ]
    client._sock.recvfrom.side_effect = recvfrom_side_effect
    return client


def test_get_raw_data(udp_client):
    data = udp_client._get_raw_data()
    assert data == struct.pack("<BBb", 2, 2, 2)


def test_get_data(udp_client):
    data = udp_client.get_data()
    assert data == (2, 2, 2)


def test_get_data_t3(udp_client):
    data = udp_client.get_data(packet_type=3)
    assert data == (2, 3, 3)


def test_get_data_dict(udp_client):
    data = udp_client.get_data_dict()
    assert data == {"u1-2-v": 2, "u1-2-t": 2, "i1-2": 2}
