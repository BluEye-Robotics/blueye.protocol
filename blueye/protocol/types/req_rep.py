# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from blueye.protocol.types import message_formats


__protobuf__ = proto.module(
    package='blueye.protocol',
    manifest={
        'SetOverlayParametersReq',
        'SetOverlayParametersRep',
        'GetOverlayParametersReq',
        'GetOverlayParametersRep',
        'SetCameraParametersReq',
        'SetCameraParametersRep',
        'GetCameraParametersReq',
        'GetCameraParametersRep',
        'SyncTimeReq',
        'SyncTimeRep',
        'PingReq',
        'PingRep',
        'SetThicknessGaugeParametersReq',
        'SetThicknessGaugeParametersRep',
        'ConnectClientReq',
        'ConnectClientRep',
        'DisconnectClientReq',
        'DisconnectClientRep',
    },
)


class SetOverlayParametersReq(proto.Message):
    r"""-

    Request to set video overlay parameters.

    Attributes:
        overlay_parameters (blueye.protocol.types.OverlayParameters):
            The video overlay parameters to apply.
    """

    overlay_parameters = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.OverlayParameters,
    )


class SetOverlayParametersRep(proto.Message):
    r"""-

    Response after setting video overlay parameters.
    """


class GetOverlayParametersReq(proto.Message):
    r"""-

    Request to get currently set video overlay parameters.
    """


class GetOverlayParametersRep(proto.Message):
    r"""-

    Response with the currently set video overlay parameters.

    Attributes:
        overlay_parameters (blueye.protocol.types.OverlayParameters):
            The currently set overlay parameters.
    """

    overlay_parameters = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.OverlayParameters,
    )


class SetCameraParametersReq(proto.Message):
    r"""-

    Request to set camera parameters.

    Attributes:
        camera_parameters (blueye.protocol.types.CameraParameters):
            The camera parameters to apply.
    """

    camera_parameters = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.CameraParameters,
    )


class SetCameraParametersRep(proto.Message):
    r"""-

    Response after setting the camera parameters.
    """


class GetCameraParametersReq(proto.Message):
    r"""-

    Request to get the currently set camera parameters.

    Attributes:
        camera (blueye.protocol.types.Camera):
            Which camera to read camera parameters from.
    """

    camera = proto.Field(proto.ENUM, number=1,
        enum=message_formats.Camera,
    )


class GetCameraParametersRep(proto.Message):
    r"""-

    Response with the currently set camera parameters.

    Attributes:
        camera_parameters (blueye.protocol.types.CameraParameters):
            The currently set camera parameters.
    """

    camera_parameters = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.CameraParameters,
    )


class SyncTimeReq(proto.Message):
    r"""-

    Request to set the system time on the drone.

    Attributes:
        time (blueye.protocol.types.SystemTime):
            The time to set on the drone.
    """

    time = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.SystemTime,
    )


class SyncTimeRep(proto.Message):
    r"""-

    Response after setting the system time on the drone.

    Attributes:
        success (bool):
            If the time was set successfully.
    """

    success = proto.Field(proto.BOOL, number=1)


class PingReq(proto.Message):
    r"""-

    The simplest message to use to test request/reply communication with
    the drone.

    The drone replies with a PingRep message immediately after receiving
    the PingReq.
    """


class PingRep(proto.Message):
    r"""-

    Response message from a PingReq request.
    """


class SetThicknessGaugeParametersReq(proto.Message):
    r"""-

    Request to set parameters for ultrasonic thickness gauge.

    The sound velocity is used to calculate the thickness of the
    material being measured.

    Attributes:
        sound_velocity (int):
            Sound velocity in m/s
    """

    sound_velocity = proto.Field(proto.UINT32, number=1)


class SetThicknessGaugeParametersRep(proto.Message):
    r"""-

    Response after setting thicknes gauge parameters.
    """


class ConnectClientReq(proto.Message):
    r"""-

    Connect a new client to the drone.

    Attributes:
        client_info (blueye.protocol.types.ClientInfo):
            Information about the client connecting to
            the drone.
    """

    client_info = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.ClientInfo,
    )


class ConnectClientRep(proto.Message):
    r"""-

    Response after connecting a client to the drone.

    Contains information about which client is in control, and a list of
    all connected clients.

    Attributes:
        client_id (int):
            The assigned ID of this client.
        client_id_in_control (int):
            The ID of the client in control of the drone.
        connected_clients (Sequence[blueye.protocol.types.ConnectedClient]):
            List of connected clients.
    """

    client_id = proto.Field(proto.UINT32, number=1)

    client_id_in_control = proto.Field(proto.UINT32, number=2)

    connected_clients = proto.RepeatedField(proto.MESSAGE, number=3,
        message=message_formats.ConnectedClient,
    )


class DisconnectClientReq(proto.Message):
    r"""-

    Disconnect a client from the drone.

    This request will remove the client from the list of connected
    clients. It allows clients to disconnect instantly, without waiting
    for a watchdog to clear the client in control, or promote a new
    client to be in control.

    Attributes:
        client_id (int):
            The assigned ID of the client to disconnect.
    """

    client_id = proto.Field(proto.UINT32, number=1)


class DisconnectClientRep(proto.Message):
    r"""-

    Response after disconnecting a client from the drone.

    Contains information about which clients are connected and in
    control.

    Attributes:
        client_id_in_control (int):
            The ID of the client in control of the drone.
        connected_clients (Sequence[blueye.protocol.types.ConnectedClient]):
            List of connected clients.
    """

    client_id_in_control = proto.Field(proto.UINT32, number=1)

    connected_clients = proto.RepeatedField(proto.MESSAGE, number=2,
        message=message_formats.ConnectedClient,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
