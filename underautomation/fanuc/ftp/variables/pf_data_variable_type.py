import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PfDataVariableType as pf_data_variable_type

class PfDataVariableType(GenericVariableType):
	'''Describes the Fanuc type PF_DATA_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pf_data_variable_type()
		else:
			self._instance = _internal

	@property
	def value(self) -> float:
		'''Value of variable $VALUE'''
		return self._instance.Value

	@property
	def group(self) -> int:
		'''Value of variable $GROUP'''
		return self._instance.Group

	@property
	def axis(self) -> int:
		'''Value of variable $AXIS'''
		return self._instance.Axis

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PfDataVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
