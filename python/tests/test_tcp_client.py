#!/usr/bin/env python3
import pytest
import socket
from p2_app_protocol.exceptions import ResponseTimeout, MismatchedReply, NoConnectionToDrone


@pytest.fixture(scope="session")
def generate_tcp_protocol():
    # This overwrites the current tcp_protocol_class.py
    import generate_tcp_protocol
    context = generate_tcp_protocol.Context()
    generate_tcp_protocol.write_tcp_protocol(context)


@pytest.fixture
def mocked_socket(mocker):
    return mocker.patch('socket.socket', autospec=True).return_value


@pytest.fixture
def mocked_logger(mocker):
    return mocker.patch("logging.Logger", autospec=True).return_value


@pytest.fixture
def tcp_client(mocked_socket, mocked_logger, generate_tcp_protocol):
    from p2_app_protocol import TcpClient
    tc = TcpClient(autoConnect=False)
    tc.connect()
    tc.logger = mocked_logger
    yield tc


@pytest.mark.parametrize('function_name, expected_message', [
    ('auto_heading_on', b'h'),
    ('auto_heading_off', b'H'),
    ('auto_depth_on', b'd'),
    ('auto_depth_off', b'D'),
    ('start_recording', b'r'),
    ('stop_recording', b'R'),
    ('start_compass_calibration', b'i'),
    ('cancel_compass_calibration', b'I'),
    ('save_compass_calibration', b'c')
])
def test_commands_produce_correct_message(tcp_client, function_name, expected_message):
    func = getattr(tcp_client, function_name)
    func()
    tcp_client._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize('top_lights, bottom_lights, expected_message', [
    (0, 0, b'l\x00\x00'),
    (50, 50, b'l\x32\x32'),
    (255, 255, b'l\xFF\xFF')
])
def test_set_light_command_produces_correct_message(tcp_client, top_lights,
                                                    bottom_lights, expected_message):
    tcp_client.set_lights(top_lights, bottom_lights)
    tcp_client._sock.send.assert_called_with(expected_message)


def test_ping_command_produces_correct_message(tcp_client, mocked_socket):
    correct_reply = b'P'
    mocked_socket.recv.return_value = correct_reply
    tcp_client.ping()
    tcp_client._sock.send.assert_called_with(b'p')


def test_exception_raised_on_wrong_reply(tcp_client, mocked_socket):
    mocked_socket.recv.return_value = "wrong reply"
    with pytest.raises(MismatchedReply):
        tcp_client.ping()


