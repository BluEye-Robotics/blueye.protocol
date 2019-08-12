    def {{name}}(self, {{field_names_string}}):
        command_identifier = b'{{command_type}}'
        msg = command_identifier
        {% if format_string is defined -%}
        msg += struct.pack('{{format_string}}', {{field_names_string}})
        {% endif -%}
        self.send_msg(msg)
        {{'\n'}}
