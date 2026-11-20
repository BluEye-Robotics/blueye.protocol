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
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='blueye.protocol',
    manifest={
        'DepthZeroReference',
        'ControlModeVertical',
        'ControlModeHorizontal',
        'TriggerKind',
        'LightTarget',
        'CameraAction',
        'InstructionType',
        'MissionState',
        'MissionResult',
        'MissionAbortReason',
        'InstructionResultState',
        'MissionRuleState',
        'Mission',
        'Instruction',
        'DepthSetPoint',
        'Waypoint',
        'ControlModeCommand',
        'DetectionTrigger',
        'DepthTrigger',
        'AltitudeTrigger',
        'LocationTrigger',
        'Trigger',
        'MissionRule',
        'MissionRuleStatus',
        'TriggerStatus',
        'InsertInstruction',
        'WaypointCommand',
        'DepthSetPointCommand',
        'TiltMainCameraCommand',
        'TiltMultibeamCommand',
        'WaitForCommand',
        'CameraCommand',
        'GoToSurfaceCommand',
        'GoToSeabedCommand',
        'GoToHomeCommand',
        'RecordMultibeamCommand',
        'ActivateMultibeamCommand',
        'MultibeamConfigCommand',
        'LightsCommand',
        'LaserCommand',
        'TiltStabilizationCommand',
        'CvModelStateCommand',
        'AnnotationCommand',
        'HeadingCommand',
        'TransectCommand',
        'RelativeDepthCommand',
        'CruiseSpeedCommand',
        'SurveyCommand',
        'PathSegment',
        'ReferenceAutoPilot',
        'MissionStatus',
        'MissionOutcome',
        'InstructionResult',
    },
)


class DepthZeroReference(proto.Enum):
    r"""Depth zero reference from surface for depth, and seabed for
    altitude.

    Attributes:
        DEPTH_ZERO_REFERENCE_UNSPECIFIED (0):
            No description available.
        DEPTH_ZERO_REFERENCE_SURFACE (1):
            No description available.
        DEPTH_ZERO_REFERENCE_SEABED (2):
            No description available.
    """
    DEPTH_ZERO_REFERENCE_UNSPECIFIED = 0
    DEPTH_ZERO_REFERENCE_SURFACE = 1
    DEPTH_ZERO_REFERENCE_SEABED = 2


class ControlModeVertical(proto.Enum):
    r"""Control mode for the vertical axis of the drone.

    Attributes:
        CONTROL_MODE_VERTICAL_UNSPECIFIED (0):
            Unspecified.
        CONTROL_MODE_VERTICAL_MANUAL (1):
            Manual control mode.
        CONTROL_MODE_VERTICAL_AUTO_DEPTH (2):
            Auto depth control mode.
        CONTROL_MODE_VERTICAL_AUTO_ALTITUDE (3):
            Auto altitude control mode.
    """
    CONTROL_MODE_VERTICAL_UNSPECIFIED = 0
    """Unspecified."""
    CONTROL_MODE_VERTICAL_MANUAL = 1
    """Manual control mode."""
    CONTROL_MODE_VERTICAL_AUTO_DEPTH = 2
    """Auto depth control mode."""
    CONTROL_MODE_VERTICAL_AUTO_ALTITUDE = 3
    """Auto altitude control mode."""


class ControlModeHorizontal(proto.Enum):
    r"""Control mode for the horizontal axis of the drone.

    Attributes:
        CONTROL_MODE_HORIZONTAL_UNSPECIFIED (0):
            Unspecified.
        CONTROL_MODE_HORIZONTAL_MANUAL (1):
            Manual control mode.
        CONTROL_MODE_HORIZONTAL_AUTO_HEADING (2):
            Auto heading control mode.
        CONTROL_MODE_HORIZONTAL_STATION_KEEPING (3):
            Station keeping control mode.
        CONTROL_MODE_HORIZONTAL_WEATHER_VANING (4):
            Weather vaning control mode (station keeping
            into the current).
    """
    CONTROL_MODE_HORIZONTAL_UNSPECIFIED = 0
    """Unspecified."""
    CONTROL_MODE_HORIZONTAL_MANUAL = 1
    """Manual control mode."""
    CONTROL_MODE_HORIZONTAL_AUTO_HEADING = 2
    """Auto heading control mode."""
    CONTROL_MODE_HORIZONTAL_STATION_KEEPING = 3
    """Station keeping control mode."""
    CONTROL_MODE_HORIZONTAL_WEATHER_VANING = 4
    """Weather vaning control mode (station keeping into the
    current)."""


class TriggerKind(proto.Enum):
    r"""Which condition a Trigger carries. The values are the field
    numbers of the Trigger oneof.

    Attributes:
        TRIGGER_KIND_UNSPECIFIED (0):
            No condition is set.
        TRIGGER_KIND_DETECTION (1):
            A DetectionTrigger.
        TRIGGER_KIND_DEPTH (2):
            A DepthTrigger.
        TRIGGER_KIND_ALTITUDE (3):
            An AltitudeTrigger.
        TRIGGER_KIND_LOCATION (4):
            A LocationTrigger.
    """
    TRIGGER_KIND_UNSPECIFIED = 0
    """No condition is set."""
    TRIGGER_KIND_DETECTION = 1
    """A DetectionTrigger."""
    TRIGGER_KIND_DEPTH = 2
    """A DepthTrigger."""
    TRIGGER_KIND_ALTITUDE = 3
    """An AltitudeTrigger."""
    TRIGGER_KIND_LOCATION = 4
    """A LocationTrigger."""


class LightTarget(proto.Enum):
    r"""Which lights a LightsCommand applies to.

    Attributes:
        LIGHT_TARGET_UNSPECIFIED (0):
            Unspecified, treated as the main lights.
        LIGHT_TARGET_MAIN (1):
            The drone's own lights.
        LIGHT_TARGET_GUESTPORT (2):
            Lights connected to a guest port.
    """
    LIGHT_TARGET_UNSPECIFIED = 0
    """Unspecified, treated as the main lights."""
    LIGHT_TARGET_MAIN = 1
    """The drone's own lights."""
    LIGHT_TARGET_GUESTPORT = 2
    """Lights connected to a guest port."""


class CameraAction(proto.Enum):
    r"""List of available camera actions.

    Attributes:
        CAMERA_ACTION_UNSPECIFIED (0):
            Unspecified command.
        CAMERA_ACTION_TAKE_PHOTO (1):
            Take one photo.
        CAMERA_ACTION_TAKE_PHOTOS_TIME (2):
            Take a photo every x second.
        CAMERA_ACTION_TAKE_PHOTOS_DISTANCE (3):
            Take a photo every x meter.
        CAMERA_ACTION_STOP_TAKING_PHOTOS (4):
            Stop taking photos.
        CAMERA_ACTION_START_RECORDING (5):
            Start recording.
        CAMERA_ACTION_STOP_RECORDING (6):
            Stop recording.
    """
    CAMERA_ACTION_UNSPECIFIED = 0
    """Unspecified command."""
    CAMERA_ACTION_TAKE_PHOTO = 1
    """Take one photo."""
    CAMERA_ACTION_TAKE_PHOTOS_TIME = 2
    """Take a photo every x second."""
    CAMERA_ACTION_TAKE_PHOTOS_DISTANCE = 3
    """Take a photo every x meter."""
    CAMERA_ACTION_STOP_TAKING_PHOTOS = 4
    """Stop taking photos."""
    CAMERA_ACTION_START_RECORDING = 5
    """Start recording."""
    CAMERA_ACTION_STOP_RECORDING = 6
    """Stop recording."""


