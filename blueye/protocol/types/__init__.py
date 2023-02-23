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

from .message_formats import (
    BinlogRecord,
    MotionInput,
    Lights,
    LatLongPosition,
    ConnectionDuration,
    AutoHeadingState,
    AutoDepthState,
    AutoAltitudeState,
    StationKeepingState,
    WeatherVaningState,
    ControlMode,
    TiltStabilizationState,
    SystemTime,
    GripperVelocities,
    ClientInfo,
    ConnectedClient,
    RecordState,
    WaterDensity,
    PingerConfiguration,
    WaterTemperature,
    CPUTemperature,
    CanisterTemperature,
    CanisterHumidity,
    Battery,
    BatteryBQ40Z50,
    Attitude,
    Altitude,
    ForwardDistance,
    PositionEstimate,
    ResetPositionSettings,
    Depth,
    Reference,
    ControlForce,
    ControllerHealth,
    DiveTime,
    RecordOn,
    StorageSpace,
    CalibrationState,
    IperfStatus,
    NStreamers,
    TiltAngle,
    TiltVelocity,
    DroneInfo,
    ErrorFlags,
    CameraParameters,
    OverlayParameters,
    NavigationSensorStatus,
    GuestPortDevice,
    GuestPortDeviceList,
    GuestPortConnectorInfo,
    GuestPortInfo,
    ThicknessGauge,
    CpProbe,
    GenericServo,
    MultibeamServo,
    GuestPortCurrent,
    Vector3,
    Imu,
    HeadingSource,
    Model,
    PressureSensorType,
    Resolution,
    Framerate,
    Camera,
    TemperatureUnit,
    LogoType,
    DepthUnit,
    ThicknessUnit,
    FontSize,
    GuestPortDeviceID,
    GuestPortNumber,
    NavigationSensorID,
    GuestPortError,
)
from .telemetry import (
    AttitudeTel,
    AltitudeTel,
    ForwardDistanceTel,
    PositionEstimateTel,
    DepthTel,
    ReferenceTel,
    ControlForceTel,
    ControllerHealthTel,
    LightsTel,
    GuestPortLightsTel,
    PilotGPSPositionTel,
    RecordStateTel,
    BatteryTel,
    BatteryBQ40Z50Tel,
    DiveTimeTel,
    DroneTimeTel,
    WaterTemperatureTel,
    CPUTemperatureTel,
    CanisterTopTemperatureTel,
    CanisterBottomTemperatureTel,
    CanisterTopHumidityTel,
    CanisterBottomHumidityTel,
    VideoStorageSpaceTel,
    DataStorageSpaceTel,
    CalibrationStateTel,
    TiltStabilizationTel,
    IperfTel,
    NStreamersTel,
    TiltAngleTel,
    DroneInfoTel,
    ErrorFlagsTel,
    ControlModeTel,
    ThicknessGaugeTel,
    CpProbeTel,
    ConnectedClientsTel,
    GenericServoTel,
    MultibeamServoTel,
    GuestPortCurrentTel,
    CalibratedImuTel,
    Imu1Tel,
    Imu2Tel,
)
from .req_rep import (
    SetOverlayParametersReq,
    SetOverlayParametersRep,
    GetOverlayParametersReq,
    GetOverlayParametersRep,
    SetCameraParametersReq,
    SetCameraParametersRep,
    GetCameraParametersReq,
    GetCameraParametersRep,
    SyncTimeReq,
    SyncTimeRep,
    PingReq,
    PingRep,
    SetThicknessGaugeParametersReq,
    SetThicknessGaugeParametersRep,
    ConnectClientReq,
    ConnectClientRep,
    DisconnectClientReq,
    DisconnectClientRep,
    GetBatteryReq,
    GetBatteryRep,
    SetPubFrequencyReq,
    SetPubFrequencyRep,
)
from .control import (
    MotionInputCtrl,
    TiltVelocityCtrl,
    LightsCtrl,
    GuestportLightsCtrl,
    PilotGPSPositionCtrl,
    WatchdogCtrl,
    RecordCtrl,
    TakePictureCtrl,
    StartCalibrationCtrl,
    CancelCalibrationCtrl,
    FinishCalibrationCtrl,
    AutoHeadingCtrl,
    AutoDepthCtrl,
    AutoAltitudeCtrl,
    StationKeepingCtrl,
    WeatherVaningCtrl,
    ResetPositionCtrl,
    ResetOdometerCtrl,
    TiltStabilizationCtrl,
    WaterDensityCtrl,
    PingerConfigurationCtrl,
    SystemTimeCtrl,
    GripperCtrl,
    GenericServoCtrl,
    MultibeamServoCtrl,
    DeactivateGuestPortsCtrl,
    ActivateGuestPortsCtrl,
)

__all__ = (
    'BinlogRecord',
    'MotionInput',
    'Lights',
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
    'ThicknessGauge',
    'CpProbe',
    'GenericServo',
    'MultibeamServo',
    'GuestPortCurrent',
    'Vector3',
    'Imu',
    'HeadingSource',
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
    'AttitudeTel',
    'AltitudeTel',
    'ForwardDistanceTel',
    'PositionEstimateTel',
    'DepthTel',
    'ReferenceTel',
    'ControlForceTel',
    'ControllerHealthTel',
    'LightsTel',
    'GuestPortLightsTel',
    'PilotGPSPositionTel',
    'RecordStateTel',
    'BatteryTel',
    'BatteryBQ40Z50Tel',
    'DiveTimeTel',
    'DroneTimeTel',
    'WaterTemperatureTel',
    'CPUTemperatureTel',
    'CanisterTopTemperatureTel',
    'CanisterBottomTemperatureTel',
    'CanisterTopHumidityTel',
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
    'ConnectedClientsTel',
    'GenericServoTel',
    'MultibeamServoTel',
    'GuestPortCurrentTel',
    'CalibratedImuTel',
    'Imu1Tel',
    'Imu2Tel',
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
    'SetPubFrequencyReq',
    'SetPubFrequencyRep',
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
    'DeactivateGuestPortsCtrl',
    'ActivateGuestPortsCtrl',
)
