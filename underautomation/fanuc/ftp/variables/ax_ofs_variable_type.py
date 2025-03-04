import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AxOfsVariableType as ax_ofs_variable_type

class AxOfsVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ax_ofs_variable_type()
		else:
			self._instance = _internal
	@property
	def x(self) -> float:
		return self._instance.X
	@property
	def y(self) -> float:
		return self._instance.Y
	@property
	def z(self) -> float:
		return self._instance.Z
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
