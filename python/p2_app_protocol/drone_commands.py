#!/usr/bin/env python3
import struct

class PioneerCommand:
    @classmethod
    def to_binary(cls, *args):
        # first byte is always a char containing the message type
        format_string = 'c' + cls._format_string
        return struct.pack(format_string, cls._cmd_type.encode('utf-8'), *args)

    @classmethod
    def get_commands(cls):
        return cls.__subclasses__()

class AutoHeadingOnCommand(PioneerCommand):
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


class SetLightCommand(PioneerCommand):
    """
    brightness_upper: uint8 , 0 = lights off, 255 = max lights
    brightness_lower: uint8 , 0 = lights off, 255 = max lights
    """
    _data = ()
    _format_string = 'BB'
    _cmd_type = 'l'

