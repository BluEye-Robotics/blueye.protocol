#!/usr/bin/env python3

import os
import json
from jinja2 import FileSystemLoader, Environment

def get_protocol(protocol_path):
        with open(protocol_path) as json_file:
            jdata = json.load(json_file)
        return jdata

class Context:
    def __init__(self, path=os.path.dirname(os.path.abspath(__file__))):
        self.path = path
        self.module_path = os.path.join(path, "p2_app_protocol")
        self.template_environment = Environment(autoescape=False, loader=FileSystemLoader(os.path.join(self.module_path, "templates")))
        self.output_file_path = os.path.join(self.module_path, "tcp_protocol_class.py")
        self.tcp_protocol = get_protocol(os.path.join(self.module_path, "tcp_protocol.json"))[0]

def dtype_to_format_char(dtype):
    STRUCT_CONVERSION = {"<u1": "B", "<i1": "b", "<u2": "H", "<i2": "h",
                         "<u4": "I", "<i4": "i", "<u8": "Q", "<i8": "q",
                         "<f4": "f", "<f8": "d"}
    return STRUCT_CONVERSION[dtype]

def write_tcp_command_class(context):
    with open(context.output_file_path, "w") as f:
        protocol_class = context.template_environment.get_template("protocol_class_template.py").render()
        f.write(protocol_class)

def write_tcp_send_functions(context):
    with open(context.output_file_path, "a") as f:
        for command in context.tcp_protocol["commands"]:
            template_context = command
            if 'fields' in command:
                format_string = ""
                for field in command['fields']:
                    format_string += dtype_to_format_char(field['dtype'])
                template_context['format_string'] = format_string
            python_command = context.template_environment.get_template("send_command_function_template.py"
            ).render(command)
            f.write(python_command)

def write_tcp_protocol(context):
    write_tcp_command_class(context)
    write_tcp_send_functions(context)

if __name__ == "__main__":
    context = Context()
    write_tcp_protocol(context)
