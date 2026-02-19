import typing
from underautomation.fanuc.ftp.variables.tbc_acc_variable_type import TbcAccVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TbccfgVariableType as tbccfg_variable_type

class TbccfgVariableType(GenericVariableType):
	'''Describes the Fanuc type TBCCFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbccfg_variable_type()
		else:
			self._instance = _internal

	@property
	def group_mask(self) -> int:
		'''Value of variable $GROUP_MASK'''
		return self._instance.GroupMask

	@property
	def mb_conflict(self) -> int:
		'''Value of variable $MB_CONFLICT'''
		return self._instance.MbConflict

	@property
	def mb_required(self) -> int:
		'''Value of variable $MB_REQUIRED'''
		return self._instance.MbRequired

	@property
	def debug(self) -> int:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def tbc_stat(self) -> typing.List[int]:
		'''Value of variable $TBC_STAT'''
		return self._instance.TbcStat

	@property
	def tc(self) -> typing.List[TbcAccVariableType]:
		'''Value of variable $TC'''
		return [TbcAccVariableType(x) for x in self._instance.Tc]

	@property
	def tbc_debug(self) -> int:
		'''Value of variable $TBC_DEBUG'''
		return self._instance.TbcDebug

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TbccfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
