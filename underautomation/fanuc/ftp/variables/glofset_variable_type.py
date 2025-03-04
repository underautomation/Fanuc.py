import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GlofsetVariableType as glofset_variable_type

class GlofsetVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = glofset_variable_type()
		else:
			self._instance = _internal
	@property
	def numfiles(self) -> int:
		return self._instance.Numfiles
	@property
	def attrptr(self) -> int:
		return self._instance.Attrptr
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
