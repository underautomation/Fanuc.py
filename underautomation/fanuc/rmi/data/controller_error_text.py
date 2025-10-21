import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import ControllerErrorText as controller_error_text

class ControllerErrorText(RmiResponseBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = controller_error_text()
		else:
			self._instance = _internal
	@property
	def error_data(self) -> str:
		return self._instance.ErrorData
	@error_data.setter
	def error_data(self, value: str):
		self._instance.ErrorData = value
