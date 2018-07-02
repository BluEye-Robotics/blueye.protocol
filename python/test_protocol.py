#!/usr/bin/env python3
import unittest
from p2_app_protocol import AppProtocol
from unittest.mock import *
import struct

fake_json = """
{
    "1": {
        "1": [
            {"description": "", "dtype": "<u1", "field_name": "u1-1-v", "unit": ""}, 
            {"description": "", "dtype": "<u1", "field_name": "u1-1-t", "unit": ""}, 
            {"description": "", "dtype": "<i1", "field_name": "i1-1", "unit": ""}, 
            {"description": "", "dtype": "<u2", "field_name": "u2-1", "unit": ""}, 
            {"description": "", "dtype": "<i2", "field_name": "i2-1", "unit": ""}, 
            {"description": "", "dtype": "<u4", "field_name": "u4-1", "unit": ""}, 
            {"description": "", "dtype": "<i4", "field_name": "i4-1", "unit": ""}, 
            {"description": "", "dtype": "<u8", "field_name": "u8-1", "unit": ""}, 
            {"description": "", "dtype": "<i8", "field_name": "i8-1", "unit": ""}, 
            {"description": "", "dtype": "<f4", "field_name": "f4-1", "unit": ""}, 
            {"description": "", "dtype": "<f8", "field_name": "f8-1", "unit": ""}
        ]
    },
    "2": {
        "1": [
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
        ],
        "2": [
            {"description": "", "dtype": "<u1", "field_name": "u1-2-v", "unit": ""}, 
            {"description": "", "dtype": "<u1", "field_name": "u1-2-t", "unit": ""}, 
            {"description": "", "dtype": "<i1", "field_name": "i1-2", "unit": ""}
        ]
    }
}
"""

fake_json_endianess = """
{
    "1": {
        "1": [
            {"description": "", "dtype": "<u1", "field_name": "u1-1", "unit": ""}, 
            {"description": "", "dtype": ">i1", "field_name": "i1-1", "unit": ""}, 
            {"description": "", "dtype": "<u2", "field_name": "u2-1", "unit": ""} 
        ]
    }
}"""

class TestAppProtocol(unittest.TestCase):
    def setUp(self):
        pass

    def test_struct(self):
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertEqual(ap.get_struct_format(1, 1), "<BBbHhIiQqfd")

    def test_struct_unpack_v1_t1(self):
        data = (1, 1, 2, 3, 4, 5, 6, 7, 8, 9., 10.)
        data_packet = struct.pack("<BBbHhIiQqfd", *data)
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertEqual(ap.unpack_data(data_packet), data)

    def test_struct_unpack_v2_t1(self):
        data = (2, 1, 2, 3, 4, 5, 6, 7, 8, 9., 10., 11.)
        data_packet = struct.pack("<BBbHhIiQqfdd", *data)
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertEqual(ap.unpack_data(data_packet), data)

    def test_struct_unpack_v2_t2(self):
        data = (2, 2, 2)
        data_packet = struct.pack("<BBb", *data)
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertEqual(ap.unpack_data(data_packet), data)

    def test_struct_pack_v2_t2(self):
        data = (2, 2, 2)
        data_packet = struct.pack("<BBb", *data)
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertEqual(ap.pack_data(data), data_packet)

    def test_struct_pack_None_t2(self):
        data_none = (None, 2, 2)
        data = (2, 2, 2)
        data_packet = struct.pack("<BBb", *data)
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertEqual(ap.pack_data(data_none), data_packet)

    def test_protocol_version_none(self):
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertEqual(ap._last_version, '2')

    def test_wrong_endianess(self):
        with patch('builtins.open', mock_open(read_data=fake_json_endianess)):
            ap = AppProtocol()
            self.assertRaises(ValueError, ap.get_json_data, 1, 1)

    def test_protocol_version_exception(self):
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertRaises(Exception, ap.get_json_data, 1, 0)

    def test_protocol_packet_type_exception(self):
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertRaises(Exception, ap.get_json_data, 0, 1)

    def test_nptypes(self):
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertEqual(ap.get_numpy_field_dtypes(1, 1), ['<u1', '<u1', '<i1', '<u2', '<i2', '<u4', '<i4', '<u8', '<i8', '<f4', '<f8'])

    def test_field_names_v1_t1(self):
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertEqual(ap.get_field_names(1, 1), ['u1-1-v', 'u1-1-t', 'i1-1', 'u2-1', 'i2-1', 'u4-1', 'i4-1', 'u8-1', 'i8-1', 'f4-1', 'f8-1'])

    def test_field_names_v2_t1(self):
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertEqual(ap.get_field_names(1, 2), ['u1-2-v', 'u1-2-t', 'i1-2', 'u2-2', 'i2-2', 'u4-2', 'i4-2', 'u8-2', 'i8-2', 'f4-2', 'f8-2-a', 'f8-2-b'])

    def test_field_names_None_t1(self):
        with patch('builtins.open', mock_open(read_data=fake_json)):
            ap = AppProtocol()
            self.assertEqual(ap.get_field_names(1), ['u1-2-v', 'u1-2-t', 'i1-2', 'u2-2', 'i2-2', 'u4-2', 'i4-2', 'u8-2', 'i8-2', 'f4-2', 'f8-2-a', 'f8-2-b'])


if __name__ == '__main__':
    unittest.main()
