import typing
from underautomation.fanuc.common.xyz_position import XYZPosition
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import XfVariableType as xf_variable_type

class XfVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = xf_variable_type()
		else:
			self._instance = _internal
	@property
	def n(self) -> XYZPosition:
		return XYZPosition(None, None, None, self._instance.N)
	@property
	def o(self) -> XYZPosition:
		return XYZPosition(None, None, None, self._instance.O)
	@property
	def a(self) -> XYZPosition:
		return XYZPosition(None, None, None, self._instance.A)
	@property
	def l(self) -> XYZPosition:
		return XYZPosition(None, None, None, self._instance.L)
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
