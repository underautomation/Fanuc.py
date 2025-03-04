import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AutoColRecVariableType as auto_col_rec_variable_type

class AutoColRecVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = auto_col_rec_variable_type()
		else:
			self._instance = _internal
	@property
	def reg_index(self) -> int:
		return self._instance.RegIndex
	@property
	def do_index(self) -> int:
		return self._instance.DoIndex
	@property
	def err_do_index(self) -> int:
		return self._instance.ErrDoIndex
	@property
	def recovery_tsk(self) -> str:
		return self._instance.RecoveryTsk
	@property
	def err_delay(self) -> int:
		return self._instance.ErrDelay
	@property
	def reset_delay(self) -> int:
		return self._instance.ResetDelay
	@property
	def use_rec_tsk(self) -> bool:
		return self._instance.UseRecTsk
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
