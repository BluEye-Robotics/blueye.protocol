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

from google.protobuf import any_pb2  # type: ignore
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='blueye.protocol',
    manifest={
        'IntervalType',
        'HeadingSource',
        'HeadingMode',
        'ResetCoordinateSource',
        'NotificationType',
        'NotificationLevel',
        'Model',
        'PressureSensorType',
        'Resolution',
        'Framerate',
        'Camera',
        'TemperatureUnit',
        'LogoType',
        'DepthUnit',
        'ThicknessUnit',
        'FontSize',
        'GuestPortDeviceID',
        'GuestPortNumber',
        'NavigationSensorID',
        'GuestPortDetachStatus',
        'GuestPortError',
        'MultibeamFrequencyMode',
        'BinlogRecord',
        'MotionInput',
        'Lights',
        'Laser',
        'LatLongPosition',
        'ConnectionDuration',
        'AutoHeadingState',
        'AutoDepthState',
        'AutoAltitudeState',
        'StationKeepingState',
        'WeatherVaningState',
        'AutoPilotSurgeYawState',
        'AutoPilotHeaveState',
        'ControlMode',
        'TiltStabilizationState',
        'SystemTime',
        'GripperVelocities',
        'ClientInfo',
        'ConnectedClient',
        'RecordState',
        'TimeLapseState',
        'WaterDensity',
        'PingerConfiguration',
        'WaterTemperature',
        'CPUTemperature',
        'CanisterTemperature',
        'CanisterHumidity',
        'Battery',
        'BatteryBQ40Z50',
        'Attitude',
        'Altitude',
        'ForwardDistance',
        'PositionEstimate',
        'ResetPositionSettings',
        'DvlTransducer',
        'DvlVelocity',
        'Depth',
        'Reference',
        'Notification',
        'ControlForce',
        'ControllerHealth',
        'DiveTime',
        'RecordOn',
        'StorageSpace',
        'CalibrationState',
        'IperfStatus',
        'NStreamers',
        'TiltAngle',
        'TiltVelocity',
        'DroneInfo',
        'ErrorFlags',
        'CameraParameters',
        'OverlayParameters',
        'NavigationSensorStatus',
        'GuestPortDevice',
        'GuestPortDeviceList',
        'GuestPortConnectorInfo',
        'GuestPortInfo',
        'GuestPortRestartInfo',
        'ThicknessGauge',
        'CpProbe',
        'GenericServo',
        'MultibeamServo',
        'GuestPortCurrent',
        'Vector3',
        'Imu',
        'MedusaSpectrometerData',
        'MultibeamPing',
        'MultibeamConfig',
        'MultibeamDiscovery',
        'MultibeamErrorFlags',
        'MultibeamFrameOffset',
        'MutltibeamRecordingIndex',
        'PersistentStorageSettings',
        'CPUInfo',
    },
)


class IntervalType(proto.Enum):
    r"""Interval type for time-lapse photos.

    Attributes:
        INTERVAL_TYPE_UNSPECIFIED (0):
            Unspecified.
        INTERVAL_TYPE_TIME (1):
            Time interval.
        INTERVAL_TYPE_DISTANCE (2):
            Distance interval.
    """
    INTERVAL_TYPE_UNSPECIFIED = 0
    """Unspecified."""
    INTERVAL_TYPE_TIME = 1
    """Time interval."""
    INTERVAL_TYPE_DISTANCE = 2
    """Distance interval."""


class HeadingSource(proto.Enum):
    r"""Heading source used during reset of the position estimate.

    Attributes:
        HEADING_SOURCE_UNSPECIFIED (0):
            Unspecified.
        HEADING_SOURCE_DRONE_COMPASS (1):
            Uses the drone magnetic compass to set the
            heading.
        HEADING_SOURCE_MANUAL_INPUT (2):
            Used when the user sets the heading manually.
    """
    HEADING_SOURCE_UNSPECIFIED = 0
    """Unspecified."""
    HEADING_SOURCE_DRONE_COMPASS = 1
    """Uses the drone magnetic compass to set the heading."""
    HEADING_SOURCE_MANUAL_INPUT = 2
    """Used when the user sets the heading manually."""


class HeadingMode(proto.Enum):
    r"""Heading mode used during dead reckoning with a DVL.

    Attributes:
        HEADING_MODE_UNSPECIFIED (0):
            Unspecified.
        HEADING_MODE_MAGNETIC_COMPASS (1):
            Uses the best available magnetic compass
            heading.
        HEADING_MODE_GYRO_ONLY (2):
            Uses the best available gyro based heading.
    """
    HEADING_MODE_UNSPECIFIED = 0
    """Unspecified."""
    HEADING_MODE_MAGNETIC_COMPASS = 1
    """Uses the best available magnetic compass heading."""
    HEADING_MODE_GYRO_ONLY = 2
    """Uses the best available gyro based heading."""


class ResetCoordinateSource(proto.Enum):
    r"""The coordinate source to use when resetting the position
    estimate.

    Attributes:
        RESET_COORDINATE_SOURCE_UNSPECIFIED (0):
            Unspecified, fallback to device GPS
        RESET_COORDINATE_SOURCE_DEVICE_GPS (1):
            Uses the device GPS to set the reset point
        RESET_COORDINATE_SOURCE_MANUAL (2):
            Uses a coordinate in decimal degrees to set
            the reset point
        RESET_COORDINATE_SOURCE_BLUEYE_GNSS (3):
            Uses the Blueye GNSS to set the reset point
    """
    RESET_COORDINATE_SOURCE_UNSPECIFIED = 0
    """Unspecified, fallback to device GPS"""
    RESET_COORDINATE_SOURCE_DEVICE_GPS = 1
    """Uses the device GPS to set the reset point"""
    RESET_COORDINATE_SOURCE_MANUAL = 2
    """Uses a coordinate in decimal degrees to set the reset point"""
    RESET_COORDINATE_SOURCE_BLUEYE_GNSS = 3
    """Uses the Blueye GNSS to set the reset point"""


class NotificationType(proto.Enum):
    r"""Notification is used for displaying info, warnings, and
    errors to the user.

    Attributes:
        NOTIFICATION_TYPE_UNSPECIFIED (0):
            Unspecified.
        NOTIFICATION_TYPE_POSITION_ESTIMATE_IS_INACCURATE (1):
            Position estimate is inaccurate.
        NOTIFICATION_TYPE_DRONE_POSITION_IS_UNKNOWN (2):
            Drone position is unknown.
        NOTIFICATION_TYPE_USER_POSITION_IS_UNKNOWN (3):
            User position is unknown.
        NOTIFICATION_TYPE_NO_MISSION_LOADED (4):
            No mission is loaded.
        NOTIFICATION_TYPE_MISSION_LOADED (5):
            Mission is loaded.
        NOTIFICATION_TYPE_FAILED_TO_LOAD_MISSION (6):
            Failed to load mission.
        NOTIFICATION_TYPE_MISSION_COMPLETE (7):
            Mission is complete.
        NOTIFICATION_TYPE_INSTRUCTION_COMPLETE (8):
            Instruction is complete.
        NOTIFICATION_TYPE_WAYPOINT_REACHED (9):
            Waypoint reached.
        NOTIFICATION_TYPE_DEPTH_TARGET_REACHED (10):
            Depth set point is reached.
        NOTIFICATION_TYPE_ALTITUDE_TARGET_REACHED (11):
            Altitude set point is reached.
        NOTIFICATION_TYPE_WAYPOINT_IS_TOO_FAR_AWAY (12):
            The waypoint is too far away.
        NOTIFICATION_TYPE_DEPTH_SET_POINT_IS_TOO_FAR_AWAY (13):
            The depth set point is too far away.
        NOTIFICATION_TYPE_TIME_TO_COMPLETE_IS_TOO_LONG (14):
            The time to complete the mission is too long.
        NOTIFICATION_TYPE_RETURNING_TO_HOME (15):
            Returning to home.
        NOTIFICATION_TYPE_GO_TO_SURFACE (16):
            Go to surface.
        NOTIFICATION_TYPE_GO_TO_SEABED (17):
            Go to seabed with an altimeter.
        NOTIFICATION_TYPE_GO_TO_WAYPOINT (18):
            Go to waypoint.
        NOTIFICATION_TYPE_GO_TO_DEPTH_SET_POINT (19):
            Go to depth set point.
        NOTIFICATION_TYPE_GO_TO_WAYPOINT_WITH_DEPTH_SET_POINT (20):
            Go to waypoint with depth set point.
        NOTIFICATION_TYPE_MISSION_STARTED (21):
            Mission is started.
        NOTIFICATION_TYPE_MISSION_PAUSED (22):
            Mission is paused.
        NOTIFICATION_TYPE_MISSION_RESUMED (23):
            Mission is resumed.
        NOTIFICATION_TYPE_MISSION_ABORTED (24):
            Mission is aborted.
        NOTIFICATION_TYPE_DRONE_IS_STUCK (25):
            Drone is stuck during a mission.
        NOTIFICATION_TYPE_WAIT_FOR (26):
            Wait for instruction running.
        NOTIFICATION_TYPE_CAMERA_ACTION (27):
            Camera action initiated.
        NOTIFICATION_TYPE_SET_TILT_MAIN_CAMERA (28):
            Set tilt for main camera.
        NOTIFICATION_TYPE_SET_TILT_MULTIBEAM (29):
            Set tilt for multibeam.
        NOTIFICATION_TYPE_INSTRUCTION_SKIPPED (30):
            When an instruction is not available in the
            ROV.
        NOTIFICATION_TYPE_DVL_HIGH_TEMPERATURE_DETECTED (31):
            DVL high temperature detected.
        NOTIFICATION_TYPE_DVL_THERMAL_PROTECTION_MODE_DETECTED (32):
            DVL thermal protection mode detected.
    """
    NOTIFICATION_TYPE_UNSPECIFIED = 0
    """Unspecified."""
    NOTIFICATION_TYPE_POSITION_ESTIMATE_IS_INACCURATE = 1
    """Position estimate is inaccurate."""
    NOTIFICATION_TYPE_DRONE_POSITION_IS_UNKNOWN = 2
    """Drone position is unknown."""
    NOTIFICATION_TYPE_USER_POSITION_IS_UNKNOWN = 3
    """User position is unknown."""
    NOTIFICATION_TYPE_NO_MISSION_LOADED = 4
    """No mission is loaded."""
    NOTIFICATION_TYPE_MISSION_LOADED = 5
    """Mission is loaded."""
    NOTIFICATION_TYPE_FAILED_TO_LOAD_MISSION = 6
    """Failed to load mission."""
    NOTIFICATION_TYPE_MISSION_COMPLETE = 7
    """Mission is complete."""
    NOTIFICATION_TYPE_INSTRUCTION_COMPLETE = 8
    """Instruction is complete."""
    NOTIFICATION_TYPE_WAYPOINT_REACHED = 9
    """Waypoint reached."""
    NOTIFICATION_TYPE_DEPTH_TARGET_REACHED = 10
    """Depth set point is reached."""
    NOTIFICATION_TYPE_ALTITUDE_TARGET_REACHED = 11
    """Altitude set point is reached."""
    NOTIFICATION_TYPE_WAYPOINT_IS_TOO_FAR_AWAY = 12
    """The waypoint is too far away."""
    NOTIFICATION_TYPE_DEPTH_SET_POINT_IS_TOO_FAR_AWAY = 13
    """The depth set point is too far away."""
    NOTIFICATION_TYPE_TIME_TO_COMPLETE_IS_TOO_LONG = 14
    """The time to complete the mission is too long."""
    NOTIFICATION_TYPE_RETURNING_TO_HOME = 15
    """Returning to home."""
    NOTIFICATION_TYPE_GO_TO_SURFACE = 16
    """Go to surface."""
    NOTIFICATION_TYPE_GO_TO_SEABED = 17
    """Go to seabed with an altimeter."""
    NOTIFICATION_TYPE_GO_TO_WAYPOINT = 18
    """Go to waypoint."""
    NOTIFICATION_TYPE_GO_TO_DEPTH_SET_POINT = 19
    """Go to depth set point."""
    NOTIFICATION_TYPE_GO_TO_WAYPOINT_WITH_DEPTH_SET_POINT = 20
    """Go to waypoint with depth set point."""
    NOTIFICATION_TYPE_MISSION_STARTED = 21
    """Mission is started."""
    NOTIFICATION_TYPE_MISSION_PAUSED = 22
    """Mission is paused."""
    NOTIFICATION_TYPE_MISSION_RESUMED = 23
    """Mission is resumed."""
    NOTIFICATION_TYPE_MISSION_ABORTED = 24
    """Mission is aborted."""
    NOTIFICATION_TYPE_DRONE_IS_STUCK = 25
    """Drone is stuck during a mission."""
    NOTIFICATION_TYPE_WAIT_FOR = 26
    """Wait for instruction running."""
    NOTIFICATION_TYPE_CAMERA_ACTION = 27
    """Camera action initiated."""
    NOTIFICATION_TYPE_SET_TILT_MAIN_CAMERA = 28
    """Set tilt for main camera."""
    NOTIFICATION_TYPE_SET_TILT_MULTIBEAM = 29
    """Set tilt for multibeam."""
    NOTIFICATION_TYPE_INSTRUCTION_SKIPPED = 30
    """When an instruction is not available in the ROV."""
    NOTIFICATION_TYPE_DVL_HIGH_TEMPERATURE_DETECTED = 31
    """DVL high temperature detected."""
    NOTIFICATION_TYPE_DVL_THERMAL_PROTECTION_MODE_DETECTED = 32
    """DVL thermal protection mode detected."""


class NotificationLevel(proto.Enum):
    r"""List of available notification levels.

    Attributes:
        NOTIFICATION_LEVEL_UNSPECIFIED (0):
            Unspecified.
        NOTIFICATION_LEVEL_INFO (1):
            Information.
        NOTIFICATION_LEVEL_WARNING (2):
            Warning.
        NOTIFICATION_LEVEL_ERROR (3):
            Error.
    """
    NOTIFICATION_LEVEL_UNSPECIFIED = 0
    """Unspecified."""
    NOTIFICATION_LEVEL_INFO = 1
    """Information."""
    NOTIFICATION_LEVEL_WARNING = 2
    """Warning."""
    NOTIFICATION_LEVEL_ERROR = 3
    """Error."""


