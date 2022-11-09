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
        'MotionInputCtrl',
        'TiltVelocityCtrl',
        'LightsCtrl',
        'GuestportLightsCtrl',
        'PilotGPSPositionCtrl',
        'WatchdogCtrl',
        'RecordCtrl',
        'TakePictureCtrl',
        'StartCalibrationCtrl',
        'CancelCalibrationCtrl',
        'FinishCalibrationCtrl',
        'AutoHeadingCtrl',
        'AutoDepthCtrl',
        'AutoAltitudeCtrl',
        'StationKeepingCtrl',
        'WeatherVaningCtrl',
        'ResetPositionCtrl',
        'ResetOdometerCtrl',
        'TiltStabilizationCtrl',
        'WaterDensityCtrl',
        'PingerConfigurationCtrl',
        'SystemTimeCtrl',
        'GripperCtrl',
        'GenericServoCtrl',
        'MultibeamServoCtrl',
    },
)


class MotionInputCtrl(proto.Message):
    r"""-

    Issue a command to move the drone in the surge, sway, heave, or yaw
    direction.

    Attributes:
        motion_input (blueye.protocol.types.MotionInput):
            Message with the desired movement in each
            direction.
    """

    motion_input = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.MotionInput,
    )


class TiltVelocityCtrl(proto.Message):
    r"""-

    Issue a command to tilt the drone camera.

    Attributes:
        velocity (blueye.protocol.types.TiltVelocity):
            Message with the desired tilt velocity
            (direction and speed).
    """

    velocity = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.TiltVelocity,
    )


class LightsCtrl(proto.Message):
    r"""-

    Issue a command to set the main light intensity.

    Attributes:
        lights (blueye.protocol.types.Lights):
            Message with the desired light intensity.
    """

    lights = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.Lights,
    )


class GuestportLightsCtrl(proto.Message):
    r"""-

    Issue a command to set the guest port light intensity.

    Attributes:
        lights (blueye.protocol.types.Lights):
            Message with the desired light intensity.
    """

    lights = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.Lights,
    )


class PilotGPSPositionCtrl(proto.Message):
    r"""-

    Issue a command with the GPS position of the pilot.

    Attributes:
        position (blueye.protocol.types.LatLongPosition):
            The GPS position of the pilot.
    """

    position = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.LatLongPosition,
    )


class WatchdogCtrl(proto.Message):
    r"""-

    Issue a watchdog message to indicate that the remote client is
    connected and working as expected.

    If a watchdog message is not received every second, the drone will
    turn off lights and other auto functions to indicate that connection
    with the client has been lost.

    Attributes:
        connection_duration (blueye.protocol.types.ConnectionDuration):
            Message with the number of seconds the client
            has been connected.
        client_id (int):
            The ID of the client, received in the
            ConnectClientRep response.
    """

    connection_duration = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.ConnectionDuration,
    )

    client_id = proto.Field(proto.UINT32, number=2)


class RecordCtrl(proto.Message):
    r"""-

    Issue a command to start video recording.

    Attributes:
        record_on (blueye.protocol.types.RecordOn):
            Message specifying which cameras to record.
    """

    record_on = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.RecordOn,
    )


class TakePictureCtrl(proto.Message):
    r"""-

    Issue a command to take a picture.
    """


class StartCalibrationCtrl(proto.Message):
    r"""-

    Issue a command to start compass calibration.
    """


class CancelCalibrationCtrl(proto.Message):
    r"""-

    Issue a command to cancel compass calibration.
    """


class FinishCalibrationCtrl(proto.Message):
    r"""-

    Issue a command to finish compass calibration.
    """


class AutoHeadingCtrl(proto.Message):
    r"""-

    Issue a command to set auto heading to a desired state.

    Attributes:
        state (blueye.protocol.types.AutoHeadingState):
            State of the heading controller
    """

    state = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.AutoHeadingState,
    )


class AutoDepthCtrl(proto.Message):
    r"""-

    Issue a command to set auto depth to a desired state.

    Attributes:
        state (blueye.protocol.types.AutoDepthState):
            State of the depth controller
    """

    state = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.AutoDepthState,
    )


class AutoAltitudeCtrl(proto.Message):
    r"""-

    Issue a command to set auto altitude to a desired state.

    Attributes:
        state (blueye.protocol.types.AutoAltitudeState):
            State of the altitude controller
    """

    state = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.AutoAltitudeState,
    )


class StationKeepingCtrl(proto.Message):
    r"""-

    Issue a command to set station keeping to a desired state.

    Attributes:
        state (blueye.protocol.types.StationKeepingState):
            State of the station keeping controller
    """

    state = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.StationKeepingState,
    )


class WeatherVaningCtrl(proto.Message):
    r"""-

    Issue a command to set station keeping with weather vaning to a
    desired state.

    Attributes:
        state (blueye.protocol.types.WeatherVaningState):
            State of the weather vaning controller
    """

    state = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.WeatherVaningState,
    )


class ResetPositionCtrl(proto.Message):
    r"""-

    Issue a command to reset the position estimate.
    """


class ResetOdometerCtrl(proto.Message):
    r"""-

    Issue a command to reset the odometer.
    """


class TiltStabilizationCtrl(proto.Message):
    r"""-

    Issue a command to enable or disable tilt stabilization.

    Attributes:
        state (blueye.protocol.types.TiltStabilizationState):
            Message with the tilt stabilization state to
            set.
    """

    state = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.TiltStabilizationState,
    )


class WaterDensityCtrl(proto.Message):
    r"""-

    Issue a command to set the water density.

    Attributes:
        density (blueye.protocol.types.WaterDensity):
            Message with the water density to set.
    """

    density = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.WaterDensity,
    )


class PingerConfigurationCtrl(proto.Message):
    r"""-

    Issue a command to set the pinger configuration.

    Attributes:
        configuration (blueye.protocol.types.PingerConfiguration):
            Message with the pinger configuration to set.
    """

    configuration = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.PingerConfiguration,
    )


class SystemTimeCtrl(proto.Message):
    r"""-

    Issue a command to set the system time on the drone.

    Attributes:
        system_time (blueye.protocol.types.SystemTime):
            Message with the system time to set.
    """

    system_time = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.SystemTime,
    )


class GripperCtrl(proto.Message):
    r"""-

    Issue a command to control the gripper.

    Attributes:
        gripper_velocities (blueye.protocol.types.GripperVelocities):
            The desired gripping and rotation velocity.
    """

    gripper_velocities = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.GripperVelocities,
    )


class GenericServoCtrl(proto.Message):
    r"""-

    Issue a command to set a generic servo value.

    Attributes:
        servo (blueye.protocol.types.GenericServo):
            Message with the desired servo value.
    """

    servo = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.GenericServo,
    )


class MultibeamServoCtrl(proto.Message):
    r"""-

    Issue a command to set multibeam servo angle.

    Attributes:
        servo (blueye.protocol.types.MultibeamServo):
            Message with the desired servo angle.
    """

    servo = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.MultibeamServo,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
