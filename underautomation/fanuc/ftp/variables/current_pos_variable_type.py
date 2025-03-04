import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CurrentPosVariableType as current_pos_variable_type

class CurrentPosVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_pos_variable_type()
		else:
			self._instance = _internal
	@property
	def posxf(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.Posxf)
	@property
	def ext1(self) -> float:
		return self._instance.Ext1
	@property
	def ext2(self) -> float:
		return self._instance.Ext2
	@property
	def ext3(self) -> float:
		return self._instance.Ext3
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
