import typing
from underautomation.fanuc.ftp.variables.tbj_acc_variable_type import TbjAccVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TbjcfgVariableType as tbjcfg_variable_type

class TbjcfgVariableType(GenericVariableType):
	'''Describes the Fanuc type TBJCFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbjcfg_variable_type()
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
	def update_time(self) -> int:
		'''Value of variable $UPDATE_TIME'''
		return self._instance.UpdateTime

	@property
	def tbj_select(self) -> int:
		'''Value of variable $TBJ_SELECT'''
		return self._instance.TbjSelect

	@property
	def tbj_stat(self) -> typing.List[int]:
		'''Value of variable $TBJ_STAT'''
		return self._instance.TbjStat

	@property
	def tj(self) -> typing.List[TbjAccVariableType]:
		'''Value of variable $TJ'''
		return [TbjAccVariableType(x) for x in self._instance.Tj]

	@property
	def jerk_ctrl(self) -> int:
		'''Value of variable $JERK_CTRL'''
		return self._instance.JerkCtrl

	@property
	def motn_inf(self) -> int:
		'''Value of variable $MOTN_INF'''
		return self._instance.MotnInf

	@property
	def tbj_debug(self) -> int:
		'''Value of variable $TBJ_DEBUG'''
		return self._instance.TbjDebug

	@property
	def hand_vb(self) -> typing.List[float]:
		'''Value of variable $HAND_VB'''
		return self._instance.HandVb

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TbjcfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
