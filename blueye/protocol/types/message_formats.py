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


from google.protobuf import any_pb2 as gp_any  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore


__protobuf__ = proto.module(
    package='blueye.protocol',
    manifest={
        'HeadingSource',
        'ResetCoordinateSource',
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
        'GuestPortError',
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
        'ControlMode',
        'TiltStabilizationState',
        'SystemTime',
        'GripperVelocities',
        'ClientInfo',
        'ConnectedClient',
        'RecordState',
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
        'Depth',
        'Reference',
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
    },
)


class HeadingSource(proto.Enum):
    r"""-

    Heading source used during reset of the position estimate.
    """
    HEADING_SOURCE_UNSPECIFIED = 0
    HEADING_SOURCE_DRONE_COMPASS = 1
    HEADING_SOURCE_MANUAL_INPUT = 2


class ResetCoordinateSource(proto.Enum):
    r""""""
    RESET_COORDINATE_SOURCE_UNSPECIFIED = 0
    RESET_COORDINATE_SOURCE_DEVICE_GPS = 1
    RESET_COORDINATE_SOURCE_MANUAL = 2


class Model(proto.Enum):
    r"""-

    Drone models produced by Blueye
    """
    MODEL_UNSPECIFIED = 0
    MODEL_PIONEER = 1
    MODEL_PRO = 2
    MODEL_X3 = 3


class PressureSensorType(proto.Enum):
    r"""-

    Depth sensors used by the drone.
    """
    PRESSURE_SENSOR_TYPE_UNSPECIFIED = 0
    PRESSURE_SENSOR_TYPE_NOT_CONNECTED = 1
    PRESSURE_SENSOR_TYPE_MS5837_30BA26 = 2
    PRESSURE_SENSOR_TYPE_KELLER_PA7LD = 3
    PRESSURE_SENSOR_TYPE_MS5637_02BA03 = 4


class Resolution(proto.Enum):
    r"""-

    Available camera resolutions.
    """
    RESOLUTION_UNSPECIFIED = 0
    RESOLUTION_FULLHD_1080P = 1
    RESOLUTION_HD_720P = 2


class Framerate(proto.Enum):
    r"""-

    Available camera framerates.
    """
    FRAMERATE_UNSPECIFIED = 0
    FRAMERATE_FPS_30 = 1
    FRAMERATE_FPS_25 = 2


class Camera(proto.Enum):
    r"""-

    Which camera to control.
    """
    CAMERA_UNSPECIFIED = 0
    CAMERA_MAIN = 1
    CAMERA_GUESTPORT = 2


class TemperatureUnit(proto.Enum):
    r"""-

    Available temperature units.
    """
    TEMPERATURE_UNIT_UNSPECIFIED = 0
    TEMPERATURE_UNIT_CELSIUS = 1
    TEMPERATURE_UNIT_FAHRENHEIT = 2


class LogoType(proto.Enum):
    r"""-

    Available logo types.
    """
    LOGO_TYPE_UNSPECIFIED = 0
    LOGO_TYPE_NONE = 1
    LOGO_TYPE_DEFAULT = 2
    LOGO_TYPE_CUSTOM = 3


class DepthUnit(proto.Enum):
    r"""-

    Available depth units.
    """
    DEPTH_UNIT_UNSPECIFIED = 0
    DEPTH_UNIT_METERS = 1
    DEPTH_UNIT_FEET = 2


class ThicknessUnit(proto.Enum):
    r"""-

    Available thickness units.
    """
    THICKNESS_UNIT_UNSPECIFIED = 0
    THICKNESS_UNIT_MILLIMETERS = 1
    THICKNESS_UNIT_INCHES = 2


class FontSize(proto.Enum):
    r"""-

    Available font sizes for overlay text elements.
    """
    FONT_SIZE_UNSPECIFIED = 0
    FONT_SIZE_PX15 = 1
    FONT_SIZE_PX20 = 2
    FONT_SIZE_PX25 = 3
    FONT_SIZE_PX30 = 4
    FONT_SIZE_PX35 = 5
    FONT_SIZE_PX40 = 6


class GuestPortDeviceID(proto.Enum):
    r"""-

    GuestPort device ID.
    """
    GUEST_PORT_DEVICE_ID_UNSPECIFIED = 0
    GUEST_PORT_DEVICE_ID_BLIND_PLUG = 1
    GUEST_PORT_DEVICE_ID_TEST_STATION = 2
    GUEST_PORT_DEVICE_ID_DEBUG_SERIAL = 3
    GUEST_PORT_DEVICE_ID_BLUEYE_LIGHT = 4
    GUEST_PORT_DEVICE_ID_BLUEYE_CAM = 5
    GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_LUMEN = 6
    GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_NEWTON = 7
    GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_PING_SONAR = 8
    GUEST_PORT_DEVICE_ID_BLUEPRINT_LAB_REACH_ALPHA = 9
    GUEST_PORT_DEVICE_ID_WATERLINKED_DVL_A50 = 10
    GUEST_PORT_DEVICE_ID_IMPACT_SUBSEA_ISS360 = 11
    GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_SEATRAC_X010 = 12
    GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_M750D = 13
    GUEST_PORT_DEVICE_ID_CYGNUS_MINI_ROV_THICKNESS_GAUGE = 14
    GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_PING360_SONAR = 15
    GUEST_PORT_DEVICE_ID_TRITECH_GEMINI_720IM = 16
    GUEST_PORT_DEVICE_ID_BLUEYE_LIGHT_PAIR = 17
    GUEST_PORT_DEVICE_ID_TRITECH_GEMINI_MICRON = 18
    GUEST_PORT_DEVICE_ID_OCEAN_TOOLS_DIGICP = 19
    GUEST_PORT_DEVICE_ID_TRITECH_GEMINI_720IK = 20
    GUEST_PORT_DEVICE_ID_NORTEK_NUCLEUS_1000 = 21
    GUEST_PORT_DEVICE_ID_BLUEYE_GENERIC_SERVO = 22
    GUEST_PORT_DEVICE_ID_BLUEYE_MULTIBEAM_SERVO = 23
    GUEST_PORT_DEVICE_ID_BLUE_ROBOTICS_DETACHABLE_NEWTON = 24
    GUEST_PORT_DEVICE_ID_INSITU_AQUA_TROLL_500 = 25
    GUEST_PORT_DEVICE_ID_MEDUSA_RADIOMETRICS_MS100 = 26
    GUEST_PORT_DEVICE_ID_LASER_TOOLS_SEA_BEAM = 27
    GUEST_PORT_DEVICE_ID_SPOT_X_LASER_SCALERS = 28
    GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_M1200D = 29
    GUEST_PORT_DEVICE_ID_BLUEPRINT_SUBSEA_OCULUS_M3000D = 30


