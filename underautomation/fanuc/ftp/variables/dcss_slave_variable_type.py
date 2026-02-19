import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DcssSlaveVariableType as dcss_slave_variable_type

class DcssSlaveVariableType(GenericVariableType):
	'''Describes the Fanuc type DCSS_SLAVE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcss_slave_variable_type()
		else:
			self._instance = _internal

	@property
	def input_byte(self) -> int:
		'''Value of variable $INPUT_BYTE'''
		return self._instance.InputByte

	@property
	def output_byte(self) -> int:
		'''Value of variable $OUTPUT_BYTE'''
		return self._instance.OutputByte

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DcssSlaveVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
