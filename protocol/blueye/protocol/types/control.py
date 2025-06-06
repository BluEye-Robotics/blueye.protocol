# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from blueye.protocol.types import aquatroll
from blueye.protocol.types import message_formats


__protobuf__ = proto.module(
    package='blueye.protocol',
    manifest={
        'MotionInputCtrl',
        'TiltVelocityCtrl',
        'LightsCtrl',
        'GuestportLightsCtrl',
        'LaserCtrl',
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
        'AutoPilotSurgeYawCtrl',
        'AutoPilotHeaveCtrl',
        'RunMissionCtrl',
        'PauseMissionCtrl',
        'ClearMissionCtrl',
        'ResetPositionCtrl',
        'ResetOdometerCtrl',
        'CalibrateDvlGyroCtrl',
        'TiltStabilizationCtrl',
        'WaterDensityCtrl',
        'PingerConfigurationCtrl',
        'SystemTimeCtrl',
        'GripperCtrl',
        'GenericServoCtrl',
        'MultibeamServoCtrl',
        'DeactivateGuestPortsCtrl',
        'ActivateGuestPortsCtrl',
        'RestartGuestPortsCtrl',
        'SetAquaTrollParameterUnitCtrl',
        'SetAquaTrollConnectionStatusCtrl',
        'SetMultibeamConfigCtrl',
        'ActivateMultibeamCtrl',
        'DeactivateMultibeamCtrl',
        'StartDiveCtrl',
        'EndDiveCtrl',
    },
)


class MotionInputCtrl(proto.Message):
    r"""Issue a command to move the drone in the surge, sway, heave,
    or yaw direction.

    Attributes:
        motion_input (blueye.protocol.types.MotionInput):
            Message with the desired movement in each
            direction.
    """

    motion_input: message_formats.MotionInput = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.MotionInput,
    )


class TiltVelocityCtrl(proto.Message):
    r"""Issue a command to tilt the drone camera.

    Attributes:
        velocity (blueye.protocol.types.TiltVelocity):
            Message with the desired tilt velocity
            (direction and speed).
    """

    velocity: message_formats.TiltVelocity = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.TiltVelocity,
    )


class LightsCtrl(proto.Message):
    r"""Issue a command to set the main light intensity.

    Attributes:
        lights (blueye.protocol.types.Lights):
            Message with the desired light intensity.
    """

    lights: message_formats.Lights = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Lights,
    )


class GuestportLightsCtrl(proto.Message):
    r"""Issue a command to set the guest port light intensity.

    Attributes:
        lights (blueye.protocol.types.Lights):
            Message with the desired light intensity.
    """

    lights: message_formats.Lights = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Lights,
    )


class LaserCtrl(proto.Message):
    r"""Issue a command to set the laser intensity.

    Attributes:
        laser (blueye.protocol.types.Laser):
            Message with the desired laser intensity.
    """

    laser: message_formats.Laser = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Laser,
    )


class PilotGPSPositionCtrl(proto.Message):
    r"""Issue a command with the GPS position of the pilot.

    Attributes:
        position (blueye.protocol.types.LatLongPosition):
            The GPS position of the pilot.
    """

    position: message_formats.LatLongPosition = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.LatLongPosition,
    )


class WatchdogCtrl(proto.Message):
    r"""Issue a watchdog message to indicate that the remote client
    is connected and working as expected.
    If a watchdog message is not received every second, the drone
    will turn off lights and other auto functions to indicate that
    connection with the client has been lost.

    Attributes:
        connection_duration (blueye.protocol.types.ConnectionDuration):
            Message with the number of seconds the client
            has been connected.
        client_id (int):
            The ID of the client, received in the
            ConnectClientRep response.
    """

    connection_duration: message_formats.ConnectionDuration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.ConnectionDuration,
    )
    client_id: int = proto.Field(
        proto.UINT32,
        number=2,
    )


class RecordCtrl(proto.Message):
    r"""Issue a command to start video recording.

    Attributes:
        record_on (blueye.protocol.types.RecordOn):
            Message specifying which cameras to record.
    """

    record_on: message_formats.RecordOn = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.RecordOn,
    )


