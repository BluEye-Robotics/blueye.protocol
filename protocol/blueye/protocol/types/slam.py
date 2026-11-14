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
        'SlamRequestError',
        'SlamOrientationSource',
        'SlamHeadingReference',
        'SlamSensor',
        'SlamRecordingState',
        'SlamSonar3dSettings',
        'SlamSensorSettings',
        'SlamSensorStatus',
        'SlamPose',
        'SlamPoseEstimate',
        'SlamKeyframe',
        'SlamSubmap',
        'SlamKeyframePoses',
        'SlamLoopClosure',
        'SlamMapUpdate',
        'SlamAiding',
        'SlamMapFrame',
        'SlamMap',
        'SlamScan',
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
    """
    SLAM_SENSOR_TYPE_UNSPECIFIED = 0
    """Unspecified."""
    SLAM_SENSOR_TYPE_SONAR_3D = 1
    """A 3D imaging sonar, e.g. the Water Linked Sonar 3D-15."""
    SLAM_SENSOR_TYPE_STEREO_CAMERA = 2
    """A stereo camera's depth."""


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


class SlamSensorSettings(proto.Message):
    r"""Settings of a sensor that feeds the SLAM.

    One message for each kind of sensor, so a client shows the
    settings of the sensors the SLAM has, and a sensor takes only
    its own.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sonar_3d (blueye.protocol.types.SlamSonar3dSettings):
            A 3D imaging sonar's settings.

            This field is a member of `oneof`_ ``settings``.
    """

    sonar_3d: 'SlamSonar3dSettings' = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='settings',
        message='SlamSonar3dSettings',
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
    the map at the platform's pose times its mount.

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
            their distance to the map's planes.
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
            Submap whose points the keyframe added to.
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


class SlamSubmap(proto.Message):
    r"""A submap: part of the map from one sensor, in the platform's
    frame at its anchor keyframe.

    A submap moves rigidly with its anchor keyframe, so a correction
    of the trajectory moves its content without sending it again. A
    submap holds one kind of content: points today; other kinds
    (e.g. a 2D sonar's mosaic) will be added to the oneof, each
    saying how a later one replaces what the submap holds.


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
            submap's (SlamSubmap.replace).
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


class SlamMapFrame(proto.Message):
    r"""How a SLAM map's frame lies in the world, for placing the map on a
    chart.

    The frame is right-handed: x along the heading reference, y to its
    right, z down (north-east-down with
    SLAM_HEADING_REFERENCE_DRONE_COMPASS). The origin is the platform's
    position at the map's first scan. The map's heading may drift from
    its reference over a dive: placing a map on a chart fits it to the
    drone's positions (PositionEstimateTel in the dive log).


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
    SLAM, but a submap is never split: each comes whole, in one part.

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


__all__ = tuple(sorted(__protobuf__.manifest))
