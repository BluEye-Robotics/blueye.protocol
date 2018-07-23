#!/usr/bin/env python3
import json
import os
protocol_json_path = os.path.join(os.path.dirname(__file__), "protocol.json")

header = "#ifndef _p2_app_protocol_h\n#define _p2_app_protocol_h\n\n"
footer = "#endif"

data = json.loads(open(protocol_json_path).read())

def get_ctype(type_):
    if type_[1:] == 'f4':
        return "float"
    elif type_[1:] == 'f8':
        return "double"
    elif type_[1] == 'i':
        return "int%d_t" % (int(type_[2]) * 8)
    elif type_[1] == 'u':
        return "uint%d_t" % (int(type_[2]) * 8)
    else:
        raise Exception("Unknown format")


code = header

for version in data:
    for message in version['messages']:
        code += "struct __attribute__((__packed__)) P2AppProtocolDataVersion%s%s {\n" % (version['version'], message['name'].title())
        for field in message['fields']:
            init = " = %s" % field['init'] if 'init' in field.keys() else ""
            code += "  %s %s%s; // %s [%s]\n" % (get_ctype(field['dtype']), field['field_name'], init, field['description'], field['unit'])
        code += "};\n\n"

code += footer

with open(os.path.join("c", "p2_app_protocol.h"), "w") as f:
    f.write(code)