class InstructionType(proto.Enum):
    r"""List of available instruction types.

    Attributes:
        INSTRUCTION_TYPE_UNSPECIFIED (0):
            Unspecified.
        INSTRUCTION_TYPE_NONE (1):
            None.
        INSTRUCTION_TYPE_GO_TO_WAYPOINT (2):
            Go to waypoint.
        INSTRUCTION_TYPE_GO_TO_WAYPOINT_WITH_DEPTH_SET_POINT (3):
            Go to waypoint with depth set point.
        INSTRUCTION_TYPE_GO_TO_DEPTH_SET_POINT (4):
            Go to depth set point.
        INSTRUCTION_TYPE_SET_CAMERA_ACTION (5):
            Command used to take photo repeatedly or
            start, stop recording.
        INSTRUCTION_TYPE_SET_CONTROL_MODE (6):
            Sets a new control mode.
        INSTRUCTION_TYPE_SET_TILT_MAIN_CAMERA (7):
            Sets a new angle for the tilt servo.
        INSTRUCTION_TYPE_SET_TILT_SERVO (8):
            Sets a new angle for the tilt servo.
        INSTRUCTION_TYPE_WAIT_FOR_SEC (9):
            Waiting for requested time in seconds.
        INSTRUCTION_TYPE_GO_TO_SURFACE (10):
            Go to the surface.
        INSTRUCTION_TYPE_GO_TO_SEABED (11):
            Go to the seabed.
        INSTRUCTION_TYPE_GO_TO_HOME (12):
            Returning to home.
        INSTRUCTION_TYPE_SURVEY (13):
            Execute a survey pattern over a polygon area.
        INSTRUCTION_TYPE_RECORD_MULTIBEAM (14):
            Start or stop multibeam recording.
        INSTRUCTION_TYPE_ACTIVATE_MULTIBEAM (15):
            Start or stop the multibeam driver.
        INSTRUCTION_TYPE_SET_MULTIBEAM_CONFIG (16):
            Change the multibeam configuration.
        INSTRUCTION_TYPE_SET_LIGHTS (17):
            Set the lights.
        INSTRUCTION_TYPE_SET_LASER (18):
            Set the laser.
        INSTRUCTION_TYPE_SET_TILT_STABILIZATION (19):
            Enable or disable tilt stabilization.
        INSTRUCTION_TYPE_SET_CV_MODEL (20):
            Start or stop a computer vision model.
        INSTRUCTION_TYPE_ANNOTATION (21):
            Record an annotation.
        INSTRUCTION_TYPE_GO_TO_HEADING (22):
            Turn to a heading.
        INSTRUCTION_TYPE_TRANSECT (23):
            Drive a straight line.
        INSTRUCTION_TYPE_GO_TO_RELATIVE_DEPTH (24):
            Change the depth by an amount.
        INSTRUCTION_TYPE_SET_CRUISE_SPEED (25):
            Change the cruise speed.
    """
    INSTRUCTION_TYPE_UNSPECIFIED = 0
    """Unspecified."""
    INSTRUCTION_TYPE_NONE = 1
    """None."""
    INSTRUCTION_TYPE_GO_TO_WAYPOINT = 2
    """Go to waypoint."""
    INSTRUCTION_TYPE_GO_TO_WAYPOINT_WITH_DEPTH_SET_POINT = 3
    """Go to waypoint with depth set point."""
    INSTRUCTION_TYPE_GO_TO_DEPTH_SET_POINT = 4
    """Go to depth set point."""
    INSTRUCTION_TYPE_SET_CAMERA_ACTION = 5
    """Command used to take photo repeatedly or start, stop
    recording."""
    INSTRUCTION_TYPE_SET_CONTROL_MODE = 6
    """Sets a new control mode."""
    INSTRUCTION_TYPE_SET_TILT_MAIN_CAMERA = 7
    """Sets a new angle for the tilt servo."""
    INSTRUCTION_TYPE_SET_TILT_SERVO = 8
    """Sets a new angle for the tilt servo."""
    INSTRUCTION_TYPE_WAIT_FOR_SEC = 9
    """Waiting for requested time in seconds."""
    INSTRUCTION_TYPE_GO_TO_SURFACE = 10
    """Go to the surface."""
    INSTRUCTION_TYPE_GO_TO_SEABED = 11
    """Go to the seabed."""
    INSTRUCTION_TYPE_GO_TO_HOME = 12
    """Returning to home."""
    INSTRUCTION_TYPE_SURVEY = 13
    """Execute a survey pattern over a polygon area."""
    INSTRUCTION_TYPE_RECORD_MULTIBEAM = 14
    """Start or stop multibeam recording."""
    INSTRUCTION_TYPE_ACTIVATE_MULTIBEAM = 15
    """Start or stop the multibeam driver."""
    INSTRUCTION_TYPE_SET_MULTIBEAM_CONFIG = 16
    """Change the multibeam configuration."""
    INSTRUCTION_TYPE_SET_LIGHTS = 17
    """Set the lights."""
    INSTRUCTION_TYPE_SET_LASER = 18
    """Set the laser."""
    INSTRUCTION_TYPE_SET_TILT_STABILIZATION = 19
    """Enable or disable tilt stabilization."""
    INSTRUCTION_TYPE_SET_CV_MODEL = 20
    """Start or stop a computer vision model."""
    INSTRUCTION_TYPE_ANNOTATION = 21
    """Record an annotation."""
    INSTRUCTION_TYPE_GO_TO_HEADING = 22
    """Turn to a heading."""
    INSTRUCTION_TYPE_TRANSECT = 23
    """Drive a straight line."""
    INSTRUCTION_TYPE_GO_TO_RELATIVE_DEPTH = 24
    """Change the depth by an amount."""
    INSTRUCTION_TYPE_SET_CRUISE_SPEED = 25
    """Change the cruise speed."""


class MissionState(proto.Enum):
    r"""List of mission supervisor states.

    Attributes:
        MISSION_STATE_UNSPECIFIED (0):
            Unspecified.
        MISSION_STATE_INACTIVE (1):
            Mission supervisor is inactive.
        MISSION_STATE_READY (2):
            Ready to start mission.
        MISSION_STATE_RUNNING (3):
            Mission is running.
        MISSION_STATE_PAUSED (4):
            Mission is paused.
        MISSION_STATE_COMPLETED (5):
            Mission is completed.
        MISSION_STATE_ABORTED (6):
            Mission is aborted by the mission supervisor.
        MISSION_STATE_FAILED_TO_LOAD_MISSION (7):
            Mission has failed to load.
        MISSION_STATE_FAILED_TO_START_MISSION (8):
            Mission has failed to start.
    """
    MISSION_STATE_UNSPECIFIED = 0
    """Unspecified."""
    MISSION_STATE_INACTIVE = 1
    """Mission supervisor is inactive."""
    MISSION_STATE_READY = 2
    """Ready to start mission."""
    MISSION_STATE_RUNNING = 3
    """Mission is running."""
    MISSION_STATE_PAUSED = 4
    """Mission is paused."""
    MISSION_STATE_COMPLETED = 5
    """Mission is completed."""
    MISSION_STATE_ABORTED = 6
    """Mission is aborted by the mission supervisor."""
    MISSION_STATE_FAILED_TO_LOAD_MISSION = 7
    """Mission has failed to load."""
    MISSION_STATE_FAILED_TO_START_MISSION = 8
    """Mission has failed to start."""


class MissionResult(proto.Enum):
    r"""How a mission run ended.

    Attributes:
        MISSION_RESULT_UNSPECIFIED (0):
            No mission has ended since the drone started.
        MISSION_RESULT_COMPLETED (1):
            The run reached the end of the mission. Instructions can
            have been skipped on the way, for a device that is not
            connected: see MissionOutcome.skipped_instruction_ids.
        MISSION_RESULT_ABORTED (2):
            The drone stopped the mission, see
            MissionOutcome.abort_reason.
        MISSION_RESULT_CANCELLED (3):
            A client cleared or replaced the mission
            while it was running or paused.
    """
    MISSION_RESULT_UNSPECIFIED = 0
    """No mission has ended since the drone started."""
    MISSION_RESULT_COMPLETED = 1
    """The run reached the end of the mission. Instructions can have been
    skipped on the way, for a device that is not connected: see
    MissionOutcome.skipped_instruction_ids."""
    MISSION_RESULT_ABORTED = 2
    """The drone stopped the mission, see MissionOutcome.abort_reason."""
    MISSION_RESULT_CANCELLED = 3
    """A client cleared or replaced the mission while it was running
    or paused."""


