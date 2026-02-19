import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VcrsmCfgVariableType as vcrsm_cfg_variable_type

class VcrsmCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type VCRSM_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcrsm_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def step_num(self) -> int:
		'''Value of variable $STEP_NUM'''
		return self._instance.StepNum

	@property
	def is_started(self) -> bool:
		'''Value of variable $IS_STARTED'''
		return self._instance.IsStarted

	@property
	def cur_prog(self) -> str:
		'''Value of variable $CUR_PROG'''
		return self._instance.CurProg

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VcrsmCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
