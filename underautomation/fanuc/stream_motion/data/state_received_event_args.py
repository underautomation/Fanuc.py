import typing
from underautomation.fanuc.stream_motion.data.state_packet import StatePacket
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import StateReceivedEventArgs as state_received_event_args

class StateReceivedEventArgs:
	def __init__(self, state: StatePacket, _internal = 0):
		if(_internal == 0):
			self._instance = state_received_event_args(state)
		else:
			self._instance = _internal
	@property
	def state(self) -> StatePacket:
		return StatePacket(self._instance.State)