class MissionAbortReason(proto.Enum):
    r"""Why the drone aborted a mission. A client that does not know
    a value treats it as unspecified.

    Attributes:
        MISSION_ABORT_REASON_UNSPECIFIED (0):
            Unspecified, see MissionOutcome.reason.
        MISSION_ABORT_REASON_CONTROL_MODE_LOST (1):
            A control mode the instruction needs was
            refused or lost.
        MISSION_ABORT_REASON_POSITION_UNKNOWN (2):
            The instruction needs the drone's position,
            which is unknown.
        MISSION_ABORT_REASON_STUCK (3):
            The drone stopped making progress towards its
            target.
        MISSION_ABORT_REASON_WAYPOINT_TOO_FAR (4):
            A waypoint is farther away than the drone
            goes.
        MISSION_ABORT_REASON_HEADING_UNKNOWN (5):
            A turn needs the drone's heading, which is
            unknown.
        MISSION_ABORT_REASON_HEADING_NOT_REACHED (6):
            A turn did not reach its heading in time.
        MISSION_ABORT_REASON_DEVICE_TIMEOUT (7):
            A camera, multibeam or other device did not
            confirm a command in time.
        MISSION_ABORT_REASON_DURATION_TOO_LONG (8):
            The time left to complete the mission grew
            past the limit.
        MISSION_ABORT_REASON_SUPERVISOR (9):
            The drone's supervisor stopped the mission:
            the pilot took control, the controlling client
            stopped answering, or the drone lost its
            position or attitude.
    """
    MISSION_ABORT_REASON_UNSPECIFIED = 0
    """Unspecified, see MissionOutcome.reason."""
    MISSION_ABORT_REASON_CONTROL_MODE_LOST = 1
    """A control mode the instruction needs was refused or lost."""
    MISSION_ABORT_REASON_POSITION_UNKNOWN = 2
    """The instruction needs the drone's position, which is unknown."""
    MISSION_ABORT_REASON_STUCK = 3
    """The drone stopped making progress towards its target."""
    MISSION_ABORT_REASON_WAYPOINT_TOO_FAR = 4
    """A waypoint is farther away than the drone goes."""
    MISSION_ABORT_REASON_HEADING_UNKNOWN = 5
    """A turn needs the drone's heading, which is unknown."""
    MISSION_ABORT_REASON_HEADING_NOT_REACHED = 6
    """A turn did not reach its heading in time."""
    MISSION_ABORT_REASON_DEVICE_TIMEOUT = 7
    """A camera, multibeam or other device did not confirm a command
    in time."""
    MISSION_ABORT_REASON_DURATION_TOO_LONG = 8
    """The time left to complete the mission grew past the limit."""
    MISSION_ABORT_REASON_SUPERVISOR = 9
    """The drone's supervisor stopped the mission: the pilot took
    control, the controlling client stopped answering, or the drone
    lost its position or attitude."""


class InstructionResultState(proto.Enum):
    r"""Outcome of an instruction started with RunInstructionCtrl.

    Attributes:
        INSTRUCTION_RESULT_STATE_UNSPECIFIED (0):
            Unspecified.
        INSTRUCTION_RESULT_STATE_ACCEPTED (1):
            The instruction was accepted and has started.
        INSTRUCTION_RESULT_STATE_REJECTED (2):
            The instruction was not started, see reason.
        INSTRUCTION_RESULT_STATE_COMPLETED (3):
            The instruction completed.
        INSTRUCTION_RESULT_STATE_FAILED (4):
            The instruction stopped before completing,
            see reason.
        INSTRUCTION_RESULT_STATE_CANCELLED (5):
            The instruction was cancelled by a client or
            by the drone.
    """
    INSTRUCTION_RESULT_STATE_UNSPECIFIED = 0
    """Unspecified."""
    INSTRUCTION_RESULT_STATE_ACCEPTED = 1
    """The instruction was accepted and has started."""
    INSTRUCTION_RESULT_STATE_REJECTED = 2
    """The instruction was not started, see reason."""
    INSTRUCTION_RESULT_STATE_COMPLETED = 3
    """The instruction completed."""
    INSTRUCTION_RESULT_STATE_FAILED = 4
    """The instruction stopped before completing, see reason."""
    INSTRUCTION_RESULT_STATE_CANCELLED = 5
    """The instruction was cancelled by a client or by the drone."""


class MissionRuleState(proto.Enum):
    r"""MissionRuleState is where a rule is in its episode.

    Attributes:
        MISSION_RULE_STATE_UNSPECIFIED (0):
            Unspecified.
        MISSION_RULE_STATE_IDLE (1):
            Waiting for the trigger.
        MISSION_RULE_STATE_ACTIVE (2):
            The rule has fired and has not released yet.
        MISSION_RULE_STATE_COOLDOWN (3):
            Released; waiting for the cooldown before it
            can fire again.
        MISSION_RULE_STATE_DISABLED (4):
            The rule is disabled.
    """
    MISSION_RULE_STATE_UNSPECIFIED = 0
    """Unspecified."""
    MISSION_RULE_STATE_IDLE = 1
    """Waiting for the trigger."""
    MISSION_RULE_STATE_ACTIVE = 2
    """The rule has fired and has not released yet."""
    MISSION_RULE_STATE_COOLDOWN = 3
    """Released; waiting for the cooldown before it can fire again."""
    MISSION_RULE_STATE_DISABLED = 4
    """The rule is disabled."""


class Mission(proto.Message):
    r"""A list of waypoints describes a mission that the auto pilot
    can execute.

    Attributes:
        id (int):
            Mission id, defined by the client.
        name (str):
            Mission name provided from the app.
        instructions (MutableSequence[blueye.protocol.types.Instruction]):
            List of instructions in the mission.
        path_segments (MutableSequence[blueye.protocol.types.PathSegment]):
            Calculated path segments from the reference
            generator (optional).
        total_distance (int):
            Total distance of the mission (m) (optional).
        total_duration_time (int):
            Total duration time of the mission (s)
            (optional).
        default_surge_speed (float):
            Default cruise speed of the mission (m/s)
            (optional).
        default_heave_speed (float):
            Default heave speed of the mission (m/s)
            (optional).
        default_circle_of_acceptance (float):
            Default circle of acceptance for waypoints
            (m) (optional).
        revision (int):
            Set by the drone, increases with every
            accepted SetInstructionUpdateReq.
        uuid (str):
            Client-defined identifier of the mission, such as a UUID,
            for clients to match the drone's status with their own
            records (optional, at most 64 characters). The drone keeps
            it through instruction updates and echoes it in
            GetMissionRep, MissionStatus and MissionOutcome. It does not
            tell loads apart: see load_id.
        load_id (int):
            Set by the drone: a random id it draws for every mission it
            loads, from 1 to 2^53 - 1 so that clients that hold numbers
            as doubles, such as JavaScript, read it exactly. An
            instruction update names it
            (SetInstructionUpdateReq.load_id), so it cannot change a
            mission loaded since. Ignored in SetMissionReq.
    """

    id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instructions: MutableSequence['Instruction'] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='Instruction',
    )
    path_segments: MutableSequence['PathSegment'] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message='PathSegment',
    )
    total_distance: int = proto.Field(
        proto.UINT32,
        number=5,
    )
    total_duration_time: int = proto.Field(
        proto.UINT32,
        number=6,
    )
    default_surge_speed: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    default_heave_speed: float = proto.Field(
        proto.FLOAT,
        number=8,
    )
    default_circle_of_acceptance: float = proto.Field(
        proto.FLOAT,
        number=9,
    )
    revision: int = proto.Field(
        proto.UINT32,
        number=10,
    )
    uuid: str = proto.Field(
        proto.STRING,
        number=11,
    )
    load_id: int = proto.Field(
        proto.UINT64,
        number=12,
    )


