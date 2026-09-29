from __future__ import annotations
import typing
from underautomation.fanuc.stream_motion.data.session_end_reason import SessionEndReason
from underautomation.fanuc.stream_motion.data.session_event_args import SessionEventArgs
from UnderAutomation.Fanuc.StreamMotion.Data import SessionEndedEventArgs as session_ended_event_args
from UnderAutomation.Fanuc.StreamMotion.Data import SessionEndReason as session_end_reason

class SessionEndedEventArgs(SessionEventArgs):
	'''Arguments of the SessionEnded event'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = session_ended_event_args()
		else:
			self._instance = _internal

	@property
	def reason(self) -> SessionEndReason:
		'''Reason of the end of the session'''
		return SessionEndReason(int(self._instance.Reason))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SessionEndedEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
