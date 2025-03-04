import typing
from underautomation.fanuc.ftp.variables.tbj_acc_variable_type import TbjAccVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TbjcfgVariableType as tbjcfg_variable_type

class TbjcfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbjcfg_variable_type()
		else:
			self._instance = _internal
	@property
	def group_mask(self) -> int:
		return self._instance.GroupMask
	@property
	def mb_conflict(self) -> int:
		return self._instance.MbConflict
	@property
	def mb_required(self) -> int:
		return self._instance.MbRequired
	@property
	def debug(self) -> int:
		return self._instance.Debug
	@property
	def update_time(self) -> int:
		return self._instance.UpdateTime
	@property
	def tbj_select(self) -> int:
		return self._instance.TbjSelect
	@property
	def tbj_stat(self) -> typing.List[int]:
		return self._instance.TbjStat
	@property
	def tj(self) -> typing.List[TbjAccVariableType]:
		return [TbjAccVariableType(x) for x in self._instance.Tj]
	@property
	def jerk_ctrl(self) -> int:
		return self._instance.JerkCtrl
	@property
	def motn_inf(self) -> int:
		return self._instance.MotnInf
	@property
	def tbj_debug(self) -> int:
		return self._instance.TbjDebug
	@property
	def hand_vb(self) -> typing.List[float]:
		return self._instance.HandVb
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