class Instruction(proto.Message):
    r"""A mission consists of one or multiple instructions. One
    instruction can be of different types.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (int):

        group_id (int):
            Group id used for polygons.
        pause_on_completion (bool):
            Pause the mission after this instruction.
            RunMissionCtrl continues it.
        waypoint_command (blueye.protocol.types.WaypointCommand):
            Go to waypoint.

            This field is a member of `oneof`_ ``command``.
        depth_set_point_command (blueye.protocol.types.DepthSetPointCommand):
            Go to depth.

            This field is a member of `oneof`_ ``command``.
        camera_command (blueye.protocol.types.CameraCommand):
            Camera commands.

            This field is a member of `oneof`_ ``command``.
        control_mode_command (blueye.protocol.types.ControlModeCommand):
            Set control modes.

            This field is a member of `oneof`_ ``command``.
        tilt_main_camera_command (blueye.protocol.types.TiltMainCameraCommand):
            Set camera to angle x.

            This field is a member of `oneof`_ ``command``.
        tilt_multibeam_command (blueye.protocol.types.TiltMultibeamCommand):
            Set multibeam tilt angle.

            This field is a member of `oneof`_ ``command``.
        wait_for_command (blueye.protocol.types.WaitForCommand):
            Wait for x seconds.

            This field is a member of `oneof`_ ``command``.
        go_to_surface_command (blueye.protocol.types.GoToSurfaceCommand):
            Go to surface.

            This field is a member of `oneof`_ ``command``.
        go_to_seabed_command (blueye.protocol.types.GoToSeabedCommand):
            Go to seabed.

            This field is a member of `oneof`_ ``command``.
        go_to_home_command (blueye.protocol.types.GoToHomeCommand):
            Go to home position.

            This field is a member of `oneof`_ ``command``.
        survey_command (blueye.protocol.types.SurveyCommand):
            Execute a survey pattern over a polygon area.

            This field is a member of `oneof`_ ``command``.
        record_multibeam_command (blueye.protocol.types.RecordMultibeamCommand):
            Start or stop multibeam recording.

            This field is a member of `oneof`_ ``command``.
        activate_multibeam_command (blueye.protocol.types.ActivateMultibeamCommand):
            Start or stop the multibeam driver.

            This field is a member of `oneof`_ ``command``.
        multibeam_config_command (blueye.protocol.types.MultibeamConfigCommand):
            Change the multibeam configuration.

            This field is a member of `oneof`_ ``command``.
        lights_command (blueye.protocol.types.LightsCommand):
            Set the main or guest port lights.

            This field is a member of `oneof`_ ``command``.
        laser_command (blueye.protocol.types.LaserCommand):
            Set the laser.

            This field is a member of `oneof`_ ``command``.
        tilt_stabilization_command (blueye.protocol.types.TiltStabilizationCommand):
            Enable or disable tilt stabilization.

            This field is a member of `oneof`_ ``command``.
        cv_model_state_command (blueye.protocol.types.CvModelStateCommand):
            Start or stop a computer vision model.

            This field is a member of `oneof`_ ``command``.
        annotation_command (blueye.protocol.types.AnnotationCommand):
            Record an annotation in the dive log.

            This field is a member of `oneof`_ ``command``.
        heading_command (blueye.protocol.types.HeadingCommand):
            Turn to a heading and hold it.

            This field is a member of `oneof`_ ``command``.
        transect_command (blueye.protocol.types.TransectCommand):
            Drive a straight line on a course for a
            distance.

            This field is a member of `oneof`_ ``command``.
        relative_depth_command (blueye.protocol.types.RelativeDepthCommand):
            Change the depth by an amount.

            This field is a member of `oneof`_ ``command``.
        cruise_speed_command (blueye.protocol.types.CruiseSpeedCommand):
            Change the cruise speed for the rest of the
            mission.

            This field is a member of `oneof`_ ``command``.
    """

    id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    group_id: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    pause_on_completion: bool = proto.Field(
        proto.BOOL,
        number=27,
    )
    waypoint_command: 'WaypointCommand' = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof='command',
        message='WaypointCommand',
    )
    depth_set_point_command: 'DepthSetPointCommand' = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof='command',
        message='DepthSetPointCommand',
    )
    camera_command: 'CameraCommand' = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof='command',
        message='CameraCommand',
    )
    control_mode_command: 'ControlModeCommand' = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof='command',
        message='ControlModeCommand',
    )
    tilt_main_camera_command: 'TiltMainCameraCommand' = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof='command',
        message='TiltMainCameraCommand',
    )
    tilt_multibeam_command: 'TiltMultibeamCommand' = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof='command',
        message='TiltMultibeamCommand',
    )
    wait_for_command: 'WaitForCommand' = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof='command',
        message='WaitForCommand',
    )
    go_to_surface_command: 'GoToSurfaceCommand' = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof='command',
        message='GoToSurfaceCommand',
    )
    go_to_seabed_command: 'GoToSeabedCommand' = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof='command',
        message='GoToSeabedCommand',
    )
    go_to_home_command: 'GoToHomeCommand' = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof='command',
        message='GoToHomeCommand',
    )
    survey_command: 'SurveyCommand' = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof='command',
        message='SurveyCommand',
    )
    record_multibeam_command: 'RecordMultibeamCommand' = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof='command',
        message='RecordMultibeamCommand',
    )
    activate_multibeam_command: 'ActivateMultibeamCommand' = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof='command',
        message='ActivateMultibeamCommand',
    )
    multibeam_config_command: 'MultibeamConfigCommand' = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof='command',
        message='MultibeamConfigCommand',
    )
    lights_command: 'LightsCommand' = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof='command',
        message='LightsCommand',
    )
    laser_command: 'LaserCommand' = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof='command',
        message='LaserCommand',
    )
    tilt_stabilization_command: 'TiltStabilizationCommand' = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof='command',
        message='TiltStabilizationCommand',
    )
    cv_model_state_command: 'CvModelStateCommand' = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof='command',
        message='CvModelStateCommand',
    )
    annotation_command: 'AnnotationCommand' = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof='command',
        message='AnnotationCommand',
    )
    heading_command: 'HeadingCommand' = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof='command',
        message='HeadingCommand',
    )
    transect_command: 'TransectCommand' = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof='command',
        message='TransectCommand',
    )
    relative_depth_command: 'RelativeDepthCommand' = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof='command',
        message='RelativeDepthCommand',
    )
    cruise_speed_command: 'CruiseSpeedCommand' = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof='command',
        message='CruiseSpeedCommand',
    )


class DepthSetPoint(proto.Message):
    r"""Depth set point is used to describe a depth set-point
    relative to the surface or the seabed.

    Attributes:
        depth (float):
            Desired depth at the wp (m).
        speed_to_depth (float):
            Desired speed to desired depth set point
            (m/s).
        depth_zero_reference (blueye.protocol.types.DepthZeroReference):
            Used to distinguish desired altitude or
            depth.
    """

    depth: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    speed_to_depth: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    depth_zero_reference: 'DepthZeroReference' = proto.Field(
        proto.ENUM,
        number=3,
        enum='DepthZeroReference',
    )


class Waypoint(proto.Message):
    r"""Waypoints used to describe a path for the auto pilot.

    Attributes:
        id (int):
            Waypoint id.
        name (str):
            Waypoint name provided from the app.
        global_position (blueye.protocol.types.LatLongPosition):
            Position if the waypoint (decimal degrees).
        circle_of_acceptance (float):
            Radius of the acceptance circle around the
            waypoint (m).
        speed_to_target (float):
            Desired speed over ground to waypoint (m/s).
        depth_set_point (blueye.protocol.types.DepthSetPoint):
            Depth set point (optional).
    """

    id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    global_position: message_formats.LatLongPosition = proto.Field(
        proto.MESSAGE,
        number=3,
        message=message_formats.LatLongPosition,
    )
    circle_of_acceptance: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    speed_to_target: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    depth_set_point: 'DepthSetPoint' = proto.Field(
        proto.MESSAGE,
        number=6,
        message='DepthSetPoint',
    )


