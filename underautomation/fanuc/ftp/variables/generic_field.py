import typing
# Circular dependencies  : GenericValue
from underautomation.fanuc.ftp.variables.generic_value import GenericValue
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GenericField as generic_field

class GenericField(GenericValue):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_field()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def access(self) -> str:
		return self._instance.Access
	@property
	def type(self) -> str:
		return self._instance.Type
	@type.setter
	def type(self, value: str):
		self._instance.Type = value
	@property
	def is_register(self) -> bool:
		return self._instance.IsRegister
	@property
	def string_length(self) -> int:
		return self._instance.StringLength
	@property
	def dimension1(self) -> int:
		return self._instance.Dimension1
	@property
	def dimension2(self) -> int:
		return self._instance.Dimension2
