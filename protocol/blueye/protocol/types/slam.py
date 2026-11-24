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

from blueye.protocol.types import message_formats
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='blueye.protocol',
    manifest={
        'SlamState',
        'SlamSensorType',
        'SlamPlatform',
        'Sonar3dFrequencyMode',
        'SlamMultibeamMode',
        'SlamRasterFormat',
        'SlamRasterValue',
        'SlamRequestError',
        'SlamOrientationSource',
        'SlamHeadingReference',
        'SlamGeoreferenceSource',
        'SlamBaseMapStage',
        'SlamBaseMapMiss',
        'SlamBaseMapAction',
        'SlamSensor',
        'SlamRecordingState',
        'SlamSonar3dSettings',
        'SlamMultibeamSettings',
        'SlamSensorSettings',
        'SlamSensorStatus',
        'SlamPose',
        'SlamPoseEstimate',
        'SlamKeyframe',
        'SlamRaster',
        'SlamSubmap',
        'SlamKeyframePoses',
        'SlamLoopClosure',
        'SlamMapUpdate',
        'SlamAiding',
        'SlamGeoreference',
        'SlamMapFrame',
        'SlamMap',
        'SlamScan',
        'SlamMapSummary',
        'SlamBaseMapState',
        'SlamBaseMapLoad',
        'SlamBaseMapClear',
        'SlamBaseMapReject',
        'SlamBaseMapHint',
    },
)


class SlamState(proto.Enum):
    r"""State of the SLAM (simultaneous localization and mapping).

    Attributes:
        SLAM_STATE_UNSPECIFIED (0):
            Unspecified.
        SLAM_STATE_WAITING (1):
            Waiting for the first scan and orientation.
        SLAM_STATE_TRACKING (2):
            The latest scan was matched against the map.
        SLAM_STATE_COASTING (3):
            The latest scan could not be matched; the
            pose follows the motion model.
        SLAM_STATE_LOST (4):
            Coasting long enough that the prediction may
            be far off: a scan is placed again only by a
            match that fixes the pose firmly.
    """
    SLAM_STATE_UNSPECIFIED = 0
    """Unspecified."""
    SLAM_STATE_WAITING = 1
    """Waiting for the first scan and orientation."""
    SLAM_STATE_TRACKING = 2
    """The latest scan was matched against the map."""
    SLAM_STATE_COASTING = 3
    """The latest scan could not be matched; the pose follows the
    motion model."""
    SLAM_STATE_LOST = 4
    """Coasting long enough that the prediction may be far off: a
    scan is placed again only by a match that fixes the pose firmly."""


class SlamSensorType(proto.Enum):
    r"""Kind of sensor a SLAM scan comes from.

    Attributes:
        SLAM_SENSOR_TYPE_UNSPECIFIED (0):
            Unspecified.
        SLAM_SENSOR_TYPE_SONAR_3D (1):
            A 3D imaging sonar, e.g. the Water Linked
            Sonar 3D-15.
        SLAM_SENSOR_TYPE_STEREO_CAMERA (2):
            A stereo camera's depth.
        SLAM_SENSOR_TYPE_MULTIBEAM_2D (3):
            A 2D imaging sonar (multibeam), e.g. the
            Oculus M750D: range and bearing, no elevation.
    """
    SLAM_SENSOR_TYPE_UNSPECIFIED = 0
    """Unspecified."""
    SLAM_SENSOR_TYPE_SONAR_3D = 1
    """A 3D imaging sonar, e.g. the Water Linked Sonar 3D-15."""
    SLAM_SENSOR_TYPE_STEREO_CAMERA = 2
    """A stereo camera's depth."""
    SLAM_SENSOR_TYPE_MULTIBEAM_2D = 3
    """A 2D imaging sonar (multibeam), e.g. the Oculus M750D: range
    and bearing, no elevation."""


class SlamPlatform(proto.Enum):
    r"""What the SLAM's poses are the poses of: its platform.

    Attributes:
        SLAM_PLATFORM_UNSPECIFIED (0):
            Not known.
        SLAM_PLATFORM_DRONE (1):
            The drone, its body frame x forward, y right,
            z down from the middle of the hull. Each sensor
            is on it through its mount (SlamPose mount in
            the messages that carry one).
        SLAM_PLATFORM_SENSOR (2):
            The sensor itself: the SLAM did not know how
            the sensor is mounted.
    """
    SLAM_PLATFORM_UNSPECIFIED = 0
    """Not known."""
    SLAM_PLATFORM_DRONE = 1
    """The drone, its body frame x forward, y right, z down from the
    middle of the hull. Each sensor is on it through its mount
    (SlamPose mount in the messages that carry one)."""
    SLAM_PLATFORM_SENSOR = 2
    """The sensor itself: the SLAM did not know how the sensor is
    mounted."""


class Sonar3dFrequencyMode(proto.Enum):
    r"""Frequency mode of a 3D imaging sonar.

    Attributes:
        SONAR_3D_FREQUENCY_MODE_UNSPECIFIED (0):
            Unspecified: left as it is.
        SONAR_3D_FREQUENCY_MODE_LOW (1):
            Wide view, long range (3D-15: 90° x 40°, 15
            m, 5 scans/s).
        SONAR_3D_FREQUENCY_MODE_HIGH (2):
            Narrow view, short range, fine detail (3D-15:
            40° x 40°, 4 m, 20 scans/s).
    """
    SONAR_3D_FREQUENCY_MODE_UNSPECIFIED = 0
    """Unspecified: left as it is."""
    SONAR_3D_FREQUENCY_MODE_LOW = 1
    """Wide view, long range (3D-15: 90° x 40°, 15 m, 5 scans/s)."""
    SONAR_3D_FREQUENCY_MODE_HIGH = 2
    """Narrow view, short range, fine detail (3D-15: 40° x 40°, 4 m,
    20 scans/s)."""


class SlamMultibeamMode(proto.Enum):
    r"""How the SLAM places the returns of a 2D multibeam sonar,
    which have a range and a bearing but no elevation.

    Attributes:
        SLAM_MULTIBEAM_MODE_UNSPECIFIED (0):
            Unspecified: left as it is.
        SLAM_MULTIBEAM_MODE_AUTO (1):
            By the sonar's tilt: on the seabed when it
            looks down, in a level plane through it when it
            is near level.
        SLAM_MULTIBEAM_MODE_SEABED (2):
            On a flat seabed, at the drone's altitude
            above it (seabed surveys).
        SLAM_MULTIBEAM_MODE_STRUCTURE (3):
            In a level plane through the sonar, each
            return at its range, as on walls, piles and nets
            (the sonar near level).
    """
    SLAM_MULTIBEAM_MODE_UNSPECIFIED = 0
    """Unspecified: left as it is."""
    SLAM_MULTIBEAM_MODE_AUTO = 1
    """By the sonar's tilt: on the seabed when it looks down, in a
    level plane through it when it is near level."""
    SLAM_MULTIBEAM_MODE_SEABED = 2
    """On a flat seabed, at the drone's altitude above it (seabed
    surveys)."""
    SLAM_MULTIBEAM_MODE_STRUCTURE = 3
    """In a level plane through the sonar, each return at its range,
    as on walls, piles and nets (the sonar near level)."""


