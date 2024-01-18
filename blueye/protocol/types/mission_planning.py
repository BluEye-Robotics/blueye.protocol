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
        'DepthZeroReference',
        'ControlModeVertical',
        'ControlModeHorizontal',
        'CameraAction',
        'InstructionType',
        'MissionState',
        'Mission',
        'Instruction',
        'DepthSetPoint',
        'Waypoint',
        'ControlModeCommand',
        'WaypointCommand',
        'DepthSetPointCommand',
        'TiltMainCameraCommand',
        'TiltMultibeamCommand',
        'WaitForCommand',
        'CameraCommand',
        'GoToSurfaceCommand',
        'GoToSeabedCommand',
        'GoToHomeCommand',
        'PathSegment',
        'ReferenceAutoPilot',
        'MissionStatus',
    },
)


class DepthZeroReference(proto.Enum):
    r"""Depth zero reference from surface for depth, and seabed for
    altitude.
    """
    DEPTH_ZERO_REFERENCE_UNSPECIFIED = 0
    DEPTH_ZERO_REFERENCE_SURFACE = 1
    DEPTH_ZERO_REFERENCE_SEABED = 2


class ControlModeVertical(proto.Enum):
    r""""""
    CONTROL_MODE_VERTICAL_UNSPECIFIED = 0
    CONTROL_MODE_VERTICAL_MANUAL = 1
    CONTROL_MODE_VERTICAL_AUTO_DEPTH = 2
    CONTROL_MODE_VERTICAL_AUTO_ALTITUDE = 3


class ControlModeHorizontal(proto.Enum):
    r""""""
    CONTROL_MODE_HORIZONTAL_UNSPECIFIED = 0
    CONTROL_MODE_HORIZONTAL_MANUAL = 1
    CONTROL_MODE_HORIZONTAL_AUTO_HEADING = 2
    CONTROL_MODE_HORIZONTAL_STATION_KEEPING = 3


class CameraAction(proto.Enum):
    r"""List of available camera actions."""
    CAMERA_ACTION_UNSPECIFIED = 0
    CAMERA_ACTION_TAKE_PHOTO = 1
    CAMERA_ACTION_TAKE_PHOTOS_TIME = 2
    CAMERA_ACTION_TAKE_PHOTOS_DISTANCE = 3
    CAMERA_ACTION_STOP_TAKING_PHOTOS = 4
    CAMERA_ACTION_START_RECORDING = 5
    CAMERA_ACTION_STOP_RECORDING = 6


class InstructionType(proto.Enum):
    r"""List of available instruction types."""
    INSTRUCTION_TYPE_UNSPECIFIED = 0
    INSTRUCTION_TYPE_NONE = 1
    INSTRUCTION_TYPE_GO_TO_WAYPOINT = 2
    INSTRUCTION_TYPE_GO_TO_WAYPOINT_WITH_DEPTH_SET_POINT = 3
    INSTRUCTION_TYPE_GO_TO_DEPTH_SET_POINT = 4
    INSTRUCTION_TYPE_SET_CAMERA_ACTION = 5
    INSTRUCTION_TYPE_SET_CONTROL_MODE = 6
    INSTRUCTION_TYPE_SET_TILT_MAIN_CAMERA = 7
    INSTRUCTION_TYPE_SET_TILT_SERVO = 8
    INSTRUCTION_TYPE_WAIT_FOR_SEC = 9
    INSTRUCTION_TYPE_GO_TO_SURFACE = 10
    INSTRUCTION_TYPE_GO_TO_SEABED = 11
    INSTRUCTION_TYPE_GO_TO_HOME = 12


class MissionState(proto.Enum):
    r"""List of mission supervisor states."""
    MISSION_STATE_UNSPECIFIED = 0
    MISSION_STATE_INACTIVE = 1
    MISSION_STATE_READY = 2
    MISSION_STATE_RUNNING = 3
    MISSION_STATE_PAUSED = 4
    MISSION_STATE_COMPLETED = 5
    MISSION_STATE_ABORTED = 6
    MISSION_STATE_FAILED_TO_LOAD_MISSION = 7
    MISSION_STATE_FAILED_TO_START_MISSION = 8


