import typing
from underautomation.fanuc.ftp.variables.cpidebug_variable_type import CpidebugVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CpdbgVariableType as cpdbg_variable_type

class CpdbgVariableType(GenericVariableType):
	'''Describes the Fanuc type CPDBG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cpdbg_variable_type()
		else:
			self._instance = _internal

	@property
	def output(self) -> bool:
		'''Value of variable $OUTPUT'''
		return self._instance.Output

	@property
	def cpidebug(self) -> CpidebugVariableType:
		'''Value of variable $CPIDEBUG'''
		return CpidebugVariableType(self._instance.Cpidebug)

	@property
	def cppdebug(self) -> CpidebugVariableType:
		'''Value of variable $CPPDEBUG'''
		return CpidebugVariableType(self._instance.Cppdebug)

	@property
	def midebug(self) -> CpidebugVariableType:
		'''Value of variable $MIDEBUG'''
		return CpidebugVariableType(self._instance.Midebug)

	@property
	def mpdebug(self) -> CpidebugVariableType:
		'''Value of variable $MPDEBUG'''
		return CpidebugVariableType(self._instance.Mpdebug)

	@property
	def mgdebug(self) -> CpidebugVariableType:
		'''Value of variable $MGDEBUG'''
		return CpidebugVariableType(self._instance.Mgdebug)

	@property
	def mfdebug(self) -> CpidebugVariableType:
		'''Value of variable $MFDEBUG'''
		return CpidebugVariableType(self._instance.Mfdebug)

	@property
	def simqstop(self) -> bool:
		'''Value of variable $SIMQSTOP'''
		return self._instance.Simqstop

	@property
	def keep(self) -> bool:
		'''Value of variable $KEEP'''
		return self._instance.Keep

	@property
	def path(self) -> str:
		'''Value of variable $PATH'''
		return self._instance.Path

	@property
	def extra1(self) -> int:
		'''Value of variable $EXTRA1'''
		return self._instance.Extra1

	@property
	def extra2(self) -> int:
		'''Value of variable $EXTRA2'''
		return self._instance.Extra2

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CpdbgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
