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

def test_auto_heading_on_message(tcp_client):
    tcp_client.auto_heading_on_command()
    tcp_client._sock.send.assert_called_with(b'h')