class Mission(proto.Message):
    r"""A list of waypoints describes a mission that the auto pilot
    can execute.

    Attributes:
        id (int):
            Mission id
        name (str):
            Mission name provided from the app
        instructions (Sequence[blueye.protocol.types.Instruction]):
            List of instructions in the mission
        path_segments (Sequence[blueye.protocol.types.PathSegment]):
            Calculated path segments from the reference
            generator (optinal)
        total_distance (int):
            Total distance of the mission (m) (optinal)
        total_duration_time (int):
            Total duration time of the mission (s)
            (optinal)
        default_surge_speed (float):
            Default cruise speed of the mission (m/s)
            (optinal)
        default_heave_speed (float):
            Default heave speed of the mission (m/s)
            (optinal)
        default_circle_of_acceptance (float):
            Default circle of acceptance for waypoints
            (m) (optinal)
    """

    id = proto.Field(proto.UINT32, number=1)

    name = proto.Field(proto.STRING, number=2)

    instructions = proto.RepeatedField(proto.MESSAGE, number=3,
        message='Instruction',
    )

    path_segments = proto.RepeatedField(proto.MESSAGE, number=4,
        message='PathSegment',
    )

    total_distance = proto.Field(proto.UINT32, number=5)

    total_duration_time = proto.Field(proto.UINT32, number=6)

    default_surge_speed = proto.Field(proto.FLOAT, number=7)

    default_heave_speed = proto.Field(proto.FLOAT, number=8)

    default_circle_of_acceptance = proto.Field(proto.FLOAT, number=9)


class Instruction(proto.Message):
    r"""A mission consitst of one or multiple instructions. One
    instruction can be of different types.

    Attributes:
        id (int):

        group_id (int):
            Group id used for polygoons
        auto_continue (bool):
            False will pause the mission after this
            instruction
        waypoint_command (blueye.protocol.types.WaypointCommand):
            Go to waypoint
        depth_set_point_command (blueye.protocol.types.DepthSetPointCommand):
            Go to depth
        camera_command (blueye.protocol.types.CameraCommand):
            Camera commands
        control_mode_command (blueye.protocol.types.ControlModeCommand):
            Set control modes
        tilt_main_camera_command (blueye.protocol.types.TiltMainCameraCommand):
            Set camera to angle x
        tilt_multibeam_command (blueye.protocol.types.TiltMultibeamCommand):
            Set multibeam tilt angle
        wait_for_command (blueye.protocol.types.WaitForCommand):
            Wait for x seconds
        go_to_surface_command (blueye.protocol.types.GoToSurfaceCommand):
            Go to surface
        go_to_seabed_command (blueye.protocol.types.GoToSeabedCommand):
            Go to seabed
        go_to_home_command (blueye.protocol.types.GoToHomeCommand):
            Go to home position
    """

    id = proto.Field(proto.UINT32, number=1)

    group_id = proto.Field(proto.UINT32, number=2)

    auto_continue = proto.Field(proto.BOOL, number=3)

    waypoint_command = proto.Field(proto.MESSAGE, number=4, oneof='command',
        message='WaypointCommand',
    )

    depth_set_point_command = proto.Field(proto.MESSAGE, number=5, oneof='command',
        message='DepthSetPointCommand',
    )

    camera_command = proto.Field(proto.MESSAGE, number=6, oneof='command',
        message='CameraCommand',
    )

    control_mode_command = proto.Field(proto.MESSAGE, number=7, oneof='command',
        message='ControlModeCommand',
    )

    tilt_main_camera_command = proto.Field(proto.MESSAGE, number=8, oneof='command',
        message='TiltMainCameraCommand',
    )

    tilt_multibeam_command = proto.Field(proto.MESSAGE, number=9, oneof='command',
        message='TiltMultibeamCommand',
    )

    wait_for_command = proto.Field(proto.MESSAGE, number=10, oneof='command',
        message='WaitForCommand',
    )

    go_to_surface_command = proto.Field(proto.MESSAGE, number=11, oneof='command',
        message='GoToSurfaceCommand',
    )

    go_to_seabed_command = proto.Field(proto.MESSAGE, number=12, oneof='command',
        message='GoToSeabedCommand',
    )

    go_to_home_command = proto.Field(proto.MESSAGE, number=13, oneof='command',
        message='GoToHomeCommand',
    )


class DepthSetPoint(proto.Message):
    r"""Depth set point is used to describe a depth setpoint relative
    to the surface or the seabed.

    Attributes:
        depth (float):
            Desired depth at the wp (m)
        speed_to_depth (float):
            Desired speed to desired depth set point
            (m/s)
        depth_zero_reference (blueye.protocol.types.DepthZeroReference):
            Used to destinguish desired altitude or depth
    """

    depth = proto.Field(proto.FLOAT, number=1)

    speed_to_depth = proto.Field(proto.FLOAT, number=2)

    depth_zero_reference = proto.Field(proto.ENUM, number=3,
        enum='DepthZeroReference',
    )