class ControlModeCommand(proto.Message):
    r"""A ControlModeCommand is used to set vertical and horizontal
    control mode during a mission.

    Attributes:
        control_mode_vertical (blueye.protocol.types.ControlModeVertical):
            Desired control mode in heave.
        control_mode_horizontal (blueye.protocol.types.ControlModeHorizontal):
            Desired control mode in surge and yaw.
    """

    control_mode_vertical: 'ControlModeVertical' = proto.Field(
        proto.ENUM,
        number=5,
        enum='ControlModeVertical',
    )
    control_mode_horizontal: 'ControlModeHorizontal' = proto.Field(
        proto.ENUM,
        number=6,
        enum='ControlModeHorizontal',
    )


class DetectionTrigger(proto.Message):
    r"""DetectionTrigger is satisfied by what the computer vision models
    see.

    The trigger is satisfied while at least one detection of the running
    models matches all of the filters below. The models have to be
    running; a trigger for a model that is not running is not satisfied
    and TriggerStatus reports sensor_unavailable.

    Attributes:
        class_names (MutableSequence[str]):
            Any of these class names; empty matches every
            class.
        model_name (str):
            Only detections from this model; empty
            matches every model.
        camera (blueye.protocol.types.Camera):
            Only detections from this camera; unspecified
            matches every camera.
        min_confidence (float):
            Detections below this confidence are ignored
            (0..1).
        min_area_fraction (float):
            Least bounding box area over image area a
            detection must have (0..1).
    """

    class_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    model_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    camera: message_formats.Camera = proto.Field(
        proto.ENUM,
        number=3,
        enum=message_formats.Camera,
    )
    min_confidence: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    min_area_fraction: float = proto.Field(
        proto.FLOAT,
        number=5,
    )


class DepthTrigger(proto.Message):
    r"""DepthTrigger is satisfied while the drone is between two depths
    below the surface.

    A depth with a tolerance is the two bounds around it: 9 and 11 for
    ten metres give or take a metre. Leaving max_depth at zero gives no
    upper bound, so a min_depth of 20 on its own is satisfied deeper
    than 20 m. Neither bound may be negative, and a max_depth that is
    set has to be above min_depth: the two are the edges of a band, not
    a single depth, and a rule whose band has no width is refused rather
    than left never firing. The drone measures its depth from the moment
    it is powered on, so this trigger reports sensor_unavailable only
    while no depth has reached the mission at all.

    Attributes:
        min_depth (float):
            Shallowest depth that satisfies the trigger
            (m below the surface).
        max_depth (float):
            Deepest depth that satisfies the trigger (m).
            Zero means no upper bound.
    """

    min_depth: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    max_depth: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class AltitudeTrigger(proto.Message):
    r"""AltitudeTrigger is satisfied while the drone is between two heights
    above the seabed.

    A height with a tolerance is the two bounds around it: 2.5 and 3.5
    for three metres off the bottom give or take half a metre. Leaving
    max_altitude at zero gives no upper bound. Neither bound may be
    negative, and a max_altitude that is set has to be above
    min_altitude, as for DepthTrigger. The height comes from a DVL or an
    altimeter; with neither mounted, out of its range, or with a reading
    the drone does not trust, the trigger is simply not satisfied and
    TriggerStatus reports sensor_unavailable.

    Attributes:
        min_altitude (float):
            Lowest height above the seabed that satisfies
            the trigger (m).
        max_altitude (float):
            Highest height that satisfies the trigger
            (m). Zero means no upper bound.
    """

    min_altitude: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    max_altitude: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class LocationTrigger(proto.Message):
    r"""LocationTrigger is satisfied while the drone is inside a circle
    around a position.

    Entering the circle makes the trigger satisfied and leaving it makes
    it unsatisfied, so a rule with one location trigger can start a
    recording in its enter instructions and stop it in its exit
    instructions. Any valid position estimate will do, whichever sensors
    it is built from; while the drone has none the trigger is simply not
    satisfied and TriggerStatus reports sensor_unavailable.

    Attributes:
        position (blueye.protocol.types.LatLongPosition):
            Centre of the circle (decimal degrees).
        circle_of_acceptance (float):
            Radius of the circle around the position (m).
            Must be above zero.
    """

    position: message_formats.LatLongPosition = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.LatLongPosition,
    )
    circle_of_acceptance: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class Trigger(proto.Message):
    r"""Trigger is one condition of a mission rule.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        detection_trigger (blueye.protocol.types.DetectionTrigger):
            Satisfied by a detection from a computer
            vision model.

            This field is a member of `oneof`_ ``condition``.
        depth_trigger (blueye.protocol.types.DepthTrigger):
            Satisfied at a depth below the surface.

            This field is a member of `oneof`_ ``condition``.
        altitude_trigger (blueye.protocol.types.AltitudeTrigger):
            Satisfied at a height above the seabed.

            This field is a member of `oneof`_ ``condition``.
        location_trigger (blueye.protocol.types.LocationTrigger):
            Satisfied inside a circle around a position.

            This field is a member of `oneof`_ ``condition``.
    """

    detection_trigger: 'DetectionTrigger' = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='condition',
        message='DetectionTrigger',
    )
    depth_trigger: 'DepthTrigger' = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='condition',
        message='DepthTrigger',
    )
    altitude_trigger: 'AltitudeTrigger' = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof='condition',
        message='AltitudeTrigger',
    )
    location_trigger: 'LocationTrigger' = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof='condition',
        message='LocationTrigger',
    )


class MissionRule(proto.Message):
    r"""MissionRule runs instructions when all of its triggers are
    satisfied at once and when they stop being so. A drone runs at
    most 16 rules with at most 8 triggers and 8 instructions per
    list, and a rule has to carry at least one instruction in one of
    its lists. A rule with no triggers never fires. Instructions
    that move the drone (waypoint, go to home, transect, survey,
    depth set point, relative depth, go to surface or seabed,
    control mode, heading) and waits are refused in rules; camera,
    tilt, lights, laser, multibeam, tilt stabilization, CV model,
    annotation and cruise speed are allowed.

    Attributes:
        id (int):
            Rule id, defined by the client. Must be
            greater than zero and unique.
        name (str):
            Rule name, for the log and the app.
        disabled (bool):
            A disabled rule never fires. Rules run unless
            this is set.
        enter_instructions (MutableSequence[blueye.protocol.types.Instruction]):
            Run when the rule fires.
        exit_instructions (MutableSequence[blueye.protocol.types.Instruction]):
            Run when the rule releases.
        triggers (MutableSequence[blueye.protocol.types.Trigger]):
            Conditions that must all be satisfied at once
            for the rule to fire.
        hold_duration (google.protobuf.duration_pb2.Duration):
            How long all the triggers must stay satisfied
            before the rule fires. At most an hour.
        release_duration (google.protobuf.duration_pb2.Duration):
            How long a trigger must stay unsatisfied
            before the rule releases. At most an hour.
        cooldown_duration (google.protobuf.duration_pb2.Duration):
            Time after a release before the rule can fire
            again. At most an hour.
    """

    id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    enter_instructions: MutableSequence['Instruction'] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message='Instruction',
    )
    exit_instructions: MutableSequence['Instruction'] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message='Instruction',
    )
    triggers: MutableSequence['Trigger'] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message='Trigger',
    )
    hold_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    release_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=9,
        message=duration_pb2.Duration,
    )
    cooldown_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=10,
        message=duration_pb2.Duration,
    )


