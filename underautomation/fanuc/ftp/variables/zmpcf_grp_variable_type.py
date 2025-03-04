import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ZmpcfGrpVariableType as zmpcf_grp_variable_type

class ZmpcfGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = zmpcf_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def zmp_enb(self) -> int:
		return self._instance.ZmpEnb
	@property
	def zmp_dmy_lnk(self) -> typing.List[float]:
		return self._instance.ZmpDmyLnk
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
