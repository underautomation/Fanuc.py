from __future__ import annotations
import typing
from UnderAutomation.Fanuc.StreamMotion.Data import SessionEventArgs as session_event_args

class SessionEventArgs:
	'''Arguments of the session events'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = session_event_args()
		else:
			self._instance = _internal

	@property
	def session_index(self) -> int:
		'''Index of the session since the connection (starts at 1)'''
		return self._instance.SessionIndex

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SessionEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