class MissionRuleStatus(proto.Message):
    r"""MissionRuleStatus is the state of one rule.

    Attributes:
        id (int):
            Rule id.
        state (blueye.protocol.types.MissionRuleState):
            What the rule is doing.
        episodes (int):
            Times the rule has fired since it was set.
        last_fired (google.protobuf.timestamp_pb2.Timestamp):
            When the rule last fired; unset before the
            first time.
        last_result (blueye.protocol.types.InstructionResultState):
            Outcome of the last instruction the rule ran.
        last_reason (str):
            Reason of the last result, when there is one.
        triggers (MutableSequence[blueye.protocol.types.TriggerStatus]):
            One entry per trigger, in the order the rule
            lists them.
    """

    id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    state: 'MissionRuleState' = proto.Field(
        proto.ENUM,
        number=2,
        enum='MissionRuleState',
    )
    episodes: int = proto.Field(
        proto.UINT32,
        number=3,
    )
    last_fired: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    last_result: 'InstructionResultState' = proto.Field(
        proto.ENUM,
        number=5,
        enum='InstructionResultState',
    )
    last_reason: str = proto.Field(
        proto.STRING,
        number=6,
    )
    triggers: MutableSequence['TriggerStatus'] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message='TriggerStatus',
    )


class TriggerStatus(proto.Message):
    r"""TriggerStatus is the state of one trigger of a rule, so a
    client can show which condition is holding the rule back.

    Attributes:
        kind (blueye.protocol.types.TriggerKind):
            Which condition the trigger carries.
        satisfied (bool):
            True while the condition holds.
        sensor_unavailable (bool):
            True while the drone has no reading to judge
            the condition by.
    """

    kind: 'TriggerKind' = proto.Field(
        proto.ENUM,
        number=1,
        enum='TriggerKind',
    )
    satisfied: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    sensor_unavailable: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class InsertInstruction(proto.Message):
    r"""InsertInstruction adds an instruction to the loaded mission. It must
    say where: an insert that sets neither before_id nor append true is
    refused.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instruction (blueye.protocol.types.Instruction):
            The instruction to add. Its id must be new to
            the mission.
        before_id (int):
            Id of the instruction to insert in front of.

            This field is a member of `oneof`_ ``placement``.
        append (bool):
            True adds the instruction at the end of the
            mission.

            This field is a member of `oneof`_ ``placement``.
    """

    instruction: 'Instruction' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Instruction',
    )
    before_id: int = proto.Field(
        proto.UINT32,
        number=2,
        oneof='placement',
    )
    append: bool = proto.Field(
        proto.BOOL,
        number=3,
        oneof='placement',
    )


class WaypointCommand(proto.Message):
    r"""A WaypointCommand will request the drone to drive to a point
    automatically.

    Attributes:
        waypoint (blueye.protocol.types.Waypoint):
            Waypoint to go to.
    """

    waypoint: 'Waypoint' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Waypoint',
    )


class DepthSetPointCommand(proto.Message):
    r"""A DepthSetPointCommand is used to go to a desired depth or
    altitude.

    Attributes:
        depth_set_point (blueye.protocol.types.DepthSetPoint):
            Depth set point to go to.
    """

    depth_set_point: 'DepthSetPoint' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='DepthSetPoint',
    )


class TiltMainCameraCommand(proto.Message):
    r"""The TiltMainCameraCommand can set the desired camera tilt
    angle.

    Attributes:
        tilt_angle (blueye.protocol.types.TiltAngle):
            Tilt angle of the camera (-30..30).
    """

    tilt_angle: message_formats.TiltAngle = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.TiltAngle,
    )


class TiltMultibeamCommand(proto.Message):
    r"""The TiltMultibeamCommand is used to set the tilt angle of the
    servo.

    Attributes:
        multibeam_servo (blueye.protocol.types.MultibeamServo):
            Tilt angle for the multibeam servo.
    """

    multibeam_servo: message_formats.MultibeamServo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.MultibeamServo,
    )


class WaitForCommand(proto.Message):
    r"""WaitForCommand is used to wait during a mission.

    Attributes:
        wait_for_seconds (float):
            Wait for x seconds.
    """

    wait_for_seconds: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class CameraCommand(proto.Message):
    r"""CameraCommands are used to control the camera from a mission.

    Attributes:
        camera_action (blueye.protocol.types.CameraAction):
            Camera command.
        action_param (float):
            Used for taking photos based on a time or
            distance interval.
        camera (blueye.protocol.types.Camera):
            Which camera the action applies to. The main
            camera when unspecified or unrecognised.
        storage_location (blueye.protocol.types.StorageLocation):
            Where to store the photos or the recording.
            Internal when unspecified.
    """

    camera_action: 'CameraAction' = proto.Field(
        proto.ENUM,
        number=1,
        enum='CameraAction',
    )
    action_param: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    camera: message_formats.Camera = proto.Field(
        proto.ENUM,
        number=3,
        enum=message_formats.Camera,
    )
    storage_location: message_formats.StorageLocation = proto.Field(
        proto.ENUM,
        number=4,
        enum=message_formats.StorageLocation,
    )


class GoToSurfaceCommand(proto.Message):
    r"""GoToSurfaceCommand is used to go to the surface.

    Attributes:
        desired_speed (float):
            Desired speed to surface (m/s).
    """

    desired_speed: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class GoToSeabedCommand(proto.Message):
    r"""GoToSeabedCommand is used to go to the seabed.

    Attributes:
        desired_speed (float):
            Desired speed to seabed (m/s).
    """

    desired_speed: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class GoToHomeCommand(proto.Message):
    r"""GoToHomeCommand is used to go to the home position.

    Attributes:
        desired_speed (float):
            Desired speed to home (m/s).
    """

    desired_speed: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class RecordMultibeamCommand(proto.Message):
    r"""RecordMultibeamCommand starts or stops recording of the
    multibeam sonar.

    Attributes:
        enable (bool):
            True to start recording, false to stop.
        storage_location (blueye.protocol.types.StorageLocation):
            Where to store the recording. Internal when
            unspecified.
    """

    enable: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    storage_location: message_formats.StorageLocation = proto.Field(
        proto.ENUM,
        number=2,
        enum=message_formats.StorageLocation,
    )


class ActivateMultibeamCommand(proto.Message):
    r"""ActivateMultibeamCommand starts or stops the multibeam sonar
    driver, as ActivateMultibeamCtrl and DeactivateMultibeamCtrl do.

    The instruction completes when the driver reports the requested
    state, so a following RecordMultibeamCommand or
    TiltMultibeamCommand finds the sonar ready.

    Attributes:
        activate (bool):
            True to start the driver, false to stop it.
        config (blueye.protocol.types.MultibeamConfig):
            Configuration to start with. When left out,
            the last known configuration is used.
        expected_device_id (blueye.protocol.types.GuestPortDeviceID):
            The sonar ``config`` was made for, as the multibeam driver
            reports it. The driver still starts or stops when a
            different sonar is connected, but ``config`` is skipped in
            favour of the last configuration the driver reported and the
            drone sends a NOTIFICATION_TYPE_MULTIBEAM_SONAR_MISMATCH
            notification. Unspecified applies ``config`` to whichever
            sonar is connected. A ``config`` that the sonar cannot run,
            measured the same way as for MultibeamConfigCommand, skips
            the whole instruction instead, so the driver is never
            started with a configuration nobody asked for.
    """

    activate: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    config: message_formats.MultibeamConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=message_formats.MultibeamConfig,
    )
    expected_device_id: message_formats.GuestPortDeviceID = proto.Field(
        proto.ENUM,
        number=3,
        enum=message_formats.GuestPortDeviceID,
    )


class MultibeamConfigCommand(proto.Message):
    r"""MultibeamConfigCommand changes the configuration of a running
    multibeam sonar.

    A configuration is made for one sonar, because ranges, frequencies
    and beam counts differ between them. The drone compares
    expected_device_id with the sonar the multibeam driver reports, not
    with what the guest port discovery found, and when they differ it
    skips the whole instruction and sends a
    NOTIFICATION_TYPE_MULTIBEAM_SONAR_MISMATCH notification; the mission
    carries on with the next instruction. Unspecified applies the
    configuration to whichever sonar is connected.

    The configuration is also measured against what that sonar can do:
    the range for the frequency mode asked for, a high frequency mode on
    a sonar that has only one, and the number of beams. A configuration
    outside them skips the instruction with a reason naming the sonar.
    Nothing is quietly clamped, so a sonar never ends up running a
    configuration nobody asked for.

    Attributes:
        config (blueye.protocol.types.MultibeamConfig):
            The configuration to apply.
        expected_device_id (blueye.protocol.types.GuestPortDeviceID):
            The sonar this configuration was made for.
    """

    config: message_formats.MultibeamConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.MultibeamConfig,
    )
    expected_device_id: message_formats.GuestPortDeviceID = proto.Field(
        proto.ENUM,
        number=2,
        enum=message_formats.GuestPortDeviceID,
    )


