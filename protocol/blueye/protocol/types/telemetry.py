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
from blueye.protocol.types import mission_planning


__protobuf__ = proto.module(
    package='blueye.protocol',
    manifest={
        'AttitudeTel',
        'AltitudeTel',
        'ForwardDistanceTel',
        'DvlVelocityTel',
        'PositionEstimateTel',
        'DepthTel',
        'ReferenceTel',
        'ReferenceAutoPilotTel',
        'MissionStatusTel',
        'NotificationTel',
        'ControlForceTel',
        'ControllerHealthTel',
        'LightsTel',
        'GuestPortLightsTel',
        'LaserTel',
        'PilotGPSPositionTel',
        'RecordStateTel',
        'TimeLapseStateTel',
        'BatteryTel',
        'BatteryBQ40Z50Tel',
        'DiveTimeTel',
        'DroneTimeTel',
        'WaterTemperatureTel',
        'CPUTemperatureTel',
        'CanisterBottomTemperatureTel',
        'CanisterBottomHumidityTel',
        'VideoStorageSpaceTel',
        'DataStorageSpaceTel',
        'CalibrationStateTel',
        'TiltStabilizationTel',
        'IperfTel',
        'NStreamersTel',
        'TiltAngleTel',
        'DroneInfoTel',
        'ErrorFlagsTel',
        'ControlModeTel',
        'ThicknessGaugeTel',
        'CpProbeTel',
        'AquaTrollProbeMetadataTel',
        'AquaTrollSensorMetadataTel',
        'AquaTrollSensorParametersTel',
        'ConnectedClientsTel',
        'GenericServoTel',
        'MultibeamServoTel',
        'GuestPortCurrentTel',
        'CalibratedImuTel',
        'Imu1Tel',
        'Imu2Tel',
        'MedusaSpectrometerDataTel',
        'MultibeamPingTel',
        'MultibeamConfigTel',
        'MultibeamDiscoveryTel',
        'CPUInfoTel',
    },
)


class AttitudeTel(proto.Message):
    r"""Receive the current attitude of the drone.

    Attributes:
        attitude (blueye.protocol.types.Attitude):
            The attitude of the drone.
    """

    attitude: message_formats.Attitude = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Attitude,
    )


class AltitudeTel(proto.Message):
    r"""Receive the current altitude of the drone.

    Attributes:
        altitude (blueye.protocol.types.Altitude):
            The altitude of the drone.
    """

    altitude: message_formats.Altitude = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Altitude,
    )


class ForwardDistanceTel(proto.Message):
    r"""Distance to an object in front of the drone when a 1D pinger
    is mounted forwards.

    Attributes:
        forward_distance (blueye.protocol.types.ForwardDistance):
            The distance to an object in front of the
            drone.
    """

    forward_distance: message_formats.ForwardDistance = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.ForwardDistance,
    )


class DvlVelocityTel(proto.Message):
    r"""Dvl raw sensor data.

    Attributes:
        dvl_velocity (blueye.protocol.types.DvlVelocity):
            Dvl velocity data.
    """

    dvl_velocity: message_formats.DvlVelocity = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.DvlVelocity,
    )


class PositionEstimateTel(proto.Message):
    r"""Position estimate of the drone if a DVL or a positioning
    system is available.

    Attributes:
        position_estimate (blueye.protocol.types.PositionEstimate):
            Position estimate of the drone.
    """

    position_estimate: message_formats.PositionEstimate = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.PositionEstimate,
    )


class DepthTel(proto.Message):
    r"""Measurement of the drones position relative to the sea
    surface.

    Attributes:
        depth (blueye.protocol.types.Depth):
            The depth of the drone.
    """

    depth: message_formats.Depth = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Depth,
    )


class ReferenceTel(proto.Message):
    r"""Reference signals indicating desired states.

    Attributes:
        reference (blueye.protocol.types.Reference):
            Reference signals.
    """

    reference: message_formats.Reference = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Reference,
    )


class ReferenceAutoPilotTel(proto.Message):
    r"""Reference for the auto pilot when a mission is active.

    Attributes:
        reference_auto_pilot (blueye.protocol.types.ReferenceAutoPilot):
            Reference for the auto pilot.
    """

    reference_auto_pilot: mission_planning.ReferenceAutoPilot = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mission_planning.ReferenceAutoPilot,
    )