@pytest.mark.parametrize('surge_input, sway_input, heave_input, yaw_input, slow_input, boost_input, expected_message', [
    (0, 0, 0, 0, 0, 0, b'j\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
    (1, 1, 1, 1, 1, 1, b'j\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?'),
    (0.555, 0.555, 0.555, 0.555, 0.555, 0.555,
     b'j{\x14\x0e?{\x14\x0e?{\x14\x0e?{\x14\x0e?{\x14\x0e?{\x14\x0e?')

])
def test_motion_command_produces_correct_message(tcp_client, surge_input, sway_input, heave_input, yaw_input, slow_input, boost_input, expected_message):
    tcp_client.motion_input(surge_input, sway_input, heave_input,
                            yaw_input, slow_input, boost_input)
    tcp_client._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize('out_of_range_input_arguments', [
    [0, 0, 0, 0, 0, -1],
    [0, 0, 0, 0, 100, 0],
    [100, 0, 0, 0, 0, 0],
    [100, 0, 0, 0, 100, 0]
])
def test_motion_command_raises_exception_when_input_out_of_range(tcp_client, out_of_range_input_arguments):
    with pytest.raises(ValueError):
        tcp_client.motion_input(*out_of_range_input_arguments)


@pytest.mark.parametrize('in_range_input_arguments', [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [-1, -1, -1, -1, 0, 0]
])
def test_motion_commmand_does_not_raise_exception_when_input_arguments_are_in_range(tcp_client, in_range_input_arguments):
    tcp_client.motion_input(*in_range_input_arguments)


@pytest.mark.parametrize('out_of_range_input_arguments', [
    [-10, -10],
    [300, 300]
])
def test_light_command_raises_exception_when_input_out_of_range(tcp_client, out_of_range_input_arguments):
    with pytest.raises(ValueError):
        tcp_client.set_lights(*out_of_range_input_arguments)


@pytest.mark.parametrize('in_range_input_arguments', [
    [0, 0],
    [255, 255]
])
def test_light_command_does_not_raise_exception_when_input_arguments_are_in_range(tcp_client, in_range_input_arguments):
    tcp_client.set_lights(*in_range_input_arguments)


def test_receive_msg_warns_on_timeout(tcp_client):
    tcp_client._sock.recv.side_effect = socket.timeout
    with pytest.raises(ResponseTimeout):
        tcp_client.receive_msg()
    tcp_client.logger.warning.assert_called_once()


@pytest.mark.parametrize('latitude, longitude, expected_message', [
    (0, 0, b'g\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
    (10, 10, b'g\x00\x00\x00\x00\x00\x00$@\x00\x00\x00\x00\x00\x00$@')
])
def test_user_geo_location_produces_correct_message(tcp_client, latitude, longitude, expected_message):
    tcp_client.user_geo_location(latitude, longitude)
    tcp_client._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize('connection_duration, expected_message', [
    (1000, b'w\xe8\x03'),
    (0, b'w\x00\x00')
])
def test_watchdog_produces_correct_message(tcp_client, connection_duration, expected_message):
    tcp_client.watchdog(connection_duration)
    tcp_client._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize('direction, expected_message', [
    (-1, b'a\xff\xff'),
    (1, b'a\x01\x00')
])
def test_auto_depth_step_produces_correct_message(tcp_client, direction, expected_message):
    tcp_client.auto_depth_step(direction)
    tcp_client._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize('direction, expected_message', [
    (-1, b'A\xff\xff'),
    (1, b'A\x01\x00')
])
def test_auto_heading_step_produces_correct_message(tcp_client, direction, expected_message):
    tcp_client.auto_heading_step(direction)
    tcp_client._sock.send.assert_called_with(expected_message)


def test_connect_logs_error_on_failure(tcp_client):
    tcp_client._sock.connect.side_effect = socket.timeout
    with pytest.raises(NoConnectionToDrone):
        tcp_client.connect()
    tcp_client.logger.error.assert_called_once()


def test_connect_retries_on_failure(tcp_client, mocker):
    tcp_client._sock.connect.side_effect = socket.timeout
    # Resetting call count as connect is called when creating the mock
    tcp_client._sock.connect.call_count = 0
    with pytest.raises(NoConnectionToDrone):
        tcp_client.connect(max_retries=3)
    assert(tcp_client._sock.connect.call_count == 4)


@pytest.mark.parametrize('system_time, expected_message', [
    (1500, b't\xdc\x05\x00\x00'),
    (0, b't\x00\x00\x00\x00')
])
def test_set_system_time_produces_correct_message(tcp_client, mocked_socket, system_time, expected_message):
    correct_reply = b'a'
    mocked_socket.recv.return_value = correct_reply
    tcp_client.set_system_time(system_time)
    tcp_client._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize('camera_parameter, parameter_value, expected_message', [
    (ord('e'), 1000, b've\x00\x00\x00\xe8\x03\x00\x00'),
    (ord('w'), 1000, b'vw\x00\x00\x00\xe8\x03\x00\x00'),
    (ord('h'), 1000, b'vh\x00\x00\x00\xe8\x03\x00\x00'),
    (ord('b'), 1000, b'vb\x00\x00\x00\xe8\x03\x00\x00'),
    (ord('r'), 1000, b'vr\x00\x00\x00\xe8\x03\x00\x00')
])
def test_set_camera_parameter_produces_correct_message(tcp_client, mocked_socket, camera_parameter, parameter_value, expected_message):
    correct_reply = b'a'
    mocked_socket.recv.return_value = correct_reply
    tcp_client.set_camera_parameter(camera_parameter, parameter_value)
    tcp_client._sock.send.assert_called_with(expected_message)