class LightsCommand(proto.Message):
    r"""LightsCommand sets the intensity of the main or guest port
    lights, as LightsCtrl and GuestportLightsCtrl do.

    Attributes:
        lights (blueye.protocol.types.Lights):
            Light intensity (0..1).
        target (blueye.protocol.types.LightTarget):
            Which lights to set. The main lights when
            unspecified or unrecognised.
    """

    lights: message_formats.Lights = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Lights,
    )
    target: 'LightTarget' = proto.Field(
        proto.ENUM,
        number=2,
        enum='LightTarget',
    )


class LaserCommand(proto.Message):
    r"""LaserCommand sets the laser connected to a guest port, as
    LaserCtrl does.

    Attributes:
        laser (blueye.protocol.types.Laser):
            Laser intensity and modulation.
    """

    laser: message_formats.Laser = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Laser,
    )


class TiltStabilizationCommand(proto.Message):
    r"""TiltStabilizationCommand enables or disables camera tilt
    stabilization, as TiltStabilizationCtrl does.

    Attributes:
        state (blueye.protocol.types.TiltStabilizationState):
            The tilt stabilization state to set.
    """

    state: message_formats.TiltStabilizationState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.TiltStabilizationState,
    )


class CvModelStateCommand(proto.Message):
    r"""CvModelStateCommand starts or stops a computer vision model
    on the drone, as SetCvModelStateReq does.
    The instruction completes when the model reports the requested
    state.

    Attributes:
        package_id (str):
            The model package to start or stop, as listed
            in CvModelInfo.
        running (bool):
            True to start the model, false to stop it.
    """

    package_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    running: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class AnnotationCommand(proto.Message):
    r"""AnnotationCommand records an annotation in the dive log, as
    AnnotationCtrl does.

    Attributes:
        annotation (blueye.protocol.types.Annotation):
            The annotation to record. The drone sets the
            timestamp and the source.
    """

    annotation: message_formats.Annotation = proto.Field(
        proto.MESSAGE,
        number=1,
        message=message_formats.Annotation,
    )


class HeadingCommand(proto.Message):
    r"""HeadingCommand turns the drone to a heading and holds it with
    auto heading. It completes once the heading has settled.

    Attributes:
        heading (float):
            Target heading from north (deg, 0..360), or
            the turn when relative is set (deg, -180..180).
        relative (bool):
            True to turn by ``heading`` degrees from the current
            heading; positive is clockwise.
    """

    heading: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    relative: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class TransectCommand(proto.Message):
    r"""TransectCommand drives a straight line from the current
    position, like a waypoint the drone computes itself from a
    course and a distance.

    Attributes:
        course (float):
            Course relative to north (deg, 0..360).
        distance (float):
            Length of the line (m).
        speed_to_target (float):
            Desired speed over ground (m/s). The mission
            default when 0.
        depth_set_point (blueye.protocol.types.DepthSetPoint):
            Optional depth or altitude to hold along the
            line.
        circle_of_acceptance (float):
            Radius of acceptance at the end of the line
            (m). The mission default when 0.
    """

    course: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    distance: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    speed_to_target: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    depth_set_point: 'DepthSetPoint' = proto.Field(
        proto.MESSAGE,
        number=4,
        message='DepthSetPoint',
    )
    circle_of_acceptance: float = proto.Field(
        proto.FLOAT,
        number=5,
    )


class RelativeDepthCommand(proto.Message):
    r"""RelativeDepthCommand changes the depth by an amount from
    where the drone is when it starts.

    Attributes:
        depth_change (float):
            Change in depth (m); positive is deeper,
            negative shallower.
        speed_to_depth (float):
            Desired speed to the new depth (m/s). The
            mission default when 0.
    """

    depth_change: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    speed_to_depth: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class CruiseSpeedCommand(proto.Message):
    r"""CruiseSpeedCommand changes the cruise speed used by the
    following instructions of the mission.

    Attributes:
        cruise_speed (float):
            Desired surge speed (m/s). Must be greater
            than zero.
    """

    cruise_speed: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class SurveyCommand(proto.Message):
    r"""A SurveyCommand defines a survey (lawn-mower) pattern over a
    polygon area. The planner generates waypoints from the polygon +
    parameters and stores them in the waypoints field. The drone
    executes these pre-computed waypoints directly without
    re-running the survey algorithm. The polygon and parameters
    remain editable in the planner — regenerate waypoints when they
    change. Planners SHOULD validate that the polygon is simple
    (non-self-intersecting) before generating waypoints, as behavior
    is undefined for invalid polygons.

    Attributes:
        vertices (MutableSequence[blueye.protocol.types.LatLongPosition]):
            Polygon vertices defining the survey area
            boundary (decimal degrees). The polygon is
            implicitly closed: the last vertex connects back
            to the first. Clients MUST NOT repeat the first
            vertex at the end of the list. Vertices should
            be ordered clockwise when viewed from above. The
            boundary must form a simple polygon (no
            self-intersections). At least three distinct
            vertices are required.
        survey_line_heading (float):
            Survey line heading relative to north in degrees (0-360).
            NOTE: Unlike PathSegment.course_to_target (which uses
            radians), this field uses degrees to match compass
            convention. Convert radians before assigning.
        lane_spacing (float):
            Distance between parallel scan lines (m).
        turnaround_distance (float):
            Overshoot distance past polygon boundary at
            each turn (m).
        cruise_speed (float):
            Desired speed over ground during survey
            (m/s).
        circle_of_acceptance (float):
            Radius of acceptance circle for generated
            waypoints (m).
        depth_set_point (blueye.protocol.types.DepthSetPoint):
            Optional depth set point for all generated
            waypoints.
        reverse (bool):
            The planner generated the pattern in reverse,
            from its last scan line to its first. The
            waypoints are already in that order: the drone
            flies them as given, and the planner reads this
            back to rebuild the pattern.
        waypoints (MutableSequence[blueye.protocol.types.Waypoint]):
            Pre-computed waypoints generated by the
            planner from the polygon and parameters. The
            drone executes these directly. Individual
            waypoint parameters (speed, CoA, depth) can be
            tweaked after generation without modifying the
            survey shape. Regenerated automatically when
            polygon or survey parameters change.
        swath_width (float):
            Sensor swath width (m). When set with overlap_percent,
            overrides lane_spacing.
        overlap_percent (float):
            Desired overlap between adjacent scan lines (0-100%). Used
            with swath_width.
    """

    vertices: MutableSequence[message_formats.LatLongPosition] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=message_formats.LatLongPosition,
    )
    survey_line_heading: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    lane_spacing: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    turnaround_distance: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    cruise_speed: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    circle_of_acceptance: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    depth_set_point: 'DepthSetPoint' = proto.Field(
        proto.MESSAGE,
        number=7,
        message='DepthSetPoint',
    )
    reverse: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    waypoints: MutableSequence['Waypoint'] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message='Waypoint',
    )
    swath_width: float = proto.Field(
        proto.FLOAT,
        number=10,
    )
    overlap_percent: float = proto.Field(
        proto.FLOAT,
        number=11,
    )


