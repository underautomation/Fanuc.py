import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TimerVariableType as timer_variable_type

class TimerVariableType(GenericVariableType):
	'''Describes the Fanuc type TIMER_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = timer_variable_type()
		else:
			self._instance = _internal

	@property
	def comment(self) -> str:
		'''Value of variable $COMMENT'''
		return self._instance.Comment

	@property
	def timer_val(self) -> int:
		'''Value of variable $TIMER_VAL'''
		return self._instance.TimerVal

	@property
	def str_ept_idx(self) -> int:
		'''Value of variable $STR_EPT_IDX'''
		return self._instance.StrEptIdx

	@property
	def str_lin_num(self) -> int:
		'''Value of variable $STR_LIN_NUM'''
		return self._instance.StrLinNum

	@property
	def end_ept_idx(self) -> int:
		'''Value of variable $END_EPT_IDX'''
		return self._instance.EndEptIdx

	@property
	def end_lin_num(self) -> int:
		'''Value of variable $END_LIN_NUM'''
		return self._instance.EndLinNum

	@property
	def tid_num(self) -> int:
		'''Value of variable $TID_NUM'''
		return self._instance.TidNum

	@property
	def dummy13(self) -> int:
		'''Value of variable $DUMMY13'''
		return self._instance.Dummy13

	@property
	def ps_overflow(self) -> int:
		'''Value of variable $PS_OVERFLOW'''
		return self._instance.PsOverflow

	@property
	def overflow(self) -> bool:
		'''Value of variable $OVERFLOW'''
		return self._instance.Overflow

	@property
	def flag_type(self) -> int:
		'''Value of variable $FLAG_TYPE'''
		return self._instance.FlagType

	@property
	def flag_idx(self) -> int:
		'''Value of variable $FLAG_IDX'''
		return self._instance.FlagIdx

	@property
	def glb_tmr_enb(self) -> bool:
		'''Value of variable $GLB_TMR_ENB'''
		return self._instance.GlbTmrEnb

	@property
	def glb_tmr_str(self) -> bool:
		'''Value of variable $GLB_TMR_STR'''
		return self._instance.GlbTmrStr

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TimerVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
