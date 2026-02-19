import typing
from underautomation.fanuc.common.xyz_position import XYZPosition
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DbRecordVariableType as db_record_variable_type

class DbRecordVariableType(GenericVariableType):
	'''Describes the Fanuc type DB_RECORD_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = db_record_variable_type()
		else:
			self._instance = _internal

	@property
	def cpos(self) -> XYZPosition:
		'''Value of variable $CPOS'''
		return XYZPosition(None, None, None, self._instance.Cpos)

	@property
	def lpos(self) -> XYZPosition:
		'''Value of variable $LPOS'''
		return XYZPosition(None, None, None, self._instance.Lpos)

	@property
	def dpos_dst(self) -> float:
		'''Value of variable $DPOS_DST'''
		return self._instance.DposDst

	@property
	def ldpos_dst(self) -> float:
		'''Value of variable $LDPOS_DST'''
		return self._instance.LdposDst

	@property
	def line_num(self) -> int:
		'''Value of variable $LINE_NUM'''
		return self._instance.LineNum

	@property
	def once_dc(self) -> bool:
		'''Value of variable $ONCE_DC'''
		return self._instance.OnceDc

	@property
	def cross(self) -> int:
		'''Value of variable $CROSS'''
		return self._instance.Cross

	@property
	def task_id(self) -> int:
		'''Value of variable $TASK_ID'''
		return self._instance.TaskId

	@property
	def enabled_tim(self) -> int:
		'''Value of variable $ENABLED_TIM'''
		return self._instance.EnabledTim

	@property
	def trigger_tim(self) -> int:
		'''Value of variable $TRIGGER_TIM'''
		return self._instance.TriggerTim

	@property
	def paused_time(self) -> int:
		'''Value of variable $PAUSED_TIME'''
		return self._instance.PausedTime

	@property
	def returned_ti(self) -> int:
		'''Value of variable $RETURNED_TI'''
		return self._instance.ReturnedTi

	@property
	def mmr_status(self) -> str:
		'''Value of variable $MMR_STATUS'''
		return self._instance.MmrStatus

	@property
	def cre_newmon(self) -> bool:
		'''Value of variable $CRE_NEWMON'''
		return self._instance.CreNewmon

	@property
	def signal_act(self) -> bool:
		'''Value of variable $SIGNAL_ACT'''
		return self._instance.SignalAct

	@property
	def last_act(self) -> bool:
		'''Value of variable $LAST_ACT'''
		return self._instance.LastAct

	@property
	def pd(self) -> XYZPosition:
		'''Value of variable $PD'''
		return XYZPosition(None, None, None, self._instance.Pd)

	@property
	def pc(self) -> XYZPosition:
		'''Value of variable $PC'''
		return XYZPosition(None, None, None, self._instance.Pc)

	@property
	def pn_at(self) -> XYZPosition:
		'''Value of variable $PN_AT'''
		return XYZPosition(None, None, None, self._instance.PnAt)

	@property
	def pd2(self) -> float:
		'''Value of variable $PD2'''
		return self._instance.Pd2

	@property
	def pc2(self) -> float:
		'''Value of variable $PC2'''
		return self._instance.Pc2

	@property
	def pt(self) -> float:
		'''Value of variable $PT'''
		return self._instance.Pt

	@property
	def pd_dot_pc(self) -> float:
		'''Value of variable $PD_DOT_PC'''
		return self._instance.PdDotPc

	@property
	def line_dst(self) -> float:
		'''Value of variable $LINE_DST'''
		return self._instance.LineDst

	@property
	def p_num(self) -> int:
		'''Value of variable $P_NUM'''
		return self._instance.PNum

	@property
	def go_away(self) -> bool:
		'''Value of variable $GO_AWAY'''
		return self._instance.GoAway

	@property
	def motion_comp(self) -> bool:
		'''Value of variable $MOTION_COMP'''
		return self._instance.MotionComp

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DbRecordVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
