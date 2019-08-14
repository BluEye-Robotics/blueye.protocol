    def {{name}}(self{% for field in fields %}, {{ field.field_name }}{% endfor %}):
        {% for field in fields %}
        if not {{field.lower_limit}} <= {{field.field_name}} <= {{field.upper_limit}}:
            raise ValueError(
                "Input argument out of range:" +
                " valid range for {{field.field_name}} is" +
                " <{lower_limit}, {upper_limit}>".format(lower_limit={{field.lower_limit}}, upper_limit={{field.upper_limit}}) +
                " but got value: {name}".format(name={{field.field_name}}))

        {% endfor %}
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
