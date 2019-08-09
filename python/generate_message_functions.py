#!/usr/bin/env python3

import os
import json
from jinja2 import FileSystemLoader, Environment


PATH = os.path.dirname(os.path.abspath(__file__))
MODULE_PATH = os.path.join(PATH, "p2_app_protocol")
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False, loader=FileSystemLoader(os.path.join(MODULE_PATH, "templates"))
)


def get_protocol(protocol_path):
    with open(protocol_path) as json_file:
        jdata = json.load(json_file)
        return jdata


def write_function():
    tcp_protocol = get_protocol(os.path.join(MODULE_PATH, "tcp_protocol.json"))[0]
    file_name = os.path.join(MODULE_PATH, "message_methods.py")
    with open(file_name, "w") as f:
        for command in tcp_protocol["commands"]:
            command_type = command["command_type"]
            python_command = TEMPLATE_ENVIRONMENT.get_template(
                "send_command_function_template.py"
            ).render(command)
            f.write(python_command)


if __name__ == "__main__":
    write_function()
