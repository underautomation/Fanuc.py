import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MndspMstVariableType as mndsp_mst_variable_type

class MndspMstVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mndsp_mst_variable_type()
		else:
			self._instance = _internal
	@property
	def disp_enable(self) -> bool:
		return self._instance.DispEnable
	@property
	def disp_edcmd(self) -> bool:
		return self._instance.DispEdcmd
	@property
	def disp_inauto(self) -> bool:
		return self._instance.DispInauto
	@property
	def disp_rsmdis(self) -> bool:
		return self._instance.DispRsmdis
	@property
	def disp_is_on(self) -> bool:
		return self._instance.DispIsOn
	@property
	def mode_grp(self) -> typing.List[int]:
		return self._instance.ModeGrp
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
