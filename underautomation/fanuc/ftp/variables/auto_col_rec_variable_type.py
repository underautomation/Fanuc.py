import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AutoColRecVariableType as auto_col_rec_variable_type

class AutoColRecVariableType(GenericVariableType):
	'''Describes the Fanuc type AUTO_COL_REC'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = auto_col_rec_variable_type()
		else:
			self._instance = _internal

	@property
	def reg_index(self) -> int:
		'''Value of variable REG_INDEX'''
		return self._instance.RegIndex

	@property
	def do_index(self) -> int:
		'''Value of variable DO_INDEX'''
		return self._instance.DoIndex

	@property
	def err_do_index(self) -> int:
		'''Value of variable ERR_DO_INDEX'''
		return self._instance.ErrDoIndex

	@property
	def recovery_tsk(self) -> str:
		'''Value of variable RECOVERY_TSK'''
		return self._instance.RecoveryTsk

	@property
	def err_delay(self) -> int:
		'''Value of variable ERR_DELAY'''
		return self._instance.ErrDelay

	@property
	def reset_delay(self) -> int:
		'''Value of variable RESET_DELAY'''
		return self._instance.ResetDelay

	@property
	def use_rec_tsk(self) -> bool:
		'''Value of variable USE_REC_TSK'''
		return self._instance.UseRecTsk

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AutoColRecVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
