#!/usr/bin/env python3
import socket

import pytest
from blueye.legacyprotocol.exceptions import (
    MismatchedReply,
    NoConnectionToDrone,
    ResponseTimeout,
)


@pytest.fixture
def mocked_socket(mocker):
    return mocker.patch("socket.socket", autospec=True).return_value


@pytest.fixture
def mocked_struct(mocker):
    mocker.patch("struct.unpack", autospec=True)


@pytest.fixture
def mocked_logger(mocker):
    return mocker.patch("logging.Logger", autospec=True).return_value


@pytest.fixture
def tcp_client_v1(mocked_socket, mocked_logger):
    from blueye.legacyprotocol import TcpClient

    tc = TcpClient(protocol_version=1, autoConnect=False)
    tc.connect()
    tc.logger = mocked_logger
    yield tc


@pytest.fixture
def tcp_client_v2(mocked_socket, mocked_logger):
    from blueye.legacyprotocol import TcpClient

    tc = TcpClient(protocol_version=2, autoConnect=False)
    tc.connect()
    tc.logger = mocked_logger
    yield tc


@pytest.fixture(params=["tcp_client_v1", "tcp_client_v2"])
def tcp_client(request):
    """
    TCP client fixture that parametrizes protocol version 1 and 2, tests that use this
    fixture will be run with both protocol version 1 and 2
    """
    return request.getfixturevalue(request.param)


@pytest.mark.parametrize(
    "function_name, expected_message",
    [
        ("auto_heading_on", b"h"),
        ("auto_heading_off", b"H"),
        ("auto_depth_on", b"d"),
        ("auto_depth_off", b"D"),
        ("start_recording", b"r"),
        ("stop_recording", b"R"),
        ("start_compass_calibration", b"i"),
        ("cancel_compass_calibration", b"I"),
        ("save_compass_calibration", b"c"),
    ],
)
def test_commands_produce_correct_message(tcp_client, function_name, expected_message):
    func = getattr(tcp_client, function_name)
    func()
    tcp_client._sock.send.assert_called_with(expected_message)


def test_take_still_picture_produces_correct_message(tcp_client_v2):
    tcp_client_v2.take_still_picture()
    tcp_client_v2._sock.send.assert_called_with(b"s")


@pytest.mark.parametrize(
    "top_lights, bottom_lights, expected_message",
    [(0, 0, b"l\x00\x00"), (50, 50, b"l\x32\x32"), (255, 255, b"l\xff\xff")],
)
def test_set_light_command_produces_correct_message(
    tcp_client, top_lights, bottom_lights, expected_message
):
    tcp_client.set_lights(top_lights, bottom_lights)
    tcp_client._sock.send.assert_called_with(expected_message)


def test_ping_command_produces_correct_message(tcp_client, mocked_socket):
    correct_reply = b"P"
    mocked_socket.recv.return_value = correct_reply
    tcp_client.ping()
    tcp_client._sock.send.assert_called_with(b"p")


def test_exception_raised_on_wrong_reply(tcp_client, mocked_socket):
    mocked_socket.recv.return_value = "wrong reply"
    with pytest.raises(MismatchedReply):
        tcp_client.ping()


@pytest.mark.parametrize(
    "surge_input, sway_input, heave_input, yaw_input, slow_input, boost_input, tilt_speed_input, expected_message",
    [
        (
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            b"J\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
        ),
        (
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            b"J\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?",
        ),
        (
            0.555,
            0.555,
            0.555,
            0.555,
            0.555,
            0.555,
            0.555,
            b"J{\x14\x0e?{\x14\x0e?{\x14\x0e?{\x14\x0e?{\x14\x0e?{\x14\x0e?{\x14\x0e?",
        ),
    ],
)
def test_motion_tilt_command_produces_correct_message(
    tcp_client_v2,
    surge_input,
    sway_input,
    heave_input,
    yaw_input,
    slow_input,
    boost_input,
    tilt_speed_input,
    expected_message,
):
    tcp_client_v2.motion_input_tilt(
        surge_input, sway_input, heave_input, yaw_input, slow_input, boost_input, tilt_speed_input
    )
    tcp_client_v2._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize(
    "out_of_range_input_arguments",
    [
        [0, 0, 0, 0, 0, -1, 0],
        [0, 0, 0, 0, 100, 0, 0],
        [100, 0, 0, 0, 0, 0, 0],
        [100, 0, 0, 0, 100, 0, 0],
        [0, 0, 0, 0, 0, 0, -100],
        [0, 0, 0, 0, 0, 0, 100],
    ],
)
def test_motion_tilt_command_raises_exception_when_input_out_of_range(
    tcp_client_v2, out_of_range_input_arguments
):
    with pytest.raises(ValueError):
        tcp_client_v2.motion_input_tilt(*out_of_range_input_arguments)