class MissionStatusTel(proto.Message):
    r"""Mission status from the mission supervisor.

    Attributes:
        mission_status (blueye.protocol.types.MissionStatus):
            Mission status.
    """

    mission_status: mission_planning.MissionStatus = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mission_planning.MissionStatus,
    )


class NotificationTel(proto.Message):
    r"""Notification from the control system.

    Attributes:
        notification (blueye.protocol.types.Notification):
            Notification from the control system.
    """

    notification: message_formats.Notification = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Notification,
    )


class ControlForceTel(proto.Message):
    r"""Control force in all directions.

    Attributes:
        control_force (blueye.protocol.types.ControlForce):
            Control force in all directions.
    """

    control_force: message_formats.ControlForce = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.ControlForce,
    )


class ControllerHealthTel(proto.Message):
    r"""Controller health indicating the load of the controller, used
    to set a color in the heading and depth bar.

    Attributes:
        controller_health (blueye.protocol.types.ControllerHealth):
            Controller health.
    """

    controller_health: message_formats.ControllerHealth = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.ControllerHealth,
    )


class LightsTel(proto.Message):
    r"""Receive the status of the main lights of the drone.

    Attributes:
        lights (blueye.protocol.types.Lights):
            Main light status.
    """

    lights: message_formats.Lights = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Lights,
    )


class GuestPortLightsTel(proto.Message):
    r"""Receive the status of any guest port lights connected to the
    drone.

    Attributes:
        lights (blueye.protocol.types.Lights):
            Guest port light status.
    """

    lights: message_formats.Lights = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Lights,
    )


class LaserTel(proto.Message):
    r"""Receive the status of any lasers connected to the drone.

    Attributes:
        laser (blueye.protocol.types.Laser):
            Laser status.
    """

    laser: message_formats.Laser = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Laser,
    )


class PilotGPSPositionTel(proto.Message):
    r"""Pilot position (originating from device GPS) for logging.

    Attributes:
        position (blueye.protocol.types.LatLongPosition):
            The GPS position of the pilot.
    """

    position: message_formats.LatLongPosition = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.LatLongPosition,
    )


class RecordStateTel(proto.Message):
    r"""Record state from the drone.

    Attributes:
        record_state (blueye.protocol.types.RecordState):
            Record state.
    """

    record_state: message_formats.RecordState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.RecordState,
    )


class TimeLapseStateTel(proto.Message):
    r"""Time-lapse state from the drone.

    Attributes:
        time_lapse_state (blueye.protocol.types.TimeLapseState):
            Time-lapse state.
    """

    time_lapse_state: message_formats.TimeLapseState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.TimeLapseState,
    )


class BatteryTel(proto.Message):
    r"""Receive essential information about the battery status.

    Attributes:
        battery (blueye.protocol.types.Battery):
            Essential battery information.
    """

    battery: message_formats.Battery = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Battery,
    )


class BatteryBQ40Z50Tel(proto.Message):
    r"""Receive detailed information about a battery using the
    BQ40Z50 battery management system.

    Attributes:
        battery (blueye.protocol.types.BatteryBQ40Z50):
            Detailed battery information.
    """

    battery: message_formats.BatteryBQ40Z50 = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.BatteryBQ40Z50,
    )


class DiveTimeTel(proto.Message):
    r"""Receive the dive time of the drone.

    Attributes:
        dive_time (blueye.protocol.types.DiveTime):
            The current dive time of the drone.
    """

    dive_time: message_formats.DiveTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.DiveTime,
    )


class DroneTimeTel(proto.Message):
    r"""Receive time information from the drone.

    Attributes:
        real_time_clock (blueye.protocol.types.SystemTime):
            The real-time clock of the drone.
        monotonic_clock (blueye.protocol.types.SystemTime):
            The monotonic clock of the drone (time since
            power on).
    """

    real_time_clock: message_formats.SystemTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.SystemTime,
    )
    monotonic_clock: message_formats.SystemTime = proto.Field(
        proto.MESSAGE,
        number=2,
        message=message_formats.SystemTime,
    )


class WaterTemperatureTel(proto.Message):
    r"""Water temperature from the depth sensor.

    Attributes:
        temperature (blueye.protocol.types.WaterTemperature):
            Water temperature.
    """

    temperature: message_formats.WaterTemperature = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.WaterTemperature,
    )


class CPUTemperatureTel(proto.Message):
    r"""Drone CPU temperature

    Attributes:
        temperature (blueye.protocol.types.CPUTemperature):
            CPU temperature.
    """

    temperature: message_formats.CPUTemperature = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.CPUTemperature,
    )


