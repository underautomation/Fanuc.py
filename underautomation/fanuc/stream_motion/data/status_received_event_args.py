from __future__ import annotations
import typing
from underautomation.fanuc.stream_motion.data.stream_motion_status import StreamMotionStatus
from UnderAutomation.Fanuc.StreamMotion.Data import StatusReceivedEventArgs as status_received_event_args

class StatusReceivedEventArgs:
	'''Arguments of the StatusReceived event'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = status_received_event_args()
		else:
			self._instance = _internal

	@property
	def status(self) -> StreamMotionStatus:
		'''Last status received from the robot'''
		__r = self._instance.Status
		return None if __r is None else StreamMotionStatus(__r)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StatusReceivedEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