class GuestPortNumber(proto.Enum):
    r"""-

    GuestPort number.
    """
    GUEST_PORT_NUMBER_UNSPECIFIED = 0
    GUEST_PORT_NUMBER_PORT_1 = 1
    GUEST_PORT_NUMBER_PORT_2 = 2
    GUEST_PORT_NUMBER_PORT_3 = 3


class NavigationSensorID(proto.Enum):
    r"""-

    List of navigation sensors that can be used by the position observer
    """
    NAVIGATION_SENSOR_ID_UNSPECIFIED = 0
    NAVIGATION_SENSOR_ID_WATERLINKED_DVL_A50 = 1
    NAVIGATION_SENSOR_ID_WATERLINKED_UGPS_G2 = 2


class GuestPortError(proto.Enum):
    r"""-

    GuestPort error.
    """
    GUEST_PORT_ERROR_UNSPECIFIED = 0
    GUEST_PORT_ERROR_NOT_CONNECTED = 1
    GUEST_PORT_ERROR_READ_ERROR = 2
    GUEST_PORT_ERROR_NOT_FLASHED = 3
    GUEST_PORT_ERROR_CRC_ERROR = 4
    GUEST_PORT_ERROR_PARSE_ERROR = 5


class BinlogRecord(proto.Message):
    r"""-

    Wrapper message for each entry in the drone telemetry logfile.

    Each entry contains the unix timestamp in UTC, the monotonic
    timestamp (time since boot), and an Any message wrapping the custom
    Blueye message.

    See separate documentation for the logfile format for more details.

    Attributes:
        payload (google.protobuf.any_pb2.Any):
            The log entry payload.
        unix_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Unix timestamp in UTC.
        clock_monotonic (google.protobuf.timestamp_pb2.Timestamp):
            Posix CLOCK_MONOTONIC timestamp.
    """

    payload = proto.Field(proto.MESSAGE, number=1,
        message=gp_any.Any,
    )

    unix_timestamp = proto.Field(proto.MESSAGE, number=2,
        message=timestamp.Timestamp,
    )

    clock_monotonic = proto.Field(proto.MESSAGE, number=3,
        message=timestamp.Timestamp,
    )


class MotionInput(proto.Message):
    r"""-

    Motion input from client.

    Used to indicate the desired motion in each direction. Typically
    these values map to the left and right joystick for motion, and the
    left and right trigger for the slow and boost modifiers.

    Attributes:
        surge (float):
            Forward (positive) and backwards (negative)
            movement. (-1..1)
        sway (float):
            Right (positive) and left (negative) lateral
            movement (-1..1)
        heave (float):
            Descend (positive) and ascend (negative)
            movement (-1..1)
        yaw (float):
            Left (positive) and right (negative) movement
            (-1..1)
        slow (float):
            Multiplier used to reduce the speed of the
            motion (0..1)
        boost (float):
            Multiplier used to increase the speed of the
            motion (0..1)
    """

    surge = proto.Field(proto.FLOAT, number=1)

    sway = proto.Field(proto.FLOAT, number=2)

    heave = proto.Field(proto.FLOAT, number=3)

    yaw = proto.Field(proto.FLOAT, number=4)

    slow = proto.Field(proto.FLOAT, number=5)

    boost = proto.Field(proto.FLOAT, number=6)


class Lights(proto.Message):
    r"""-

    Lights message used to represent the intensity of the main light or
    external lights.

    Attributes:
        value (float):
            Light intensity (0..1)
    """

    value = proto.Field(proto.FLOAT, number=1)


class Laser(proto.Message):
    r"""-

    Laser message used to represent the intensity of connected laser.

    If the laser does not support dimming but only on and off, a value
    of 0 turns the laser off, and any value above 0 turns the laser on.

    Attributes:
        value (float):
            Laser intensity, any value above 0 turns the
            laser on (0..1)
    """

    value = proto.Field(proto.FLOAT, number=1)


class LatLongPosition(proto.Message):
    r"""-

    Latitude and longitude position in WGS 84 decimal degrees format.

    Attributes:
        latitude (float):
            Latitude (°)
        longitude (float):
            Longitude (°)
    """

    latitude = proto.Field(proto.DOUBLE, number=1)

    longitude = proto.Field(proto.DOUBLE, number=2)


class ConnectionDuration(proto.Message):
    r"""-

    Connection duration of a remote client.

    Attributes:
        value (int):
            time since connected to drone (s)
    """

    value = proto.Field(proto.INT32, number=1)


class AutoHeadingState(proto.Message):
    r"""-

    Auto heading state.

    Attributes:
        enabled (bool):
            If auto heading is enabled
    """

    enabled = proto.Field(proto.BOOL, number=1)


class AutoDepthState(proto.Message):
    r"""-

    Auto depth state.

    Attributes:
        enabled (bool):
            If auto depth is enabled
    """

    enabled = proto.Field(proto.BOOL, number=1)


class AutoAltitudeState(proto.Message):
    r"""-

    Auto altitude state.

    Attributes:
        enabled (bool):
            If auto altitude is enabled
    """

    enabled = proto.Field(proto.BOOL, number=1)


class StationKeepingState(proto.Message):
    r"""-

    Station keeping state.

    Attributes:
        enabled (bool):
            If station keeping is enabled
    """

    enabled = proto.Field(proto.BOOL, number=1)


class WeatherVaningState(proto.Message):
    r"""-

    Weather vaning state.

    Attributes:
        enabled (bool):
            If weather vaning is enabled
    """

    enabled = proto.Field(proto.BOOL, number=1)


class ControlMode(proto.Message):
    r"""-

    Control mode from drone supervisor

    Attributes:
        auto_depth (bool):
            If auto depth is enabled
        auto_heading (bool):
            If auto heading is enabled
        auto_altitude (bool):
            If auto altitude is enabled
        station_keeping (bool):
            If station keeping is enabled
        weather_vaning (bool):
            If weather vaning is enabled
    """

    auto_depth = proto.Field(proto.BOOL, number=1)

    auto_heading = proto.Field(proto.BOOL, number=2)

    auto_altitude = proto.Field(proto.BOOL, number=3)

    station_keeping = proto.Field(proto.BOOL, number=4)

    weather_vaning = proto.Field(proto.BOOL, number=5)


class TiltStabilizationState(proto.Message):
    r"""-

    Tilt stabilization state.

    Blueye drones with mechanical tilt has the ability to enable camera
    stabilization.

    Attributes:
        enabled (bool):
            If tilt stabilization is enabled
    """

    enabled = proto.Field(proto.BOOL, number=1)


class SystemTime(proto.Message):
    r"""-

    System time.

    Attributes:
        unix_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Unix timestamp
    """

    unix_timestamp = proto.Field(proto.MESSAGE, number=1,
        message=timestamp.Timestamp,
    )


class GripperVelocities(proto.Message):
    r"""-

    Gripper velocity values.

    Attributes:
        grip_velocity (float):
            The gripping velocity (-1.0..1.0)
        rotate_velocity (float):
            The rotating velocity (-1.0..1.0)
    """

    grip_velocity = proto.Field(proto.FLOAT, number=1)

    rotate_velocity = proto.Field(proto.FLOAT, number=2)