class Waypoint(proto.Message):
    r"""Waypoints used to describe a path for the auto pilot.

    Attributes:
        id (int):
            Waypoint id
        name (str):
            Waypoint name provided from the app
        global_position (blueye.protocol.types.LatLongPosition):
            Position if the waypoint (decimal degrees)
        circle_of_acceptance (float):
            Radius of the accepance circle around the
            waypoint (m)
        speed_to_target (float):
            Desired speed over ground to waypoint (m/s)
        depth_set_point (blueye.protocol.types.DepthSetPoint):
            Depth set point (optional)
    """

    id = proto.Field(proto.UINT32, number=1)

    name = proto.Field(proto.STRING, number=2)

    global_position = proto.Field(proto.MESSAGE, number=3,
        message=message_formats.LatLongPosition,
    )

    circle_of_acceptance = proto.Field(proto.FLOAT, number=4)

    speed_to_target = proto.Field(proto.FLOAT, number=5)

    depth_set_point = proto.Field(proto.MESSAGE, number=6,
        message='DepthSetPoint',
    )


class ControlModeCommand(proto.Message):
    r"""A ControlModeCommand is used to set vertical and horizontal
    control mode during a mission.

    Attributes:
        control_mode_vertical (blueye.protocol.types.ControlModeVertical):
            Desired control mode in heave
        control_mode_horizontal (blueye.protocol.types.ControlModeHorizontal):
            Desired control mode in surge and yaw
    """

    control_mode_vertical = proto.Field(proto.ENUM, number=5,
        enum='ControlModeVertical',
    )

    control_mode_horizontal = proto.Field(proto.ENUM, number=6,
        enum='ControlModeHorizontal',
    )


class WaypointCommand(proto.Message):
    r"""A WaypointCommand will request the drone to drive to a point
    automatically.

    Attributes:
        waypoint (blueye.protocol.types.Waypoint):
            Waypoint to go to
    """

    waypoint = proto.Field(proto.MESSAGE, number=1,
        message='Waypoint',
    )


class DepthSetPointCommand(proto.Message):
    r"""A DepthSetPointCommand is used to go to a desired depth or
    altitude.

    Attributes:
        depth_set_point (blueye.protocol.types.DepthSetPoint):
            Depth set point to go to
    """

    depth_set_point = proto.Field(proto.MESSAGE, number=1,
        message='DepthSetPoint',
    )


class TiltMainCameraCommand(proto.Message):
    r"""The TiltMainCameraCommand can set the desired camera tilt
    angle.

    Attributes:
        tilt_angle (blueye.protocol.types.TiltAngle):
            Tilt angle of the camera (-30..30)
    """

    tilt_angle = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.TiltAngle,
    )


class TiltMultibeamCommand(proto.Message):
    r"""The TiltMultibeamCommand is used to set the tilt angle of the
    servo.

    Attributes:
        multibeam_servo (blueye.protocol.types.MultibeamServo):
            Tilt angle for the multibeam servo
    """

    multibeam_servo = proto.Field(proto.MESSAGE, number=1,
        message=message_formats.MultibeamServo,
    )


class WaitForCommand(proto.Message):
    r"""WaitForCommand is used to wait duringing a mission.

    Attributes:
        wait_for_seconds (float):
            Wait for x seconds
    """

    wait_for_seconds = proto.Field(proto.FLOAT, number=1)


class CameraCommand(proto.Message):
    r"""CameraCommands are used to control the camera from a mission.

    Attributes:
        camera_action (blueye.protocol.types.CameraAction):
            Camera command
        action_param (float):
            Used for taking photos based on a time or
            distance interval
    """

    camera_action = proto.Field(proto.ENUM, number=1,
        enum='CameraAction',
    )

    action_param = proto.Field(proto.FLOAT, number=2)


class GoToSurfaceCommand(proto.Message):
    r"""GoToSurfaceCommand is used to go to the surface.

    Attributes:
        desired_speed (float):
            Desired speed to surface (m/s)
    """

    desired_speed = proto.Field(proto.FLOAT, number=1)


class GoToSeabedCommand(proto.Message):
    r"""GoToSeabedCommand is used to go to the seabed.

    Attributes:
        desired_speed (float):
            Desired speed to seabed (m/s)
    """

    desired_speed = proto.Field(proto.FLOAT, number=1)


class GoToHomeCommand(proto.Message):
    r"""GoToHomeCommand is used to go to the home position.

    Attributes:
        desired_speed (float):
            Desired speed to home (m/s)
    """

    desired_speed = proto.Field(proto.FLOAT, number=1)