@pytest.mark.parametrize(
    "in_range_input_arguments",
    [[0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, 0, 0, -1]],
)
def test_motion_tilt_commmand_does_not_raise_exception_when_input_arguments_are_in_range(
    tcp_client_v2, in_range_input_arguments
):
    tcp_client_v2.motion_input_tilt(*in_range_input_arguments)


@pytest.mark.parametrize(
    "surge_input, sway_input, heave_input, yaw_input, slow_input, boost_input, expected_message",
    [
        (
            0,
            0,
            0,
            0,
            0,
            0,
            b"j\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
        ),
        (
            1,
            1,
            1,
            1,
            1,
            1,
            b"j\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?",
        ),
        (
            0.555,
            0.555,
            0.555,
            0.555,
            0.555,
            0.555,
            b"j{\x14\x0e?{\x14\x0e?{\x14\x0e?{\x14\x0e?{\x14\x0e?{\x14\x0e?",
        ),
    ],
)
def test_motion_command_produces_correct_message(
    tcp_client,
    surge_input,
    sway_input,
    heave_input,
    yaw_input,
    slow_input,
    boost_input,
    expected_message,
):
    tcp_client.motion_input(
        surge_input, sway_input, heave_input, yaw_input, slow_input, boost_input
    )
    tcp_client._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize(
    "out_of_range_input_arguments",
    [
        [0, 0, 0, 0, 0, -1],
        [0, 0, 0, 0, 100, 0],
        [100, 0, 0, 0, 0, 0],
        [100, 0, 0, 0, 100, 0],
    ],
)
def test_motion_command_raises_exception_when_input_out_of_range(
    tcp_client, out_of_range_input_arguments
):
    with pytest.raises(ValueError):
        tcp_client.motion_input(*out_of_range_input_arguments)


@pytest.mark.parametrize(
    "in_range_input_arguments",
    [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, 0, 0]],
)
def test_motion_commmand_does_not_raise_exception_when_input_arguments_are_in_range(
    tcp_client, in_range_input_arguments
):
    tcp_client.motion_input(*in_range_input_arguments)


@pytest.mark.parametrize("out_of_range_input_arguments", [[-10, -10], [300, 300]])
def test_light_command_raises_exception_when_input_out_of_range(
    tcp_client, out_of_range_input_arguments
):
    with pytest.raises(ValueError):
        tcp_client.set_lights(*out_of_range_input_arguments)


@pytest.mark.parametrize("in_range_input_arguments", [[0, 0], [255, 255]])
def test_light_command_does_not_raise_exception_when_input_arguments_are_in_range(
    tcp_client, in_range_input_arguments
):
    tcp_client.set_lights(*in_range_input_arguments)


def test_receive_msg_warns_on_timeout(tcp_client):
    tcp_client._sock.recv.side_effect = socket.timeout
    with pytest.raises(ResponseTimeout):
        tcp_client.receive_msg()
    tcp_client.logger.warning.assert_called_once()