class TakePictureCtrl(proto.Message):
    r"""Issue a command to take a picture.
    """


class StartCalibrationCtrl(proto.Message):
    r"""Issue a command to start compass calibration.
    """


class CancelCalibrationCtrl(proto.Message):
    r"""Issue a command to cancel compass calibration.
    """


class FinishCalibrationCtrl(proto.Message):
    r"""Issue a command to finish compass calibration.
    """


class AutoHeadingCtrl(proto.Message):
    r"""Issue a command to set auto heading to a desired state.

    Attributes:
        state (blueye.protocol.types.AutoHeadingState):
            State of the heading controller.
    """

    state: message_formats.AutoHeadingState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.AutoHeadingState,
    )


class AutoDepthCtrl(proto.Message):
    r"""Issue a command to set auto depth to a desired state.

    Attributes:
        state (blueye.protocol.types.AutoDepthState):
            State of the depth controller.
    """

    state: message_formats.AutoDepthState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.AutoDepthState,
    )


class AutoAltitudeCtrl(proto.Message):
    r"""Issue a command to set auto altitude to a desired state.

    Attributes:
        state (blueye.protocol.types.AutoAltitudeState):
            State of the altitude controller.
    """

    state: message_formats.AutoAltitudeState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.AutoAltitudeState,
    )


class StationKeepingCtrl(proto.Message):
    r"""Issue a command to set station keeping to a desired state.

    Attributes:
        state (blueye.protocol.types.StationKeepingState):
            State of the station keeping controller.
    """

    state: message_formats.StationKeepingState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.StationKeepingState,
    )


class WeatherVaningCtrl(proto.Message):
    r"""Issue a command to set station keeping with weather vaning to
    a desired state.

    Attributes:
        state (blueye.protocol.types.WeatherVaningState):
            State of the weather vaning controller.
    """

    state: message_formats.WeatherVaningState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.WeatherVaningState,
    )


class AutoPilotSurgeYawCtrl(proto.Message):
    r"""Issue a command to set Auto Pilot for cruising and turning to
    a desired state.

    Attributes:
        state (blueye.protocol.types.AutoPilotSurgeYawState):
            State of the auto pilot surge yaw controller.
    """

    state: message_formats.AutoPilotSurgeYawState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.AutoPilotSurgeYawState,
    )


class AutoPilotHeaveCtrl(proto.Message):
    r"""Issue a command to set Auto Pilot for vertiacl movement to a
    desired state.

    Attributes:
        state (blueye.protocol.types.AutoPilotHeaveState):
            State of the auto pilot heave controller-
    """

    state: message_formats.AutoPilotHeaveState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.AutoPilotHeaveState,
    )


class RunMissionCtrl(proto.Message):
    r"""Issue a command to start and pause the loaded mission.
    """


class PauseMissionCtrl(proto.Message):
    r"""Issue a command to pause the loaded mission.
    """


class ClearMissionCtrl(proto.Message):
    r"""Clear the loaded mission.
    """


class ResetPositionCtrl(proto.Message):
    r"""Issue a command to reset the position estimate.

    Attributes:
        settings (blueye.protocol.types.ResetPositionSettings):
            Reset settings.
    """

    settings: message_formats.ResetPositionSettings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.ResetPositionSettings,
    )


class ResetOdometerCtrl(proto.Message):
    r"""Issue a command to reset the odometer.
    """


class CalibrateDvlGyroCtrl(proto.Message):
    r"""Issue a command to calibrate the DVL gyro.
    """


class TiltStabilizationCtrl(proto.Message):
    r"""Issue a command to enable or disable tilt stabilization.

    Attributes:
        state (blueye.protocol.types.TiltStabilizationState):
            Message with the tilt stabilization state to
            set.
    """

    state: message_formats.TiltStabilizationState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.TiltStabilizationState,
    )


class WaterDensityCtrl(proto.Message):
    r"""Issue a command to set the water density.

    Attributes:
        density (blueye.protocol.types.WaterDensity):
            Message with the water density to set.
    """

    density: message_formats.WaterDensity = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.WaterDensity,
    )


