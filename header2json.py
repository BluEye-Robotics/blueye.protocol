#!/usr/bin/env python3
import re
import os
import json
import struct


def get_struct_info(version):
    PYTYPES = {"uint8_t": "B", "int16_t": "h", "uint16_t": "H",
               "int32_t": "i", "uint32_t": "I", "int64_t": "q",
               "uint64_t": "Q", "float": "f", "double": "d"}

    NPTYPES = {"uint8_t": "<u1",
               "int16_t": "<i2", "uint16_t": "<u2",
               "uint32_t": "<u4", "uint64_t": "<u8",
               "int32_t": "<i4", "int64_t": "<i8",
               "float": "<f4", "double": "<f8"}

    HEADER = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                          "..", "p2_drone", "src",
                                          "node_telecommunication",
                                          "app_protocol.h"))

    with open(HEADER) as file_:
        header_data = file_.read()

    field_names = []
    field_ctypes = []
    field_nptypes = []

    udpstruct = re.search(r"UdpData_%d_1\s*{([^}]*)}" % version, header_data).group(1)
    for line in udpstruct.split("\n"):
        if line.strip().startswith("//"):
            continue
        regex = re.search(r"\s*(\S*)\s*([^\s;]*)", line)
        field_ctype = regex.group(1)
        field_name = regex.group(2)
        if field_name != "" and field_ctype != "":
            field_ctypes.append(field_ctype)
            field_names.append(field_name.split("=")[0])
            field_nptypes.append(NPTYPES[field_ctype])

    struct_str = "<" + "".join([PYTYPES[n] for n in field_ctypes])
    struct_size = struct.Struct(struct_str).size
    return {'struct_str': struct_str, 'struct_size': struct_size,
            'field_names': field_names, 'np_types': field_nptypes}


if __name__ == "__main__":
    data = dict()
    for n in range(1, 3):
        si = get_struct_info(n)
        sil = list(zip(si['field_names'], si['np_types']))
        sid = []
        for s in sil:
            sid.append({'field_name': s[0], 'dtype': s[1],
                        'description': '', 'unit': ''})

        data[n] = sid
    jd = json.dumps(data, sort_keys=True, indent=4)
    with open("protocol.json", "w") as f:
        f.write(jd)
