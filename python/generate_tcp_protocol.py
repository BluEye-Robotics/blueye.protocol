#!/usr/bin/env python3

import os
import json
from jinja2 import FileSystemLoader, Environment


PATH = os.path.dirname(os.path.abspath(__file__))
MODULE_PATH = os.path.join(PATH, "p2_app_protocol")
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False, loader=FileSystemLoader(os.path.join(MODULE_PATH, "templates"))
)
OUTPUT_FILE = os.path.join(MODULE_PATH, "tcp_protocol_class.py")


def get_protocol(protocol_path):
    with open(protocol_path) as json_file:
        jdata = json.load(json_file)
        return jdata

STRUCT_CONVERSION = {"<u1": "B", "<i1": "b", "<u2": "H", "<i2": "h",
                         "<u4": "I", "<i4": "i", "<u8": "Q", "<i8": "q",
                         "<f4": "f", "<f8": "d"}
def dtype_to_format_char(dtype):
    return STRUCT_CONVERSION[dtype]

def write_tcp_command_class():
    with open(OUTPUT_FILE, "w") as f:
        protocol_class = TEMPLATE_ENVIRONMENT.get_template("protocol_class_template.py").render()
        f.write(protocol_class)

def write_tcp_send_functions():
    tcp_protocol = get_protocol(os.path.join(MODULE_PATH, "tcp_protocol.json"))[0]
    with open(OUTPUT_FILE, "a") as f:
        for command in tcp_protocol["commands"]:
            template_context = command
            if 'fields' in command:
                field_names_string = ""
                format_string = ""
                for field in command['fields']:
                    field_names_string += f"{field['field_name']}, "
                    format_string += dtype_to_format_char(field['dtype'])
                template_context['format_string'] = format_string
                template_context['field_names_string'] = field_names_string
            python_command = TEMPLATE_ENVIRONMENT.get_template("send_command_function_template.py"
            ).render(command)
            f.write(python_command)

def write_tcp_protocol():
    write_tcp_command_class()
    write_tcp_send_functions()

if __name__ == "__main__":
    write_tcp_protocol()