class SlamRasterFormat(proto.Enum):
    r"""How a raster's pixels are stored.

    Attributes:
        SLAM_RASTER_FORMAT_UNSPECIFIED (0):
            Unspecified.
        SLAM_RASTER_FORMAT_UINT8 (1):
            One byte a pixel, 0 to 255.
    """
    SLAM_RASTER_FORMAT_UNSPECIFIED = 0
    """Unspecified."""
    SLAM_RASTER_FORMAT_UINT8 = 1
    """One byte a pixel, 0 to 255."""


class SlamRasterValue(proto.Enum):
    r"""What a raster's pixels measure.

    Attributes:
        SLAM_RASTER_VALUE_UNSPECIFIED (0):
            Unspecified.
        SLAM_RASTER_VALUE_ECHO (1):
            Echo strength (a sonar mosaic), on one
            relative scale for all of a sensor's rasters:
            higher is stronger.
    """
    SLAM_RASTER_VALUE_UNSPECIFIED = 0
    """Unspecified."""
    SLAM_RASTER_VALUE_ECHO = 1
    """Echo strength (a sonar mosaic), on one relative scale for all
    of a sensor's rasters: higher is stronger."""


class SlamRequestError(proto.Enum):
    r"""Why the SLAM did not do what a request asked (the reply says
    what it did do).

    Attributes:
        SLAM_REQUEST_ERROR_UNSPECIFIED (0):
            None: the request was done, or asked for what
            already was.
        SLAM_REQUEST_ERROR_NOT_READABLE (1):
            The request could not be read.
        SLAM_REQUEST_ERROR_OTHER_MAP (2):
            The request named a map that is not the
            current one.
        SLAM_REQUEST_ERROR_NO_SUCH_SENSOR (3):
            The request named a sensor the SLAM does not
            have, or named none where it has several that
            fit.
        SLAM_REQUEST_ERROR_SENSOR (4):
            The sensor did not take it (it did not
            answer, or refused).
        SLAM_REQUEST_ERROR_BUSY (5):
            Another change to the sensor is under way;
            ask again after it.
        SLAM_REQUEST_ERROR_NOT_MAPPING (6):
            It needs the SLAM to be mapping (a
            recording).
        SLAM_REQUEST_ERROR_STORAGE (7):
            No storage to record to, or it is full.
        SLAM_REQUEST_ERROR_NOT_SUPPORTED (8):
            The SLAM or its sensor cannot do it.
        SLAM_REQUEST_ERROR_NO_BASE_MAP (9):
            It needs a base map, and none is loaded.
        SLAM_REQUEST_ERROR_BASE_MAP_UNREADABLE (10):
            The base map named cannot be loaded. For a
            name that is not a bare file name (.sbez), or a
            file that is not there, the reply has this error
            at once, and the base map before stays. A file
            that holds no map the SLAM can localize in ends
            its load FAILED, with this error in
            SlamBaseMapState.error.
        SLAM_REQUEST_ERROR_OTHER_BASE_MAP (11):
            The request named a load of a base map that
            is not the current one.
        SLAM_REQUEST_ERROR_OTHER_FIX (12):
            The request named a place found that is not
            the current one.
    """
    SLAM_REQUEST_ERROR_UNSPECIFIED = 0
    """None: the request was done, or asked for what already was."""
    SLAM_REQUEST_ERROR_NOT_READABLE = 1
    """The request could not be read."""
    SLAM_REQUEST_ERROR_OTHER_MAP = 2
    """The request named a map that is not the current one."""
    SLAM_REQUEST_ERROR_NO_SUCH_SENSOR = 3
    """The request named a sensor the SLAM does not have, or named
    none where it has several that fit."""
    SLAM_REQUEST_ERROR_SENSOR = 4
    """The sensor did not take it (it did not answer, or refused)."""
    SLAM_REQUEST_ERROR_BUSY = 5
    """Another change to the sensor is under way; ask again after
    it."""
    SLAM_REQUEST_ERROR_NOT_MAPPING = 6
    """It needs the SLAM to be mapping (a recording)."""
    SLAM_REQUEST_ERROR_STORAGE = 7
    """No storage to record to, or it is full."""
    SLAM_REQUEST_ERROR_NOT_SUPPORTED = 8
    """The SLAM or its sensor cannot do it."""
    SLAM_REQUEST_ERROR_NO_BASE_MAP = 9
    """It needs a base map, and none is loaded."""
    SLAM_REQUEST_ERROR_BASE_MAP_UNREADABLE = 10
    """The base map named cannot be loaded. For a name that is not a
    bare file name (.sbez), or a file that is not there, the reply
    has this error at once, and the base map before stays. A file
    that holds no map the SLAM can localize in ends its load FAILED,
    with this error in SlamBaseMapState.error."""
    SLAM_REQUEST_ERROR_OTHER_BASE_MAP = 11
    """The request named a load of a base map that is not the
    current one."""
    SLAM_REQUEST_ERROR_OTHER_FIX = 12
    """The request named a place found that is not the current one."""


class SlamOrientationSource(proto.Enum):
    r"""Where the SLAM's orientation comes from.

    Attributes:
        SLAM_ORIENTATION_SOURCE_UNSPECIFIED (0):
            None: the scans are matched without an
            orientation.
        SLAM_ORIENTATION_SOURCE_SENSOR_IMU (1):
            The sensor's own IMU.
        SLAM_ORIENTATION_SOURCE_DRONE_ATTITUDE (2):
            The drone's attitude, its heading from the
            compass.
        SLAM_ORIENTATION_SOURCE_DRONE_GYRO (3):
            The drone's attitude for roll and pitch, its
            turn from the drone's calibrated gyro (not the
            compass).
        SLAM_ORIENTATION_SOURCE_DRONE_ESTIMATE (4):
            The drone's attitude for roll and pitch, its
            heading the one the drone's position estimate
            keeps (its navigation's: from a gyro, a DVL or
            the compass, as the drone has them).
    """
    SLAM_ORIENTATION_SOURCE_UNSPECIFIED = 0
    """None: the scans are matched without an orientation."""
    SLAM_ORIENTATION_SOURCE_SENSOR_IMU = 1
    """The sensor's own IMU."""
    SLAM_ORIENTATION_SOURCE_DRONE_ATTITUDE = 2
    """The drone's attitude, its heading from the compass."""
    SLAM_ORIENTATION_SOURCE_DRONE_GYRO = 3
    """The drone's attitude for roll and pitch, its turn from the
    drone's calibrated gyro (not the compass)."""
    SLAM_ORIENTATION_SOURCE_DRONE_ESTIMATE = 4
    """The drone's attitude for roll and pitch, its heading the one
    the drone's position estimate keeps (its navigation's: from a
    gyro, a DVL or the compass, as the drone has them)."""


class SlamHeadingReference(proto.Enum):
    r"""What the x axis of a SLAM map's frame points along.

    Attributes:
        SLAM_HEADING_REFERENCE_UNSPECIFIED (0):
            Not known.
        SLAM_HEADING_REFERENCE_FIRST_SCAN (1):
            The platform's heading at the map's first
            scan; without gravity alignment, the platform's
            frame at the first scan as it is.
        SLAM_HEADING_REFERENCE_DRONE_COMPASS (2):
            North, as the drone's compass heading
            (AttitudeTel yaw) gave it at the map's first
            scan.
    """
    SLAM_HEADING_REFERENCE_UNSPECIFIED = 0
    """Not known."""
    SLAM_HEADING_REFERENCE_FIRST_SCAN = 1
    """The platform's heading at the map's first scan; without
    gravity alignment, the platform's frame at the first scan as it
    is."""
    SLAM_HEADING_REFERENCE_DRONE_COMPASS = 2
    """North, as the drone's compass heading (AttitudeTel yaw) gave
    it at the map's first scan."""


