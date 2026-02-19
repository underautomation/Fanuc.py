import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import McspGrpVariableType as mcsp_grp_variable_type

class McspGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type MCSP_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mcsp_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def joglim_ovr(self) -> int:
		'''Value of variable $JOGLIM_OVR'''
		return self._instance.JoglimOvr

	@property
	def trqlim_flg(self) -> bool:
		'''Value of variable $TRQLIM_FLG'''
		return self._instance.TrqlimFlg

	@property
	def sv_ptlim(self) -> typing.List[int]:
		'''Value of variable $SV_PTLIM'''
		return self._instance.SvPtlim

	@property
	def org_ptlim(self) -> typing.List[int]:
		'''Value of variable $ORG_PTLIM'''
		return self._instance.OrgPtlim

	@property
	def org_rclmc(self) -> typing.List[int]:
		'''Value of variable $ORG_RCLMC'''
		return self._instance.OrgRclmc

	@property
	def reserve1(self) -> int:
		'''Value of variable $RESERVE1'''
		return self._instance.Reserve1

	@property
	def reserve2(self) -> int:
		'''Value of variable $RESERVE2'''
		return self._instance.Reserve2

	@property
	def reserve3(self) -> typing.List[int]:
		'''Value of variable $RESERVE3'''
		return self._instance.Reserve3

	@property
	def reserve4(self) -> typing.List[int]:
		'''Value of variable $RESERVE4'''
		return self._instance.Reserve4

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, McspGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
