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
from blueye.protocol.types import mission_planning
from google.protobuf import any_pb2 as gp_any  # type: ignore


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
        'GetBatteryReq',
        'GetBatteryRep',
        'SetMissionReq',
        'SetMissionRep',
        'GetMissionReq',
        'GetMissionRep',
        'SetInstructionUpdateReq',
        'SetInstructionUpdateRep',
        'SetPubFrequencyReq',
        'SetPubFrequencyRep',
        'GetTelemetryReq',
        'GetTelemetryRep',
    },
)


class SetOverlayParametersReq(proto.Message):
    r"""Request to set video overlay parameters.

    Attributes:
        overlay_parameters (blueye.protocol.types.OverlayParameters):
            The video overlay parameters to apply.
    """

    overlay_parameters = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.OverlayParameters,
    )


class SetOverlayParametersRep(proto.Message):
    r"""Response after setting video overlay parameters."""


class GetOverlayParametersReq(proto.Message):
    r"""Request to get currently set video overlay parameters."""


class GetOverlayParametersRep(proto.Message):
    r"""Response with the currently set video overlay parameters.

    Attributes:
        overlay_parameters (blueye.protocol.types.OverlayParameters):
            The currently set overlay parameters.
    """

    overlay_parameters = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.OverlayParameters,
    )


class SetCameraParametersReq(proto.Message):
    r"""Request to set camera parameters.

    Attributes:
        camera_parameters (blueye.protocol.types.CameraParameters):
            The camera parameters to apply.
    """

    camera_parameters = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.CameraParameters,
    )


class SetCameraParametersRep(proto.Message):
    r"""Response after setting the camera parameters."""


class GetCameraParametersReq(proto.Message):
    r"""Request to get the currently set camera parameters.

    Attributes:
        camera (blueye.protocol.types.Camera):
            Which camera to read camera parameters from.
    """

    camera = proto.Field(proto.ENUM, number=1,
        enum=message_formats.Camera,
    )


class GetCameraParametersRep(proto.Message):
    r"""Response with the currently set camera parameters.

    Attributes:
        camera_parameters (blueye.protocol.types.CameraParameters):
            The currently set camera parameters.
    """

    camera_parameters = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.CameraParameters,
    )


class SyncTimeReq(proto.Message):
    r"""Request to set the system time on the drone.

    Attributes:
        time (blueye.protocol.types.SystemTime):
            The time to set on the drone.
    """

    time = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.SystemTime,
    )


class SyncTimeRep(proto.Message):
    r"""Response after setting the system time on the drone.

    Attributes:
        success (bool):
            If the time was set successfully.
    """

    success = proto.Field(proto.BOOL, number=1)


class PingReq(proto.Message):
    r"""The simplest message to use to test request/reply
    communication with the drone.
    The drone replies with a PingRep message immediately after
    receiving the PingReq.
    """


class PingRep(proto.Message):
    r"""Response message from a PingReq request."""


class SetThicknessGaugeParametersReq(proto.Message):
    r"""Request to set parameters for ultrasonic thickness gauge.
    The sound velocity is used to calculate the thickness of the
    material being measured.

    Attributes:
        sound_velocity (int):
            Sound velocity in m/s
    """

    sound_velocity = proto.Field(proto.UINT32, number=1)


class SetThicknessGaugeParametersRep(proto.Message):
    r"""Response after setting thicknes gauge parameters."""


class ConnectClientReq(proto.Message):
    r"""Connect a new client to the drone.

    Attributes:
        client_info (blueye.protocol.types.ClientInfo):
            Information about the client connecting to
            the drone.
    """

    client_info = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.ClientInfo,
    )


class ConnectClientRep(proto.Message):
    r"""Response after connecting a client to the drone.
    Contains information about which client is in control, and a
    list of all connected clients.

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
    r"""Disconnect a client from the drone.
    This request will remove the client from the list of connected
    clients. It allows clients to disconnect instantly, without
    waiting for a watchdog to clear the client in control, or
    promote a new client to be in control.

    Attributes:
        client_id (int):
            The assigned ID of the client to disconnect.
    """

    client_id = proto.Field(proto.UINT32, number=1)


class DisconnectClientRep(proto.Message):
    r"""Response after disconnecting a client from the drone.
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


class GetBatteryReq(proto.Message):
    r"""Request essential battery information.
    Can be used to instantly get battery information,
    instead of having to wait for the BatteryTel message to be
    received.
    """


class GetBatteryRep(proto.Message):
    r"""Response with essential battery information.

    Attributes:
        battery (blueye.protocol.types.Battery):
            Essential battery information.
    """

    battery = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.Battery,
    )


class SetMissionReq(proto.Message):
    r"""Issue a desired mission to the reference_generator.

    Attributes:
        mission (blueye.protocol.types.Mission):
            requested mission isseued to the reference
            generator
    """

    mission = proto.Field(proto.MESSAGE, number=1,
        message=mission_planning.Mission,
    )


class SetMissionRep(proto.Message):
    r"""Response after setting a new mission."""


class GetMissionReq(proto.Message):
    r"""Service request to the reference_generator to get the active
    mission.
    """


class GetMissionRep(proto.Message):
    r"""Get active mission response.

    Attributes:
        mission (blueye.protocol.types.Mission):
            active mission with waypoints
    """

    mission = proto.Field(proto.MESSAGE, number=1,
        message=mission_planning.Mission,
    )


class SetInstructionUpdateReq(proto.Message):
    r"""Updates an instruction in current mission with a new
    instruction payload.

    Attributes:
        instruction (blueye.protocol.types.Instruction):
            instruction that will replace the desired
            instruction
    """

    instruction = proto.Field(proto.MESSAGE, number=1,
        message=mission_planning.Instruction,
    )


class SetInstructionUpdateRep(proto.Message):
    r"""Response after updating an instruction in the current
    mission.
    """


class SetPubFrequencyReq(proto.Message):
    r"""Request to update the publish frequency

    Attributes:
        message_type (str):
            Message name, f. ex. "AttitudeTel".
        frequency (float):
            Publish frequency (max 100 Hz).
    """

    message_type = proto.Field(proto.STRING, number=1)

    frequency = proto.Field(proto.FLOAT, number=2)


class SetPubFrequencyRep(proto.Message):
    r"""Response after updating publish frequency

    Attributes:
        success (bool):
            True if message name valid and frequency
            successfully updated.
    """

    success = proto.Field(proto.BOOL, number=1)


class GetTelemetryReq(proto.Message):
    r"""Request to get latest telemetry data

    Attributes:
        message_type (str):
            Message name, f. ex. "AttitudeTel".
    """

    message_type = proto.Field(proto.STRING, number=1)


class GetTelemetryRep(proto.Message):
    r"""Response with latest telemetry

    Attributes:
        payload (google.protobuf.any_pb2.Any):
            The latest telemetry data, empty if no data
            available.
    """

    payload = proto.Field(proto.MESSAGE, number=1,
        message=gp_any.Any,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
