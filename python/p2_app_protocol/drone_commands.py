#!/usr/bin/env python3
import struct
from dataclasses import dataclass

class PioneerCommand:
    @property
    def to_binary(self):
        # first byte is always a char containing the message type
        format_string = 'c' + self._format_string
        return struct.pack(format_string, self._cmd_type.encode('utf-8'), *self._data)

@dataclass
class LightCommand(PioneerCommand):
    """
    brightness_upper: uint8 , 0 = lights off, 255 = max lights
    brightness_lower: uint8 , 0 = lights off, 255 = max lights
    """
    brightness_upper: int
    brightness_lower: int
    def __post_init__(self):
        self._data = (self.brightness_upper, self.brightness_lower)
        self._format_string = 'BB'
        self._cmd_type = 'l'
