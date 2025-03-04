import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TimerVariableType as timer_variable_type

class TimerVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = timer_variable_type()
		else:
			self._instance = _internal
	@property
	def comment(self) -> str:
		return self._instance.Comment
	@property
	def timer_val(self) -> int:
		return self._instance.TimerVal
	@property
	def str_ept_idx(self) -> int:
		return self._instance.StrEptIdx
	@property
	def str_lin_num(self) -> int:
		return self._instance.StrLinNum
	@property
	def end_ept_idx(self) -> int:
		return self._instance.EndEptIdx
	@property
	def end_lin_num(self) -> int:
		return self._instance.EndLinNum
	@property
	def tid_num(self) -> int:
		return self._instance.TidNum
	@property
	def dummy13(self) -> int:
		return self._instance.Dummy13
	@property
	def ps_overflow(self) -> int:
		return self._instance.PsOverflow
	@property
	def overflow(self) -> bool:
		return self._instance.Overflow
	@property
	def flag_type(self) -> int:
		return self._instance.FlagType
	@property
	def flag_idx(self) -> int:
		return self._instance.FlagIdx
	@property
	def glb_tmr_enb(self) -> bool:
		return self._instance.GlbTmrEnb
	@property
	def glb_tmr_str(self) -> bool:
		return self._instance.GlbTmrStr
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
