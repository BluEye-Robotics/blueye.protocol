def auto_heading_on(self):
   command_identifier = b'h'
   self.send_msg(command_identifier)

def auto_heading_off(self):
   command_identifier = b'H'
   self.send_msg(command_identifier)

def auto_depth_on(self):
   command_identifier = b'd'
   self.send_msg(command_identifier)

def auto_depth_off(self):
   command_identifier = b'D'
   self.send_msg(command_identifier)

