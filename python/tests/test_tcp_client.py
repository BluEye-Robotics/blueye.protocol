#!/usr/bin/env python3
import pytest
from p2_app_protocol import TcpClient


@pytest.fixture
def mocked_socket(mocker):
    mocker.patch("socket.socket", autospec=True)


@pytest.fixture
def tcp_client(mocked_socket):
    tc = TcpClient()
    tc.connect()
    yield tc


@pytest.mark.parametrize(
    "function_name, expected_message",
    [
        ("auto_heading_on", b"h"),
        ("auto_heading_off", b"H"),
        ("auto_depth_on", b"d"),
        ("auto_depth_off", b"D"),
    ],
)
def test_commands_produce_correct_message(tcp_client, function_name, expected_message):
    func = getattr(tcp_client, function_name)
    func()
    tcp_client._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize(
    "top_lights, bottom_lights, expected_reply",
    [(0, 0, b"l\x00\x00"), (50, 50, b"l\x32\x32"), (255, 255, b"l\xFF\xFF")],
)
def test_set_light_command_produces_correct_message(
    tcp_client, top_lights, bottom_lights, expected_reply
):
    tcp_client.set_light_command(top_lights, bottom_lights)
    tcp_client._sock.send.assert_called_with(expected_reply)
