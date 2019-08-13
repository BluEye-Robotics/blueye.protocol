    def {{name}}(self{% for field in fields %}, {{ field.field_name }}{% endfor %}):
        command_identifier = b'{{command_type}}'
        msg = command_identifier
        {% if format_string is defined %}
        msg += struct.pack('{{format_string}}'{% for field in fields %}, {{ field.field_name }}{% endfor %})
        {% endif %}
        try:
            self.send_msg(msg)
            {% if expected_reply is defined %}
            reply = self.receive_msg()
            self.check_reply(reply, b'{{expected_reply}}')
            {% endif %}
        except IOError:
            pass
{{'\n'}}
