import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import UFrameUToolNumbers as u_frame_u_tool_numbers

class UFrameUToolNumbers(RmiResponseBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = u_frame_u_tool_numbers()
		else:
			self._instance = _internal
	@property
	def u_frame_number(self) -> int:
		return self._instance.UFrameNumber
	@u_frame_number.setter
	def u_frame_number(self, value: int):
		self._instance.UFrameNumber = value
	@property
	def u_tool_number(self) -> int:
		return self._instance.UToolNumber
	@u_tool_number.setter
	def u_tool_number(self, value: int):
		self._instance.UToolNumber = value