class SlamGeoreferenceSource(proto.Enum):
    r"""What placed a SLAM map on the Earth.

    Attributes:
        SLAM_GEOREFERENCE_SOURCE_UNSPECIFIED (0):
            Unspecified.
        SLAM_GEOREFERENCE_SOURCE_GNSS (1):
            The drone's GNSS receiver (the Blueye GNSS),
            from its fixes at the surface.
    """
    SLAM_GEOREFERENCE_SOURCE_UNSPECIFIED = 0
    """Unspecified."""
    SLAM_GEOREFERENCE_SOURCE_GNSS = 1
    """The drone's GNSS receiver (the Blueye GNSS), from its fixes
    at the surface."""


class SlamBaseMapStage(proto.Enum):
    r"""Where finding the SLAM's map in a base map stands. A base map
    is a map saved earlier (a recording's, or a file a client
    uploaded), loaded so that the SLAM finds where its own map lies
    in it: it searches the base map for what it swept lately, and
    once found, ties its map to the base map with each later match.

    Attributes:
        SLAM_BASE_MAP_STAGE_UNSPECIFIED (0):
            No base map.
        SLAM_BASE_MAP_STAGE_LOADING (1):
            Being read; a recording without its map file
            takes longest.
        SLAM_BASE_MAP_STAGE_SWEEPING (2):
            Loaded; too little swept yet to search with
            (progress).
        SLAM_BASE_MAP_STAGE_SEARCHING (3):
            Searched, no place taken yet (miss says why).
        SLAM_BASE_MAP_STAGE_CANDIDATE (4):
            A place passed one search; the next must
            agree before it is taken.
        SLAM_BASE_MAP_STAGE_FOUND (5):
            Found: base_map_pose is known, and each later match keeps
            it.
        SLAM_BASE_MAP_STAGE_FAILED (6):
            It could not be loaded (error); the SLAM maps
            without it.
    """
    SLAM_BASE_MAP_STAGE_UNSPECIFIED = 0
    """No base map."""
    SLAM_BASE_MAP_STAGE_LOADING = 1
    """Being read; a recording without its map file takes longest."""
    SLAM_BASE_MAP_STAGE_SWEEPING = 2
    """Loaded; too little swept yet to search with (progress)."""
    SLAM_BASE_MAP_STAGE_SEARCHING = 3
    """Searched, no place taken yet (miss says why)."""
    SLAM_BASE_MAP_STAGE_CANDIDATE = 4
    """A place passed one search; the next must agree before it is
    taken."""
    SLAM_BASE_MAP_STAGE_FOUND = 5
    """Found: base_map_pose is known, and each later match keeps it."""
    SLAM_BASE_MAP_STAGE_FAILED = 6
    """It could not be loaded (error); the SLAM maps without it."""


class SlamBaseMapMiss(proto.Enum):
    r"""Why the last search of a base map took no place.

    Attributes:
        SLAM_BASE_MAP_MISS_UNSPECIFIED (0):
            None: a place was taken, or nothing searched
            yet.
        SLAM_BASE_MAP_MISS_NO_MATCH (1):
            Nothing scored: what was swept matched
            nothing in the base map.
        SLAM_BASE_MAP_MISS_OFF_MAP (2):
            Too little of what was swept lies on the base
            map: the drone may be off it.
        SLAM_BASE_MAP_MISS_AMBIGUOUS (3):
            Another place scores nearly as well: places
            that look alike.
        SLAM_BASE_MAP_MISS_REJECTED (4):
            Only places a client rejected scored
            (SlamBaseMapReject).
        SLAM_BASE_MAP_MISS_WEAK (5):
            Found before; near there this search scored
            too low (the drone may be off it).
        SLAM_BASE_MAP_MISS_OUTSIDE_HINT (6):
            A place outside the hint scored better than
            any in it, by the margin a place needs: the hint
            was dropped.
    """
    SLAM_BASE_MAP_MISS_UNSPECIFIED = 0
    """None: a place was taken, or nothing searched yet."""
    SLAM_BASE_MAP_MISS_NO_MATCH = 1
    """Nothing scored: what was swept matched nothing in the base
    map."""
    SLAM_BASE_MAP_MISS_OFF_MAP = 2
    """Too little of what was swept lies on the base map: the drone
    may be off it."""
    SLAM_BASE_MAP_MISS_AMBIGUOUS = 3
    """Another place scores nearly as well: places that look alike."""
    SLAM_BASE_MAP_MISS_REJECTED = 4
    """Only places a client rejected scored (SlamBaseMapReject)."""
    SLAM_BASE_MAP_MISS_WEAK = 5
    """Found before; near there this search scored too low (the
    drone may be off it)."""
    SLAM_BASE_MAP_MISS_OUTSIDE_HINT = 6
    """A place outside the hint scored better than any in it, by the
    margin a place needs: the hint was dropped."""


class SlamBaseMapAction(proto.Enum):
    r"""What a client may ask of the base map (SetSlamBaseMapReq's
    actions).

    Attributes:
        SLAM_BASE_MAP_ACTION_UNSPECIFIED (0):
            None.
        SLAM_BASE_MAP_ACTION_LOAD (1):
            SlamBaseMapLoad.
        SLAM_BASE_MAP_ACTION_CLEAR (2):
            SlamBaseMapClear.
        SLAM_BASE_MAP_ACTION_REJECT (3):
            SlamBaseMapReject.
        SLAM_BASE_MAP_ACTION_HINT (4):
            SlamBaseMapHint.
    """
    SLAM_BASE_MAP_ACTION_UNSPECIFIED = 0
    """None."""
    SLAM_BASE_MAP_ACTION_LOAD = 1
    """SlamBaseMapLoad."""
    SLAM_BASE_MAP_ACTION_CLEAR = 2
    """SlamBaseMapClear."""
    SLAM_BASE_MAP_ACTION_REJECT = 3
    """SlamBaseMapReject."""
    SLAM_BASE_MAP_ACTION_HINT = 4
    """SlamBaseMapHint."""


