#!/usr/bin/env python3
import struct

class PioneerCommand:
    @classmethod
    def to_binary(cls):
        # first byte is always a char containing the message type
        format_string = 'c' + cls._format_string
        return struct.pack(format_string, cls._cmd_type.encode('utf-8'), *cls._data)

    @classmethod
    def get_commands(cls):
        return cls.__subclasses__()

class AutoHeadingOnCommand(PioneerCommand):
    # Updating only this one for testing static acces to this class from Pioneercommands
    _data = ()
    _format_string = ''
    _cmd_type = 'h'

class AutoHeadingOffCommand(PioneerCommand):
    _data = ()
    _format_string = ''
    _cmd_type = 'H'

class AutoDepthOnCommand(PioneerCommand):
    _data = ()
    _format_string = ''
    _cmd_type = 'd'

class AutoDepthOffCommand(PioneerCommand):
    _data = ()
    _format_string = ''
    _cmd_type = 'D'
