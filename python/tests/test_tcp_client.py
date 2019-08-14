#!/usr/bin/env python3
import pytest

@pytest.fixture(scope="session")
def generate_tcp_protocol():
    # This overwrites the current tcp_protocol_class.py
    import sys
    sys.path.append('../')
    import generate_tcp_protocol
    context = generate_tcp_protocol.Context(path='../')
    generate_tcp_protocol.write_tcp_protocol(context)

@pytest.fixture
def mocked_socket(mocker):
    return mocker.patch('socket.socket', autospec=True).return_value

@pytest.fixture
def tcp_client(mocked_socket, generate_tcp_protocol):
    from p2_app_protocol import TcpClient
    tc = TcpClient()
    tc.connect()
    yield tc

@pytest.mark.parametrize('function_name, expected_message', [
    ('auto_heading_on', b'h'),
    ('auto_heading_off', b'H'),
    ('auto_depth_on', b'd'),
    ('auto_depth_off', b'D'),
    ('start_recording', b'r'),
    ('stop_recording', b'R')
])
def test_commands_produce_correct_message(tcp_client, function_name, expected_message):
    func = getattr(tcp_client, function_name)
    func()
    tcp_client._sock.send.assert_called_with(expected_message)

@pytest.mark.parametrize('top_lights, bottom_lights, expected_reply', [
    (0, 0, b'l\x00\x00'),
    (50, 50, b'l\x32\x32'),
    (255, 255, b'l\xFF\xFF')
])
def test_set_light_command_produces_correct_message(tcp_client, top_lights, bottom_lights, expected_reply):
    tcp_client.set_lights(top_lights, bottom_lights)
    tcp_client._sock.send.assert_called_with(expected_reply)

def test_ping_command_produces_correct_message(tcp_client, mocked_socket):
    correct_reply = b'P'
    mocked_socket.recv.return_value = correct_reply
    tcp_client.ping()
    tcp_client._sock.send.assert_called_with(b'p')

def test_exception_raised_on_wrong_reply(tcp_client, mocked_socket):
    mocked_socket.recv.return_value = "wrong reply"
    with pytest.raises(ValueError):
        tcp_client.ping()
