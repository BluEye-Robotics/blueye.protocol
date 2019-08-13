import struct

class TcpBaseClient:
    def auto_heading_on(self):
        command_identifier = b'h'
        msg = command_identifier
        self.send_msg(msg)
        
    def auto_heading_off(self):
        command_identifier = b'H'
        msg = command_identifier
        self.send_msg(msg)
        
    def auto_depth_on(self):
        command_identifier = b'd'
        msg = command_identifier
        self.send_msg(msg)
        
    def auto_depth_off(self):
        command_identifier = b'D'
        msg = command_identifier
        self.send_msg(msg)
        
    def set_lights(self, brightness_upper, brightness_lower):
        command_identifier = b'l'
        msg = command_identifier
        msg += struct.pack('BB', brightness_upper, brightness_lower)
        self.send_msg(msg)
        
