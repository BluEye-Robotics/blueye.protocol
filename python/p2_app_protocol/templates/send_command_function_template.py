    def {{name}}(self{% for field in fields %}, {{ field.field_name }}{% endfor %}):
        command_identifier = b'{{command_type}}'
        msg = command_identifier
        {% if format_string is defined -%}
        msg += struct.pack('{{format_string}}'{% for field in fields %}, {{ field.field_name }}{% endfor %})
        {% endif -%}
        self.send_msg(msg)
        {{'\n'}}