class CanisterBottomTemperatureTel(proto.Message):
    r"""Receive temperature information from the bottom canister.

    Attributes:
        temperature (blueye.protocol.types.CanisterTemperature):
            Temperature information.
    """

    temperature: message_formats.CanisterTemperature = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.CanisterTemperature,
    )


class CanisterBottomHumidityTel(proto.Message):
    r"""Receive humidity information from the bottom canister.

    Attributes:
        humidity (blueye.protocol.types.CanisterHumidity):
            Humidity information.
    """

    humidity: message_formats.CanisterHumidity = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.CanisterHumidity,
    )


class VideoStorageSpaceTel(proto.Message):
    r"""Video storage info.

    Attributes:
        storage_space (blueye.protocol.types.StorageSpace):
            Video storage information.
    """

    storage_space: message_formats.StorageSpace = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.StorageSpace,
    )


class DataStorageSpaceTel(proto.Message):
    r"""Data storage info.

    Attributes:
        storage_space (blueye.protocol.types.StorageSpace):
            Data storage information.
    """

    storage_space: message_formats.StorageSpace = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.StorageSpace,
    )


class CalibrationStateTel(proto.Message):
    r"""Calibration state used for calibration routine.

    Attributes:
        calibration_state (blueye.protocol.types.CalibrationState):
            Calibration state.
    """

    calibration_state: message_formats.CalibrationState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.CalibrationState,
    )


class TiltStabilizationTel(proto.Message):
    r"""Tilt stabilization state.

    Attributes:
        state (blueye.protocol.types.TiltStabilizationState):
            Tilt stabilization state.
    """

    state: message_formats.TiltStabilizationState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.TiltStabilizationState,
    )


class IperfTel(proto.Message):
    r"""Iperf indicates the available bandwidth on the tether from
    drone to surface unit.

    Attributes:
        status (blueye.protocol.types.IperfStatus):
            Information about the available bandwidth.
    """

    status: message_formats.IperfStatus = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.IperfStatus,
    )


class NStreamersTel(proto.Message):
    r"""Number of connected clients streaming video.

    Attributes:
        n_streamers (blueye.protocol.types.NStreamers):
            Information about the number of connected
            clients.
    """

    n_streamers: message_formats.NStreamers = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.NStreamers,
    )


class TiltAngleTel(proto.Message):
    r"""Tilt angle state on main camera.

    Attributes:
        angle (blueye.protocol.types.TiltAngle):
            Main camera tilt angle.
    """

    angle: message_formats.TiltAngle = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.TiltAngle,
    )


class DroneInfoTel(proto.Message):
    r"""Receive metadata and information about the connected drone.

    Attributes:
        drone_info (blueye.protocol.types.DroneInfo):
            Various metadata such as software versions
            and serial number.
    """

    drone_info: message_formats.DroneInfo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.DroneInfo,
    )


class ErrorFlagsTel(proto.Message):
    r"""Receive currently set error flags.

    Attributes:
        error_flags (blueye.protocol.types.ErrorFlags):
            Currently set error flags on the drone.
    """

    error_flags: message_formats.ErrorFlags = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.ErrorFlags,
    )


class ControlModeTel(proto.Message):
    r"""Receive the current state of the control system.

    Attributes:
        state (blueye.protocol.types.ControlMode):
            State of the control system.
    """

    state: message_formats.ControlMode = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.ControlMode,
    )


class ThicknessGaugeTel(proto.Message):
    r"""Thickness gauge measurement telemetry message.

    Attributes:
        thickness_gauge (blueye.protocol.types.ThicknessGauge):
            Thickness measurement with a cygnus gauge.
    """

    thickness_gauge: message_formats.ThicknessGauge = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.ThicknessGauge,
    )


class CpProbeTel(proto.Message):
    r"""Cathodic Protection Potential probe telemetry message

    Attributes:
        cp_probe (blueye.protocol.types.CpProbe):
            Reading from cp probe.
    """

    cp_probe: message_formats.CpProbe = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.CpProbe,
    )


class AquaTrollProbeMetadataTel(proto.Message):
    r"""Metadata from the In-Situ Aqua Troll probe's common registers

    Attributes:
        probe (blueye.protocol.types.AquaTrollProbeMetadata):
            AquaTroll message containing sensor array.
    """

    probe: aquatroll.AquaTrollProbeMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=aquatroll.AquaTrollProbeMetadata,
    )


