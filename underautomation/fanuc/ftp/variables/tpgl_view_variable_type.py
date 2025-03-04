import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TpglViewVariableType as tpgl_view_variable_type

class TpglViewVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpgl_view_variable_type()
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
	def wz(self) -> float:
		return self._instance.Wz
	@property
	def p(self) -> float:
		return self._instance.P
	@property
	def r(self) -> float:
		return self._instance.R
	@property
	def camera(self) -> int:
		return self._instance.Camera
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