class Model(proto.Enum):
    r"""Drone models produced by Blueye.

    Attributes:
        MODEL_UNSPECIFIED (0):
            ModelName not specified.
        MODEL_PIONEER (1):
            Blueye Pioneer, the first model.
        MODEL_PRO (2):
            Blueye Pro, features camera tilt.
        MODEL_X1 (4):
            Blueye X1, features camera tilt and one guest
            port.
        MODEL_X3 (3):
            Blueye X3, features support for peripherals.
        MODEL_X3_ULTRA (6):
            Blueye X3 Ultra.
        MODEL_NEXT (5):
            Blueye ?
    """
    MODEL_UNSPECIFIED = 0
    """ModelName not specified."""
    MODEL_PIONEER = 1
    """Blueye Pioneer, the first model."""
    MODEL_PRO = 2
    """Blueye Pro, features camera tilt."""
    MODEL_X1 = 4
    """Blueye X1, features camera tilt and one guest port."""
    MODEL_X3 = 3
    """Blueye X3, features support for peripherals."""
    MODEL_X3_ULTRA = 6
    """Blueye X3 Ultra."""
    MODEL_NEXT = 5
    """Blueye ?"""


class PressureSensorType(proto.Enum):
    r"""Depth sensors used by the drone.

    Attributes:
        PRESSURE_SENSOR_TYPE_UNSPECIFIED (0):
            Depth sensor type not specified.
        PRESSURE_SENSOR_TYPE_NOT_CONNECTED (1):
            No sensor connected.
        PRESSURE_SENSOR_TYPE_MS5837_30BA26 (2):
            Thh MS5837 30BA26 pressure sensor.
        PRESSURE_SENSOR_TYPE_KELLER_PA7LD (3):
            The extended depth sensor using the Keller
            PA7LD pressure sensor.
        PRESSURE_SENSOR_TYPE_MS5637_02BA03 (4):
            The internal pressure sensor using the MS5637
            02BA03 pressure sensor.
    """
    PRESSURE_SENSOR_TYPE_UNSPECIFIED = 0
    """Depth sensor type not specified."""
    PRESSURE_SENSOR_TYPE_NOT_CONNECTED = 1
    """No sensor connected."""
    PRESSURE_SENSOR_TYPE_MS5837_30BA26 = 2
    """Thh MS5837 30BA26 pressure sensor."""
    PRESSURE_SENSOR_TYPE_KELLER_PA7LD = 3
    """The extended depth sensor using the Keller PA7LD pressure
    sensor."""
    PRESSURE_SENSOR_TYPE_MS5637_02BA03 = 4
    """The internal pressure sensor using the MS5637 02BA03 pressure
    sensor."""


class Resolution(proto.Enum):
    r"""Available camera resolutions.

    Attributes:
        RESOLUTION_UNSPECIFIED (0):
            Resolution not specified.
        RESOLUTION_FULLHD_1080P (1):
            1080p Full HD resolution.
        RESOLUTION_HD_720P (2):
            720p HD resolution.
        RESOLUTION_UHD_4K (3):
            4K Ultra HD resolution.
    """
    RESOLUTION_UNSPECIFIED = 0
    """Resolution not specified."""
    RESOLUTION_FULLHD_1080P = 1
    """1080p Full HD resolution."""
    RESOLUTION_HD_720P = 2
    """720p HD resolution."""
    RESOLUTION_UHD_4K = 3
    """4K Ultra HD resolution."""


class Framerate(proto.Enum):
    r"""Available camera frame rates.

    Attributes:
        FRAMERATE_UNSPECIFIED (0):
            Framerate not specified.
        FRAMERATE_FPS_30 (1):
            30 frames per second.
        FRAMERATE_FPS_25 (2):
            25 frames per second.
    """
    FRAMERATE_UNSPECIFIED = 0
    """Framerate not specified."""
    FRAMERATE_FPS_30 = 1
    """30 frames per second."""
    FRAMERATE_FPS_25 = 2
    """25 frames per second."""


class Camera(proto.Enum):
    r"""Which camera to control.

    Attributes:
        CAMERA_UNSPECIFIED (0):
            Camera not specified.
        CAMERA_MAIN (1):
            Main camera.
        CAMERA_GUESTPORT (2):
            Guest port camera.
    """
    CAMERA_UNSPECIFIED = 0
    """Camera not specified."""
    CAMERA_MAIN = 1
    """Main camera."""
    CAMERA_GUESTPORT = 2
    """Guest port camera."""


class TemperatureUnit(proto.Enum):
    r"""Available temperature units.

    Attributes:
        TEMPERATURE_UNIT_UNSPECIFIED (0):
            Temperature unit not specified.
        TEMPERATURE_UNIT_CELSIUS (1):
            Temperature should be displayed as Celsius.
        TEMPERATURE_UNIT_FAHRENHEIT (2):
            Temperature should be displayed as
            Fahrenheit.
    """
    TEMPERATURE_UNIT_UNSPECIFIED = 0
    """Temperature unit not specified."""
    TEMPERATURE_UNIT_CELSIUS = 1
    """Temperature should be displayed as Celsius."""
    TEMPERATURE_UNIT_FAHRENHEIT = 2
    """Temperature should be displayed as Fahrenheit."""


class LogoType(proto.Enum):
    r"""Available logo types.

    Attributes:
        LOGO_TYPE_UNSPECIFIED (0):
            Logo type not specified
        LOGO_TYPE_NONE (1):
            Do not add any logo.
        LOGO_TYPE_DEFAULT (2):
            Add default logo.
        LOGO_TYPE_CUSTOM (3):
            Add user defined logo.
    """
    LOGO_TYPE_UNSPECIFIED = 0
    """Logo type not specified"""
    LOGO_TYPE_NONE = 1
    """Do not add any logo."""
    LOGO_TYPE_DEFAULT = 2
    """Add default logo."""
    LOGO_TYPE_CUSTOM = 3
    """Add user defined logo."""


class DepthUnit(proto.Enum):
    r"""Available depth units.

    Attributes:
        DEPTH_UNIT_UNSPECIFIED (0):
            Depth unit not specified.
        DEPTH_UNIT_METERS (1):
            Depth should be displayed as meters.
        DEPTH_UNIT_FEET (2):
            Depth should be displayed as feet.
    """
    DEPTH_UNIT_UNSPECIFIED = 0
    """Depth unit not specified."""
    DEPTH_UNIT_METERS = 1
    """Depth should be displayed as meters."""
    DEPTH_UNIT_FEET = 2
    """Depth should be displayed as feet."""


class ThicknessUnit(proto.Enum):
    r"""Available thickness units.

    Attributes:
        THICKNESS_UNIT_UNSPECIFIED (0):
            Thickness unit not specified.
        THICKNESS_UNIT_MILLIMETERS (1):
            Thickness should be displayed as millimeters.
        THICKNESS_UNIT_INCHES (2):
            Thickness should be displayed as inches.
    """
    THICKNESS_UNIT_UNSPECIFIED = 0
    """Thickness unit not specified."""
    THICKNESS_UNIT_MILLIMETERS = 1
    """Thickness should be displayed as millimeters."""
    THICKNESS_UNIT_INCHES = 2
    """Thickness should be displayed as inches."""


class FontSize(proto.Enum):
    r"""Available font sizes for overlay text elements.

    Attributes:
        FONT_SIZE_UNSPECIFIED (0):
            Font size not specified.
        FONT_SIZE_PX15 (1):
            15 px.
        FONT_SIZE_PX20 (2):
            20 px.
        FONT_SIZE_PX25 (3):
            25 px.
        FONT_SIZE_PX30 (4):
            30 px.
        FONT_SIZE_PX35 (5):
            35 px.
        FONT_SIZE_PX40 (6):
            40 px.
    """
    FONT_SIZE_UNSPECIFIED = 0
    """Font size not specified."""
    FONT_SIZE_PX15 = 1
    """15 px."""
    FONT_SIZE_PX20 = 2
    """20 px."""
    FONT_SIZE_PX25 = 3
    """25 px."""
    FONT_SIZE_PX30 = 4
    """30 px."""
    FONT_SIZE_PX35 = 5
    """35 px."""
    FONT_SIZE_PX40 = 6
    """40 px."""


class GuestPortDeviceID(proto.Enum):
    r"""Complete set of supported guest port devices.

    Attributes:
        GUEST_PORT_DEVICE_ID_UNSPECIFIED (0):
            Unspecified.
        GUEST_PORT_DEVICE_ID_BLIND_PLUG (1):
            Blueye Blind Plug.
        GUEST_PORT_DEVICE_ID_TEST_STATION (2):
            Blueye Test Station.
        GUEST_PORT_DEVICE_ID_DEBUG_SERIAL (3):
            Blueye Debug Serial.
        GUEST_PORT_DEVICE_ID_BLUEYE_LIGHT (4):
            Blueye Light.
        GUEST_PORT_DEVICE_ID_BLUEYE_CAM (5):
            Blueye Camera.
        GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_LUMEN (6):
            Blue Robotics Lumen.
        GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_NEWTON (7):
            Blue Robotics Newton.
        GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_PING_SONAR (8):
            Blue Robotics Ping Sonar.
        GUEST_PORT_DEVICE_ID_BLUEPRINT_LAB_REACH_ALPHA (9):
            Blueprint Lab Reach Alpha.
        GUEST_PORT_DEVICE_ID_WATERLINKED_DVL_A50 (10):
            Waterlinked DVL A50.
        GUEST_PORT_DEVICE_ID_IMPACT_SUBSEA_ISS360 (11):
            Impact Subsea ISS360 Sonar.
        GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_SEATRAC_X010 (12):
            Blueprint Subsea Seatrac X110.
        GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_M750D (13):
            Blueprint Subsea Oculus M750d.
        GUEST_PORT_DEVICE_ID_CYGNUS_MINI_ROV_THICKNESS_GAUGE (14):
            Cygnus Mini ROV Thickness Gauge.
        GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_PING360_SONAR (15):
            Blue Robotics Ping360 Scanning Imaging Sonar.
        GUEST_PORT_DEVICE_ID_TRITECH_GEMINI_720IM (16):
            Tritech Gemini 720im Multibeam Sonar.
        GUEST_PORT_DEVICE_ID_BLUEYE_LIGHT_PAIR (17):
            Blueye Light Pair.
        GUEST_PORT_DEVICE_ID_TRITECH_GEMINI_MICRON (18):
            Tritech Micron Gemini.
        GUEST_PORT_DEVICE_ID_OCEAN_TOOLS_DIGICP (19):
            Ocean Tools DigiCP.
        GUEST_PORT_DEVICE_ID_TRITECH_GEMINI_720IK (20):
            Tritech Gemini 720ik Multibeam Sonar.
        GUEST_PORT_DEVICE_ID_NORTEK_NUCLEUS_1000 (21):
            Nortek Nucleus 1000 DVL.
        GUEST_PORT_DEVICE_ID_BLUEYE_GENERIC_SERVO (22):
            Blueye Generic Servo.
        GUEST_PORT_DEVICE_ID_BLUEYE_MULTIBEAM_SERVO (23):
            Blueye Multibeam Skid Servo.
        GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_DETACHABLE_NEWTON (24):
            Detachable Blue Robotics Newton.
        GUEST_PORT_DEVICE_ID_INSITU_AQUA_TROLL_500 (25):
            In-Situ Aqua TROLL 500.
        GUEST_PORT_DEVICE_ID_MEDUSA_RADIOMETRICS_MS100 (26):
            Medusa Radiometrics Gamma Ray Sensor.
        GUEST_PORT_DEVICE_ID_LASER_TOOLS_SEA_BEAM (27):
            Laser Tools Sea Beam Underwater Laser.
        GUEST_PORT_DEVICE_ID_SPOT_X_LASER_SCALERS (28):
            Spot X Laser Scalers.
        GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_M1200D (29):
            Blueprint Subsea Oculus M1200d.
        GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_M3000D (30):
            Blueprint Subsea Oculus M3000d.
        GUEST_PORT_DEVICE_ID_INSITU_AQUA_TROLL_100 (31):
            In-Situ Aqua TROLL 100.
        GUEST_PORT_DEVICE_ID_INSITU_RDO_PRO_X (32):
            In-Situ RDO PRO-X.
        GUEST_PORT_DEVICE_ID_INSITU_RDO_BLUE (33):
            In-Situ RDO Blue.
        GUEST_PORT_DEVICE_ID_BLUEYE_CAMERA_SERVO (34):
            Blueye Camera Servo.
        GUEST_PORT_DEVICE_ID_BLUEYE_MULTIBEAM_HEAD_SERVO (35):
            Blueye Multibeam Head Servo.
        GUEST_PORT_DEVICE_ID_CERULEAN_OMNISCAN_450FS (36):
            Cerulean Omniscan 450 FS.
        GUEST_PORT_DEVICE_ID_CERULEAN_OMNISCAN_450SS (37):
            Cerulean Omniscan 450 SS.
        GUEST_PORT_DEVICE_ID_BLUEYE_GNSS_DEVICE (38):
            Blueye GNSS device.
        GUEST_PORT_DEVICE_ID_WATERLINKED_DVL_A50_600 (39):
            Waterlinked DVL A50 600m.
        GUEST_PORT_DEVICE_ID_IMAGENEX_831L (40):
            Imagenex 831L Pipe Profiling Sonar.
        GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_C550D (41):
            Blueprint Subsea Oculus C550d.
        GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_M370S (42):
            Blueprint Subsea Oculus M370s.
        GUEST_PORT_DEVICE_ID_WATERLINKED_SONAR_3D15 (43):
            Waterlinked Sonar 3D-15.
    """
    GUEST_PORT_DEVICE_ID_UNSPECIFIED = 0
    """Unspecified."""
    GUEST_PORT_DEVICE_ID_BLIND_PLUG = 1
    """Blueye Blind Plug."""
    GUEST_PORT_DEVICE_ID_TEST_STATION = 2
    """Blueye Test Station."""
    GUEST_PORT_DEVICE_ID_DEBUG_SERIAL = 3
    """Blueye Debug Serial."""
    GUEST_PORT_DEVICE_ID_BLUEYE_LIGHT = 4
    """Blueye Light."""
    GUEST_PORT_DEVICE_ID_BLUEYE_CAM = 5
    """Blueye Camera."""
    GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_LUMEN = 6
    """Blue Robotics Lumen."""
    GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_NEWTON = 7
    """Blue Robotics Newton."""
    GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_PING_SONAR = 8
    """Blue Robotics Ping Sonar."""
    GUEST_PORT_DEVICE_ID_BLUEPRINT_LAB_REACH_ALPHA = 9
    """Blueprint Lab Reach Alpha."""
    GUEST_PORT_DEVICE_ID_WATERLINKED_DVL_A50 = 10
    """Waterlinked DVL A50."""
    GUEST_PORT_DEVICE_ID_IMPACT_SUBSEA_ISS360 = 11
    """Impact Subsea ISS360 Sonar."""
    GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_SEATRAC_X010 = 12
    """Blueprint Subsea Seatrac X110."""
    GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_M750D = 13
    """Blueprint Subsea Oculus M750d."""
    GUEST_PORT_DEVICE_ID_CYGNUS_MINI_ROV_THICKNESS_GAUGE = 14
    """Cygnus Mini ROV Thickness Gauge."""
    GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_PING360_SONAR = 15
    """Blue Robotics Ping360 Scanning Imaging Sonar."""
    GUEST_PORT_DEVICE_ID_TRITECH_GEMINI_720IM = 16
    """Tritech Gemini 720im Multibeam Sonar."""
    GUEST_PORT_DEVICE_ID_BLUEYE_LIGHT_PAIR = 17
    """Blueye Light Pair."""
    GUEST_PORT_DEVICE_ID_TRITECH_GEMINI_MICRON = 18
    """Tritech Micron Gemini."""
    GUEST_PORT_DEVICE_ID_OCEAN_TOOLS_DIGICP = 19
    """Ocean Tools DigiCP."""
    GUEST_PORT_DEVICE_ID_TRITECH_GEMINI_720IK = 20
    """Tritech Gemini 720ik Multibeam Sonar."""
    GUEST_PORT_DEVICE_ID_NORTEK_NUCLEUS_1000 = 21
    """Nortek Nucleus 1000 DVL."""
    GUEST_PORT_DEVICE_ID_BLUEYE_GENERIC_SERVO = 22
    """Blueye Generic Servo."""
    GUEST_PORT_DEVICE_ID_BLUEYE_MULTIBEAM_SERVO = 23
    """Blueye Multibeam Skid Servo."""
    GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_DETACHABLE_NEWTON = 24
    """Detachable Blue Robotics Newton."""
    GUEST_PORT_DEVICE_ID_INSITU_AQUA_TROLL_500 = 25
    """In-Situ Aqua TROLL 500."""
    GUEST_PORT_DEVICE_ID_MEDUSA_RADIOMETRICS_MS100 = 26
    """Medusa Radiometrics Gamma Ray Sensor."""
    GUEST_PORT_DEVICE_ID_LASER_TOOLS_SEA_BEAM = 27
    """Laser Tools Sea Beam Underwater Laser."""
    GUEST_PORT_DEVICE_ID_SPOT_X_LASER_SCALERS = 28
    """Spot X Laser Scalers."""
    GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_M1200D = 29
    """Blueprint Subsea Oculus M1200d."""
    GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_M3000D = 30
    """Blueprint Subsea Oculus M3000d."""
    GUEST_PORT_DEVICE_ID_INSITU_AQUA_TROLL_100 = 31
    """In-Situ Aqua TROLL 100."""
    GUEST_PORT_DEVICE_ID_INSITU_RDO_PRO_X = 32
    """In-Situ RDO PRO-X."""
    GUEST_PORT_DEVICE_ID_INSITU_RDO_BLUE = 33
    """In-Situ RDO Blue."""
    GUEST_PORT_DEVICE_ID_BLUEYE_CAMERA_SERVO = 34
    """Blueye Camera Servo."""
    GUEST_PORT_DEVICE_ID_BLUEYE_MULTIBEAM_HEAD_SERVO = 35
    """Blueye Multibeam Head Servo."""
    GUEST_PORT_DEVICE_ID_CERULEAN_OMNISCAN_450FS = 36
    """Cerulean Omniscan 450 FS."""
    GUEST_PORT_DEVICE_ID_CERULEAN_OMNISCAN_450SS = 37
    """Cerulean Omniscan 450 SS."""
    GUEST_PORT_DEVICE_ID_BLUEYE_GNSS_DEVICE = 38
    """Blueye GNSS device."""
    GUEST_PORT_DEVICE_ID_WATERLINKED_DVL_A50_600 = 39
    """Waterlinked DVL A50 600m."""
    GUEST_PORT_DEVICE_ID_IMAGENEX_831L = 40
    """Imagenex 831L Pipe Profiling Sonar."""
    GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_C550D = 41
    """Blueprint Subsea Oculus C550d."""
    GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_M370S = 42
    """Blueprint Subsea Oculus M370s."""
    GUEST_PORT_DEVICE_ID_WATERLINKED_SONAR_3D15 = 43
    """Waterlinked Sonar 3D-15."""


