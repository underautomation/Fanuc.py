import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import IoslaveVariableType as ioslave_variable_type

class IoslaveVariableType(GenericVariableType):
	'''Describes the Fanuc type IOSLAVE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ioslave_variable_type()
		else:
			self._instance = _internal

	@property
	def input_n(self) -> int:
		'''Value of variable $INPUT_N'''
		return self._instance.InputN

	@property
	def output_n(self) -> int:
		'''Value of variable $OUTPUT_N'''
		return self._instance.OutputN

	@property
	def input_n2(self) -> int:
		'''Value of variable $INPUT_N2'''
		return self._instance.InputN2

	@property
	def output_n2(self) -> int:
		'''Value of variable $OUTPUT_N2'''
		return self._instance.OutputN2

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoslaveVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
