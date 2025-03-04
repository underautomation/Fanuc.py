import typing
from underautomation.fanuc.ftp.variables.generic_field import GenericField
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ArrayElement as array_element

class ArrayElement(GenericField):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = array_element()
		else:
			self._instance = _internal
	@property
	def access(self) -> str:
		return self._instance.Access
	@property
	def type(self) -> str:
		return self._instance.Type
	@property
	def is_register(self) -> bool:
		return self._instance.IsRegister
	@property
	def string_length(self) -> int:
		return self._instance.StringLength
	@property
	def name(self) -> str:
		return self._instance.Name