class GuestPortNumber(proto.Enum):
    r"""Guest port number.

    Attributes:
        GUEST_PORT_NUMBER_UNSPECIFIED (0):
            Unspecified.
        GUEST_PORT_NUMBER_PORT_1 (1):
            Guest port 1.
        GUEST_PORT_NUMBER_PORT_2 (2):
            Guest port 2.
        GUEST_PORT_NUMBER_PORT_3 (3):
            Guest port 3.
    """
    GUEST_PORT_NUMBER_UNSPECIFIED = 0
    """Unspecified."""
    GUEST_PORT_NUMBER_PORT_1 = 1
    """Guest port 1."""
    GUEST_PORT_NUMBER_PORT_2 = 2
    """Guest port 2."""
    GUEST_PORT_NUMBER_PORT_3 = 3
    """Guest port 3."""


class NavigationSensorID(proto.Enum):
    r"""List of navigation sensors that can be used by the position
    observer.

    Attributes:
        NAVIGATION_SENSOR_ID_UNSPECIFIED (0):
            Unspecified.
        NAVIGATION_SENSOR_ID_WATERLINKED_DVL_A50 (1):
            Water Linked DVL A50.
        NAVIGATION_SENSOR_ID_WATERLINKED_UGPS_G2 (2):
            Water Linked UGPS G2.
        NAVIGATION_SENSOR_ID_NMEA (3):
            NMEA stream from external positioning system.
        NAVIGATION_SENSOR_ID_BLUEYE_GNSS (4):
            Blueye GNSS device on the ROV.
        NAVIGATION_SENSOR_ID_NORTEK_DVL_NUCLEUS (5):
            Nortek DVL Nucleus 1000.
    """
    NAVIGATION_SENSOR_ID_UNSPECIFIED = 0
    """Unspecified."""
    NAVIGATION_SENSOR_ID_WATERLINKED_DVL_A50 = 1
    """Water Linked DVL A50."""
    NAVIGATION_SENSOR_ID_WATERLINKED_UGPS_G2 = 2
    """Water Linked UGPS G2."""
    NAVIGATION_SENSOR_ID_NMEA = 3
    """NMEA stream from external positioning system."""
    NAVIGATION_SENSOR_ID_BLUEYE_GNSS = 4
    """Blueye GNSS device on the ROV."""
    NAVIGATION_SENSOR_ID_NORTEK_DVL_NUCLEUS = 5
    """Nortek DVL Nucleus 1000."""


class GuestPortDetachStatus(proto.Enum):
    r"""Status for guest port devices that can be attached and
    detached.

    Attributes:
        GUEST_PORT_DETACH_STATUS_UNSPECIFIED (0):
            Unspecified (Default for non-detachable
            devices).
        GUEST_PORT_DETACH_STATUS_ATTACHED (1):
            Detachable device attached.
        GUEST_PORT_DETACH_STATUS_DETACHED (2):
            Detachable device detached.
    """
    GUEST_PORT_DETACH_STATUS_UNSPECIFIED = 0
    """Unspecified (Default for non-detachable devices)."""
    GUEST_PORT_DETACH_STATUS_ATTACHED = 1
    """Detachable device attached."""
    GUEST_PORT_DETACH_STATUS_DETACHED = 2
    """Detachable device detached."""


class GuestPortError(proto.Enum):
    r"""GuestPort error types.

    Only indicated errors on the guest port connector itself.

    Attributes:
        GUEST_PORT_ERROR_UNSPECIFIED (0):
            Unspecified value.
        GUEST_PORT_ERROR_NOT_CONNECTED (1):
            Device not connected.
        GUEST_PORT_ERROR_READ_ERROR (2):
            EEPROM read error.
        GUEST_PORT_ERROR_NOT_FLASHED (3):
            Connector not flashed.
        GUEST_PORT_ERROR_CRC_ERROR (4):
            Wrong CRC for protobuf message.
        GUEST_PORT_ERROR_PARSE_ERROR (5):
            Protobuf message cannot be parsed.
    """
    GUEST_PORT_ERROR_UNSPECIFIED = 0
    """Unspecified value."""
    GUEST_PORT_ERROR_NOT_CONNECTED = 1
    """Device not connected."""
    GUEST_PORT_ERROR_READ_ERROR = 2
    """EEPROM read error."""
    GUEST_PORT_ERROR_NOT_FLASHED = 3
    """Connector not flashed."""
    GUEST_PORT_ERROR_CRC_ERROR = 4
    """Wrong CRC for protobuf message."""
    GUEST_PORT_ERROR_PARSE_ERROR = 5
    """Protobuf message cannot be parsed."""


class MultibeamFrequencyMode(proto.Enum):
    r"""The frequency mode to use for multibeam devices with dual
    frequency.

    Attributes:
        MULTIBEAM_FREQUENCY_MODE_UNSPECIFIED (0):
            No description available.
        MULTIBEAM_FREQUENCY_MODE_AUTO (1):
            Auto switching mode (if available).
        MULTIBEAM_FREQUENCY_MODE_LOW_FREQUENCY (2):
            Low frequency mode (wide aperture,
            navigation).
        MULTIBEAM_FREQUENCY_MODE_HIGH_FREQUENCY (3):
            High frequency mode (narrow aperture, target
            identification).
    """
    MULTIBEAM_FREQUENCY_MODE_UNSPECIFIED = 0
    MULTIBEAM_FREQUENCY_MODE_AUTO = 1
    """Auto switching mode (if available)."""
    MULTIBEAM_FREQUENCY_MODE_LOW_FREQUENCY = 2
    """Low frequency mode (wide aperture, navigation)."""
    MULTIBEAM_FREQUENCY_MODE_HIGH_FREQUENCY = 3
    """High frequency mode (narrow aperture, target identification)."""


class BinlogRecord(proto.Message):
    r"""Wrapper message for each entry in the drone telemetry
    logfile.
    Each entry contains the unix timestamp in UTC, the monotonic
    timestamp (time since boot), and an Any message wrapping the
    custom Blueye message.

    See separate documentation for the logfile format for more
    details.

    Attributes:
        payload (google.protobuf.any_pb2.Any):
            The log entry payload.
        unix_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Unix timestamp in UTC.
        clock_monotonic (google.protobuf.timestamp_pb2.Timestamp):
            Posix CLOCK_MONOTONIC timestamp.
    """

    payload: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=1,
        message=any_pb2.Any,
    )
    unix_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    clock_monotonic: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class MotionInput(proto.Message):
    r"""If you use both values at the same time they cancel each
    other out.

    Attributes:
        surge (float):
            Forward (positive) and backwards (negative)
            movement. (-1..1).
        sway (float):
            Right (positive) and left (negative) lateral
            movement (-1..1).
        heave (float):
            Descend (positive) and ascend (negative)
            movement (-1..1).
        roll (float):
            Roll left (negative) or right (positive).
            (-1..1).
        pitch (float):
            Pitch down (negative) or up (positive).
            (-1..1).
        yaw (float):
            Left (positive) and right (negative) movement
            (-1..1).
        slow (float):
            Modifier used to reduce the speed of the
            motion (0..1).
        boost (float):
            Modifier used to increase the speed of the
            motion (0..1).
    """

    surge: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    sway: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    heave: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    roll: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    pitch: float = proto.Field(
        proto.FLOAT,
        number=8,
    )
    yaw: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    slow: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    boost: float = proto.Field(
        proto.FLOAT,
        number=6,
    )


class Lights(proto.Message):
    r"""Lights message used to represent the intensity of the main
    light or external lights.

    Attributes:
        value (float):
            Light intensity (0..1).
    """

    value: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class Laser(proto.Message):
    r"""Laser message used to represent the intensity of connected
    laser.
    If the laser does not support dimming but only on and off, a
    value of 0 turns the laser off, and any value above 0 turns the
    laser on.

    Attributes:
        value (float):
            Laser intensity, any value above 0 turns the
            laser on (0..1).
    """

    value: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class LatLongPosition(proto.Message):
    r"""Latitude and longitude position in WGS 84 decimal degrees
    format.

    Attributes:
        latitude (float):
            Latitude (°).
        longitude (float):
            Longitude (°).
    """

    latitude: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    longitude: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


class ConnectionDuration(proto.Message):
    r"""Connection duration of a remote client.

    Attributes:
        value (int):
            Time since connected to drone (s).
    """

    value: int = proto.Field(
        proto.INT32,
        number=1,
    )


