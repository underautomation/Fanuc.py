import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import RmiSequenceResponse as rmi_sequence_response

class RmiSequenceResponse(RmiResponseBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_sequence_response()
		else:
			self._instance = _internal
	@property
	def sequence_id(self) -> int:
		return self._instance.SequenceId
	@sequence_id.setter
	def sequence_id(self, value: int):
		self._instance.SequenceId = value
