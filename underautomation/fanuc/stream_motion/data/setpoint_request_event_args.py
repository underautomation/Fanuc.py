from __future__ import annotations
import typing
from underautomation.fanuc.stream_motion.data.stream_motion_status import StreamMotionStatus
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.common.xyzwpr_position import XYZWPRPosition
from UnderAutomation.Fanuc.StreamMotion.Data import SetpointRequestEventArgs as setpoint_request_event_args

class SetpointRequestEventArgs:
	'''Arguments of the SetpointRequested event. Call set_joints(), set_cartesian() or hold() to give the next position to send. The object is only valid during the call of the event handler.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = setpoint_request_event_args()
		else:
			self._instance = _internal

	def set_joints(self, position: JointsPosition) -> None:
		'''Gives the next joint position to send. The callback streaming must be in joint format.

		:param position: Joint position in degrees (mm for linear axes)
		'''
		self._instance.SetJoints(position._instance if position else None)

	def set_cartesian(self, position: XYZWPRPosition) -> None:
		'''Gives the next Cartesian position to send (flange center in the world frame). The callback streaming must be in Cartesian format. Extended axes values are used when the position is an ExtendedCartesianPosition, otherwise they are 0.

		:param position: Cartesian position
		'''
		self._instance.SetCartesian(position._instance if position else None)

	def hold(self) -> None:
		'''Keeps the last position. If the robot is moving, it stops smoothly.'''
		self._instance.Hold()

	@property
	def status(self) -> StreamMotionStatus:
		'''Last status received from the robot'''
		return StreamMotionStatus(self._instance.Status)

	@property
	def cycle_index(self) -> int:
		'''Index of the requested position since the start of the callback streaming (starts at 0)'''
		return self._instance.CycleIndex

	@property
	def time(self) -> float:
		'''Time of the requested position since the start of the callback streaming, in seconds (CycleIndex x cycle time)'''
		return self._instance.Time

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SetpointRequestEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