class PingerConfigurationCtrl(proto.Message):
    r"""Issue a command to set the pinger configuration.

    Attributes:
        configuration (blueye.protocol.types.PingerConfiguration):
            Message with the pinger configuration to set.
    """

    configuration: message_formats.PingerConfiguration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.PingerConfiguration,
    )


class SystemTimeCtrl(proto.Message):
    r"""Issue a command to set the system time on the drone.

    Attributes:
        system_time (blueye.protocol.types.SystemTime):
            Message with the system time to set.
    """

    system_time: message_formats.SystemTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.SystemTime,
    )


class GripperCtrl(proto.Message):
    r"""Issue a command to control the gripper.

    Attributes:
        gripper_velocities (blueye.protocol.types.GripperVelocities):
            The desired gripping and rotation velocity.
    """

    gripper_velocities: message_formats.GripperVelocities = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.GripperVelocities,
    )


class GenericServoCtrl(proto.Message):
    r"""Issue a command to set a generic servo value.

    Attributes:
        servo (blueye.protocol.types.GenericServo):
            Message with the desired servo value.
    """

    servo: message_formats.GenericServo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.GenericServo,
    )


class MultibeamServoCtrl(proto.Message):
    r"""Issue a command to set multibeam servo angle.

    Attributes:
        servo (blueye.protocol.types.MultibeamServo):
            Message with the desired servo angle.
    """

    servo: message_formats.MultibeamServo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.MultibeamServo,
    )


class DeactivateGuestPortsCtrl(proto.Message):
    r"""Deactivate the guest port power.
    """


class ActivateGuestPortsCtrl(proto.Message):
    r"""Activated the guest port power.
    """


class RestartGuestPortsCtrl(proto.Message):
    r"""Restart the guest ports by turning power on and off.

    Attributes:
        restart_info (blueye.protocol.types.GuestPortRestartInfo):
            Message with information about how long to
            keep the guest ports off.
    """

    restart_info: message_formats.GuestPortRestartInfo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.GuestPortRestartInfo,
    )


class SetAquaTrollParameterUnitCtrl(proto.Message):
    r"""Request to set an In-Situ Aqua Troll parameter unit.

    Attributes:
        parameter_info (blueye.protocol.types.SetAquaTrollParameterUnit):
            Message with information about which
            parameter to set and the unit to set it to.
    """

    parameter_info: aquatroll.SetAquaTrollParameterUnit = proto.Field(
        proto.MESSAGE,
        number=1,
        message=aquatroll.SetAquaTrollParameterUnit,
    )


class SetAquaTrollConnectionStatusCtrl(proto.Message):
    r"""Request to change the In-Situ Aqua Troll connection status.

    Attributes:
        connection_status (blueye.protocol.types.SetAquaTrollConnectionStatus):
            Message with information about which
            parameter to set and the unit to set it to.
    """

    connection_status: aquatroll.SetAquaTrollConnectionStatus = proto.Field(
        proto.MESSAGE,
        number=1,
        message=aquatroll.SetAquaTrollConnectionStatus,
    )


class SetMultibeamConfigCtrl(proto.Message):
    r"""Update the multibeam settings.

    Attributes:
        config (blueye.protocol.types.MultibeamConfig):
            Message with the multibeam ping configuration
            to set.
    """

    config: message_formats.MultibeamConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.MultibeamConfig,
    )


class ActivateMultibeamCtrl(proto.Message):
    r"""Activate the multibeam with specified configuration.

    Attributes:
        config (blueye.protocol.types.MultibeamConfig):
            Message with the multibeam ping configuration
            to set on connect.
    """

    config: message_formats.MultibeamConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.MultibeamConfig,
    )


class DeactivateMultibeamCtrl(proto.Message):
    r"""Deactivate the multibeam.
    """


class StartDiveCtrl(proto.Message):
    r"""Message sent when the user hits the start dive button in the
    app.
    The message does not do anything, but is included in the log
    files so we can see at which point the user entered the dive
    view.

    """


class EndDiveCtrl(proto.Message):
    r"""Message sent when the user hits the end dive button in the
    app.
    The message does not do anything, but is included in the log
    files so we can see at which point the user exited the dive
    view.

    """


__all__ = tuple(sorted(__protobuf__.manifest))