class SlamSensor(proto.Message):
    r"""A sensor whose scans feed the SLAM, and its field of view.

    Attributes:
        id (str):
            Sensor id, unique among the SLAM's sensors. A
            sensor keeps the id it was given for as long as
            it is connected, whatever other sensors connect
            or disconnect: the model's (e.g.
            "waterlinked-sonar-3d15") when no other sensor
            of that model is connected, and else the model's
            with the guest port the sensor is on added (e.g.
            "waterlinked-sonar-3d15-gp2").
        sensor_type (blueye.protocol.types.SlamSensorType):
            Kind of sensor.
        fov_horizontal (float):
            Horizontal field of view, about the sensor's
            z axis (°).
        fov_vertical (float):
            Vertical field of view, about the sensor's y
            axis (°).
        max_range (float):
            Range the sensor is set to (m).
        device_id (blueye.protocol.types.GuestPortDeviceID):
            The sensor as a guest port device (e.g.
            GUEST_PORT_DEVICE_ID_WATERLINKED_SONAR_3D15), for a client
            to show the device itself; GUEST_PORT_DEVICE_ID_UNSPECIFIED
            when it is not one (a simulated sensor).
        simulated (bool):
            True if the sensor is simulated (its scans
            are made up, for testing).
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sensor_type: 'SlamSensorType' = proto.Field(
        proto.ENUM,
        number=2,
        enum='SlamSensorType',
    )
    fov_horizontal: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    fov_vertical: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    max_range: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    device_id: message_formats.GuestPortDeviceID = proto.Field(
        proto.ENUM,
        number=6,
        enum=message_formats.GuestPortDeviceID,
    )
    simulated: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class SlamRecordingState(proto.Message):
    r"""A recording of the SLAM, as the SLAM reports it.

    A recording is a .sbez file (a binlog) with the SLAM's output:
    the map at its start, then the poses, the map updates and the
    status. It may hold several maps (a reset, or a new mode, starts
    one), and each map it holds ends with the whole map (SlamMapTel,
    in parts when it is large). With sensor data it also has the
    sensor's raw data beside it (for a 3D sonar a .sonar file), and
    the drone's dive log logs its telemetry at higher rates while it
    runs, so the SLAM can be run again on both without the drone.

    Attributes:
        is_recording (bool):
            True while recording.
        name (str):
            File name of the .sbez, without its folder.
        seconds (int):
            Time recorded (s).
        size (int):
            Size of the recording's files so far (bytes).
        sensor_data (bool):
            True if the sensor's raw data is recorded
            too.
        storage_location (blueye.protocol.types.StorageLocation):
            Where the recording is stored.
    """

    is_recording: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    seconds: int = proto.Field(
        proto.INT32,
        number=3,
    )
    size: int = proto.Field(
        proto.UINT64,
        number=4,
    )
    sensor_data: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    storage_location: message_formats.StorageLocation = proto.Field(
        proto.ENUM,
        number=6,
        enum=message_formats.StorageLocation,
    )


class SlamSonar3dSettings(proto.Message):
    r"""Settings of a 3D imaging sonar that feeds the SLAM.

    In a request, unspecified or 0 leaves a setting as it is; in a
    report, it means the sonar does not say (e.g. a firmware without
    frequency modes).

    Attributes:
        frequency_mode (blueye.protocol.types.Sonar3dFrequencyMode):
            Frequency mode.
        max_range (float):
            Maximum range (m).
    """

    frequency_mode: 'Sonar3dFrequencyMode' = proto.Field(
        proto.ENUM,
        number=1,
        enum='Sonar3dFrequencyMode',
    )
    max_range: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class SlamMultibeamSettings(proto.Message):
    r"""Settings of a 2D multibeam sonar that feeds the SLAM.

    The sonar's own settings (range, gain, frequency, ping rate)
    belong to the multibeam page: the SLAM reads the sonar's images
    and follows those settings without changing them. In a request,
    unspecified leaves a setting as it is; in a report, the mode is
    as set (AUTO, not the one it chose).

    Attributes:
        mode (blueye.protocol.types.SlamMultibeamMode):
            How the returns are placed.
    """

    mode: 'SlamMultibeamMode' = proto.Field(
        proto.ENUM,
        number=1,
        enum='SlamMultibeamMode',
    )


class SlamSensorSettings(proto.Message):
    r"""Settings of a sensor that feeds the SLAM.

    One message for each kind of sensor, so a client shows the
    settings of the sensors the SLAM has, and a sensor takes only
    its own.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sonar_3d (blueye.protocol.types.SlamSonar3dSettings):
            A 3D imaging sonar's settings.

            This field is a member of `oneof`_ ``settings``.
        multibeam (blueye.protocol.types.SlamMultibeamSettings):
            A 2D multibeam sonar's settings.

            This field is a member of `oneof`_ ``settings``.
    """

    sonar_3d: 'SlamSonar3dSettings' = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='settings',
        message='SlamSonar3dSettings',
    )
    multibeam: 'SlamMultibeamSettings' = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='settings',
        message='SlamMultibeamSettings',
    )


class SlamSensorStatus(proto.Message):
    r"""A sensor that feeds the SLAM, as the SLAM reports it.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sensor (blueye.protocol.types.SlamSensor):
            The sensor, as its latest scan described it
            (before its first scan, its id and type only).
        settings (blueye.protocol.types.SlamSensorSettings):
            The sensor's settings, unset when it has none
            or they cannot be read.
        mount (blueye.protocol.types.SlamPose):
            The sensor's pose on the platform now: its
            mount, at the mount's tilt now. Unset when the
            platform is the sensor.
        mount_tilt (float):
            Tilt of the sensor's mount (°, positive up),
            for a mount that tilts.

            This field is a member of `oneof`_ ``_mount_tilt``.
    """

    sensor: 'SlamSensor' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='SlamSensor',
    )
    settings: 'SlamSensorSettings' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='SlamSensorSettings',
    )
    mount: 'SlamPose' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='SlamPose',
    )
    mount_tilt: float = proto.Field(
        proto.FLOAT,
        number=4,
        optional=True,
    )


class SlamPose(proto.Message):
    r"""A pose: of a body in the SLAM map frame, or of a sensor on
    the platform.
    The map frame is fixed where the map was started (see
    SlamMapFrame): z down, x along the heading the map started with
    (north when a compass heading was used), y to the right of it,
    in metres. The body is the one the field names (the platform, or
    a sensor), its frame x forward, y right, z down. A mount is a
    sensor's pose in the platform's frame instead: the sensor is in
    the map at the platform's pose times its mount. A raster's
    origin is its pose in the frame the enclosing message names (see
    SlamRaster).

    Attributes:
        position (blueye.protocol.types.Vector3):
            Position of the body (m).
        orientation (blueye.protocol.types.Quaternion):
            Rotation from the body's frame to the frame
            it is placed in.
    """

    position: message_formats.Vector3 = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Vector3,
    )
    orientation: message_formats.Quaternion = proto.Field(
        proto.MESSAGE,
        number=2,
        message=message_formats.Quaternion,
    )


class SlamPoseEstimate(proto.Message):
    r"""The SLAM estimate of its platform's pose, published for every
    scan.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        map_id (int):
            Identifier of the map; a new one is chosen
            whenever the map restarts.
        state (blueye.protocol.types.SlamState):
            State of the SLAM.
        pose (blueye.protocol.types.SlamPose):
            Pose of the platform (SlamMapFrame.platform)
            at the scan.
        time (google.protobuf.timestamp_pb2.Timestamp):
            Host time the scan was received.
        scan_points (int):
            Points (or cells) of the scan used for
            matching.
        match_inlier_ratio (float):
            Share of those matched to the map (0..1).
        match_rms (float):
            Root mean square residual of the matched
            points against the map (m); for a 3D sonar,
            their distance to the map's planes. 0 when the
            matcher has none (a 2D multibeam matches
            images).
        keyframe_count (int):
            Keyframes in the map.
        map_point_count (int):
            Points (or cells) in the map.
        depth (float):
            Depth used for the scan (m), when there was
            one: the sensor's, from the drone's depth sensor
            through the mount (without a mount, the depth
            sensor's own).

            This field is a member of `oneof`_ ``_depth``.
        sensor_id (str):
            Sensor whose scan was placed (SlamSensor.id).
        mount (blueye.protocol.types.SlamPose):
            The sensor's pose on the platform at the
            scan: the sensor was at pose times mount. Unset
            when the platform is the sensor.
        covariance_elements (MutableSequence[float]):
            Covariance of pose as the scan's match placed
            it against the map, given the prediction: 6 x 6,
            row by row, of a rotation about the map's x, y
            and z axes (rad) and then a position along them
            (m). It says how well this scan fixed the pose,
            not how far the map has drifted. Empty when the
            match gave none: the scan was not matched, the
            map's first scan (nothing to match it against),
            or a fit whose covariance was not finite.
        keyframe_id (int):
            The newest keyframe when the scan was placed
            (SlamKeyframe.id), 0 before the map's first. A
            client keeping poses can move one with that
            keyframe when a loop closure moves it: the pose
            becomes the keyframe's new pose times its pose
            then, inverted, times the pose.
    """

    map_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    state: 'SlamState' = proto.Field(
        proto.ENUM,
        number=2,
        enum='SlamState',
    )
    pose: 'SlamPose' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='SlamPose',
    )
    time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    scan_points: int = proto.Field(
        proto.UINT32,
        number=5,
    )
    match_inlier_ratio: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    match_rms: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    keyframe_count: int = proto.Field(
        proto.UINT32,
        number=8,
    )
    map_point_count: int = proto.Field(
        proto.UINT32,
        number=9,
    )
    depth: float = proto.Field(
        proto.FLOAT,
        number=10,
        optional=True,
    )
    sensor_id: str = proto.Field(
        proto.STRING,
        number=11,
    )
    mount: 'SlamPose' = proto.Field(
        proto.MESSAGE,
        number=12,
        message='SlamPose',
    )
    covariance_elements: MutableSequence[float] = proto.RepeatedField(
        proto.FLOAT,
        number=13,
    )
    keyframe_id: int = proto.Field(
        proto.UINT32,
        number=14,
    )


class SlamKeyframe(proto.Message):
    r"""A keyframe: a scan kept in the map, the nodes of the SLAM
    trajectory.

    Attributes:
        id (int):
            Keyframe id, increasing along the trajectory.
        submap_id (int):
            Submap whose content the keyframe added to.
        pose (blueye.protocol.types.SlamPose):
            Pose of the platform at the keyframe. It
            moves when the trajectory is corrected.
        time (google.protobuf.timestamp_pb2.Timestamp):
            Host time the keyframe's scan was received.
        sensor_id (str):
            Sensor whose scan the keyframe is
            (SlamSensor.id).
        mount (blueye.protocol.types.SlamPose):
            The sensor's pose on the platform at the
            keyframe. Unset when the platform is the sensor.
    """

    id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    submap_id: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    pose: 'SlamPose' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='SlamPose',
    )
    time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    sensor_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    mount: 'SlamPose' = proto.Field(
        proto.MESSAGE,
        number=6,
        message='SlamPose',
    )


class SlamRaster(proto.Message):
    r"""A raster: an image laid on a plane, such as a 2D imaging sonar's
    mosaic of what it saw around a submap.

    The raster has a frame of its own, which origin places in the frame
    the enclosing message names: in a SlamSubmap, the platform's frame
    at its anchor keyframe, so the raster is in the map at the anchor's
    pose times its origin. It lies on the plane z = 0 of its frame, with
    the corner of row 0 and column 0 at the origin: row r and column c
    cover x from r \* resolution and y from c \* resolution, each over
    one resolution.

    Its planes come deflated (zlib): pixels_deflated inflates to exactly
    rows \* columns pixels as pixel_format stores them, and
    coverage_deflated is empty or inflates to exactly rows \* columns
    bytes. A raster that disagrees, whose resolution is not positive or
    origin is unset, or whose pixel_format or value the client does not
    know, is not used: the submap keeps the raster it had. A change to
    how pixels are placed or read comes as a new pixel_format, a new
    kind of content, or new fields that leave pixels_deflated empty,
    never as a field old clients would ignore while they read
    pixels_deflated.

    Attributes:
        origin (blueye.protocol.types.SlamPose):
            The raster's frame, in the frame the
            enclosing message names.
        rows (int):
            Rows: the raster spans rows \* resolution along its x.
        columns (int):
            Columns: the raster spans columns \* resolution along its y.
        resolution (float):
            Size of a pixel, along x and along y (m).
            Rasters of one map may differ in it: a
            multibeam's submaps are painted as finely as
            their sonar's range calls for.
        pixel_format (blueye.protocol.types.SlamRasterFormat):
            How the pixels are stored.
        value (blueye.protocol.types.SlamRasterValue):
            What the pixels measure.
        pixels_deflated (bytes):
            The pixels, rows \* columns of them row by row, each as
            pixel_format stores it, compressed with zlib (deflate in a
            zlib stream, RFC 1950): a fraction of the bytes over the
            link.
        coverage_deflated (bytes):
            How well each pixel was seen, compressed the same way: rows
            \* columns bytes, row by row, from 0 (not seen: the pixel
            holds nothing) to 255, for weighing rasters where they
            overlap. Empty: every pixel seen fully, as 255.
    """

    origin: 'SlamPose' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='SlamPose',
    )
    rows: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    columns: int = proto.Field(
        proto.UINT32,
        number=3,
    )
    resolution: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    pixel_format: 'SlamRasterFormat' = proto.Field(
        proto.ENUM,
        number=5,
        enum='SlamRasterFormat',
    )
    value: 'SlamRasterValue' = proto.Field(
        proto.ENUM,
        number=6,
        enum='SlamRasterValue',
    )
    pixels_deflated: bytes = proto.Field(
        proto.BYTES,
        number=7,
    )
    coverage_deflated: bytes = proto.Field(
        proto.BYTES,
        number=8,
    )


class SlamSubmap(proto.Message):
    r"""A submap: part of the map from one sensor, in the platform's
    frame at its anchor keyframe.

    A submap moves rigidly with its anchor keyframe, so a correction
    of the trajectory moves its content without sending it again. A
    submap holds one kind of content: points, or a raster (e.g. a 2D
    sonar's mosaic). Each kind says how a later one replaces what
    the submap holds.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        submap_id (int):
            Submap id.
        anchor_keyframe_id (int):
            Keyframe whose platform frame the content is
            in.
        sensor_id (str):
            Sensor the content comes from
            (SlamSensor.id).
        points (blueye.protocol.types.PointCloud):
            Points in the platform's frame at the anchor
            keyframe. In a map update they are appended to
            the submap's points, unless replace is set.

            This field is a member of `oneof`_ ``content``.
        raster (blueye.protocol.types.SlamRaster):
            A raster placed in the platform's frame at
            the anchor keyframe (SlamRaster.origin). It is
            sent whole, and replaces the submap's raster so
            far: as the submap grows, its raster is sent
            again.

            This field is a member of `oneof`_ ``content``.
        replace (bool):
            Points: true if they replace the submap's
            points so far, rather than adding to them.
    """

    submap_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    anchor_keyframe_id: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    sensor_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    points: message_formats.PointCloud = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof='content',
        message=message_formats.PointCloud,
    )
    raster: 'SlamRaster' = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof='content',
        message='SlamRaster',
    )
    replace: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class SlamKeyframePoses(proto.Message):
    r"""Poses of consecutive keyframes, packed: what a correction of
    the trajectory moved, sent without the rest of each keyframe.

    Attributes:
        first_keyframe_id (int):
            Keyframe id of the first pose; the others
            follow it in id order.
        poses (bytes):
            Platform poses as in SlamKeyframe.pose, 7
            little-endian float32 each: x, y, z (m), then
            the orientation's x, y, z, w. 28 bytes per
            keyframe.
    """

    first_keyframe_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    poses: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class SlamLoopClosure(proto.Message):
    r"""A loop closure: a keyframe's scan matched to the map where
    the trajectory had been before, which corrected the trajectory.
    The keyframes the correction moved come in the same update, so a
    client that held the map before has the trajectory as it was.

    Attributes:
        keyframe_id (int):
            Keyframe whose scan closed the loop.
        matched_keyframe_id (int):
            Earlier keyframe it was matched near.
        position_correction (float):
            How far the correction moved the newest
            keyframe it reached (m): the loop's keyframe, or
            one added while the loop was being closed.
        heading_correction (float):
            How far it turned that keyframe about the
            map's z axis (°, positive clockwise seen from
            above in a gravity-aligned map).
    """

    keyframe_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    matched_keyframe_id: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    position_correction: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    heading_correction: float = proto.Field(
        proto.FLOAT,
        number=4,
    )


class SlamMapUpdate(proto.Message):
    r"""A change to the SLAM map.

    Updates are numbered: a client that has the map at sequence N
    applies the update with sequence N + 1 next. When it misses one,
    or the map id changes, it asks to catch up (GetSlamMapReq): it
    gets the updates it missed again, or the whole map.

    Attributes:
        map_id (int):
            Identifier of the map.
        sequence (int):
            Sequence number of this update, from 1.
        keyframes (MutableSequence[blueye.protocol.types.SlamKeyframe]):
            Keyframes added.
        submaps (MutableSequence[blueye.protocol.types.SlamSubmap]):
            Content added to submaps, or replacing a
            submap's: points with SlamSubmap.replace set,
            and rasters.
        frame (blueye.protocol.types.SlamMapFrame):
            The map's frame, on the update that adds the
            first keyframe and on any that learns more of
            it: a recording cut short has it without its
            last SlamMapTel.
        loop_closures (MutableSequence[blueye.protocol.types.SlamLoopClosure]):
            Loop closures whose correction moved the
            keyframes.
        moved_poses (MutableSequence[blueye.protocol.types.SlamKeyframePoses]):
            New poses of the keyframes a correction
            moved, in runs.
        removed_submap_ids (MutableSequence[int]):
            Submaps taken out of the map, with whatever
            they hold.
    """

    map_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    sequence: int = proto.Field(
        proto.UINT64,
        number=2,
    )
    keyframes: MutableSequence['SlamKeyframe'] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='SlamKeyframe',
    )
    submaps: MutableSequence['SlamSubmap'] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message='SlamSubmap',
    )
    frame: 'SlamMapFrame' = proto.Field(
        proto.MESSAGE,
        number=5,
        message='SlamMapFrame',
    )
    loop_closures: MutableSequence['SlamLoopClosure'] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message='SlamLoopClosure',
    )
    moved_poses: MutableSequence['SlamKeyframePoses'] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message='SlamKeyframePoses',
    )
    removed_submap_ids: MutableSequence[int] = proto.RepeatedField(
        proto.UINT32,
        number=8,
    )


class SlamAiding(proto.Message):
    r"""What other than its sensors the SLAM's estimate rests on now.

    Attributes:
        orientation (blueye.protocol.types.SlamOrientationSource):
            Where the orientation comes from.
        depth (bool):
            True if a depth is used (from the drone's
            depth sensor).
        velocity (bool):
            True if a velocity over the ground is used (a
            DVL with bottom lock).
    """

    orientation: 'SlamOrientationSource' = proto.Field(
        proto.ENUM,
        number=1,
        enum='SlamOrientationSource',
    )
    depth: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    velocity: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class SlamGeoreference(proto.Message):
    r"""Where a SLAM map lies on the Earth, as position fixes placed it: a
    point of the map, where it lies, and the bearing of the map's x
    axis.

    The fixes do not bend the map: it moves and turns as a whole. A
    point (x, y) of the map lies R(bearing) (x - anchor_x, y - anchor_y)
    north and east of anchor_position, where R turns north towards east
    (clockwise seen from above): with bearing 0, x is north and y east.
    The bearing is known only once fixes from places far enough apart
    pin it (bearing_known). Until then it is the map's own, as the
    drone's heading gave it at the map's first scan, which near steel
    can be far off; anchor_position holds whatever the bearing.

    Attributes:
        source (blueye.protocol.types.SlamGeoreferenceSource):
            What placed the map.
        anchor_x (float):
            x of the map point the fixes place (m, in the
            map frame): where they were taken, weighted.
        anchor_y (float):
            y of the map point the fixes place (m, in the
            map frame).
        anchor_position (blueye.protocol.types.LatLongPosition):
            Where the anchor lies (WGS84).
        anchor_stddev (float):
            Standard deviation of the anchor's position
            (m), along its least sure direction.
        bearing (float):
            Bearing of the map's x axis from true north
            (°, clockwise, 0 to 360).
        bearing_stddev (float):
            Standard deviation of the bearing as the fixes give it (°).
            While bearing_known is false, it is how unsure the fixes so
            far leave the bearing, up to 180° (fixes from one place say
            nothing of it); it is not the uncertainty of bearing, which
            is then the map's own (from the drone's heading), and a
            client does not draw it as one.
        bearing_known (bool):
            True if fixes pin the bearing; false: the
            map's own (the drone's heading at its start).
        origin_position (blueye.protocol.types.LatLongPosition):
            Where the map's origin lies, at that bearing.
        origin_stddev (float):
            Standard deviation of the origin's position
            (m). With the bearing unknown, the anchor's plus
            the origin's distance from it: any bearing may
            hold.
        places (int):
            Places the fixes were taken at (surfacings,
            each counted as one position).
        fixes (int):
            Fixes used.
        last_fix_time (google.protobuf.timestamp_pb2.Timestamp):
            Host time of the newest fix used.
    """

    source: 'SlamGeoreferenceSource' = proto.Field(
        proto.ENUM,
        number=1,
        enum='SlamGeoreferenceSource',
    )
    anchor_x: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    anchor_y: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    anchor_position: message_formats.LatLongPosition = proto.Field(
        proto.MESSAGE,
        number=4,
        message=message_formats.LatLongPosition,
    )
    anchor_stddev: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    bearing: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    bearing_stddev: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    bearing_known: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    origin_position: message_formats.LatLongPosition = proto.Field(
        proto.MESSAGE,
        number=9,
        message=message_formats.LatLongPosition,
    )
    origin_stddev: float = proto.Field(
        proto.FLOAT,
        number=10,
    )
    places: int = proto.Field(
        proto.UINT32,
        number=11,
    )
    fixes: int = proto.Field(
        proto.UINT32,
        number=12,
    )
    last_fix_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )


class SlamMapFrame(proto.Message):
    r"""How a SLAM map's frame lies in the world, for placing the map on a
    chart.

    The frame is right-handed: x along the heading reference, y to its
    right, z down (north-east-down with
    SLAM_HEADING_REFERENCE_DRONE_COMPASS). The origin is the platform's
    position at the map's first scan. The map's heading may drift from
    its reference over a dive: placing a map on a chart fits it to the
    drone's positions (PositionEstimateTel in the dive log), or takes
    georeference where position fixes have placed it.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gravity_aligned (bool):
            True if z is down and x and y level; false:
            the first scan's platform frame.
        heading_reference (blueye.protocol.types.SlamHeadingReference):
            What x points along.
        magnetic_declination (float):
            The magnetic declination the drone applied to its compass
            heading at the map's first scan (°, as
            MagneticDeclination.declination; 0 when it applied none),
            with SLAM_HEADING_REFERENCE_DRONE_COMPASS: x then points the
            place's declination less this east of true north (0 when the
            drone applied the place's). Unset when not known.

            This field is a member of `oneof`_ ``_magnetic_declination``.
        origin_depth (float):
            Depth of the origin below the surface (m), for a
            gravity-aligned map: a point at z in the map is at depth
            origin_depth + z. Unset without a depth.

            This field is a member of `oneof`_ ``_origin_depth``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Host time of the map's first scan (its first
            keyframe's).
        platform (blueye.protocol.types.SlamPlatform):
            What the map's poses are the poses of.
        georeference (blueye.protocol.types.SlamGeoreference):
            Where the map lies on the Earth, once
            position fixes have placed it; unset without.
    """

    gravity_aligned: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    heading_reference: 'SlamHeadingReference' = proto.Field(
        proto.ENUM,
        number=2,
        enum='SlamHeadingReference',
    )
    magnetic_declination: float = proto.Field(
        proto.FLOAT,
        number=3,
        optional=True,
    )
    origin_depth: float = proto.Field(
        proto.FLOAT,
        number=4,
        optional=True,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    platform: 'SlamPlatform' = proto.Field(
        proto.ENUM,
        number=6,
        enum='SlamPlatform',
    )
    georeference: 'SlamGeoreference' = proto.Field(
        proto.MESSAGE,
        number=7,
        message='SlamGeoreference',
    )


class SlamMap(proto.Message):
    r"""The whole SLAM map, or a part of it.

    A large map comes in parts (part_count of them, in order), each a
    message of its own. Every part has the map's map_id, sequence and
    part_count, and its own part: a client groups parts by them, and
    drops a set whose parts disagree (one of another map or sequence, or
    missing). Every other field that is not repeated is set in the first
    part (part 0). A client has the map once it has every part, and puts
    them together field by field: every repeated field is the parts'
    concatenated in part order, and every other field is the first
    part's, whatever a later part has (proto3 does not tell a field set
    to its default from an unset one, so a client could not tell which
    part sets it). Which part carries which repeated values is up to the
    SLAM, but a submap is never split: each comes whole, in one part,
    with all its points or its raster.

    Attributes:
        map_id (int):
            Identifier of the map (0 when the SLAM has no
            map); a new one each time the map starts, unique
            while the SLAM runs.
        sequence (int):
            Sequence number of the last update the map
            includes (0 for none).
        keyframes (MutableSequence[blueye.protocol.types.SlamKeyframe]):
            Every keyframe, in id order.
        submaps (MutableSequence[blueye.protocol.types.SlamSubmap]):
            Submaps, with all they hold.
        frame (blueye.protocol.types.SlamMapFrame):
            How the map's frame lies in the world (unset
            before the first scan).
        loop_closures (MutableSequence[blueye.protocol.types.SlamLoopClosure]):
            Every loop closure, in the order they were
            made.
        part (int):
            Index of this part, from 0.
        part_count (int):
            Parts the map comes in (0 or 1: this message
            is the whole map).
    """

    map_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    sequence: int = proto.Field(
        proto.UINT64,
        number=2,
    )
    keyframes: MutableSequence['SlamKeyframe'] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='SlamKeyframe',
    )
    submaps: MutableSequence['SlamSubmap'] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message='SlamSubmap',
    )
    frame: 'SlamMapFrame' = proto.Field(
        proto.MESSAGE,
        number=5,
        message='SlamMapFrame',
    )
    loop_closures: MutableSequence['SlamLoopClosure'] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message='SlamLoopClosure',
    )
    part: int = proto.Field(
        proto.UINT32,
        number=7,
    )
    part_count: int = proto.Field(
        proto.UINT32,
        number=8,
    )


class SlamScan(proto.Message):
    r"""The latest scan of a sensor, as the SLAM placed it.

    Attributes:
        map_id (int):
            Identifier of the map.
        pose (blueye.protocol.types.SlamPose):
            Pose of the platform at the scan.
        points (blueye.protocol.types.PointCloud):
            Points of the scan in the sensor frame: in
            the map at pose times mount.
        sensor (blueye.protocol.types.SlamSensor):
            Sensor the scan comes from.
        mount (blueye.protocol.types.SlamPose):
            The sensor's pose on the platform at the
            scan. Unset when the platform is the sensor.
        time (google.protobuf.timestamp_pb2.Timestamp):
            Host time the scan was received (as
            SlamPoseEstimate.time).
    """

    map_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    pose: 'SlamPose' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='SlamPose',
    )
    points: message_formats.PointCloud = proto.Field(
        proto.MESSAGE,
        number=3,
        message=message_formats.PointCloud,
    )
    sensor: 'SlamSensor' = proto.Field(
        proto.MESSAGE,
        number=4,
        message='SlamSensor',
    )
    mount: 'SlamPose' = proto.Field(
        proto.MESSAGE,
        number=5,
        message='SlamPose',
    )
    time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class SlamMapSummary(proto.Message):
    r"""A saved map, in brief: the first record of a map file (\_map.sbez:
    this, then the map as SlamMapTel parts, its rasters deflated, which
    a client's file may follow with SlamMapUpdateTel), so that a client
    lists maps and shows them small without reading them whole. A SLAM
    that can localize in a base map writes one beside each of its
    recordings; a client makes one of a recording it has (a file on the
    pilot's device) and puts it in the drone's media folder, where the
    SLAM loads it as its own. A map file is written under a name ending
    in .part.sbez and renamed once whole: a reader skips such names.

    Attributes:
        recording (str):
            File name of the recording the map ends
            (.sbez), without its folder.
        map_id (int):
            The map's id in that recording.
        frame (blueye.protocol.types.SlamMapFrame):
            How the map's frame lies in the world; start_time is its
            first scan's.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Host time of the map's last scan (in a
            client's file, its last record).
        sensor_type (blueye.protocol.types.SlamSensorType):
            Kind of sensor that made the map.
        keyframe_count (int):
            Keyframes in the map.
        min_x (float):
            What the map's content covers in its frame
            (m), along x and along y.
        max_x (float):

        min_y (float):

        max_y (float):

        log_name (str):
            The dive log the recording belongs with
            (DroneInfo.log_name), when known.
        preview (blueye.protocol.types.SlamRaster):
            The map's mosaic, coarse (at most 256 pixels
            a side), its origin in the map's frame: for a
            list to show. Unset when the client that made
            the file did not draw one. A client's file
            (uploaded) may break the bound, so a reader
            checks it and treats a larger preview as absent.
        uploaded (bool):
            Made by a client from a recording it had, not
            by the SLAM beside its own.
        start_position (blueye.protocol.types.LatLongPosition):
            Where the drone was at the map's first scan, as its own
            position estimate had it (PositionEstimate.global_position),
            or else where it was when the estimate was first valid after
            that: a rough place of the map on the Earth, for a list to
            tell the maps nearby. Unset when the estimate was not valid
            while the map was made.
    """

    recording: str = proto.Field(
        proto.STRING,
        number=1,
    )
    map_id: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    frame: 'SlamMapFrame' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='SlamMapFrame',
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    sensor_type: 'SlamSensorType' = proto.Field(
        proto.ENUM,
        number=5,
        enum='SlamSensorType',
    )
    keyframe_count: int = proto.Field(
        proto.UINT32,
        number=6,
    )
    min_x: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    max_x: float = proto.Field(
        proto.FLOAT,
        number=8,
    )
    min_y: float = proto.Field(
        proto.FLOAT,
        number=9,
    )
    max_y: float = proto.Field(
        proto.FLOAT,
        number=10,
    )
    log_name: str = proto.Field(
        proto.STRING,
        number=11,
    )
    preview: 'SlamRaster' = proto.Field(
        proto.MESSAGE,
        number=12,
        message='SlamRaster',
    )
    uploaded: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    start_position: message_formats.LatLongPosition = proto.Field(
        proto.MESSAGE,
        number=14,
        message=message_formats.LatLongPosition,
    )


class SlamBaseMapState(proto.Message):
    r"""The SLAM's base map, and where finding its map in it stands
    (SlamStatusTel.base_map, SetSlamBaseMapRep). Set only by a SLAM that
    can localize in a base map: unset, a client offers none.

    Attributes:
        revision (int):
            One more at each change, but for what a search updates as it
            goes (progress, score, margin, overlap, base_map_pose,
            last_match_time): of this and of a reply, the one with the
            higher revision is the newer, and of two with the same, the
            later. It starts at the SLAM's start time (in milliseconds),
            so a SLAM started again is newer still.
        actions (MutableSequence[blueye.protocol.types.SlamBaseMapAction]):
            What this SLAM takes; a client offers no
            other.
        stage (blueye.protocol.types.SlamBaseMapStage):
            Where it stands.
        name (str):
            The base map's file (.sbez) in the drone's
            media folder, without the folder.
        storage_location (blueye.protocol.types.StorageLocation):
            Where the file is.
        load_id (int):
            The load, a new one each time a base map is loaded (0: none
            yet). A Clear keeps it: a Clear naming it again is taken,
            and a Hint after it is refused with
            SLAM_REQUEST_ERROR_NO_BASE_MAP, whatever load it names.
        base_map_id (int):
            Which map the file holds (SlamMapSummary):
            its id in its recording, and its first scan's
            time. A client draws the file it read only when
            they agree.
        base_map_start_time (google.protobuf.timestamp_pb2.Timestamp):

        progress (float):
            SWEEPING: how much of the sweep a search
            needs is there, from 0 to 1.
        miss (blueye.protocol.types.SlamBaseMapMiss):
            SEARCHING: why the last search took no place.
        map_id (int):
            The SLAM map base_map_pose is in (SlamPoseEstimate.map_id).
        base_map_pose (blueye.protocol.types.SlamPose):
            FOUND: the base map's frame in that map's frame, as the
            SLAM's back end has it: a point p of the base map is at
            base_map_pose times p in the map.
        fix_id (int):
            The place found (FOUND), or passed
            (CANDIDATE): a new one each, for
            SlamBaseMapReject. An id is never repeated while
            the SLAM runs, whatever base maps it loads.
        matches (int):
            FOUND: the matches that keep it.
        last_match_time (google.protobuf.timestamp_pb2.Timestamp):
            FOUND: host time of the scan the last match
            was made at.
        score (float):
            The last search's best place: its score (from
            0, nothing alike, to 1), how far it stands above
            the next place's (margin), and the share of the
            sweep that lies on the base map there (overlap).
            A place is taken only with the margin and the
            overlap the SLAM requires.
        margin (float):

        overlap (float):

        hinted (bool):
            The searches look where a hint says
            (SlamBaseMapHint).
        error (blueye.protocol.types.SlamRequestError):
            FAILED: why.
    """

    revision: int = proto.Field(
        proto.UINT64,
        number=1,
    )
    actions: MutableSequence['SlamBaseMapAction'] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum='SlamBaseMapAction',
    )
    stage: 'SlamBaseMapStage' = proto.Field(
        proto.ENUM,
        number=3,
        enum='SlamBaseMapStage',
    )
    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    storage_location: message_formats.StorageLocation = proto.Field(
        proto.ENUM,
        number=5,
        enum=message_formats.StorageLocation,
    )
    load_id: int = proto.Field(
        proto.UINT32,
        number=6,
    )
    base_map_id: int = proto.Field(
        proto.UINT32,
        number=7,
    )
    base_map_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    progress: float = proto.Field(
        proto.FLOAT,
        number=9,
    )
    miss: 'SlamBaseMapMiss' = proto.Field(
        proto.ENUM,
        number=10,
        enum='SlamBaseMapMiss',
    )
    map_id: int = proto.Field(
        proto.UINT32,
        number=11,
    )
    base_map_pose: 'SlamPose' = proto.Field(
        proto.MESSAGE,
        number=12,
        message='SlamPose',
    )
    fix_id: int = proto.Field(
        proto.UINT32,
        number=13,
    )
    matches: int = proto.Field(
        proto.UINT32,
        number=14,
    )
    last_match_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    score: float = proto.Field(
        proto.FLOAT,
        number=16,
    )
    margin: float = proto.Field(
        proto.FLOAT,
        number=17,
    )
    overlap: float = proto.Field(
        proto.FLOAT,
        number=18,
    )
    hinted: bool = proto.Field(
        proto.BOOL,
        number=19,
    )
    error: 'SlamRequestError' = proto.Field(
        proto.ENUM,
        number=20,
        enum='SlamRequestError',
    )


class SlamBaseMapLoad(proto.Message):
    r"""Load a base map (SetSlamBaseMapReq): a file in the drone's
    media folder, in place of any loaded before. The reply comes at
    once; the status follows the load (LOADING, then SWEEPING or
    FAILED). A map of this dive is searched in a window around its
    heading (both maps are north up, by a compass that drifts a few
    degrees between them); one of another dive at every heading.

    Attributes:
        name (str):
            The file (.sbez), without a folder: a recording, or its map
            file (\_map.sbez).
        storage_location (blueye.protocol.types.StorageLocation):
            Where it is.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    storage_location: message_formats.StorageLocation = proto.Field(
        proto.ENUM,
        number=2,
        enum=message_formats.StorageLocation,
    )


class SlamBaseMapClear(proto.Message):
    r"""Take the base map away (SetSlamBaseMapReq): the map goes back
    to where its own scans put it.

    Attributes:
        load_id (int):
            The load to clear. It must be the current one
            (SlamBaseMapState.load_id), else the request is refused with
            SLAM_REQUEST_ERROR_OTHER_BASE_MAP. 0 is the current one only
            before any base map was loaded: once one was, a clear with 0
            is refused.
    """

    load_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )


