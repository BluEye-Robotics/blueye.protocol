#!/usr/bin/env python3
import struct

class PioneerCommand:
    @property
    def to_binary(self):
        # first byte is always a char containing the message type
        format_string = 'c' + self._format_string
        return struct.pack(format_string, self._cmd_type.encode('utf-8'), *self._data)

class LightCommand(PioneerCommand):
    """
    brightness_upper: uint8 , 0 = lights off, 255 = max lights
    brightness_lower: uint8 , 0 = lights off, 255 = max lights
    """
    def __init__(self, brightness_upper, brightness_lower):
        self._data = (brightness_upper, brightness_lower)
        self._format_string = 'BB'
        self._cmd_type = 'l'


class AutoDepthOnCommand(PioneerCommand):
    def __init__(self):
        self._data = ()
        self._format_string = ''
        self._cmd_type = 'd'

class AutoDepthOffCommand(PioneerCommand):
    def __init__(self):
        self._data = ()
        self._format_string = ''
        self._cmd_type = 'D'

class AutoHeadingOnCommand(PioneerCommand):
    def __init__(self):
        self._data = ()
        self._format_string = ''
        self._cmd_type = 'h'

class AutoHeadingOffCommand(PioneerCommand):
    def __init__(self):
        self._data = ()
        self._format_string = ''
        self._cmd_type = 'H'
