import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import RmiTimedResponse as rmi_timed_response

class RmiTimedResponse(RmiResponseBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_timed_response()
		else:
			self._instance = _internal
	@property
	def time_tag(self) -> int:
		return self._instance.TimeTag
	@time_tag.setter
	def time_tag(self, value: int):
		self._instance.TimeTag = value
