import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GrsmtGrpVariableType as grsmt_grp_variable_type

class GrsmtGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = grsmt_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def grv_sw(self) -> int:
		return self._instance.GrvSw
	@property
	def grv_param(self) -> float:
		return self._instance.GrvParam
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
