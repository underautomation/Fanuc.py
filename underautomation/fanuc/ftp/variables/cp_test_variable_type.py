import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CpTestVariableType as cp_test_variable_type

class CpTestVariableType(GenericVariableType):
	'''Describes the Fanuc type $CP_TEST'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cp_test_variable_type()
		else:
			self._instance = _internal

	@property
	def enable_test(self) -> bool:
		'''Value of variable $ENABLE_TEST'''
		return self._instance.EnableTest

	@property
	def num_lines(self) -> int:
		'''Value of variable $NUM_LINES'''
		return self._instance.NumLines

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CpTestVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
