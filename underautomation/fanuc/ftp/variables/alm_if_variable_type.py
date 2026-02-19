import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AlmIfVariableType as alm_if_variable_type

class AlmIfVariableType(GenericVariableType):
	'''Describes the Fanuc type ALM_IF_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = alm_if_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def last_alm(self) -> str:
		'''Value of variable $LAST_ALM'''
		return self._instance.LastAlm

	@property
	def last_ualm(self) -> str:
		'''Value of variable $LAST_UALM'''
		return self._instance.LastUalm

	@property
	def kalm_max(self) -> int:
		'''Value of variable $KALM_MAX'''
		return self._instance.KalmMax

	@property
	def ldebug(self) -> typing.List[int]:
		'''Value of variable $LDEBUG'''
		return self._instance.Ldebug

	@property
	def prog_stat(self) -> str:
		'''Value of variable $PROG_STAT'''
		return self._instance.ProgStat

	@property
	def curr_prog(self) -> str:
		'''Value of variable $CURR_PROG'''
		return self._instance.CurrProg

	@property
	def curr_line(self) -> int:
		'''Value of variable $CURR_LINE'''
		return self._instance.CurrLine

	@property
	def curr_stat(self) -> str:
		'''Value of variable $CURR_STAT'''
		return self._instance.CurrStat

	@property
	def last_cause(self) -> str:
		'''Value of variable $LAST_CAUSE'''
		return self._instance.LastCause

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AlmIfVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