class AutoHeadingState(proto.Message):
    r"""Auto heading state.

    Attributes:
        enabled (bool):
            If auto heading is enabled.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class AutoDepthState(proto.Message):
    r"""Auto depth state.

    Attributes:
        enabled (bool):
            If auto depth is enabled.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class AutoAltitudeState(proto.Message):
    r"""Auto altitude state.

    Attributes:
        enabled (bool):
            If auto altitude is enabled.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class StationKeepingState(proto.Message):
    r"""Station keeping state.

    Attributes:
        enabled (bool):
            If station keeping is enabled.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class WeatherVaningState(proto.Message):
    r"""Weather vaning state.

    Attributes:
        enabled (bool):
            If weather vaning is enabled.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class AutoPilotSurgeYawState(proto.Message):
    r"""Auto pilot surge yaw state.

    Attributes:
        enabled (bool):
            If auto pilot surge yaw is enabled.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class AutoPilotHeaveState(proto.Message):
    r"""Auto pilot heave state.

    Attributes:
        enabled (bool):
            If auto pilot heave is enabled.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class ControlMode(proto.Message):
    r"""Control mode from drone supervisor

    Attributes:
        auto_depth (bool):
            If auto depth is enabled.
        auto_heading (bool):
            If auto heading is enabled.
        auto_altitude (bool):
            If auto altitude is enabled.
        station_keeping (bool):
            If station keeping is enabled.
        weather_vaning (bool):
            If weather vaning is enabled.
        auto_pilot_surge_yaw (bool):
            If auto pilot surge yaw is enabled.
        auto_pilot_heave (bool):
            If auto pilot heave is enabled.
    """

    auto_depth: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    auto_heading: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    auto_altitude: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    station_keeping: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    weather_vaning: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    auto_pilot_surge_yaw: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    auto_pilot_heave: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class TiltStabilizationState(proto.Message):
    r"""Tilt stabilization state.

    Blueye drones with mechanical tilt has the ability to enable
    camera stabilization.

    Attributes:
        enabled (bool):
            If tilt stabilization is enabled.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class SystemTime(proto.Message):
    r"""System time.

    Attributes:
        unix_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Unix timestamp.
    """

    unix_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