class PathSegment(proto.Message):
    r"""Path segment used to describe segments of a mission as a line
    between to waypoints.

    Attributes:
        id (int):
            Path segment id starting at 0, -1 for
            inactive.
        speed_to_target (float):
            Desired speed over ground in (m/s).
        course_to_target (float):
            Course to target relative to north (rad) [-pi, pi].
        depth_speed (float):
            Desired speed in heave (m/s).
        horizontal_length (float):
            Horizontal length of the path segment (m).
        vertical_length (float):
            Vertical length of the path segment (m).
        from_wp_id (int):
            Id of the starting waypoint.
        to_wp_id (int):
            Id of the ending waypoint.
        duration_time (float):
            Estimated time it takes to complete given
            length and desired speed (s).
    """

    id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    speed_to_target: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    course_to_target: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    depth_speed: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    horizontal_length: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    vertical_length: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    from_wp_id: int = proto.Field(
        proto.UINT32,
        number=7,
    )
    to_wp_id: int = proto.Field(
        proto.UINT32,
        number=8,
    )
    duration_time: float = proto.Field(
        proto.FLOAT,
        number=9,
    )


class ReferenceAutoPilot(proto.Message):
    r"""Reference for the auto pilot when a mission is active.

    Attributes:
        instruction_type (blueye.protocol.types.InstructionType):
            Instruction type.
        active_instruction_id (int):
            Id of the active instruction.
        active_path_segment_id (int):
            Id of the active path segment.
        course_to_target (float):
            Course to the next waypoint from north (rad) [-pi, pi].
        speed_over_ground (float):
            Desired speed over ground (m/s).
        horizontal_distance_to_target (float):
            Horizontal distance to the next waypoint (m).
        circle_of_acceptance (float):
            Circle of acceptance to mark waypoint as
            visited (m).
        depth_set_point (float):
            Desired depth set point (m).
        heave_velocity (float):
            Desired heave velocity (m/s).
        vertical_distance_to_target (float):
            Vertical distance to the next waypoint (m).
        depth_zero_reference (blueye.protocol.types.DepthZeroReference):
            Indicates if depth is measured from the
            surface or seabed.
        time_to_complete (float):
            Estimated time to complete the instruction
            (s).
    """

    instruction_type: 'InstructionType' = proto.Field(
        proto.ENUM,
        number=1,
        enum='InstructionType',
    )
    active_instruction_id: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    active_path_segment_id: int = proto.Field(
        proto.UINT32,
        number=3,
    )
    course_to_target: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    speed_over_ground: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    horizontal_distance_to_target: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    circle_of_acceptance: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    depth_set_point: float = proto.Field(
        proto.FLOAT,
        number=8,
    )
    heave_velocity: float = proto.Field(
        proto.FLOAT,
        number=9,
    )
    vertical_distance_to_target: float = proto.Field(
        proto.FLOAT,
        number=10,
    )
    depth_zero_reference: 'DepthZeroReference' = proto.Field(
        proto.ENUM,
        number=11,
        enum='DepthZeroReference',
    )
    time_to_complete: float = proto.Field(
        proto.FLOAT,
        number=12,
    )


class MissionStatus(proto.Message):
    r"""Mission Status is used for showing the status of the mission.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        state (blueye.protocol.types.MissionState):
            State of the mission supervisor.
        time_elapsed (int):
            Time elapsed since mission started (s).
        estimated_time_to_complete (int):
            Estimated time to complete the mission (s).
        distance_to_complete (int):
            Distance left of the mission (m).
        completed_instruction_ids (MutableSequence[int]):
            Ids of the completed instructions, skipped
            ones included.
        total_number_of_instructions (int):
            Total number of instructions in the mission.
        completed_path_segment_ids (MutableSequence[int]):
            Ids of the completed path segments.
        total_number_of_path_segments (int):
            Total number of path segments in the mission.
        id (int):
            Mission id of the active mission.
        active_instruction_id (int):
            Id of the instruction that is running, not
            set when none.

            This field is a member of `oneof`_ ``_active_instruction_id``.
        revision (int):
            Revision of the loaded mission, see
            Mission.revision.
        failure_reason (str):
            Why the mission failed to load or start or
            was aborted by the drone.
        uuid (str):
            Mission.uuid of the loaded mission.
        last_outcome (blueye.protocol.types.MissionOutcome):
            How the last mission run ended. It stays when
            the mission is cleared or another one is loaded,
            is replaced when a run ends again, including one
            resumed after an abort, and is lost when the
            drone restarts.
        load_id (int):
            Mission.load_id of the loaded mission, 0 when none.
    """

    state: 'MissionState' = proto.Field(
        proto.ENUM,
        number=1,
        enum='MissionState',
    )
    time_elapsed: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    estimated_time_to_complete: int = proto.Field(
        proto.UINT32,
        number=3,
    )
    distance_to_complete: int = proto.Field(
        proto.UINT32,
        number=4,
    )
    completed_instruction_ids: MutableSequence[int] = proto.RepeatedField(
        proto.UINT32,
        number=5,
    )
    total_number_of_instructions: int = proto.Field(
        proto.UINT32,
        number=6,
    )
    completed_path_segment_ids: MutableSequence[int] = proto.RepeatedField(
        proto.UINT32,
        number=7,
    )
    total_number_of_path_segments: int = proto.Field(
        proto.UINT32,
        number=8,
    )
    id: int = proto.Field(
        proto.UINT32,
        number=9,
    )
    active_instruction_id: int = proto.Field(
        proto.UINT32,
        number=10,
        optional=True,
    )
    revision: int = proto.Field(
        proto.UINT32,
        number=11,
    )
    failure_reason: str = proto.Field(
        proto.STRING,
        number=12,
    )
    uuid: str = proto.Field(
        proto.STRING,
        number=13,
    )
    last_outcome: 'MissionOutcome' = proto.Field(
        proto.MESSAGE,
        number=14,
        message='MissionOutcome',
    )
    load_id: int = proto.Field(
        proto.UINT64,
        number=15,
    )


class MissionOutcome(proto.Message):
    r"""How a mission run ended, kept after the mission is cleared so
    a client that reconnects can tell.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        result (blueye.protocol.types.MissionResult):
            How the run ended.
        mission_id (int):
            Mission.id of the mission.
        mission_uuid (str):
            Mission.uuid of the mission.
        revision (int):
            Mission.revision when the run ended.
        instruction_id (int):
            Id of the instruction that was running when
            it ended, not set when none.

            This field is a member of `oneof`_ ``_instruction_id``.
        abort_reason (blueye.protocol.types.MissionAbortReason):
            Why the drone aborted the mission.
        reason (str):
            Why the drone aborted the mission, as text.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            When the run ended, by the drone's clock.
        skipped_instruction_ids (MutableSequence[int]):
            Ids of the instructions the run skipped.
        load_id (int):
            Mission.load_id of the mission.
    """

    result: 'MissionResult' = proto.Field(
        proto.ENUM,
        number=1,
        enum='MissionResult',
    )
    mission_id: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    mission_uuid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    revision: int = proto.Field(
        proto.UINT32,
        number=4,
    )
    instruction_id: int = proto.Field(
        proto.UINT32,
        number=5,
        optional=True,
    )
    abort_reason: 'MissionAbortReason' = proto.Field(
        proto.ENUM,
        number=6,
        enum='MissionAbortReason',
    )
    reason: str = proto.Field(
        proto.STRING,
        number=7,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    skipped_instruction_ids: MutableSequence[int] = proto.RepeatedField(
        proto.UINT32,
        number=9,
    )
    load_id: int = proto.Field(
        proto.UINT64,
        number=10,
    )


class InstructionResult(proto.Message):
    r"""Result of an instruction started with RunInstructionCtrl.

    Attributes:
        request_id (int):
            The request_id given to RunInstructionCtrl.
        instruction_id (int):
            Id of the instruction, as given by the
            client.
        state (blueye.protocol.types.InstructionResultState):
            Outcome so far.
        reason (str):
            Why the instruction was rejected, failed or
            was cancelled (optional).
    """

    request_id: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    instruction_id: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    state: 'InstructionResultState' = proto.Field(
        proto.ENUM,
        number=3,
        enum='InstructionResultState',
    )
    reason: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
