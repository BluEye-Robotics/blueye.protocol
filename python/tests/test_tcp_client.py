#!/usr/bin/env python3
import pytest
from p2_app_protocol import TcpClient

@pytest.fixture
def mocked_socket(mocker):
    mocker.patch('socket.socket', autospec=True)

@pytest.fixture
def tcp_client(mocked_socket):
    tc = TcpClient()
    tc.connect()
    yield tc

@pytest.mark.parametrize('function_name, expected_message', [
    ('auto_heading_on_command', b'h'),
    ('auto_heading_off_command', b'H'),
    ('auto_depth_on_command', b'd'),
    ('auto_depth_off_command', b'D')
])
def test_commands_produce_correct_message(tcp_client, function_name, expected_message):
    func = getattr(tcp_client, function_name)
    func()
    tcp_client._sock.send.assert_called_with(expected_message)