class GripperVelocities(proto.Message):
    r"""Gripper velocity values.

    Rotating velocity is only used if the gripper supports rotation.

    Attributes:
        grip_velocity (float):
            The gripping velocity (-1.0..1.0).
        rotate_velocity (float):
            The rotating velocity (-1.0..1.0).
    """

    grip_velocity: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    rotate_velocity: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class ClientInfo(proto.Message):
    r"""Information about a remote client.

    Attributes:
        type_ (str):
            The type of client (such as Blueye App,
            Observer App, SDK, etc).
        version (str):
            Client software version string.
        device_type (str):
            Device type, such as mobile, tablet, or
            computer.
        platform (str):
            Platform, such as iOS, Android, Linux, etc.
        platform_version (str):
            Platform software version string.
        name (str):
            Name of the client.
        is_observer (bool):
            If the client should be connected as an
            observer or not.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    device_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    platform: str = proto.Field(
        proto.STRING,
        number=4,
    )
    platform_version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    is_observer: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class ConnectedClient(proto.Message):
    r"""Information about a connected client with an id assigned by
    the drone.

    Attributes:
        client_id (int):
            The assigned client id.
        client_info (blueye.protocol.types.ClientInfo):
            Client information.
    """

    client_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    client_info: 'ClientInfo' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='ClientInfo',
    )


class RecordState(proto.Message):
    r"""Camera recording state.

    Attributes:
        main_is_recording (bool):
            If the main camera is recording.
        main_seconds (int):
            Main record time (s).
        main_fps (float):
            Main record fps.
        guestport_is_recording (bool):
            If the guestport camera is recording.
        guestport_seconds (int):
            Guestport record time (s).
        guestport_fps (float):
            Guestport record fps.
        multibeam_is_recording (bool):
            If the multibeam is recording.
        multibeam_seconds (int):
            Multibeam record time (s).
        multibeam_fps (float):
            Multibeam record fps.
    """

    main_is_recording: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    main_seconds: int = proto.Field(
        proto.INT32,
        number=2,
    )
    main_fps: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    guestport_is_recording: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    guestport_seconds: int = proto.Field(
        proto.INT32,
        number=4,
    )
    guestport_fps: float = proto.Field(
        proto.FLOAT,
        number=8,
    )
    multibeam_is_recording: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    multibeam_seconds: int = proto.Field(
        proto.INT32,
        number=6,
    )
    multibeam_fps: float = proto.Field(
        proto.FLOAT,
        number=9,
    )


class TimeLapseState(proto.Message):
    r"""Time-lapse state published if time-lapse mission is running.

    Attributes:
        interval (float):
            Interval between photos.
        photos_taken (int):
            Number of photos taken.
        interval_type (blueye.protocol.types.IntervalType):
            Interval type for photos, distance or time.
    """

    interval: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    photos_taken: int = proto.Field(
        proto.INT32,
        number=2,
    )
    interval_type: 'IntervalType' = proto.Field(
        proto.ENUM,
        number=3,
        enum='IntervalType',
    )


class WaterDensity(proto.Message):
    r"""Water density.

    Used to specify the water density the drone is operating in, to
    achieve more accurate depth measurements, f. ex. influenced by
    salinity.

    Attributes:
        value (float):
            Water density (g/l).
    """

    value: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class PingerConfiguration(proto.Message):
    r"""Pinger configuration.

    Used to specify the configuration the BR 1D-Pinger.

    Attributes:
        mounting_direction (blueye.protocol.types.PingerConfiguration.MountingDirection):
            Mounting direction of the pinger.
    """
    class MountingDirection(proto.Enum):
        r"""

        Attributes:
            MOUNTING_DIRECTION_UNSPECIFIED (0):
                Mounting direction is unspecified.
            MOUNTING_DIRECTION_FORWARDS (1):
                Pointing forwards from the drones
                perspective.
            MOUNTING_DIRECTION_DOWNWARDS (2):
                Pointing downwards from the drones
                perspective.
        """
        MOUNTING_DIRECTION_UNSPECIFIED = 0
        """Mounting direction is unspecified."""
        MOUNTING_DIRECTION_FORWARDS = 1
        """Pointing forwards from the drones perspective."""
        MOUNTING_DIRECTION_DOWNWARDS = 2
        """Pointing downwards from the drones perspective."""

    mounting_direction: MountingDirection = proto.Field(
        proto.ENUM,
        number=1,
        enum=MountingDirection,
    )


class WaterTemperature(proto.Message):
    r"""Water temperature measured by the drone's combined depth and
    temperature sensor.

    Attributes:
        value (float):
            Water temperature (°C).
    """

    value: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class CPUTemperature(proto.Message):
    r"""CPU temperature.

    Attributes:
        value (float):
            CPU temperature (°C).
    """

    value: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class CanisterTemperature(proto.Message):
    r"""Canister temperature.

    Temperature measured in the top or bottom canister of the drone.

    Attributes:
        temperature (float):
            Temperature (°C).
    """

    temperature: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


class CanisterHumidity(proto.Message):
    r"""Canister humidity.

    Humidity measured in the top or bottom canister of the drone.

    Attributes:
        humidity (float):
            Air humidity (%).
    """

    humidity: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


class Battery(proto.Message):
    r"""Essential battery information.

    Attributes:
        voltage (float):
            Battery voltage (V).
        level (float):
            Battery level (0..1).
        temperature (float):
            Battery temperature (°C).
    """

    voltage: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    level: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    temperature: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


class BatteryBQ40Z50(proto.Message):
    r"""Battery information message.

    Detailed information about all aspects of the connected Blueye
    Smart Battery, using the BQ40Z50 BMS.

    Attributes:
        voltage (blueye.protocol.types.BatteryBQ40Z50.Voltage):
            Voltage of the battery cells.
        temperature (blueye.protocol.types.BatteryBQ40Z50.Temperature):
            Temperature of the battery cells.
        status (blueye.protocol.types.BatteryBQ40Z50.BatteryStatus):
            Battery status flags.
        current (float):
            Measured current from the coulomb counter
            (A).
        average_current (float):
            Average current (A).
        relative_state_of_charge (float):
            Predicted remaining battery capacity as a
            factor of full capacity (0..1).
        absolute_state_of_charge (float):
            Predicted remaining battery capacity (0..1).
        calculated_state_of_charge (float):
            Calculated state of charge (0..1).
        remaining_capacity (float):
            Predicted remaining battery capacity (Ah).
        full_charge_capacity (float):
            Predicted battery capacity when fully charged
            (Ah).
        runtime_to_empty (int):
            Predicted remaining battery capacity based on
            the present rate of discharge (s).
        average_time_to_empty (int):
            Predicted remaining battery capacity based on
            average_current (s).
        average_time_to_full (int):
            Predicted time-to-full charge based on average_current (s).
        charging_current (float):
            Desired charging current (A).
        charging_voltage (float):
            Desired charging voltage (V).
        cycle_count (int):
            Number of charging cycles.
        design_capacity (float):
            Design capacity (Ah).
        manufacture_date (google.protobuf.timestamp_pb2.Timestamp):
            Manufacture date.
        serial_number (int):
            Serial number.
        manufacturer_name (str):
            Manufacturer name.
        device_name (str):
            Device name.
        device_chemistry (str):
            Battery chemistry.
        lifetimes (blueye.protocol.types.BatteryBQ40Z50.BatteryLifetimes):
            Battery lifetimes.
        safety_events (blueye.protocol.types.BatteryBQ40Z50.BatterySafetyEvents):
            Battery safety events.
        charging_events (blueye.protocol.types.BatteryBQ40Z50.BatteryChargingEvents):
            Battery charging events.
    """

    class Voltage(proto.Message):
        r"""Battery voltage levels.

        Attributes:
            total (float):
                Battery pack voltage level (V).
            cell_1 (float):
                Cell 1 voltage level (V).
            cell_2 (float):
                Vell 2 voltage level (V).
            cell_3 (float):
                Cell 3 voltage level (V).
            cell_4 (float):
                Cell 4 voltage level (V).
        """

        total: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        cell_1: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        cell_2: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        cell_3: float = proto.Field(
            proto.FLOAT,
            number=4,
        )
        cell_4: float = proto.Field(
            proto.FLOAT,
            number=5,
        )

    class Temperature(proto.Message):
        r"""Battery temperature.

        Attributes:
            average (float):
                Average temperature accross cells (°C).
            cell_1 (float):
                Cell 1 temperature (°C).
            cell_2 (float):
                Cell 2 temperature (°C).
            cell_3 (float):
                Cell 3 temperature (°C).
            cell_4 (float):
                Cell 4 temperature (°C).
        """

        average: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        cell_1: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        cell_2: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        cell_3: float = proto.Field(
            proto.FLOAT,
            number=4,
        )
        cell_4: float = proto.Field(
            proto.FLOAT,
            number=5,
        )

    class BatteryStatus(proto.Message):
        r"""Battery status from BQ40Z50 ref data sheet 0x16.

        Attributes:
            overcharged_alarm (bool):

            terminate_charge_alarm (bool):

            over_temperature_alarm (bool):

            terminate_discharge_alarm (bool):

            remaining_capacity_alarm (bool):

            remaining_time_alarm (bool):

            initialization (bool):

            discharging_or_relax (bool):

            fully_charged (bool):

            fully_discharged (bool):

            error (blueye.protocol.types.BatteryBQ40Z50.BatteryStatus.BatteryError):
                Battery error codes.
        """
        class BatteryError(proto.Enum):
            r"""Battery error code from BQ40Z50 BMS data sheet.

            Attributes:
                BATTERY_ERROR_UNSPECIFIED (0):
                    No description available.
                BATTERY_ERROR_OK (1):
                    No description available.
                BATTERY_ERROR_BUSY (2):
                    No description available.
                BATTERY_ERROR_RESERVED_COMMAND (3):
                    No description available.
                BATTERY_ERROR_UNSUPPORTED_COMMAND (4):
                    No description available.
                BATTERY_ERROR_ACCESS_DENIED (5):
                    No description available.
                BATTERY_ERROR_OVERFLOW_UNDERFLOW (6):
                    No description available.
                BATTERY_ERROR_BAD_SIZE (7):
                    No description available.
                BATTERY_ERROR_UNKNOWN_ERROR (8):
                    No description available.
            """
            BATTERY_ERROR_UNSPECIFIED = 0
            BATTERY_ERROR_OK = 1
            BATTERY_ERROR_BUSY = 2
            BATTERY_ERROR_RESERVED_COMMAND = 3
            BATTERY_ERROR_UNSUPPORTED_COMMAND = 4
            BATTERY_ERROR_ACCESS_DENIED = 5
            BATTERY_ERROR_OVERFLOW_UNDERFLOW = 6
            BATTERY_ERROR_BAD_SIZE = 7
            BATTERY_ERROR_UNKNOWN_ERROR = 8

        overcharged_alarm: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        terminate_charge_alarm: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        over_temperature_alarm: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        terminate_discharge_alarm: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        remaining_capacity_alarm: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        remaining_time_alarm: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        initialization: bool = proto.Field(
            proto.BOOL,
            number=7,
        )
        discharging_or_relax: bool = proto.Field(
            proto.BOOL,
            number=8,
        )
        fully_charged: bool = proto.Field(
            proto.BOOL,
            number=9,
        )
        fully_discharged: bool = proto.Field(
            proto.BOOL,
            number=10,
        )
        error: 'BatteryBQ40Z50.BatteryStatus.BatteryError' = proto.Field(
            proto.ENUM,
            number=11,
            enum='BatteryBQ40Z50.BatteryStatus.BatteryError',
        )

    class BatteryLifetimes(proto.Message):
        r"""

        Attributes:
            max_cell_voltages (blueye.protocol.types.BatteryBQ40Z50.BatteryLifetimes.CellVoltages):
                Maximum reported cell voltages.
            min_cell_voltages (blueye.protocol.types.BatteryBQ40Z50.BatteryLifetimes.CellVoltages):
                Minimum reported cell voltages.
            max_delta_cell_voltage (float):
                Max delta between cells (V).
            max_charge_current (float):
                Max reported current in the charge direction
                (A).
            max_discharge_current (float):
                Max reported current in the discharge
                direction (A).
            max_avg_discharge_current (float):
                Max reported average current in the discharge
                direction (A).
            max_avg_discharge_power (float):
                Max reported power in discharge direction
                (W).
            max_cell_temperature (float):
                Max reported cell temperature (°C).
            min_cell_temperature (float):
                Min reported cell temperature (°C).
            max_delta_cell_temperature (float):
                Max reported temperature delta for TSx inputs
                configured as cell temperature (°C).
            max_temperature_internal_sensor (float):
                Max reported internal temperature sensor
                temperature (°C).
            min_temperature_internal_sensor (float):
                Min reported internal temperature sensor
                temperature (°C).
            max_temperature_fet (float):
                Max reported FET temperature (°C).
        """

        class CellVoltages(proto.Message):
            r"""

            Attributes:
                cell_1 (float):
                    Voltage for cell number 1 (V).
                cell_2 (float):
                    Voltage for cell number 2 (V).
                cell_3 (float):
                    Voltage for cell number 3 (V).
                cell_4 (float):
                    Voltage for cell number 4 (V).
            """

            cell_1: float = proto.Field(
                proto.FLOAT,
                number=1,
            )
            cell_2: float = proto.Field(
                proto.FLOAT,
                number=2,
            )
            cell_3: float = proto.Field(
                proto.FLOAT,
                number=3,
            )
            cell_4: float = proto.Field(
                proto.FLOAT,
                number=4,
            )

        max_cell_voltages: 'BatteryBQ40Z50.BatteryLifetimes.CellVoltages' = proto.Field(
            proto.MESSAGE,
            number=1,
            message='BatteryBQ40Z50.BatteryLifetimes.CellVoltages',
        )
        min_cell_voltages: 'BatteryBQ40Z50.BatteryLifetimes.CellVoltages' = proto.Field(
            proto.MESSAGE,
            number=2,
            message='BatteryBQ40Z50.BatteryLifetimes.CellVoltages',
        )
        max_delta_cell_voltage: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        max_charge_current: float = proto.Field(
            proto.FLOAT,
            number=4,
        )
        max_discharge_current: float = proto.Field(
            proto.FLOAT,
            number=5,
        )
        max_avg_discharge_current: float = proto.Field(
            proto.FLOAT,
            number=6,
        )
        max_avg_discharge_power: float = proto.Field(
            proto.FLOAT,
            number=7,
        )
        max_cell_temperature: float = proto.Field(
            proto.FLOAT,
            number=8,
        )
        min_cell_temperature: float = proto.Field(
            proto.FLOAT,
            number=9,
        )
        max_delta_cell_temperature: float = proto.Field(
            proto.FLOAT,
            number=10,
        )
        max_temperature_internal_sensor: float = proto.Field(
            proto.FLOAT,
            number=11,
        )
        min_temperature_internal_sensor: float = proto.Field(
            proto.FLOAT,
            number=12,
        )
        max_temperature_fet: float = proto.Field(
            proto.FLOAT,
            number=13,
        )

    class BatterySafetyEvents(proto.Message):
        r"""

        Attributes:
            cov_events_count (int):
                Number of cell over voltage (COV) events
                (events).
            cov_last_event (int):
                Last COV event in cycle count cycles
                (cycles).
            cuv_events_count (int):
                Number of cell under voltage (CUV) events
                (events).
            cuv_last_event (int):
                Last CUV event in cycle count cycles
                (cycles).
            ocd1_events_count (int):
                Number of over current in Discharge 1 (OCD1)
                events (events).
            ocd1_last_event (int):
                Last OCD1 event in cycle count cycles
                (cycles).
            ocd2_events_count (int):
                Number of over current in Discharge 2 (OCD2)
                events (events).
            ocd2_last_event (int):
                Last OCD2 event in cycle count cycles
                (cycles).
            occ1_events_count (int):
                Number of over current in Charge 1 (OCC1)
                events (events).
            occ1_last_event (int):
                Last OCC1 event in cycle count cycles
                (cycles).
            occ2_events_count (int):
                Number of over current in Charge 2 (OCC2)
                events (events).
            occ2_last_event (int):
                Last OCC2 event in cycle count cycles
                (cycles).
            aold_events_count (int):
                Number of Overload in discharge (AOLD) events
                (events).
            aold_last_event (int):
                Last AOLD event in cycle count cycles
                (cycles).
            ascd_events_count (int):
                Number of Short Circuit in Discharge (ASCD)
                events (events).
            ascd_last_event (int):
                Last ASCD event in cycle count cycles
                (cycles).
            ascc_events_count (int):
                Number of Short Circuit in Charge (ASCC)
                events (events).
            ascc_last_event (int):
                Last ASCC event in cycle count cycles
                (cycles).
            otc_events_count (int):
                Number of over temperature in Charge (OTC)
                events (events).
            otc_last_event (int):
                Last OTC event in cycle count cycles
                (cycles).
            otd_events_count (int):
                Number of over temperature in Discharge (OTD)
                events (events).
            otd_last_event (int):
                Last OTD event in cycle count cycles
                (cycles).
            otf_events_count (int):
                Number of over temperature in FET (OTF)
                events (events).
            otf_last_event (int):
                Last OTF event in cycle count cycles
                (cycles).
        """

        cov_events_count: int = proto.Field(
            proto.UINT32,
            number=1,
        )
        cov_last_event: int = proto.Field(
            proto.UINT32,
            number=2,
        )
        cuv_events_count: int = proto.Field(
            proto.UINT32,
            number=3,
        )
        cuv_last_event: int = proto.Field(
            proto.UINT32,
            number=4,
        )
        ocd1_events_count: int = proto.Field(
            proto.UINT32,
            number=5,
        )
        ocd1_last_event: int = proto.Field(
            proto.UINT32,
            number=6,
        )
        ocd2_events_count: int = proto.Field(
            proto.UINT32,
            number=7,
        )
        ocd2_last_event: int = proto.Field(
            proto.UINT32,
            number=8,
        )
        occ1_events_count: int = proto.Field(
            proto.UINT32,
            number=9,
        )
        occ1_last_event: int = proto.Field(
            proto.UINT32,
            number=10,
        )
        occ2_events_count: int = proto.Field(
            proto.UINT32,
            number=11,
        )
        occ2_last_event: int = proto.Field(
            proto.UINT32,
            number=12,
        )
        aold_events_count: int = proto.Field(
            proto.UINT32,
            number=13,
        )
        aold_last_event: int = proto.Field(
            proto.UINT32,
            number=14,
        )
        ascd_events_count: int = proto.Field(
            proto.UINT32,
            number=15,
        )
        ascd_last_event: int = proto.Field(
            proto.UINT32,
            number=16,
        )
        ascc_events_count: int = proto.Field(
            proto.UINT32,
            number=17,
        )
        ascc_last_event: int = proto.Field(
            proto.UINT32,
            number=18,
        )
        otc_events_count: int = proto.Field(
            proto.UINT32,
            number=19,
        )
        otc_last_event: int = proto.Field(
            proto.UINT32,
            number=20,
        )
        otd_events_count: int = proto.Field(
            proto.UINT32,
            number=21,
        )
        otd_last_event: int = proto.Field(
            proto.UINT32,
            number=22,
        )
        otf_events_count: int = proto.Field(
            proto.UINT32,
            number=23,
        )
        otf_last_event: int = proto.Field(
            proto.UINT32,
            number=24,
        )

    class BatteryChargingEvents(proto.Message):
        r"""

        Attributes:
            charge_termination_events_count (int):
                Total number of valid charge termination
                events (events).
            charge_termination_last_event (int):
                Last valid charge termination in cycle count
                cycles (cycles).
        """

        charge_termination_events_count: int = proto.Field(
            proto.UINT32,
            number=1,
        )
        charge_termination_last_event: int = proto.Field(
            proto.UINT32,
            number=2,
        )

    voltage: Voltage = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Voltage,
    )
    temperature: Temperature = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Temperature,
    )
    status: BatteryStatus = proto.Field(
        proto.MESSAGE,
        number=4,
        message=BatteryStatus,
    )
    current: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    average_current: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    relative_state_of_charge: float = proto.Field(
        proto.FLOAT,
        number=8,
    )
    absolute_state_of_charge: float = proto.Field(
        proto.FLOAT,
        number=9,
    )
    calculated_state_of_charge: float = proto.Field(
        proto.FLOAT,
        number=26,
    )
    remaining_capacity: float = proto.Field(
        proto.FLOAT,
        number=10,
    )
    full_charge_capacity: float = proto.Field(
        proto.FLOAT,
        number=11,
    )
    runtime_to_empty: int = proto.Field(
        proto.UINT32,
        number=12,
    )
    average_time_to_empty: int = proto.Field(
        proto.UINT32,
        number=13,
    )
    average_time_to_full: int = proto.Field(
        proto.UINT32,
        number=14,
    )
    charging_current: float = proto.Field(
        proto.FLOAT,
        number=17,
    )
    charging_voltage: float = proto.Field(
        proto.FLOAT,
        number=18,
    )
    cycle_count: int = proto.Field(
        proto.UINT32,
        number=19,
    )
    design_capacity: float = proto.Field(
        proto.FLOAT,
        number=20,
    )
    manufacture_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=21,
        message=timestamp_pb2.Timestamp,
    )
    serial_number: int = proto.Field(
        proto.UINT32,
        number=22,
    )
    manufacturer_name: str = proto.Field(
        proto.STRING,
        number=23,
    )
    device_name: str = proto.Field(
        proto.STRING,
        number=24,
    )
    device_chemistry: str = proto.Field(
        proto.STRING,
        number=25,
    )
    lifetimes: BatteryLifetimes = proto.Field(
        proto.MESSAGE,
        number=27,
        message=BatteryLifetimes,
    )
    safety_events: BatterySafetyEvents = proto.Field(
        proto.MESSAGE,
        number=28,
        message=BatterySafetyEvents,
    )
    charging_events: BatteryChargingEvents = proto.Field(
        proto.MESSAGE,
        number=29,
        message=BatteryChargingEvents,
    )


class Attitude(proto.Message):
    r"""The attitude of the drone.

    Attributes:
        roll (float):
            Roll angle (-180°..180°).
        pitch (float):
            Pitch angle (-180°..180°).
        yaw (float):
            Yaw angle (-180°..180°).
    """

    roll: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    pitch: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    yaw: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


class Altitude(proto.Message):
    r"""Drone altitude over seabed, typically obtained from a DVL.

    Attributes:
        value (float):
            Drone altitude over seabed (m).
        is_valid (bool):
            If altitude is valid or not.
    """

    value: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    is_valid: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ForwardDistance(proto.Message):
    r"""Distance to an object in front of the drone.

    Typically obtained from a 1D pinger.

    Attributes:
        value (float):
            Distance in front of drone (m).
        is_valid (bool):
            If distance reading is valid or not.
    """

    value: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    is_valid: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class PositionEstimate(proto.Message):
    r"""Position estimate from the Extended Kalman filter based
    observer if a DVL is connected.

    Attributes:
        northing (float):
            Position from reset point (m).
        easting (float):
            Position from reset point (m).
        heading (float):
            Continuous heading estimate (rad).
        surge_rate (float):
            Velocity in surge (m/s).
        sway_rate (float):
            Velocity in sway (m/s).
        yaw_rate (float):
            Rotaion rate in yaw (rad/s).
        ocean_current (float):
            Estimated ocean current (m/s).
        odometer (float):
            Travelled distance since reset (m).
        is_valid (bool):
            If the estimate can be trusted.
        global_position (blueye.protocol.types.LatLongPosition):
            Best estimate of the global position in
            decimal degrees.
        navigation_sensors (MutableSequence[blueye.protocol.types.NavigationSensorStatus]):
            List of available sensors with status.
        speed_over_ground (float):
            Speed over ground (m/s).
        course_over_ground (float):
            Course over ground (°).
        time_since_reset_sec (int):
            Time since reset (s).
        accuracy (float):
            Accuracy radius of this position at the 95th
            percentile confidence level (m).
    """

    northing: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    easting: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    heading: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    surge_rate: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    sway_rate: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    yaw_rate: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    ocean_current: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    odometer: float = proto.Field(
        proto.FLOAT,
        number=8,
    )
    is_valid: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    global_position: 'LatLongPosition' = proto.Field(
        proto.MESSAGE,
        number=10,
        message='LatLongPosition',
    )
    navigation_sensors: MutableSequence['NavigationSensorStatus'] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message='NavigationSensorStatus',
    )
    speed_over_ground: float = proto.Field(
        proto.FLOAT,
        number=12,
    )
    course_over_ground: float = proto.Field(
        proto.FLOAT,
        number=13,
    )
    time_since_reset_sec: int = proto.Field(
        proto.INT32,
        number=14,
    )
    accuracy: float = proto.Field(
        proto.FLOAT,
        number=15,
    )


class ResetPositionSettings(proto.Message):
    r"""Settings used when resetting the position estimate.

    Attributes:
        heading_source_during_reset (blueye.protocol.types.HeadingSource):
            Option to use the drone compass or due North
            as heading during reset.
        manual_heading (float):
            Heading in degrees (0-359).
        reset_coordinate_source (blueye.protocol.types.ResetCoordinateSource):
            Option to use the device GPS or a manual
            coordinate.
        reset_coordinate (blueye.protocol.types.LatLongPosition):
            Reset coordinate in decimal degrees.
        heading_mode (blueye.protocol.types.HeadingMode):
            Heading mode used in dead reckoning.
    """

    heading_source_during_reset: 'HeadingSource' = proto.Field(
        proto.ENUM,
        number=1,
        enum='HeadingSource',
    )
    manual_heading: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    reset_coordinate_source: 'ResetCoordinateSource' = proto.Field(
        proto.ENUM,
        number=3,
        enum='ResetCoordinateSource',
    )
    reset_coordinate: 'LatLongPosition' = proto.Field(
        proto.MESSAGE,
        number=4,
        message='LatLongPosition',
    )
    heading_mode: 'HeadingMode' = proto.Field(
        proto.ENUM,
        number=5,
        enum='HeadingMode',
    )


class DvlTransducer(proto.Message):
    r"""DVL raw transducer data.

    Attributes:
        id (int):
            Transducer ID, 3 beams for Nucleus DVL, 4
            beams for DVL A50.
        velocity (float):
            Velocity (m/s).
        distance (float):
            Distance (m).
        beam_valid (bool):
            Beam validity.
        rssi (float):
            Received signal strength indicator: strength
            of the signal received by this transducer (dBm).
        nsd (float):
            Noise spectral density: strength of the
            background noise received by this transducer
            (dBm).
    """

    id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    velocity: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    distance: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    beam_valid: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    rssi: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    nsd: float = proto.Field(
        proto.FLOAT,
        number=6,
    )


class DvlVelocity(proto.Message):
    r"""DVL raw velocity data.

    Attributes:
        sensor_id (blueye.protocol.types.NavigationSensorID):
            Sensor id.
        status (int):
            Vendor-specific status of the DVL.
        delta_time (float):
            Time since last velocity measurement (ms).
        fom (float):
            Figure of merit, a measure of the accuracy of
            the velocities (m/s).
        velocity (blueye.protocol.types.Vector3):
            Velocity, x forward, y left, z down (m/s).
        is_water_tracking (bool):
            Water tracking status.
        transducers (MutableSequence[blueye.protocol.types.DvlTransducer]):
            List of transducers.
    """

    sensor_id: 'NavigationSensorID' = proto.Field(
        proto.ENUM,
        number=1,
        enum='NavigationSensorID',
    )
    status: int = proto.Field(
        proto.INT32,
        number=2,
    )
    delta_time: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    fom: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    velocity: 'Vector3' = proto.Field(
        proto.MESSAGE,
        number=5,
        message='Vector3',
    )
    is_water_tracking: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    transducers: MutableSequence['DvlTransducer'] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message='DvlTransducer',
    )


class Depth(proto.Message):
    r"""Water depth of the drone.

    Attributes:
        value (float):
            Drone depth below surface (m).
    """

    value: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class Reference(proto.Message):
    r"""Reference for the control system. Note that the internal heading
    reference is not relative to North, use (ControlHealth.heading_error
    + pose.yaw) instead.

    Attributes:
        surge (float):
            Reference from joystick surge input (0..1).
        sway (float):
            Reference from joystick sway input (0..1).
        heave (float):
            Reference from joystick heave input (0..1).
        yaw (float):
            Reference from joystick yaw input (0..1).
        depth (float):
            Reference drone depth below surface (m).
        heading (float):
            Reference used in auto heading mode, gyro
            based (°).
        altitude (float):
            Reference used in auto altitude mode (m).
    """

    surge: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    sway: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    heave: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    yaw: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    depth: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    heading: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    altitude: float = proto.Field(
        proto.FLOAT,
        number=7,
    )


class Notification(proto.Message):
    r"""Notification is used for displaying info, warnings, and
    errors to the user.

    Attributes:
        type_ (blueye.protocol.types.NotificationType):
            Notification to be displayed to the user.
        level (blueye.protocol.types.NotificationLevel):
            Level of the notification, info, warning or
            error.
        value (google.protobuf.any_pb2.Any):
            Optional value to be displayed in the
            message.
        timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp of the notification.
    """

    type_: 'NotificationType' = proto.Field(
        proto.ENUM,
        number=1,
        enum='NotificationType',
    )
    level: 'NotificationLevel' = proto.Field(
        proto.ENUM,
        number=2,
        enum='NotificationLevel',
    )
    value: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=3,
        message=any_pb2.Any,
    )
    timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class ControlForce(proto.Message):
    r"""Control Force is used for showing the requested control force
    in each direction in Newtons.

    Attributes:
        surge (float):
            Force in surge (N).
        sway (float):
            Force in sway (N).
        heave (float):
            Force in heave (N).
        yaw (float):
            Moment in yaw (Nm).
    """

    surge: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    sway: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    heave: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    yaw: float = proto.Field(
        proto.FLOAT,
        number=4,
    )


class ControllerHealth(proto.Message):
    r"""Controller health is used for showing the state of the
    controller with an relative error and load from 0 to 1.

    Attributes:
        depth_error (float):
            Depth error in meters (m).
        depth_health (float):
            Depth controller load (0..1).
        heading_error (float):
            Heading error in degrees (°).
        heading_health (float):
            Heading controller load (0..1).
    """

    depth_error: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    depth_health: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    heading_error: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    heading_health: float = proto.Field(
        proto.FLOAT,
        number=4,
    )


class DiveTime(proto.Message):
    r"""Amount of time the drone has been submerged.

    The drone starts incrementing this value when the depth is above
    250 mm.

    Attributes:
        value (int):
            Number of seconds the drone has been
            submerged.
    """

    value: int = proto.Field(
        proto.INT32,
        number=1,
    )


class RecordOn(proto.Message):
    r"""Which cameras are supposed to be recording.

    Attributes:
        main (bool):
            Record the main camera.
        guestport (bool):
            Record external camera.
        multibeam (bool):
            Record multibeam.
    """

    main: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    guestport: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    multibeam: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class StorageSpace(proto.Message):
    r"""Storage space.

    Attributes:
        total_space (int):
            Total bytes of storage space (B).
        free_space (int):
            Available bytes of storage space (B).
    """

    total_space: int = proto.Field(
        proto.INT64,
        number=1,
    )
    free_space: int = proto.Field(
        proto.INT64,
        number=2,
    )


class CalibrationState(proto.Message):
    r"""Compass calibration state.

    Attributes:
        status (blueye.protocol.types.CalibrationState.Status):
            Current calibration status.
        progress_x_positive (float):
            Progress for the positive X axis (0..1).
        progress_x_negative (float):
            Progress for the negative X axis (0..1).
        progress_y_positive (float):
            Progress for the positive Y axis (0..1).
        progress_y_negative (float):
            Progress for the negative X axis (0..1).
        progress_z_positive (float):
            Progress for the positive Z axis (0..1).
        progress_z_negative (float):
            Progress for the negative Z axis (0..1).
        progress_thruster (float):
            Progress for the thruster calibration (0..1).
    """
    class Status(proto.Enum):
        r"""Status of the compass calibration procedure.

        When calibration is started, the status will indicate the active
        (upfacing) axis.

        Attributes:
            STATUS_UNSPECIFIED (0):
                Unspecified status.
            STATUS_NOT_CALIBRATING (1):
                Compass is not currently calibrating.
            STATUS_CALIBRATING_NO_AXIS (2):
                Compass is calibrating but active calibration
                axis cannot be determined.
            STATUS_CALIBRATING_X_POSITIVE (3):
                Compass is calibrating and the positive X
                axis is active.
            STATUS_CALIBRATING_X_NEGATIVE (4):
                Compass is calibrating and the negative X
                axis is active.
            STATUS_CALIBRATING_Y_POSITIVE (5):
                Compass is calibrating and the positive Y
                axis is active.
            STATUS_CALIBRATING_Y_NEGATIVE (6):
                Compass is calibrating and the negative Y
                axis is active.
            STATUS_CALIBRATING_Z_POSITIVE (7):
                Compass is calibrating and the positive Z
                axis is active.
            STATUS_CALIBRATING_Z_NEGATIVE (8):
                Compass is calibrating and the negative Z
                axis is active.
            STATUS_CALIBRATING_THRUSTER (9):
                Compass is calibrating for thruster
                interferance.
        """
        STATUS_UNSPECIFIED = 0
        """Unspecified status."""
        STATUS_NOT_CALIBRATING = 1
        """Compass is not currently calibrating."""
        STATUS_CALIBRATING_NO_AXIS = 2
        """Compass is calibrating but active calibration axis cannot be
        determined."""
        STATUS_CALIBRATING_X_POSITIVE = 3
        """Compass is calibrating and the positive X axis is active."""
        STATUS_CALIBRATING_X_NEGATIVE = 4
        """Compass is calibrating and the negative X axis is active."""
        STATUS_CALIBRATING_Y_POSITIVE = 5
        """Compass is calibrating and the positive Y axis is active."""
        STATUS_CALIBRATING_Y_NEGATIVE = 6
        """Compass is calibrating and the negative Y axis is active."""
        STATUS_CALIBRATING_Z_POSITIVE = 7
        """Compass is calibrating and the positive Z axis is active."""
        STATUS_CALIBRATING_Z_NEGATIVE = 8
        """Compass is calibrating and the negative Z axis is active."""
        STATUS_CALIBRATING_THRUSTER = 9
        """Compass is calibrating for thruster interferance."""

    status: Status = proto.Field(
        proto.ENUM,
        number=1,
        enum=Status,
    )
    progress_x_positive: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    progress_x_negative: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    progress_y_positive: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    progress_y_negative: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    progress_z_positive: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    progress_z_negative: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    progress_thruster: float = proto.Field(
        proto.FLOAT,
        number=8,
    )


class IperfStatus(proto.Message):
    r"""Connection speed between drone and Surface Unit.

    Attributes:
        sent (float):
            Transfer rate from drone to Surface Unit
            (Mbit/s).
        received (float):
            Transfer rate from Surface Unit to drone
            (Mbit/s).
    """

    sent: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    received: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class NStreamers(proto.Message):
    r"""Number of spectators connected to video stream.

    Attributes:
        main (int):
            The number of clients to the main camera
            stream.
        guestport (int):
            The number of clients to the guestport camera
            stream.
    """

    main: int = proto.Field(
        proto.INT32,
        number=1,
    )
    guestport: int = proto.Field(
        proto.INT32,
        number=2,
    )


class TiltAngle(proto.Message):
    r"""Angle of tilt camera in degrees.

    Attributes:
        value (float):
            Tilt angle (°).
    """

    value: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class TiltVelocity(proto.Message):
    r"""Relative velocity of tilt.

    Attributes:
        value (float):
            Relative angular velocity of tilt (-1..1),
            negative means down and positive means up.
    """

    value: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class DroneInfo(proto.Message):
    r"""Information about the drone.

    This message contains serial numbers and version information for
    internal components in the drone. Primarily used for
    diagnostics, or to determine the origin of a logfile.

    Attributes:
        blunux_version (str):
            Blunux version string.
        serial_number (bytes):
            Drone serial number.
        hardware_id (bytes):
            Main computer unique identifier.
        model (blueye.protocol.types.Model):
            Drone model.
        mb_serial (bytes):
            Motherboard serial number.
        bb_serial (bytes):
            Backbone serial number.
        ds_serial (bytes):
            Drone stack serial number.
        mb_uid (bytes):
            Motherboard unique identifier.
        bb_uid (bytes):
            Backbone unique identifier.
        gp (blueye.protocol.types.GuestPortInfo):
            Guest port information.
        depth_sensor (blueye.protocol.types.PressureSensorType):
            Type of depth sensor that is connected to the
            drone.
    """

    blunux_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    serial_number: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    hardware_id: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    model: 'Model' = proto.Field(
        proto.ENUM,
        number=4,
        enum='Model',
    )
    mb_serial: bytes = proto.Field(
        proto.BYTES,
        number=5,
    )
    bb_serial: bytes = proto.Field(
        proto.BYTES,
        number=6,
    )
    ds_serial: bytes = proto.Field(
        proto.BYTES,
        number=10,
    )
    mb_uid: bytes = proto.Field(
        proto.BYTES,
        number=7,
    )
    bb_uid: bytes = proto.Field(
        proto.BYTES,
        number=8,
    )
    gp: 'GuestPortInfo' = proto.Field(
        proto.MESSAGE,
        number=9,
        message='GuestPortInfo',
    )
    depth_sensor: 'PressureSensorType' = proto.Field(
        proto.ENUM,
        number=11,
        enum='PressureSensorType',
    )


class ErrorFlags(proto.Message):
    r"""Known error states for the drone.

    Attributes:
        pmu_comm_ack (bool):
            Acknowledge message not received for a
            message published to internal micro controller.
        pmu_comm_stream (bool):
            Error in communication with internal micro
            controller.
        depth_read (bool):
            Error reading depth sensor value.
        depth_spike (bool):
            Sudden spike in value read from depth sensor.
        inner_pressure_read (bool):
            Error reading inner pressure of the drone.
        inner_pressure_spike (bool):
            Sudden spike in inner preassure.
        compass_calibration (bool):
            Compass needs calibration.
        tilt_calibration (bool):
            Error during calibration of tilt endpoints.
        gp1_read (bool):
            Guest port 1 read error.
        gp2_read (bool):
            Guest port 2 read error.
        gp3_read (bool):
            Guest port 3 read error.
        gp1_not_flashed (bool):
            Guest port 1 not flashed.
        gp2_not_flashed (bool):
            Guest port 2 not flashed.
        gp3_not_flashed (bool):
            Guest port 3 not flashed.
        gp1_unknown_device (bool):
            Unknown device on guest port 1.
        gp2_unknown_device (bool):
            Unknown device on guest port 2.
        gp3_unknown_device (bool):
            Unknown device on guest port 3.
        gp1_device_connection (bool):
            Guest port 1 connection error.
        gp2_device_connection (bool):
            Guest port 2 connection error.
        gp3_device_connection (bool):
            Guest port 3 connection error.
        gp1_device (bool):
            Guest port 1 device error.
        gp2_device (bool):
            Guest port 2 device error.
        gp3_device (bool):
            Guest port 3 device error.
        drone_serial_not_set (bool):
            Drone serial number not set.
        drone_serial (bool):
            Drone serial number error.
        mb_eeprom_read (bool):
            MB eeprom read error.
        bb_eeprom_read (bool):
            BB eeprom read error.
        mb_eeprom_not_flashed (bool):
            MB eeprom not flashed.
        bb_eeprom_not_flashed (bool):
            BB eeprom not flashed.
        main_camera_connection (bool):
            We don't get buffers from the main camera.
        main_camera_firmware (bool):
            The main camera firmware is wrong.
        guestport_camera_connection (bool):
            We don't get buffers from the guestport
            camera.
        guestport_camera_firmware (bool):
            The guestport camera firmware is wrong.
        mb_serial (bool):
            MB serial number error.
        bb_serial (bool):
            BB serial number error.
        ds_serial (bool):
            DS serial number error.
        gp_current_read (bool):
            Error reading GP current.
        gp_current (bool):
            Max GP current exceeded.
        gp1_bat_current (bool):
            Max battery current exceeded on GP1.
        gp2_bat_current (bool):
            Max battery current exceeded on GP2.
        gp3_bat_current (bool):
            Max battery current exceeded on GP3.
        gp_20v_current (bool):
            Max 20V current exceeded on GP.
        dvl_thermal_protection_mode (bool):
            DVL is in thermal protection mode.
        dvl_no_power (bool):
            GP protection has been triggered at boot or
            faulty DVL.
        usb_disconnect (bool):
            USB disconnect.
        video_urb_error (bool):
            Video URB error.
        hardware_not_supported (bool):
            Hardware not supported on current blunux
            version.
    """

    pmu_comm_ack: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    pmu_comm_stream: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    depth_read: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    depth_spike: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    inner_pressure_read: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    inner_pressure_spike: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    compass_calibration: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    tilt_calibration: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    gp1_read: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    gp2_read: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    gp3_read: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    gp1_not_flashed: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    gp2_not_flashed: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    gp3_not_flashed: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    gp1_unknown_device: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    gp2_unknown_device: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    gp3_unknown_device: bool = proto.Field(
        proto.BOOL,
        number=17,
    )
    gp1_device_connection: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    gp2_device_connection: bool = proto.Field(
        proto.BOOL,
        number=19,
    )
    gp3_device_connection: bool = proto.Field(
        proto.BOOL,
        number=20,
    )
    gp1_device: bool = proto.Field(
        proto.BOOL,
        number=21,
    )
    gp2_device: bool = proto.Field(
        proto.BOOL,
        number=22,
    )
    gp3_device: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    drone_serial_not_set: bool = proto.Field(
        proto.BOOL,
        number=24,
    )
    drone_serial: bool = proto.Field(
        proto.BOOL,
        number=25,
    )
    mb_eeprom_read: bool = proto.Field(
        proto.BOOL,
        number=26,
    )
    bb_eeprom_read: bool = proto.Field(
        proto.BOOL,
        number=27,
    )
    mb_eeprom_not_flashed: bool = proto.Field(
        proto.BOOL,
        number=28,
    )
    bb_eeprom_not_flashed: bool = proto.Field(
        proto.BOOL,
        number=29,
    )
    main_camera_connection: bool = proto.Field(
        proto.BOOL,
        number=30,
    )
    main_camera_firmware: bool = proto.Field(
        proto.BOOL,
        number=31,
    )
    guestport_camera_connection: bool = proto.Field(
        proto.BOOL,
        number=32,
    )
    guestport_camera_firmware: bool = proto.Field(
        proto.BOOL,
        number=33,
    )
    mb_serial: bool = proto.Field(
        proto.BOOL,
        number=34,
    )
    bb_serial: bool = proto.Field(
        proto.BOOL,
        number=35,
    )
    ds_serial: bool = proto.Field(
        proto.BOOL,
        number=36,
    )
    gp_current_read: bool = proto.Field(
        proto.BOOL,
        number=37,
    )
    gp_current: bool = proto.Field(
        proto.BOOL,
        number=38,
    )
    gp1_bat_current: bool = proto.Field(
        proto.BOOL,
        number=39,
    )
    gp2_bat_current: bool = proto.Field(
        proto.BOOL,
        number=40,
    )
    gp3_bat_current: bool = proto.Field(
        proto.BOOL,
        number=41,
    )
    gp_20v_current: bool = proto.Field(
        proto.BOOL,
        number=42,
    )
    dvl_thermal_protection_mode: bool = proto.Field(
        proto.BOOL,
        number=43,
    )
    dvl_no_power: bool = proto.Field(
        proto.BOOL,
        number=44,
    )
    usb_disconnect: bool = proto.Field(
        proto.BOOL,
        number=45,
    )
    video_urb_error: bool = proto.Field(
        proto.BOOL,
        number=46,
    )
    hardware_not_supported: bool = proto.Field(
        proto.BOOL,
        number=47,
    )


class CameraParameters(proto.Message):
    r"""Camera parameters.

    Attributes:
        h264_bitrate (int):
            Bitrate of the h264 stream (bit/sec).
        mjpg_bitrate (int):
            Bitrate of the MJPG stream used for still
            pictures (bit/sec).
        exposure (int):
            Shutter speed (1/10000 \* s), -1 for automatic exposure.
        white_balance (int):
            White balance temperature (2800..9300), -1
            for automatic white balance.
        hue (int):
            Hue (-40..40), 0 as default.
        gain (float):
            Iso gain (0..1).
        resolution (blueye.protocol.types.Resolution):
            Stream, recording and image resolution
            (deprecated).
        stream_resolution (blueye.protocol.types.Resolution):
            Stream resolution.
        recording_resolution (blueye.protocol.types.Resolution):
            Recording and image resolution.
        framerate (blueye.protocol.types.Framerate):
            Stream and recording framerate.
        camera (blueye.protocol.types.Camera):
            Which camera the parameters belong to.
    """

    h264_bitrate: int = proto.Field(
        proto.INT32,
        number=1,
    )
    mjpg_bitrate: int = proto.Field(
        proto.INT32,
        number=2,
    )
    exposure: int = proto.Field(
        proto.INT32,
        number=3,
    )
    white_balance: int = proto.Field(
        proto.INT32,
        number=4,
    )
    hue: int = proto.Field(
        proto.INT32,
        number=5,
    )
    gain: float = proto.Field(
        proto.FLOAT,
        number=9,
    )
    resolution: 'Resolution' = proto.Field(
        proto.ENUM,
        number=6,
        enum='Resolution',
    )
    stream_resolution: 'Resolution' = proto.Field(
        proto.ENUM,
        number=10,
        enum='Resolution',
    )
    recording_resolution: 'Resolution' = proto.Field(
        proto.ENUM,
        number=11,
        enum='Resolution',
    )
    framerate: 'Framerate' = proto.Field(
        proto.ENUM,
        number=7,
        enum='Framerate',
    )
    camera: 'Camera' = proto.Field(
        proto.ENUM,
        number=8,
        enum='Camera',
    )


class OverlayParameters(proto.Message):
    r"""Overlay parameters.

    All available parameters that can be used to configure telemetry
    overlay on video recordings.

    Attributes:
        temperature_enabled (bool):
            If temperature should be included.
        depth_enabled (bool):
            If depth should be included.
        heading_enabled (bool):
            If heading should be included.
        tilt_enabled (bool):
            If camera tilt angle should be included.
        thickness_enabled (bool):
            If camera tilt angle should be included.
        date_enabled (bool):
            If date should be included.
        distance_enabled (bool):
            If distance should be included.
        altitude_enabled (bool):
            If altitude should be included.
        cp_probe_enabled (bool):
            If cp-probe should be included.
        medusa_enabled (bool):
            If medusa measurement should be included.
        drone_location_enabled (bool):
            If the drone location coordinates should be
            included.
        logo_type (blueye.protocol.types.LogoType):
            Which logo should be used.
        depth_unit (blueye.protocol.types.DepthUnit):
            Which unit should be used for depth: Meter,
            Feet or None.
        temperature_unit (blueye.protocol.types.TemperatureUnit):
            Which unit should be used for temperature:
            Celsius or Fahrenheit.
        thickness_unit (blueye.protocol.types.ThicknessUnit):
            Which unit should be used for thickness:
            Millimeters or Inches.
        timezone_offset (int):
            Timezone offset from UTC (min).
        margin_width (int):
            Horizontal margins of text elements (px).
        margin_height (int):
            Vertical margins of text elements (px).
        font_size (blueye.protocol.types.FontSize):
            Font size of text elements.
        title (str):
            Optional title.
        subtitle (str):
            Optional subtitle.
        date_format (str):
            Posix strftime format string for time stamp.
        shading (float):
            Pixel intensity to subtract from text
            background (0..1), 0: transparent, 1: black.
    """

    temperature_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    depth_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    heading_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    tilt_enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    thickness_enabled: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    date_enabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    distance_enabled: bool = proto.Field(
        proto.BOOL,
        number=20,
    )
    altitude_enabled: bool = proto.Field(
        proto.BOOL,
        number=21,
    )
    cp_probe_enabled: bool = proto.Field(
        proto.BOOL,
        number=22,
    )
    medusa_enabled: bool = proto.Field(
        proto.BOOL,
        number=24,
    )
    drone_location_enabled: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    logo_type: 'LogoType' = proto.Field(
        proto.ENUM,
        number=6,
        enum='LogoType',
    )
    depth_unit: 'DepthUnit' = proto.Field(
        proto.ENUM,
        number=7,
        enum='DepthUnit',
    )
    temperature_unit: 'TemperatureUnit' = proto.Field(
        proto.ENUM,
        number=8,
        enum='TemperatureUnit',
    )
    thickness_unit: 'ThicknessUnit' = proto.Field(
        proto.ENUM,
        number=19,
        enum='ThicknessUnit',
    )
    timezone_offset: int = proto.Field(
        proto.INT32,
        number=9,
    )
    margin_width: int = proto.Field(
        proto.INT32,
        number=10,
    )
    margin_height: int = proto.Field(
        proto.INT32,
        number=11,
    )
    font_size: 'FontSize' = proto.Field(
        proto.ENUM,
        number=12,
        enum='FontSize',
    )
    title: str = proto.Field(
        proto.STRING,
        number=13,
    )
    subtitle: str = proto.Field(
        proto.STRING,
        number=14,
    )
    date_format: str = proto.Field(
        proto.STRING,
        number=16,
    )
    shading: float = proto.Field(
        proto.FLOAT,
        number=17,
    )


class NavigationSensorStatus(proto.Message):
    r"""Navigation sensor used in the position observer with validity
    state.

    Attributes:
        sensor_id (blueye.protocol.types.NavigationSensorID):
            Sensor id.
        is_valid (bool):
            Sensor validity.
        northing (float):
            Position from reset point (m).
        easting (float):
            Position from reset point (m).
        heading (float):
            Heading from sensor (-pi..pi).
        fom (float):
            Figure of merit.
        std (float):
            Standard deviation.
        global_position (blueye.protocol.types.LatLongPosition):
            Global position from sensor.
    """

    sensor_id: 'NavigationSensorID' = proto.Field(
        proto.ENUM,
        number=1,
        enum='NavigationSensorID',
    )
    is_valid: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    northing: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    easting: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    heading: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    fom: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    std: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    global_position: 'LatLongPosition' = proto.Field(
        proto.MESSAGE,
        number=8,
        message='LatLongPosition',
    )


class GuestPortDevice(proto.Message):
    r"""Information about a device connected to one of the guest
    ports.

    Attributes:
        device_id (blueye.protocol.types.GuestPortDeviceID):
            Blueye device identifier.
        manufacturer (str):
            Manufacturer name.
        name (str):
            Device name.
        serial_number (str):
            Serial number.
        depth_rating (float):
            Depth rating (m).
        required_blunux_version (str):
            Required Blunux version (x.y.z).
        detach_status (blueye.protocol.types.GuestPortDetachStatus):
            Detach status based on detection pin.
    """

    device_id: 'GuestPortDeviceID' = proto.Field(
        proto.ENUM,
        number=1,
        enum='GuestPortDeviceID',
    )
    manufacturer: str = proto.Field(
        proto.STRING,
        number=2,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    serial_number: str = proto.Field(
        proto.STRING,
        number=4,
    )
    depth_rating: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    required_blunux_version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    detach_status: 'GuestPortDetachStatus' = proto.Field(
        proto.ENUM,
        number=7,
        enum='GuestPortDetachStatus',
    )


class GuestPortDeviceList(proto.Message):
    r"""List of guest port devices.

    Attributes:
        devices (MutableSequence[blueye.protocol.types.GuestPortDevice]):
            List of guest port devices.
    """

    devices: MutableSequence['GuestPortDevice'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='GuestPortDevice',
    )


class GuestPortConnectorInfo(proto.Message):
    r"""GuestPort connector information.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        device_list (blueye.protocol.types.GuestPortDeviceList):
            List of devices on this connector.

            This field is a member of `oneof`_ ``connected_device``.
        error (blueye.protocol.types.GuestPortError):
            Guest port connector error.

            This field is a member of `oneof`_ ``connected_device``.
        guest_port_number (blueye.protocol.types.GuestPortNumber):
            Guest port the connector is connected to.
    """

    device_list: 'GuestPortDeviceList' = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='connected_device',
        message='GuestPortDeviceList',
    )
    error: 'GuestPortError' = proto.Field(
        proto.ENUM,
        number=2,
        oneof='connected_device',
        enum='GuestPortError',
    )
    guest_port_number: 'GuestPortNumber' = proto.Field(
        proto.ENUM,
        number=3,
        enum='GuestPortNumber',
    )


class GuestPortInfo(proto.Message):
    r"""GuestPort information.

    Attributes:
        gp1 (blueye.protocol.types.GuestPortConnectorInfo):
            Information about guest port 1.
        gp2 (blueye.protocol.types.GuestPortConnectorInfo):
            Information about guest port 2.
        gp3 (blueye.protocol.types.GuestPortConnectorInfo):
            Information about guest port 3.
    """

    gp1: 'GuestPortConnectorInfo' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='GuestPortConnectorInfo',
    )
    gp2: 'GuestPortConnectorInfo' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='GuestPortConnectorInfo',
    )
    gp3: 'GuestPortConnectorInfo' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='GuestPortConnectorInfo',
    )


class GuestPortRestartInfo(proto.Message):
    r"""GuestPort restart information.

    Attributes:
        power_off_duration (float):
            Duration to keep the guest ports off (s).
    """

    power_off_duration: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )


class ThicknessGauge(proto.Message):
    r"""Thickness measurement data from a Cygnus Thickness Gauge.

    Attributes:
        thickness_measurement (float):
            Thickness measurement of a steel plate.
        echo_count (int):
            Indicating the quality of the reading when
            invalid (0-3).
        sound_velocity (int):
            Speed of sound in the steel member (m/s).
        is_measurement_valid (bool):
            Indicating if the measurement is valid.
    """

    thickness_measurement: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    echo_count: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    sound_velocity: int = proto.Field(
        proto.UINT32,
        number=3,
    )
    is_measurement_valid: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class CpProbe(proto.Message):
    r"""Reading from a Cathodic Protection Potential probe.

    Attributes:
        measurement (float):
            Potential measurement (V).
        is_measurement_valid (bool):
            Indicating if the measurement is valid.
    """

    measurement: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    is_measurement_valid: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class GenericServo(proto.Message):
    r"""Servo message used to represent the angle of the servo.

    Attributes:
        value (float):
            Servo value (0..1).
        guest_port_number (blueye.protocol.types.GuestPortNumber):
            Guest port the servo is on.
    """

    value: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    guest_port_number: 'GuestPortNumber' = proto.Field(
        proto.ENUM,
        number=2,
        enum='GuestPortNumber',
    )


class MultibeamServo(proto.Message):
    r"""Servo message used to represent the angle of the servo.

    Attributes:
        angle (float):
            Servo degrees (-30..30).
    """

    angle: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class GuestPortCurrent(proto.Message):
    r"""GuestPort current readings.

    Attributes:
        gp1_bat (float):
            Current on GP1 battery voltage (A).
        gp2_bat (float):
            Current on GP2 battery voltage (A).
        gp3_bat (float):
            Current on GP3 battery voltage (A).
        gp_20v (float):
            Current on common 20V supply (A).
    """

    gp1_bat: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    gp2_bat: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    gp3_bat: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    gp_20v: float = proto.Field(
        proto.DOUBLE,
        number=4,
    )


class Vector3(proto.Message):
    r"""Vector with 3 elements.

    Attributes:
        x (float):
            X-component.
        y (float):
            Y-component.
        z (float):
            Z-component.
    """

    x: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    y: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    z: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )


class Imu(proto.Message):
    r"""Imu data in drone body frame.

    x - forward
    y - right
    z - down

    Attributes:
        accelerometer (blueye.protocol.types.Vector3):
            Acceleration (g).
        gyroscope (blueye.protocol.types.Vector3):
            Angular velocity (rad/s).
        magnetometer (blueye.protocol.types.Vector3):
            Magnetic field (μT).
        temperature (float):
            Temperature (°C).
    """

    accelerometer: 'Vector3' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Vector3',
    )
    gyroscope: 'Vector3' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='Vector3',
    )
    magnetometer: 'Vector3' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='Vector3',
    )
    temperature: float = proto.Field(
        proto.FLOAT,
        number=4,
    )


class MedusaSpectrometerData(proto.Message):
    r"""Medusa gamma ray sensor spectrometer data.

    Attributes:
        drone_time (google.protobuf.timestamp_pb2.Timestamp):
            Time stamp when the data is received.
        sensor_time (google.protobuf.timestamp_pb2.Timestamp):
            Time stamp the sensor reports.
        realtime (float):
            Time the sensor actually measured (s).
        livetime (float):
            Time the measurement took (s).
        total (int):
            Total counts inside the spectrum.
        countrate (int):
            Counts per second inside the spectrum
            (rounded).
        cosmics (int):
            Detected counts above the last channel.
    """

    drone_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    sensor_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    realtime: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    livetime: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    total: int = proto.Field(
        proto.UINT32,
        number=3,
    )
    countrate: int = proto.Field(
        proto.UINT32,
        number=4,
    )
    cosmics: int = proto.Field(
        proto.UINT32,
        number=5,
    )


class MultibeamPing(proto.Message):
    r"""Multibeam sonar ping.

    Contains all the information for rendering a multibeam sonar
    frame.

    Attributes:
        range_ (float):
            Maximum range value (m).
        gain (float):
            Percentage of gain (0 to 1).
        frequency (float):
            Ping acoustic frequency (Hz).
        speed_of_sound_used (float):
            Speed of sound used by the sonar for range
            calculations (m/s).
        frequency_mode (blueye.protocol.types.MultibeamFrequencyMode):
            Frequency mode used by the sonar for this
            frame.
        number_of_ranges (int):
            Height of the ping image data.
        number_of_beams (int):
            Width of the ping image data.
        step (int):
            Size in bytes of each row in the ping data
            image.
        bearings (MutableSequence[float]):
            Bearing angle of each column of the sonar
            data (in 100th of a degree, multiply by 0.01 to
            get a value in degrees). The sonar image is not
            sampled uniformly in the bearing direction.
        ping_data (bytes):
            Ping data (row major, 2D, grayscale image).
        device_id (blueye.protocol.types.GuestPortDeviceID):
            Device ID of the sonar.
        frame_generation_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the frame was generated.
    """

    range_: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    gain: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    frequency: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    speed_of_sound_used: float = proto.Field(
        proto.DOUBLE,
        number=4,
    )
    frequency_mode: 'MultibeamFrequencyMode' = proto.Field(
        proto.ENUM,
        number=5,
        enum='MultibeamFrequencyMode',
    )
    number_of_ranges: int = proto.Field(
        proto.UINT32,
        number=6,
    )
    number_of_beams: int = proto.Field(
        proto.UINT32,
        number=7,
    )
    step: int = proto.Field(
        proto.UINT32,
        number=8,
    )
    bearings: MutableSequence[float] = proto.RepeatedField(
        proto.FLOAT,
        number=9,
    )
    ping_data: bytes = proto.Field(
        proto.BYTES,
        number=10,
    )
    device_id: 'GuestPortDeviceID' = proto.Field(
        proto.ENUM,
        number=11,
        enum='GuestPortDeviceID',
    )
    frame_generation_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )


class MultibeamConfig(proto.Message):
    r"""Configuration message for sonar devices.

    Attributes:
        frequency_mode (blueye.protocol.types.MultibeamFrequencyMode):
            Frequency mode used by the sonar if
            supported.
        ping_rate (blueye.protocol.types.MultibeamConfig.PingRate):
            Sets the maximum ping rate.
        gamma_correction (float):
            Gamma correction (0..1.0).
        gain_assist (bool):
            Enable gain assist.
        gain_boost (bool):
            Enable gain boost (only available on
            Blueprint devices).
        maximum_number_of_beams (blueye.protocol.types.MultibeamConfig.MaximumNumberOfBeams):
            Maximum number of beams. Used to throttle
            bandwidth.
        range_ (float):
            The range demand (m).
        gain (float):
            The gain demand (0..1).
        salinity (float):
            Set water salinity (ppt). Defaults to zero in
            fresh water.
        device_id (blueye.protocol.types.GuestPortDeviceID):
            Device ID of the sonar.
        bandwidth_limit (int):
            Network bandwidth limit (Mbit/s), applies
            only to Oculus devices.
    """
    class PingRate(proto.Enum):
        r"""Defines the desired ping rate to use when capturing sonar
        data.

        Attributes:
            PING_RATE_UNSPECIFIED (0):
                No description available.
            PING_RATE_NORMAL (1):
                10Hz max ping rate.
            PING_RATE_HIGH (2):
                15Hz max ping rate.
            PING_RATE_HIGHEST (3):
                40Hz max ping rate.
            PING_RATE_LOW (4):
                5Hz max ping rate.
            PING_RATE_LOWEST (5):
                2Hz max ping rate.
            PING_RATE_STANDBY (6):
                Disable ping.
        """
        PING_RATE_UNSPECIFIED = 0
        PING_RATE_NORMAL = 1
        """10Hz max ping rate."""
        PING_RATE_HIGH = 2
        """15Hz max ping rate."""
        PING_RATE_HIGHEST = 3
        """40Hz max ping rate."""
        PING_RATE_LOW = 4
        """5Hz max ping rate."""
        PING_RATE_LOWEST = 5
        """2Hz max ping rate."""
        PING_RATE_STANDBY = 6
        """Disable ping."""

    class MaximumNumberOfBeams(proto.Enum):
        r"""The maximum number of beams to use by the multibeam sonar.

        Attributes:
            MAXIMUM_NUMBER_OF_BEAMS_UNSPECIFIED (0):
                No description available.
            MAXIMUM_NUMBER_OF_BEAMS_MAX_128 (1):
                128 beams.
            MAXIMUM_NUMBER_OF_BEAMS_MAX_256 (2):
                256 beams.
            MAXIMUM_NUMBER_OF_BEAMS_MAX_512 (3):
                512 beams.
            MAXIMUM_NUMBER_OF_BEAMS_MAX_1024 (4):
                1024 beams.
        """
        MAXIMUM_NUMBER_OF_BEAMS_UNSPECIFIED = 0
        MAXIMUM_NUMBER_OF_BEAMS_MAX_128 = 1
        """128 beams."""
        MAXIMUM_NUMBER_OF_BEAMS_MAX_256 = 2
        """256 beams."""
        MAXIMUM_NUMBER_OF_BEAMS_MAX_512 = 3
        """512 beams."""
        MAXIMUM_NUMBER_OF_BEAMS_MAX_1024 = 4
        """1024 beams."""

    frequency_mode: 'MultibeamFrequencyMode' = proto.Field(
        proto.ENUM,
        number=1,
        enum='MultibeamFrequencyMode',
    )
    ping_rate: PingRate = proto.Field(
        proto.ENUM,
        number=2,
        enum=PingRate,
    )
    gamma_correction: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    gain_assist: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    gain_boost: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    maximum_number_of_beams: MaximumNumberOfBeams = proto.Field(
        proto.ENUM,
        number=5,
        enum=MaximumNumberOfBeams,
    )
    range_: float = proto.Field(
        proto.DOUBLE,
        number=6,
    )
    gain: float = proto.Field(
        proto.DOUBLE,
        number=7,
    )
    salinity: float = proto.Field(
        proto.DOUBLE,
        number=8,
    )
    device_id: 'GuestPortDeviceID' = proto.Field(
        proto.ENUM,
        number=9,
        enum='GuestPortDeviceID',
    )
    bandwidth_limit: int = proto.Field(
        proto.UINT32,
        number=10,
    )


class MultibeamDiscovery(proto.Message):
    r"""Discovery message for multibeam sonar devices.

    Attributes:
        enabled (bool):
            If the sonar driver is enabled.
        ip (str):
            IP address of the sonar.
        mask (str):
            Subnet mask of the sonar.
        serial_number (str):
            Serial number of the sonar.
        fw_version (str):
            Firmware version of the sonar.
        connected_ip (str):
            IP address of the connected device.
        device_id (blueye.protocol.types.GuestPortDeviceID):
            Device ID of the sonar.
        error_flags (blueye.protocol.types.MultibeamErrorFlags):
            Error flags specific for the connected
            multibeam device.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    ip: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mask: str = proto.Field(
        proto.STRING,
        number=3,
    )
    serial_number: str = proto.Field(
        proto.STRING,
        number=4,
    )
    fw_version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    connected_ip: str = proto.Field(
        proto.STRING,
        number=6,
    )
    device_id: 'GuestPortDeviceID' = proto.Field(
        proto.ENUM,
        number=7,
        enum='GuestPortDeviceID',
    )
    error_flags: 'MultibeamErrorFlags' = proto.Field(
        proto.MESSAGE,
        number=8,
        message='MultibeamErrorFlags',
    )