class PathSegment(proto.Message):
    r"""Path segment used to describe segments of a mission as a line
    between to waypoints.

    Attributes:
        id (int):
            Path segment id starting at 0, -1 for
            inactive
        speed_to_target (float):
            Desired speed over ground in (m/s)
        course_to_target (float):
            Course to target relative to north (rad) [-pi, pi]
        depth_speed (float):
            Desired speed in heave (m/s)
        horizontal_length (float):
            Horizontal length of the path segment (m)
        vertical_length (float):
            Vertical legth of the path segment (m)
        from_wp_id (int):
            Id of the starting waypoint
        to_wp_id (int):
            Id of the ending waypoint
        duration_time (float):
            Estmated time it takes to complete given
            legth and desired speed (s)
    """

    id = proto.Field(proto.UINT32, number=1)

    speed_to_target = proto.Field(proto.FLOAT, number=2)

    course_to_target = proto.Field(proto.FLOAT, number=3)

    depth_speed = proto.Field(proto.FLOAT, number=4)

    horizontal_length = proto.Field(proto.FLOAT, number=5)

    vertical_length = proto.Field(proto.FLOAT, number=6)

    from_wp_id = proto.Field(proto.UINT32, number=7)

    to_wp_id = proto.Field(proto.UINT32, number=8)

    duration_time = proto.Field(proto.FLOAT, number=9)


class ReferenceAutoPilot(proto.Message):
    r"""Reference for the auto pilot when a mission is active.

    Attributes:
        instruction_type (blueye.protocol.types.InstructionType):
            Instruction type
        active_instruction_id (int):
            Id of the active instruction
        active_path_segment_id (int):
            Id of the active path segment
        course_to_target (float):
            Course to the next waypoint from north (rad) [-pi, pi]
        speed_over_ground (float):
            Desired speed over ground (m/s)
        horizontal_distance_to_target (float):
            Horizontal distance to the next waypoint (m)
        circle_of_acceptance (float):
            Circle of acceptance to mark waypoint as
            visited (m)
        depth_set_point (float):
            Desired depth set point (m)
        heave_velocity (float):
            Desired heave velocity (m/s)
        vertical_distance_to_target (float):
            Vertical distance to the next waypoint (m)
        depth_zero_reference (blueye.protocol.types.DepthZeroReference):
            Indicates if depth is measured from the
            surface or seabed
        time_to_complete (float):
            Estimated time to complete the instruction
            (s)
    """

    instruction_type = proto.Field(proto.ENUM, number=1,
        enum='InstructionType',
    )

    active_instruction_id = proto.Field(proto.UINT32, number=2)

    active_path_segment_id = proto.Field(proto.UINT32, number=3)

    course_to_target = proto.Field(proto.FLOAT, number=4)

    speed_over_ground = proto.Field(proto.FLOAT, number=5)

    horizontal_distance_to_target = proto.Field(proto.FLOAT, number=6)

    circle_of_acceptance = proto.Field(proto.FLOAT, number=7)

    depth_set_point = proto.Field(proto.FLOAT, number=8)

    heave_velocity = proto.Field(proto.FLOAT, number=9)

    vertical_distance_to_target = proto.Field(proto.FLOAT, number=10)

    depth_zero_reference = proto.Field(proto.ENUM, number=11,
        enum='DepthZeroReference',
    )

    time_to_complete = proto.Field(proto.FLOAT, number=12)


class MissionStatus(proto.Message):
    r"""Mission Status is used for showing the status of the mission.

    Attributes:
        state (blueye.protocol.types.MissionState):
            State of the mission supervisor
        time_elapsed (int):
            Time elapsed since mission started (s)
        estimated_time_to_complete (int):
            Estimated time to complete the mission (s)
        distance_to_complete (int):
            Distance left of the mission (m)
        completed_instruction_ids (Sequence[int]):
            Ids of the completed instructions
        total_number_of_instructions (int):
            Total number of instructions in the mission
        completed_path_segment_ids (Sequence[int]):
            Ids of the completed path segments
        total_number_of_path_segments (int):
            Total number of path segments in the mission
    """

    state = proto.Field(proto.ENUM, number=1,
        enum='MissionState',
    )

    time_elapsed = proto.Field(proto.UINT32, number=2)

    estimated_time_to_complete = proto.Field(proto.UINT32, number=3)

    distance_to_complete = proto.Field(proto.UINT32, number=4)

    completed_instruction_ids = proto.RepeatedField(proto.UINT32, number=5)

    total_number_of_instructions = proto.Field(proto.UINT32, number=6)

    completed_path_segment_ids = proto.RepeatedField(proto.UINT32, number=7)

    total_number_of_path_segments = proto.Field(proto.UINT32, number=8)


__all__ = tuple(sorted(__protobuf__.manifest))