class SlamBaseMapReject(proto.Message):
    r"""The place found (or passed) is wrong (SetSlamBaseMapReq): it
    is dropped, the map goes back to where its own scans put it, and
    the search goes on without that place or one near it.

    Attributes:
        fix_id (int):
            The place (SlamBaseMapState.fix_id): only if it is still the
            current one. A fix id is never repeated while the SLAM runs,
            so a late reject drops no place found since, in this load or
            another.
    """

    fix_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )


class SlamBaseMapHint(proto.Message):
    r"""Where the drone is in the base map, roughly (SetSlamBaseMapReq):
    until found, a place is taken only within radius of it, and only
    while no place outside scores better by the margin a place needs
    (else the hint is dropped: SLAM_BASE_MAP_MISS_OUTSIDE_HINT). Radius
    0 drops the hint.

    Attributes:
        load_id (int):
            The load it is for. It must be the current one
            (SlamBaseMapState.load_id), else the request is refused with
            SLAM_REQUEST_ERROR_OTHER_BASE_MAP; once a base map was
            loaded, a hint with 0 is refused. A hint also needs a base
            map loaded, else SLAM_REQUEST_ERROR_NO_BASE_MAP.
        position (blueye.protocol.types.Vector3):
            The drone's position in the base map's frame
            (m; z is not used).
        radius (float):
            How far from position it may be (m).
    """

    load_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    position: message_formats.Vector3 = proto.Field(
        proto.MESSAGE,
        number=2,
        message=message_formats.Vector3,
    )
    radius: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