class MultibeamErrorFlags(proto.Message):
    r"""Error flags for multibeam sonar devices.

    Attributes:
        connected_to_another_client (bool):
            If the sonar is captured by another client than the drone.
            The connected client IP is reported in connected_ip
            property.
        device_overheating (bool):
            If the multibeam is reporting to overheat.
        out_of_water (bool):
            If a TriTech multibeam is reporting to be out
            of water.
    """

    connected_to_another_client: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    device_overheating: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    out_of_water: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class MultibeamFrameOffset(proto.Message):
    r"""Frame offset for multibeam recordings index cache.

    Attributes:
        duration (google.protobuf.duration_pb2.Duration):
            Duration from the start of the recording.
        offset (int):
            Offset in bytes from the start of the file.
    """

    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    offset: int = proto.Field(
        proto.INT64,
        number=2,
    )


class MutltibeamRecordingIndex(proto.Message):
    r"""Multibeam recording index cache.

    Attributes:
        frame_offsets (MutableSequence[blueye.protocol.types.MultibeamFrameOffset]):
            List of frame offsets.
    """

    frame_offsets: MutableSequence['MultibeamFrameOffset'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='MultibeamFrameOffset',
    )


class PersistentStorageSettings(proto.Message):
    r"""PersistentStorageSettings defines settings for writing
    various types of data in the persistent storage on the drone.
    Some of the data is written during factory calibration (acc
    calibration), while other data is written during user
    calubration or during normal operation.

    Attributes:
        videos (bool):
            Indicates if videos should be written to the
            video partition.
        images (bool):
            Indicates if images should be written to the
            video partition.
        binlog (bool):
            Indicates if binary logs with telemetry data
            should be written to the data partition.
        multibeam (bool):
            Indicates if multibeam data should be written
            to the video partition.
        webserver_log (bool):
            Indicates if webserver logs should be written
            to the data partition.
        control_system_log (bool):
            Indicates if control system logs should be
            written to the data partition.
        gyro_calibration (bool):
            Indicates if gyro calibration data should be
            written to the data partition.
        compass_calibration (bool):
            Indicates if compass calibration data should
            be written to the data partition.
        acc_calibration (bool):
            Indicates if accelerometer calibration data
            should be written to the data partition.
    """

    videos: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    images: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    binlog: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    multibeam: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    webserver_log: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    control_system_log: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    gyro_calibration: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    compass_calibration: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    acc_calibration: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class CPUInfo(proto.Message):
    r"""CPU information.

    Contains information about the CPU load and memory usage of the
    drone.

    Attributes:
        cpu_load (float):
            CPU load (0..1).
        memory_bus_load (float):
            Memory bus load (0..1).
        main_queue_load (float):
            Main queue load (0..1).
        guestport_queue_load (float):
            Guestport queue load (0..1).
    """

    cpu_load: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    memory_bus_load: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    main_queue_load: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    guestport_queue_load: float = proto.Field(
        proto.FLOAT,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