class AquaTrollSensorMetadataTel(proto.Message):
    r"""Metadata from a single sensor from In-Situ Aqua Troll probe

    Attributes:
        sensors (blueye.protocol.types.AquaTrollSensorMetadataArray):
            AquaTroll message containing sensor array.
    """

    sensors: aquatroll.AquaTrollSensorMetadataArray = proto.Field(
        proto.MESSAGE,
        number=1,
        message=aquatroll.AquaTrollSensorMetadataArray,
    )


class AquaTrollSensorParametersTel(proto.Message):
    r"""Single sensor from In-Situ Aqua Troll probe

    Attributes:
        sensors (blueye.protocol.types.AquaTrollSensorParametersArray):
            AquaTroll message containing parameter array.
    """

    sensors: aquatroll.AquaTrollSensorParametersArray = proto.Field(
        proto.MESSAGE,
        number=1,
        message=aquatroll.AquaTrollSensorParametersArray,
    )


class ConnectedClientsTel(proto.Message):
    r"""List of connected clients telemetry message.

    Attributes:
        client_id_in_control (int):
            The client id of the client in control.
        connected_clients (MutableSequence[blueye.protocol.types.ConnectedClient]):
            List of connected clients.
    """

    client_id_in_control: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    connected_clients: MutableSequence[message_formats.ConnectedClient] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=message_formats.ConnectedClient,
    )


class GenericServoTel(proto.Message):
    r"""State of a generic servo.

    Attributes:
        servo (blueye.protocol.types.GenericServo):
            Servo state.
    """

    servo: message_formats.GenericServo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.GenericServo,
    )


class MultibeamServoTel(proto.Message):
    r"""State of the servo installed in the multibeam.

    Attributes:
        servo (blueye.protocol.types.MultibeamServo):
            Multibeam servo state.
    """

    servo: message_formats.MultibeamServo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.MultibeamServo,
    )


class GuestPortCurrentTel(proto.Message):
    r"""GuestPort current readings.

    Attributes:
        current (blueye.protocol.types.GuestPortCurrent):
            Guest port current readings.
    """

    current: message_formats.GuestPortCurrent = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.GuestPortCurrent,
    )


class CalibratedImuTel(proto.Message):
    r"""Calibrated IMU data.

    Attributes:
        imu (blueye.protocol.types.Imu):
            Calibrated IMU data.
    """

    imu: message_formats.Imu = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Imu,
    )


class Imu1Tel(proto.Message):
    r"""Raw IMU data from IMU 1

    Attributes:
        imu (blueye.protocol.types.Imu):
            Raw IMU data.
    """

    imu: message_formats.Imu = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Imu,
    )


class Imu2Tel(proto.Message):
    r"""Raw IMU data from IMU 2

    Attributes:
        imu (blueye.protocol.types.Imu):
            Raw IMU data.
    """

    imu: message_formats.Imu = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Imu,
    )


class MedusaSpectrometerDataTel(proto.Message):
    r"""Medusa gamma ray sensor spectrometer data.

    Attributes:
        data (blueye.protocol.types.MedusaSpectrometerData):
            Medusa gamma ray sensor spectrometer data.
    """

    data: message_formats.MedusaSpectrometerData = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.MedusaSpectrometerData,
    )


class MultibeamPingTel(proto.Message):
    r"""Multibeam sonar ping data.

    Attributes:
        ping (blueye.protocol.types.MultibeamPing):
            Ping data from a multibeam sonar.
    """

    ping: message_formats.MultibeamPing = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.MultibeamPing,
    )


class MultibeamConfigTel(proto.Message):
    r"""Multibeam sonar config.

    Attributes:
        config (blueye.protocol.types.MultibeamConfig):
            Config data from a multibeam sonar.
    """

    config: message_formats.MultibeamConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.MultibeamConfig,
    )


class MultibeamDiscoveryTel(proto.Message):
    r"""Multibeam sonar status message.

    Attributes:
        discovery (blueye.protocol.types.MultibeamDiscovery):
            Discovery data from a multibeam sonar.
    """

    discovery: message_formats.MultibeamDiscovery = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.MultibeamDiscovery,
    )


class CPUInfoTel(proto.Message):
    r"""Information about cpu and memory usage.

    Attributes:
        cpu_info (blueye.protocol.types.CPUInfo):
            CPU information.
    """

    cpu_info: message_formats.CPUInfo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.CPUInfo,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