@pytest.mark.parametrize(
    "latitude, longitude, expected_message",
    [
        (0, 0, b"g\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"),
        (10, 10, b"g\x00\x00\x00\x00\x00\x00$@\x00\x00\x00\x00\x00\x00$@"),
    ],
)
def test_user_geo_location_produces_correct_message(
    tcp_client, latitude, longitude, expected_message
):
    tcp_client.user_geo_location(latitude, longitude)
    tcp_client._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize(
    "connection_duration, expected_message", [(1000, b"w\xe8\x03"), (0, b"w\x00\x00")]
)
def test_watchdog_produces_correct_message(tcp_client, connection_duration, expected_message):
    tcp_client.watchdog(connection_duration)
    tcp_client._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize("direction, expected_message", [(-1, b"a\xff\xff"), (1, b"a\x01\x00")])
def test_auto_depth_step_produces_correct_message(tcp_client_v2, direction, expected_message):
    tcp_client_v2.auto_depth_step(direction)
    tcp_client_v2._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize("direction, expected_message", [(-1, b"A\xff\xff"), (1, b"A\x01\x00")])
def test_auto_heading_step_produces_correct_message(tcp_client_v2, direction, expected_message):
    tcp_client_v2.auto_heading_step(direction)
    tcp_client_v2._sock.send.assert_called_with(expected_message)


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
    assert tcp_client._sock.connect.call_count == 4


@pytest.mark.parametrize(
    "system_time, expected_message",
    [(1500, b"t\xdc\x05\x00\x00"), (0, b"t\x00\x00\x00\x00")],
)
def test_set_system_time_produces_correct_message(
    tcp_client, mocked_socket, system_time, expected_message
):
    correct_reply = b"a"
    mocked_socket.recv.return_value = correct_reply
    tcp_client.set_system_time(system_time)
    tcp_client._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize(
    "camera_setting_function, parameter_value, expected_message",
    [
        ("set_camera_exposure", 1000, b"ve\xe8\x03\x00\x00"),
        ("set_camera_whitebalance", 1000, b"vw\xe8\x03\x00\x00"),
        ("set_camera_hue", 1000, b"vh\xe8\x03\x00\x00"),
        ("set_camera_bitrate", 1000, b"vb\xe8\x03\x00\x00"),
    ],
)
def test_camera_setting_functions_v1_produces_correct_messages(
    tcp_client_v1,
    mocked_socket,
    camera_setting_function,
    parameter_value,
    expected_message,
):
    correct_reply = b"a"
    mocked_socket.recv.return_value = correct_reply
    func = getattr(tcp_client_v1, camera_setting_function)
    func(parameter_value)
    tcp_client_v1._sock.send.assert_called_with(expected_message)


@pytest.mark.parametrize(
    "camera_setting_function, parameter_value, expected_message",
    [
        ("set_camera_framerate", 1000, b"vf\xe8\x03\x00\x00"),
        ("set_camera_resolution", 1000, b"vr\xe8\x03\x00\x00"),
    ],
)
def test_camera_setting_functions_v2_produce_correct_messages(
    tcp_client_v2,
    mocked_socket,
    camera_setting_function,
    parameter_value,
    expected_message,
):
    """
    Test that runs the camera setting functions introduced in the second tcp protocol version
    """
    correct_reply = b"a"
    mocked_socket.recv.return_value = correct_reply
    func = getattr(tcp_client_v2, camera_setting_function)
    func(parameter_value)
    tcp_client_v2._sock.send.assert_called_with(expected_message)


def test_get_camera_parameters_produces_correct_message(tcp_client, mocked_socket, mocked_struct):
    tcp_client.get_camera_parameters()
    tcp_client._sock.send.assert_called_with(b"Va")


def test_not_specifying_protocol_results_in_latest_protocol(mocked_socket, mocked_logger):
    from blueye.legacyprotocol import TcpClient

    tc = TcpClient(autoConnect=False)
    assert tc.protocol_version == 2


@pytest.mark.parametrize("density, expected_message", [(0, b"W\x00\x00"), (1000, b"W\xe8\x03")])
def test_set_water_density_produces_correct_message(
    tcp_client_v2, mocked_socket, density, expected_message
):
    tcp_client_v2.set_water_density(density)
    tcp_client_v2._sock.send.assert_called_with(expected_message)
    tcp_client_v2._sock.send.assert_called_with(expected_message)
    tcp_client_v2._sock.send.assert_called_with(expected_message)