class ClientInfo(proto.Message):
    r"""-

    Information about a remote client.

    Attributes:
        type_ (str):
            The type of client (such as Blueye App,
            Observer App, SDK, etc)
        version (str):
            Client software version string
        device_type (str):
            Device type, such as mobile, tablet, or
            computer
        platform (str):
            Platform, such as iOS, Android, Linux, etc
        platform_version (str):
            Platform software version string
        name (str):
            Name of the client
    """

    type_ = proto.Field(proto.STRING, number=1)

    version = proto.Field(proto.STRING, number=2)

    device_type = proto.Field(proto.STRING, number=3)

    platform = proto.Field(proto.STRING, number=4)

    platform_version = proto.Field(proto.STRING, number=5)

    name = proto.Field(proto.STRING, number=6)


class ConnectedClient(proto.Message):
    r"""-

    Information about a connected client with an id assigned by the
    drone.

    Attributes:
        client_id (int):
            The assigned client id
        client_info (blueye.protocol.types.ClientInfo):
            Client information.
    """

    client_id = proto.Field(proto.UINT32, number=1)

    client_info = proto.Field(proto.MESSAGE, number=2,
        message='ClientInfo',
    )


class RecordState(proto.Message):
    r"""-

    Camera recording state.

    Attributes:
        main_is_recording (bool):
            If the main camera is recording
        main_seconds (int):
            Main record time (s)
        guestport_is_recording (bool):
            If the guestport camera is recording
        guestport_seconds (int):
            Guestport record time (s)
    """

    main_is_recording = proto.Field(proto.BOOL, number=1)

    main_seconds = proto.Field(proto.INT32, number=2)

    guestport_is_recording = proto.Field(proto.BOOL, number=3)

    guestport_seconds = proto.Field(proto.INT32, number=4)


class WaterDensity(proto.Message):
    r"""-

    Water density.

    Used to specify the water density the drone is operating in, to
    achieve more accruate depth measurements.

    Attributes:
        value (float):
            Salinity (kg/l)
    """

    value = proto.Field(proto.FLOAT, number=1)


class PingerConfiguration(proto.Message):
    r"""-

    Pinger configuration.

    Used to specify the configuration the BR 1D-Pinger.

    Attributes:
        mounting_direction (blueye.protocol.types.PingerConfiguration.MountingDirection):
            Mounting direction of the pinger
    """
    class MountingDirection(proto.Enum):
        r""""""
        MOUNTING_DIRECTION_UNSPECIFIED = 0
        MOUNTING_DIRECTION_FORWARDS = 1
        MOUNTING_DIRECTION_DOWNWARDS = 2

    mounting_direction = proto.Field(proto.ENUM, number=1,
        enum=MountingDirection,
    )


class WaterTemperature(proto.Message):
    r"""-

    Water temperature measured by the drone's combined depth and
    temperature sensor.

    Attributes:
        value (float):
            Water temperature (°C)
    """

    value = proto.Field(proto.FLOAT, number=1)


class CPUTemperature(proto.Message):
    r"""-

    CPU temperature.

    Attributes:
        value (float):
            CPU temperature (°C)
    """

    value = proto.Field(proto.FLOAT, number=1)


class CanisterTemperature(proto.Message):
    r"""-

    Canister temperature.

    Temperature measured in the top or bottom canister of the drone.

    Attributes:
        temperature (float):
            Temperature (°C)
    """

    temperature = proto.Field(proto.FLOAT, number=3)


class CanisterHumidity(proto.Message):
    r"""-

    Canister humidity.

    Humidity measured in the top or bottom canister of the drone.

    Attributes:
        humidity (float):
            Air humidity (%)
    """

    humidity = proto.Field(proto.FLOAT, number=3)


class Battery(proto.Message):
    r"""-

    Essential battery information.

    Attributes:
        voltage (float):
            Battery voltage (V)
        level (float):
            Battery level (0..1)
        temperature (float):
            Battery temperature (°C)
    """

    voltage = proto.Field(proto.FLOAT, number=1)

    level = proto.Field(proto.FLOAT, number=2)

    temperature = proto.Field(proto.FLOAT, number=3)


