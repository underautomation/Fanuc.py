import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MorGrpSvVariableType as mor_grp_sv_variable_type

class MorGrpSvVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mor_grp_sv_variable_type()
		else:
			self._instance = _internal
	@property
	def cur_sv_ang(self) -> typing.List[float]:
		return self._instance.CurSvAng
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
