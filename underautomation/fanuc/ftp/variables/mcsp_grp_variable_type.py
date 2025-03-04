import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import McspGrpVariableType as mcsp_grp_variable_type

class McspGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mcsp_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def joglim_ovr(self) -> int:
		return self._instance.JoglimOvr
	@property
	def trqlim_flg(self) -> bool:
		return self._instance.TrqlimFlg
	@property
	def sv_ptlim(self) -> typing.List[int]:
		return self._instance.SvPtlim
	@property
	def org_ptlim(self) -> typing.List[int]:
		return self._instance.OrgPtlim
	@property
	def org_rclmc(self) -> typing.List[int]:
		return self._instance.OrgRclmc
	@property
	def reserve1(self) -> int:
		return self._instance.Reserve1
	@property
	def reserve2(self) -> int:
		return self._instance.Reserve2
	@property
	def reserve3(self) -> typing.List[int]:
		return self._instance.Reserve3
	@property
	def reserve4(self) -> typing.List[int]:
		return self._instance.Reserve4
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
