#!/usr/bin/env python3
import json
import os
import struct


class AppProtocol:
    STRUCT_CONVERSION = {"<u1": "B", "<i1": "b", "<u2": "H", "<i2": "h",
                         "<u4": "I", "<i4": "i", "<u8": "Q", "<i8": "q",
                         "<f4": "f", "<f8": "d"}

    def __init__(self):
        protocol_json_path = os.path.join(os.path.dirname(__file__), "data", "protocol.json")
        self._jdata = json.loads(open(protocol_json_path).read())
        self._last_version = sorted(self._jdata.keys())[-1]

    def get_json_data(self, packet_type, version=None):
        if version is None:
            version = self._last_version
        try:
            data = self._jdata[str(version)][str(packet_type)]
        except KeyError:
            raise Exception("Version or packet type not present")
        if len([f['dtype'] for f in data if f['dtype'][0] != "<"]) > 0:
            raise ValueError("Endianess not supported")
        return data

    def get_field_names(self, packet_type, version=None):
        return [f['field_name'] for f in self.get_json_data(packet_type, version=version)]

    def get_numpy_field_dtypes(self, packet_type, version=None):
        return [f['dtype'] for f in self.get_json_data(packet_type, version=version)]

    def get_struct_format(self, packet_type, version):
        return "<" + "".join([self.STRUCT_CONVERSION[f] for f in self.get_numpy_field_dtypes(packet_type, version=version)])

    def unpack_data(self, data):
        version = data[0]
        packet_type = data[1]
        return struct.unpack(self.get_struct_format(packet_type, version=version), data)

    def pack_data(self, data):
        version = data[0]
        packet_type = data[1]
        if version is None:
            data = list(data)
            data[0] = int(self._last_version)
        return struct.pack(self.get_struct_format(packet_type, version=version), *data)
