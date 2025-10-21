import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi import RmiException as rmi_exception

class RmiException:
	def __init__(self, message: str, inner: typing.Any, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_exception(message, inner)
		else:
			self._instance = _internal
	@property
	def error_id(self) -> int:
		return self._instance.ErrorId
