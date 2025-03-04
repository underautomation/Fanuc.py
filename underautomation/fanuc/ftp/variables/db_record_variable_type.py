import typing
from underautomation.fanuc.common.xyz_position import XYZPosition
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DbRecordVariableType as db_record_variable_type

class DbRecordVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = db_record_variable_type()
		else:
			self._instance = _internal
	@property
	def cpos(self) -> XYZPosition:
		return XYZPosition(None, None, None, self._instance.Cpos)
	@property
	def lpos(self) -> XYZPosition:
		return XYZPosition(None, None, None, self._instance.Lpos)
	@property
	def dpos_dst(self) -> float:
		return self._instance.DposDst
	@property
	def ldpos_dst(self) -> float:
		return self._instance.LdposDst
	@property
	def line_num(self) -> int:
		return self._instance.LineNum
	@property
	def once_dc(self) -> bool:
		return self._instance.OnceDc
	@property
	def cross(self) -> int:
		return self._instance.Cross
	@property
	def task_id(self) -> int:
		return self._instance.TaskId
	@property
	def enabled_tim(self) -> int:
		return self._instance.EnabledTim
	@property
	def trigger_tim(self) -> int:
		return self._instance.TriggerTim
	@property
	def paused_time(self) -> int:
		return self._instance.PausedTime
	@property
	def returned_ti(self) -> int:
		return self._instance.ReturnedTi
	@property
	def mmr_status(self) -> str:
		return self._instance.MmrStatus
	@property
	def cre_newmon(self) -> bool:
		return self._instance.CreNewmon
	@property
	def signal_act(self) -> bool:
		return self._instance.SignalAct
	@property
	def last_act(self) -> bool:
		return self._instance.LastAct
	@property
	def pd(self) -> XYZPosition:
		return XYZPosition(None, None, None, self._instance.Pd)
	@property
	def pc(self) -> XYZPosition:
		return XYZPosition(None, None, None, self._instance.Pc)
	@property
	def pn_at(self) -> XYZPosition:
		return XYZPosition(None, None, None, self._instance.PnAt)
	@property
	def pd2(self) -> float:
		return self._instance.Pd2
	@property
	def pc2(self) -> float:
		return self._instance.Pc2
	@property
	def pt(self) -> float:
		return self._instance.Pt
	@property
	def pd_dot_pc(self) -> float:
		return self._instance.PdDotPc
	@property
	def line_dst(self) -> float:
		return self._instance.LineDst
	@property
	def p_num(self) -> int:
		return self._instance.PNum
	@property
	def go_away(self) -> bool:
		return self._instance.GoAway
	@property
	def motion_comp(self) -> bool:
		return self._instance.MotionComp
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
