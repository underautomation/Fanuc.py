import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CfcfgVariableType as cfcfg_variable_type

class CfcfgVariableType(GenericVariableType):
	'''Describes the Fanuc type CFCFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cfcfg_variable_type()
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
	def comp_switch(self) -> int:
		'''Value of variable $COMP_SWITCH'''
		return self._instance.CompSwitch

	@property
	def max_nsets(self) -> int:
		'''Value of variable $MAX_NSETS'''
		return self._instance.MaxNsets

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CfcfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