class BatteryBQ40Z50(proto.Message):
    r"""-

    Battery information message.

    Detailed information about all aspects of the connected Blueye Smart
    Battery, using the BQ40Z50 BMS.

    Attributes:
        voltage (blueye.protocol.types.BatteryBQ40Z50.Voltage):
            Voltage of the battery cells
        temperature (blueye.protocol.types.BatteryBQ40Z50.Temperature):
            Temperature of the battery cells
        status (blueye.protocol.types.BatteryBQ40Z50.BatteryStatus):
            Battery status flags
        current (float):
            Current (A)
        average_current (float):
            Average current (A)
        relative_state_of_charge (float):
            Relative state of charge (0..1)
        absolute_state_of_charge (float):
            Absolute state of charge (0..1)
        calculated_state_of_charge (float):
            Calculated state of charge (0..1)
        remaining_capacity (float):
            Remaining capacity (Ah)
        full_charge_capacity (float):
            Full charge capacity (Ah)
        runtime_to_empty (int):
            Runtime to empty (s)
        average_time_to_empty (int):
            Average time to empty (s)
        average_time_to_full (int):
            Average time to full (s)
        charging_current (float):
            Charging current (A)
        charging_voltage (float):
            Charging voltage (V)
        cycle_count (int):
            Number of charging cycles
        design_capacity (float):
            Design capacity (Ah)
        manufacture_date (google.protobuf.timestamp_pb2.Timestamp):
            Manufacture date
        serial_number (int):
            Serial number
        manufacturer_name (str):
            Manufacturer name
        device_name (str):
            Device name
        device_chemistry (str):
            Battery chemistry
    """
    class Voltage(proto.Message):
        r"""-

        Battery voltage levels.

        Attributes:
            total (float):
                Battery pack voltage level (V)
            cell_1 (float):
                Cell 1 voltage level (V)
            cell_2 (float):
                Vell 2 voltage level (V)
            cell_3 (float):
                Cell 3 voltage level (V)
            cell_4 (float):
                Cell 4 voltage level (V)
        """

        total = proto.Field(proto.FLOAT, number=1)

        cell_1 = proto.Field(proto.FLOAT, number=2)

        cell_2 = proto.Field(proto.FLOAT, number=3)

        cell_3 = proto.Field(proto.FLOAT, number=4)

        cell_4 = proto.Field(proto.FLOAT, number=5)

    class Temperature(proto.Message):
        r"""-

        Battery temperature.

        Attributes:
            average (float):
                Average temperature accross cells (°C)
            cell_1 (float):
                Cell 1 temperature (°C)
            cell_2 (float):
                Cell 2 temperature (°C)
            cell_3 (float):
                Cell 3 temperature (°C)
            cell_4 (float):
                Cell 4 temperature (°C)
        """

        average = proto.Field(proto.FLOAT, number=1)

        cell_1 = proto.Field(proto.FLOAT, number=2)

        cell_2 = proto.Field(proto.FLOAT, number=3)

        cell_3 = proto.Field(proto.FLOAT, number=4)

        cell_4 = proto.Field(proto.FLOAT, number=5)

    class BatteryStatus(proto.Message):
        r"""-

        Battery status from BQ40Z50 ref data sheet 0x16.

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
                Battery error codes
        """
        class BatteryError(proto.Enum):
            r"""-

            Battery errror code from BQ40Z50 BMS data sheet.
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

        overcharged_alarm = proto.Field(proto.BOOL, number=1)

        terminate_charge_alarm = proto.Field(proto.BOOL, number=2)

        over_temperature_alarm = proto.Field(proto.BOOL, number=3)

        terminate_discharge_alarm = proto.Field(proto.BOOL, number=4)

        remaining_capacity_alarm = proto.Field(proto.BOOL, number=5)

        remaining_time_alarm = proto.Field(proto.BOOL, number=6)

        initialization = proto.Field(proto.BOOL, number=7)

        discharging_or_relax = proto.Field(proto.BOOL, number=8)

        fully_charged = proto.Field(proto.BOOL, number=9)

        fully_discharged = proto.Field(proto.BOOL, number=10)

        error = proto.Field(proto.ENUM, number=11,
            enum='BatteryBQ40Z50.BatteryStatus.BatteryError',
        )

    voltage = proto.Field(proto.MESSAGE, number=1,
        message=Voltage,
    )

    temperature = proto.Field(proto.MESSAGE, number=2,
        message=Temperature,
    )

    status = proto.Field(proto.MESSAGE, number=4,
        message=BatteryStatus,
    )

    current = proto.Field(proto.FLOAT, number=6)

    average_current = proto.Field(proto.FLOAT, number=7)

    relative_state_of_charge = proto.Field(proto.FLOAT, number=8)

    absolute_state_of_charge = proto.Field(proto.FLOAT, number=9)

    calculated_state_of_charge = proto.Field(proto.FLOAT, number=26)

    remaining_capacity = proto.Field(proto.FLOAT, number=10)

    full_charge_capacity = proto.Field(proto.FLOAT, number=11)

    runtime_to_empty = proto.Field(proto.UINT32, number=12)

    average_time_to_empty = proto.Field(proto.UINT32, number=13)

    average_time_to_full = proto.Field(proto.UINT32, number=14)

    charging_current = proto.Field(proto.FLOAT, number=17)

    charging_voltage = proto.Field(proto.FLOAT, number=18)

    cycle_count = proto.Field(proto.UINT32, number=19)

    design_capacity = proto.Field(proto.FLOAT, number=20)

    manufacture_date = proto.Field(proto.MESSAGE, number=21,
        message=timestamp.Timestamp,
    )

    serial_number = proto.Field(proto.UINT32, number=22)

    manufacturer_name = proto.Field(proto.STRING, number=23)

    device_name = proto.Field(proto.STRING, number=24)

    device_chemistry = proto.Field(proto.STRING, number=25)


class Attitude(proto.Message):
    r"""-

    The attitude of the drone.

    Attributes:
        roll (float):
            Roll angle (-180°..180°)
        pitch (float):
            Pitch angle (-180°..180°)
        yaw (float):
            Yaw angle (-180°..180°)
    """

    roll = proto.Field(proto.FLOAT, number=1)

    pitch = proto.Field(proto.FLOAT, number=2)

    yaw = proto.Field(proto.FLOAT, number=3)


class Altitude(proto.Message):
    r"""-

    Drone altitude over seabed, typically obtained from a DVL.

    Attributes:
        value (float):
            Drone altitude over seabed (m)
        is_valid (bool):
            If altitude is valid or not
    """

    value = proto.Field(proto.FLOAT, number=1)

    is_valid = proto.Field(proto.BOOL, number=2)


class ForwardDistance(proto.Message):
    r"""-

    Distance to an object infront of the drone, typically obtained from
    an 1D pinger.

    Attributes:
        value (float):
            Distance in front of drone (m)
        is_valid (bool):
            If distance reading is valid or not
    """

    value = proto.Field(proto.FLOAT, number=1)

    is_valid = proto.Field(proto.BOOL, number=2)


class PositionEstimate(proto.Message):
    r"""-

    Position estimate from the Extended Kalman filter based observer if
    a DVL is connected.

    Attributes:
        northing (float):
            Position from reset point (m)
        easting (float):
            Position from reset point (m)
        heading (float):
            Gyro based heading estimate (continous
            radians)
        surge_rate (float):
            Velocity in surge (m/s)
        sway_rate (float):
            Velocity in sway (m/s)
        yaw_rate (float):
            Rotaion rate in yaw (rad/s)
        ocean_current (float):
            Estimated ocean current (m/s)
        odometer (float):
            Travelled distance since reset (m)
        is_valid (bool):
            If the estimate can be trusted
        global_position (blueye.protocol.types.LatLongPosition):
            Best estimate of the global position in
            decimal degrees
        navigation_sensors (Sequence[blueye.protocol.types.NavigationSensorStatus]):
            List of available sensors with status
    """

    northing = proto.Field(proto.FLOAT, number=1)

    easting = proto.Field(proto.FLOAT, number=2)

    heading = proto.Field(proto.FLOAT, number=3)

    surge_rate = proto.Field(proto.FLOAT, number=4)

    sway_rate = proto.Field(proto.FLOAT, number=5)

    yaw_rate = proto.Field(proto.FLOAT, number=6)

    ocean_current = proto.Field(proto.FLOAT, number=7)

    odometer = proto.Field(proto.FLOAT, number=8)

    is_valid = proto.Field(proto.BOOL, number=9)

    global_position = proto.Field(proto.MESSAGE, number=10,
        message='LatLongPosition',
    )

    navigation_sensors = proto.RepeatedField(proto.MESSAGE, number=11,
        message='NavigationSensorStatus',
    )


class ResetPositionSettings(proto.Message):
    r"""-

    ResetPositionSettings used during reset of the position estimate.

    Attributes:
        heading_source_during_reset (blueye.protocol.types.HeadingSource):
            Option to use the drone compass or due North
            as heading during reset
        manual_heading (float):
            Heading in degrees (0-359)
        reset_coordinate_source (blueye.protocol.types.ResetCoordinateSource):
            Option to use the device GPS or a manual
            coordinate.
        reset_coordinate (blueye.protocol.types.LatLongPosition):
            Reset coordinate in decimal degrees
    """

    heading_source_during_reset = proto.Field(proto.ENUM, number=1,
        enum='HeadingSource',
    )

    manual_heading = proto.Field(proto.FLOAT, number=2)

    reset_coordinate_source = proto.Field(proto.ENUM, number=3,
        enum='ResetCoordinateSource',
    )

    reset_coordinate = proto.Field(proto.MESSAGE, number=4,
        message='LatLongPosition',
    )


class Depth(proto.Message):
    r"""-

    Water depth of the drone.

    Attributes:
        value (float):
            Drone depth below surface (m)
    """

    value = proto.Field(proto.FLOAT, number=1)


class Reference(proto.Message):
    r"""-

    Reference for the control system. Note that the internal heading
    referece is not relative to North. Use (ControlHealth.heading_error
    + pose.yaw) instead.

    Attributes:
        surge (float):
            Reference from joystick surge input (0..1)
        sway (float):
            Reference from joystick sway input (0..1)
        heave (float):
            Reference from joystick heave input (0..1)
        yaw (float):
            Reference from joystick yaw input (0..1)
        depth (float):
            Reference drone depth below surface (m)
        heading (float):
            Reference used in auto heading mode, gyro
            based (°)
        altitude (float):
            Reference used in auto altitude mode (m)
    """

    surge = proto.Field(proto.FLOAT, number=1)

    sway = proto.Field(proto.FLOAT, number=2)

    heave = proto.Field(proto.FLOAT, number=3)

    yaw = proto.Field(proto.FLOAT, number=4)

    depth = proto.Field(proto.FLOAT, number=5)

    heading = proto.Field(proto.FLOAT, number=6)

    altitude = proto.Field(proto.FLOAT, number=7)


class ControlForce(proto.Message):
    r"""-

    Control Force is used for showing the requested control force in
    each direction in Newtons.

    Attributes:
        surge (float):
            Force in surge (N)
        sway (float):
            Force in sway (N)
        heave (float):
            Force in heave (N)
        yaw (float):
            Moment in yaw (Nm)
    """

    surge = proto.Field(proto.FLOAT, number=1)

    sway = proto.Field(proto.FLOAT, number=2)

    heave = proto.Field(proto.FLOAT, number=3)

    yaw = proto.Field(proto.FLOAT, number=4)


class ControllerHealth(proto.Message):
    r"""-

    Controller health is used for showing the state of the controller
    with an relative error and load from 0 to 1.

    Attributes:
        depth_error (float):
            Depth error in meters (m)
        depth_health (float):
            Depth controller load (0..1)
        heading_error (float):
            Heading error in degrees (°)
        heading_health (float):
            Heading controller load (0..1)
    """

    depth_error = proto.Field(proto.FLOAT, number=1)

    depth_health = proto.Field(proto.FLOAT, number=2)

    heading_error = proto.Field(proto.FLOAT, number=3)

    heading_health = proto.Field(proto.FLOAT, number=4)


class DiveTime(proto.Message):
    r"""-

    Amount of time the drone has been submerged.

    The drone starts incrementing this value when the depth is above 250
    mm.

    Attributes:
        value (int):
            Number of seconds the drone has been
            submerged
    """

    value = proto.Field(proto.INT32, number=1)


class RecordOn(proto.Message):
    r"""-

    Which cameras are supposed to be recording

    Attributes:
        main (bool):
            Record the main camera
        guestport (bool):
            Record external camera
    """

    main = proto.Field(proto.BOOL, number=1)

    guestport = proto.Field(proto.BOOL, number=2)


class StorageSpace(proto.Message):
    r"""-

    Storage space.

    Attributes:
        total_space (int):
            Total bytes of storage space (B)
        free_space (int):
            Available bytes of storage space (B)
    """

    total_space = proto.Field(proto.INT64, number=1)

    free_space = proto.Field(proto.INT64, number=2)


class CalibrationState(proto.Message):
    r"""-

    Compass calibration state.

    Attributes:
        status (blueye.protocol.types.CalibrationState.Status):
            Current calibration status
        progress_x_positive (float):
            Progress for the positive X axis (0..1)
        progress_x_negative (float):
            Progress for the negative X axis (0..1)
        progress_y_positive (float):
            Progress for the positive Y axis (0..1)
        progress_y_negative (float):
            Progress for the negative X axis (0..1)
        progress_z_positive (float):
            Progress for the positive Z axis (0..1)
        progress_z_negative (float):
            Progress for the negative Z axis (0..1)
        progress_thruster (float):
            Progress for the thruster calibration (0..1)
    """
    class Status(proto.Enum):
        r"""-

        Status of the compass calibration procedure.

        When calibration is started, the status will indicate the active
        (upfacing) axis.
        """
        STATUS_UNSPECIFIED = 0
        STATUS_NOT_CALIBRATING = 1
        STATUS_CALIBRATING_NO_AXIS = 2
        STATUS_CALIBRATING_X_POSITIVE = 3
        STATUS_CALIBRATING_X_NEGATIVE = 4
        STATUS_CALIBRATING_Y_POSITIVE = 5
        STATUS_CALIBRATING_Y_NEGATIVE = 6
        STATUS_CALIBRATING_Z_POSITIVE = 7
        STATUS_CALIBRATING_Z_NEGATIVE = 8
        STATUS_CALIBRATING_THRUSTER = 9

    status = proto.Field(proto.ENUM, number=1,
        enum=Status,
    )

    progress_x_positive = proto.Field(proto.FLOAT, number=2)

    progress_x_negative = proto.Field(proto.FLOAT, number=3)

    progress_y_positive = proto.Field(proto.FLOAT, number=4)

    progress_y_negative = proto.Field(proto.FLOAT, number=5)

    progress_z_positive = proto.Field(proto.FLOAT, number=6)

    progress_z_negative = proto.Field(proto.FLOAT, number=7)

    progress_thruster = proto.Field(proto.FLOAT, number=8)


class IperfStatus(proto.Message):
    r"""-

    Connection speed between drone and Surface Unit.

    Attributes:
        sent (float):
            Transfer rate from drone to Surface Unit
            (Mbit/s)
        received (float):
            Transfer rate from Surface Unit to drone
            (Mbit/s)
    """

    sent = proto.Field(proto.FLOAT, number=1)

    received = proto.Field(proto.FLOAT, number=2)


class NStreamers(proto.Message):
    r"""-

    Number of spectators connected to video stream.

    Attributes:
        main (int):
            The number of clients to the main camera
            stream
        guestport (int):
            The number of clients to the guestport camera
            stream
    """

    main = proto.Field(proto.INT32, number=1)

    guestport = proto.Field(proto.INT32, number=2)


class TiltAngle(proto.Message):
    r"""-

    Angle of tilt camera in degrees.

    Attributes:
        value (float):
            Tilt angle (°)
    """

    value = proto.Field(proto.FLOAT, number=1)


class TiltVelocity(proto.Message):
    r"""-

    Relative velocity of tilt

    Attributes:
        value (float):
            Relative angular velocity of tilt (-1..1),
            negative means down and positive means up
    """

    value = proto.Field(proto.FLOAT, number=1)


class DroneInfo(proto.Message):
    r"""-

    Information about the drone.

    This message contains serial numbers and version information for
    internal components in the drone. Primarily used for diagnostics, or
    to determine the origin of a logfile.

    Attributes:
        blunux_version (str):
            Blunux version string
        serial_number (bytes):
            Drone serial number
        hardware_id (bytes):
            Main computer unique identifier
        model (blueye.protocol.types.Model):
            Drone model
        mb_serial (bytes):
            Motherboard serial number
        bb_serial (bytes):
            Backbone serial number
        ds_serial (bytes):
            Drone stack serial number
        mb_uid (bytes):
            Motherboard unique identifier
        bb_uid (bytes):
            Backbone unique identifier
        gp (blueye.protocol.types.GuestPortInfo):
            GuestPortInfo
        depth_sensor (blueye.protocol.types.PressureSensorType):
            Type of depth sensor that is connected to the
            drone
    """

    blunux_version = proto.Field(proto.STRING, number=1)

    serial_number = proto.Field(proto.BYTES, number=2)

    hardware_id = proto.Field(proto.BYTES, number=3)

    model = proto.Field(proto.ENUM, number=4,
        enum='Model',
    )

    mb_serial = proto.Field(proto.BYTES, number=5)

    bb_serial = proto.Field(proto.BYTES, number=6)

    ds_serial = proto.Field(proto.BYTES, number=10)

    mb_uid = proto.Field(proto.BYTES, number=7)

    bb_uid = proto.Field(proto.BYTES, number=8)

    gp = proto.Field(proto.MESSAGE, number=9,
        message='GuestPortInfo',
    )

    depth_sensor = proto.Field(proto.ENUM, number=11,
        enum='PressureSensorType',
    )


class ErrorFlags(proto.Message):
    r"""-

    Known error states for the drone.

    Attributes:
        pmu_comm_ack (bool):
            Acknowledge message not received for a
            message published to internal micro controller
        pmu_comm_stream (bool):
            Error in communication with internal micro
            controller
        depth_read (bool):
            Error reading depth sensor value
        depth_spike (bool):
            Sudden spike in value read from depth sensor
        inner_pressure_read (bool):
            Error reading inner pressure of the drone
        inner_pressure_spike (bool):
            Sudden spike in inner preassure
        compass_calibration (bool):
            Compass needs calibration
        tilt_calibration (bool):
            Error during calibration of tilt endpoints
        gp1_read (bool):
            Guest port 1 read error
        gp2_read (bool):
            Guest port 2 read error
        gp3_read (bool):
            Guest port 3 read error
        gp1_not_flashed (bool):
            Guest port 1 not flashed
        gp2_not_flashed (bool):
            Guest port 2 not flashed
        gp3_not_flashed (bool):
            Guest port 3 not flashed
        gp1_unknown_device (bool):
            Unknown device on guest port 1
        gp2_unknown_device (bool):
            Unknown device on guest port 2
        gp3_unknown_device (bool):
            Unknown device on guest port 3
        gp1_device_connection (bool):
            Guest port 1 connection error
        gp2_device_connection (bool):
            Guest port 2 connection error
        gp3_device_connection (bool):
            Guest port 3 connection error
        gp1_device (bool):
            Guest port 1 device error
        gp2_device (bool):
            Guest port 2 device error
        gp3_device (bool):
            Guest port 3 device error
        drone_serial_not_set (bool):
            Drone serial number not set
        drone_serial (bool):
            Drone serial number error
        mb_eeprom_read (bool):
            MB eeprom read error
        bb_eeprom_read (bool):
            BB eeprom read error
        mb_eeprom_not_flashed (bool):
            MB eeprom not flashed
        bb_eeprom_not_flashed (bool):
            BB eeprom not flashed
        main_camera_connection (bool):
            We don't get buffers from the main camera
        main_camera_firmware (bool):
            The main camera firmware is wrong
        guestport_camera_connection (bool):
            We don't get buffers from the guestport
            camera
        guestport_camera_firmware (bool):
            The guestport camera firmware is wrong
        mb_serial (bool):
            MB serial number error
        bb_serial (bool):
            BB serial number error
        ds_serial (bool):
            DS serial number error
        gp_current_read (bool):
            Error reading GP current
        gp_current (bool):
            Max GP current exceeded
        gp1_bat_current (bool):
            Max battery current exceeded on GP1
        gp2_bat_current (bool):
            Max battery current exceeded on GP2
        gp3_bat_current (bool):
            Max battery current exceeded on GP3
        gp_20v_current (bool):
            Max 20V current exceeded on GP
    """

    pmu_comm_ack = proto.Field(proto.BOOL, number=1)

    pmu_comm_stream = proto.Field(proto.BOOL, number=2)

    depth_read = proto.Field(proto.BOOL, number=3)

    depth_spike = proto.Field(proto.BOOL, number=4)

    inner_pressure_read = proto.Field(proto.BOOL, number=5)

    inner_pressure_spike = proto.Field(proto.BOOL, number=6)

    compass_calibration = proto.Field(proto.BOOL, number=7)

    tilt_calibration = proto.Field(proto.BOOL, number=8)

    gp1_read = proto.Field(proto.BOOL, number=9)

    gp2_read = proto.Field(proto.BOOL, number=10)

    gp3_read = proto.Field(proto.BOOL, number=11)

    gp1_not_flashed = proto.Field(proto.BOOL, number=12)

    gp2_not_flashed = proto.Field(proto.BOOL, number=13)

    gp3_not_flashed = proto.Field(proto.BOOL, number=14)

    gp1_unknown_device = proto.Field(proto.BOOL, number=15)

    gp2_unknown_device = proto.Field(proto.BOOL, number=16)

    gp3_unknown_device = proto.Field(proto.BOOL, number=17)

    gp1_device_connection = proto.Field(proto.BOOL, number=18)

    gp2_device_connection = proto.Field(proto.BOOL, number=19)

    gp3_device_connection = proto.Field(proto.BOOL, number=20)

    gp1_device = proto.Field(proto.BOOL, number=21)

    gp2_device = proto.Field(proto.BOOL, number=22)

    gp3_device = proto.Field(proto.BOOL, number=23)

    drone_serial_not_set = proto.Field(proto.BOOL, number=24)

    drone_serial = proto.Field(proto.BOOL, number=25)

    mb_eeprom_read = proto.Field(proto.BOOL, number=26)

    bb_eeprom_read = proto.Field(proto.BOOL, number=27)

    mb_eeprom_not_flashed = proto.Field(proto.BOOL, number=28)

    bb_eeprom_not_flashed = proto.Field(proto.BOOL, number=29)

    main_camera_connection = proto.Field(proto.BOOL, number=30)

    main_camera_firmware = proto.Field(proto.BOOL, number=31)

    guestport_camera_connection = proto.Field(proto.BOOL, number=32)

    guestport_camera_firmware = proto.Field(proto.BOOL, number=33)

    mb_serial = proto.Field(proto.BOOL, number=34)

    bb_serial = proto.Field(proto.BOOL, number=35)

    ds_serial = proto.Field(proto.BOOL, number=36)

    gp_current_read = proto.Field(proto.BOOL, number=37)

    gp_current = proto.Field(proto.BOOL, number=38)

    gp1_bat_current = proto.Field(proto.BOOL, number=39)

    gp2_bat_current = proto.Field(proto.BOOL, number=40)

    gp3_bat_current = proto.Field(proto.BOOL, number=41)

    gp_20v_current = proto.Field(proto.BOOL, number=42)


class CameraParameters(proto.Message):
    r"""-

    Camera parameters.

    Attributes:
        h264_bitrate (int):
            Bitrate of the h264 stream (bit/sec)
        mjpg_bitrate (int):
            Bitrate of the MJPG stream used for still
            pictures (bit/sec)
        exposure (int):
            Shutter speed (1/10000 \* s), -1 for automatic exposure
        white_balance (int):
            White balance temperature (2800..9300), -1
            for automatic white balance
        hue (int):
            Hue (-40..40), 0 as default
        gain (float):
            Iso gain (0..1)
        resolution (blueye.protocol.types.Resolution):
            Stream, recording and image resolution
        framerate (blueye.protocol.types.Framerate):
            Stream and recording framerate
        camera (blueye.protocol.types.Camera):
            Which camera the parameters belong to.
    """

    h264_bitrate = proto.Field(proto.INT32, number=1)

    mjpg_bitrate = proto.Field(proto.INT32, number=2)

    exposure = proto.Field(proto.INT32, number=3)

    white_balance = proto.Field(proto.INT32, number=4)

    hue = proto.Field(proto.INT32, number=5)

    gain = proto.Field(proto.FLOAT, number=9)

    resolution = proto.Field(proto.ENUM, number=6,
        enum='Resolution',
    )

    framerate = proto.Field(proto.ENUM, number=7,
        enum='Framerate',
    )

    camera = proto.Field(proto.ENUM, number=8,
        enum='Camera',
    )


class OverlayParameters(proto.Message):
    r"""-

    Overlay parameters.

    All available parameters that can be used to configure telemetry
    overlay on video recordings.

    Attributes:
        temperature_enabled (bool):
            If temperature should be included
        depth_enabled (bool):
            If depth should be included
        heading_enabled (bool):
            If heading should be included
        tilt_enabled (bool):
            If camera tilt angle should be included
        thickness_enabled (bool):
            If camera tilt angle should be included
        date_enabled (bool):
            If date should be included
        distance_enabled (bool):
            If distance should be included
        altitude_enabled (bool):
            If altitude should be included
        cp_probe_enabled (bool):
            If cp-probe should be included
        medusa_enabled (bool):
            If medusa measurement should be included
        drone_location_enabled (bool):
            If the drone location coordinates should be
            included
        logo_type (blueye.protocol.types.LogoType):
            Which logo should be used
        depth_unit (blueye.protocol.types.DepthUnit):
            Which unit should be used for depth: Meter,
            Feet or None
        temperature_unit (blueye.protocol.types.TemperatureUnit):
            Which unit should be used for temperature:
            Celcius or Fahrenheit
        thickness_unit (blueye.protocol.types.ThicknessUnit):
            Which unit should be used for thickness:
            Millimeters or Inches
        timezone_offset (int):
            Timezone offset from UTC (min)
        margin_width (int):
            Horizontal margins of text elements (px)
        margin_height (int):
            Vertical margins of text elements (px)
        font_size (blueye.protocol.types.FontSize):
            Font size of text elements
        title (str):
            Optional title
        subtitle (str):
            Optional subtitle
        date_format (str):
            Posix strftime format string for time stamp
        shading (float):
            Pixel intensity to subtract from text
            background (0..1), 0: transparent, 1: black
    """

    temperature_enabled = proto.Field(proto.BOOL, number=1)

    depth_enabled = proto.Field(proto.BOOL, number=2)

    heading_enabled = proto.Field(proto.BOOL, number=3)

    tilt_enabled = proto.Field(proto.BOOL, number=4)

    thickness_enabled = proto.Field(proto.BOOL, number=18)

    date_enabled = proto.Field(proto.BOOL, number=5)

    distance_enabled = proto.Field(proto.BOOL, number=20)

    altitude_enabled = proto.Field(proto.BOOL, number=21)

    cp_probe_enabled = proto.Field(proto.BOOL, number=22)

    medusa_enabled = proto.Field(proto.BOOL, number=24)

    drone_location_enabled = proto.Field(proto.BOOL, number=23)

    logo_type = proto.Field(proto.ENUM, number=6,
        enum='LogoType',
    )

    depth_unit = proto.Field(proto.ENUM, number=7,
        enum='DepthUnit',
    )

    temperature_unit = proto.Field(proto.ENUM, number=8,
        enum='TemperatureUnit',
    )

    thickness_unit = proto.Field(proto.ENUM, number=19,
        enum='ThicknessUnit',
    )

    timezone_offset = proto.Field(proto.INT32, number=9)

    margin_width = proto.Field(proto.INT32, number=10)

    margin_height = proto.Field(proto.INT32, number=11)

    font_size = proto.Field(proto.ENUM, number=12,
        enum='FontSize',
    )

    title = proto.Field(proto.STRING, number=13)

    subtitle = proto.Field(proto.STRING, number=14)

    date_format = proto.Field(proto.STRING, number=16)

    shading = proto.Field(proto.FLOAT, number=17)


class NavigationSensorStatus(proto.Message):
    r"""-

    Navigation sensor used in the position observer with validity state

    Attributes:
        sensor_id (blueye.protocol.types.NavigationSensorID):
            Sensor id
        is_valid (bool):
            Sensor validity
    """

    sensor_id = proto.Field(proto.ENUM, number=1,
        enum='NavigationSensorID',
    )

    is_valid = proto.Field(proto.BOOL, number=2)


class GuestPortDevice(proto.Message):
    r"""-

    GuestPort device.

    Attributes:
        device_id (blueye.protocol.types.GuestPortDeviceID):
            Blueye device identifier
        manufacturer (str):
            Manufacturer name
        name (str):
            Device name
        serial_number (str):
            Serial number
        depth_rating (float):
            Depth rating (m)
        required_blunux_version (str):
            Required Blunux version (x.y.z)
    """

    device_id = proto.Field(proto.ENUM, number=1,
        enum='GuestPortDeviceID',
    )

    manufacturer = proto.Field(proto.STRING, number=2)

    name = proto.Field(proto.STRING, number=3)

    serial_number = proto.Field(proto.STRING, number=4)

    depth_rating = proto.Field(proto.FLOAT, number=5)

    required_blunux_version = proto.Field(proto.STRING, number=6)


class GuestPortDeviceList(proto.Message):
    r"""-

    List of guest port devices.

    Attributes:
        devices (Sequence[blueye.protocol.types.GuestPortDevice]):
            List of guest port devices
    """

    devices = proto.RepeatedField(proto.MESSAGE, number=1,
        message='GuestPortDevice',
    )


class GuestPortConnectorInfo(proto.Message):
    r"""-

    GuestPort connector information.

    Attributes:
        device_list (blueye.protocol.types.GuestPortDeviceList):
            List of devices on this connector
        error (blueye.protocol.types.GuestPortError):
            Guest port error
        guest_port_number (blueye.protocol.types.GuestPortNumber):
            Guest port the connector is connected to
    """

    device_list = proto.Field(proto.MESSAGE, number=1, oneof='connected_device',
        message='GuestPortDeviceList',
    )

    error = proto.Field(proto.ENUM, number=2, oneof='connected_device',
        enum='GuestPortError',
    )

    guest_port_number = proto.Field(proto.ENUM, number=3,
        enum='GuestPortNumber',
    )


class GuestPortInfo(proto.Message):
    r"""-

    GuestPort information.

    Attributes:
        gp1 (blueye.protocol.types.GuestPortConnectorInfo):
            GuestPortConnectorInfo 1
        gp2 (blueye.protocol.types.GuestPortConnectorInfo):
            GuestPortConnectorInfo 2
        gp3 (blueye.protocol.types.GuestPortConnectorInfo):
            GuestPortConnectorInfo 3
    """

    gp1 = proto.Field(proto.MESSAGE, number=1,
        message='GuestPortConnectorInfo',
    )

    gp2 = proto.Field(proto.MESSAGE, number=2,
        message='GuestPortConnectorInfo',
    )

    gp3 = proto.Field(proto.MESSAGE, number=3,
        message='GuestPortConnectorInfo',
    )


class GuestPortRestartInfo(proto.Message):
    r"""-

    GuestPort restart information.

    Attributes:
        power_off_duration (float):
            Duration to keep the guest ports off (s)
    """

    power_off_duration = proto.Field(proto.DOUBLE, number=1)


class ThicknessGauge(proto.Message):
    r"""-

    Thickness measurement data from a Cygnus Thickness Gauge.

    Attributes:
        thickness_measurement (float):
            Thickness measurement of a steel plate
        echo_count (int):
            Indicating the quality of the reading when
            invalid (0-3)
        sound_velocity (int):
            Speed of sound in the steel member (m/s)
        is_measurement_valid (bool):
            Indicating if the measurement is valid
    """

    thickness_measurement = proto.Field(proto.FLOAT, number=1)

    echo_count = proto.Field(proto.UINT32, number=2)

    sound_velocity = proto.Field(proto.UINT32, number=3)

    is_measurement_valid = proto.Field(proto.BOOL, number=4)


class CpProbe(proto.Message):
    r"""-

    Reading from a Cathodic Protection Potential probe.

    Attributes:
        measurement (float):
            Potential measurement (V)
        is_measurement_valid (bool):
            Indicating if the measurement is valid
    """

    measurement = proto.Field(proto.FLOAT, number=1)

    is_measurement_valid = proto.Field(proto.BOOL, number=2)


class GenericServo(proto.Message):
    r"""-

    Servo message used to represent the angle of the servo.

    Attributes:
        value (float):
            Servo value (0..1)
        guest_port_number (blueye.protocol.types.GuestPortNumber):
            Guest port the servo is on
    """

    value = proto.Field(proto.FLOAT, number=1)

    guest_port_number = proto.Field(proto.ENUM, number=2,
        enum='GuestPortNumber',
    )


class MultibeamServo(proto.Message):
    r"""-

    Servo message used to represent the angle of the servo.

    Attributes:
        angle (float):
            Servo degrees (-30..30)
    """

    angle = proto.Field(proto.FLOAT, number=1)


class GuestPortCurrent(proto.Message):
    r"""-

    GuestPort current readings.

    Attributes:
        gp1_bat (float):
            Current on GP1 battery voltage (A)
        gp2_bat (float):
            Current on GP2 battery voltage (A)
        gp3_bat (float):
            Current on GP3 battery voltage (A)
        gp_20v (float):
            Current on common 20V supply (A)
    """

    gp1_bat = proto.Field(proto.DOUBLE, number=1)

    gp2_bat = proto.Field(proto.DOUBLE, number=2)

    gp3_bat = proto.Field(proto.DOUBLE, number=3)

    gp_20v = proto.Field(proto.DOUBLE, number=4)


class Vector3(proto.Message):
    r"""-

    Vector with 3 elements

    Attributes:
        x (float):
            x-component
        y (float):
            y-component
        z (float):
            z-component
    """

    x = proto.Field(proto.DOUBLE, number=1)

    y = proto.Field(proto.DOUBLE, number=2)

    z = proto.Field(proto.DOUBLE, number=3)


class Imu(proto.Message):
    r"""-

    Imu data in drone body frame

    x - forward y - right z - down

    Attributes:
        accelerometer (blueye.protocol.types.Vector3):
            Acceleration (g)
        gyroscope (blueye.protocol.types.Vector3):
            Angular velocity (rad/s)
        magnetometer (blueye.protocol.types.Vector3):
            Magnetic field (μT)
        temperature (float):
            Temperature (°C)
    """

    accelerometer = proto.Field(proto.MESSAGE, number=1,
        message='Vector3',
    )

    gyroscope = proto.Field(proto.MESSAGE, number=2,
        message='Vector3',
    )

    magnetometer = proto.Field(proto.MESSAGE, number=3,
        message='Vector3',
    )

    temperature = proto.Field(proto.FLOAT, number=4)


class MedusaSpectrometerData(proto.Message):
    r"""-

    Medusa gamma ray sensor spectrometer data

    Attributes:
        drone_time (google.protobuf.timestamp_pb2.Timestamp):
            Time stamp when the data is received
        sensor_time (google.protobuf.timestamp_pb2.Timestamp):
            Time stamp the sensor reports
        realtime (float):
            Time the sensor actually measured (s)
        livetime (float):
            Time the measurement took (s)
        total (int):
            Total counts inside the spectrum
        countrate (int):
            Counts per second inside the spectrum
            (rounded)
        cosmics (int):
            Detected counts above the last channel
    """

    drone_time = proto.Field(proto.MESSAGE, number=6,
        message=timestamp.Timestamp,
    )

    sensor_time = proto.Field(proto.MESSAGE, number=7,
        message=timestamp.Timestamp,
    )

    realtime = proto.Field(proto.FLOAT, number=1)

    livetime = proto.Field(proto.FLOAT, number=2)

    total = proto.Field(proto.UINT32, number=3)

    countrate = proto.Field(proto.UINT32, number=4)

    cosmics = proto.Field(proto.UINT32, number=5)


__all__ = tuple(sorted(__protobuf__.manifest))
