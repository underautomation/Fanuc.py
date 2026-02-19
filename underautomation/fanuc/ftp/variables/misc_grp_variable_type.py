import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MiscGrpVariableType as misc_grp_variable_type

class MiscGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type MISC_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = misc_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def hpd_trq(self) -> typing.List[float]:
		'''Value of variable $HPD_TRQ'''
		return self._instance.HpdTrq

	@property
	def dstb_max(self) -> typing.List[int]:
		'''Value of variable $DSTB_MAX'''
		return self._instance.DstbMax

	@property
	def dstb_min(self) -> typing.List[int]:
		'''Value of variable $DSTB_MIN'''
		return self._instance.DstbMin

	@property
	def dstb_maxenb(self) -> typing.List[bool]:
		'''Value of variable $DSTB_MAXENB'''
		return self._instance.DstbMaxenb

	@property
	def dstb_minenb(self) -> typing.List[bool]:
		'''Value of variable $DSTB_MINENB'''
		return self._instance.DstbMinenb

	@property
	def dstb_excess(self) -> bool:
		'''Value of variable $DSTB_EXCESS'''
		return self._instance.DstbExcess

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MiscGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
