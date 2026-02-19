import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import IolnkVariableType as iolnk_variable_type

class IolnkVariableType(GenericVariableType):
	'''Describes the Fanuc type IOLNK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = iolnk_variable_type()
		else:
			self._instance = _internal

	@property
	def rack(self) -> int:
		'''Value of variable $RACK'''
		return self._instance.Rack

	@property
	def slot(self) -> int:
		'''Value of variable $SLOT'''
		return self._instance.Slot

	@property
	def input_n(self) -> int:
		'''Value of variable $INPUT_N'''
		return self._instance.InputN

	@property
	def output_n(self) -> int:
		'''Value of variable $OUTPUT_N'''
		return self._instance.OutputN

	@property
	def option(self) -> int:
		'''Value of variable $OPTION'''
		return self._instance.Option

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IolnkVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
