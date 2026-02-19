import typing
from underautomation.fanuc.stream_motion.data.state_packet import StatePacket
from UnderAutomation.Fanuc.StreamMotion.Data import StateReceivedEventArgs as state_received_event_args

class StateReceivedEventArgs:
	'''Event arguments for state received events'''
	def __init__(self, state: StatePacket, _internal = 0):
		'''Creates a new instance of StateReceivedEventArgs

		:param state: The state packet received from the robot
		'''
		if(_internal == 0):
			self._instance = state_received_event_args(state)
		else:
			self._instance = _internal

	@property
	def state(self) -> StatePacket:
		'''The state packet received from the robot'''
		return StatePacket(self._instance.State)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StateReceivedEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
