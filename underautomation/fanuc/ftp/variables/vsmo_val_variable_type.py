import typing
from underautomation.fanuc.ftp.variables.position_variable_type import PositionVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VsmoValVariableType as vsmo_val_variable_type

class VsmoValVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vsmo_val_variable_type()
		else:
			self._instance = _internal
	@property
	def position(self) -> PositionVariableType:
		return PositionVariableType(self._instance.Position)
	@property
	def speed(self) -> PositionVariableType:
		return PositionVariableType(self._instance.Speed)
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
