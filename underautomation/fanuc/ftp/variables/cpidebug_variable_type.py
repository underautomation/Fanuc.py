import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CpidebugVariableType as cpidebug_variable_type

class CpidebugVariableType(GenericVariableType):
	'''Describes the Fanuc type $CPIDEBUG'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cpidebug_variable_type()
		else:
			self._instance = _internal

	@property
	def output(self) -> int:
		'''Value of variable $OUTPUT'''
		return self._instance.Output

	@property
	def filename(self) -> str:
		'''Value of variable $FILENAME'''
		return self._instance.Filename

	@property
	def group_mask(self) -> int:
		'''Value of variable $GROUP_MASK'''
		return self._instance.GroupMask

	@property
	def debugmask(self) -> int:
		'''Value of variable $DEBUGMASK'''
		return self._instance.Debugmask

	@property
	def maxdata(self) -> int:
		'''Value of variable $MAXDATA'''
		return self._instance.Maxdata

	@property
	def count(self) -> int:
		'''Value of variable $COUNT'''
		return self._instance.Count

	@property
	def tail(self) -> int:
		'''Value of variable $TAIL'''
		return self._instance.Tail

	@property
	def bufexist(self) -> bool:
		'''Value of variable $BUFEXIST'''
		return self._instance.Bufexist

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CpidebugVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
