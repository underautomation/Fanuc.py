import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import RmiResponseBase as rmi_response_base

class RmiResponseBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_response_base()
		else:
			self._instance = _internal
	@property
	def error_id(self) -> int:
		return self._instance.ErrorId
	@error_id.setter
	def error_id(self, value: int):
		self._instance.ErrorId = value
