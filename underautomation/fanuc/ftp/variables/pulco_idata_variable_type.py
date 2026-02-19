import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PulcoIdataVariableType as pulco_idata_variable_type

class PulcoIdataVariableType(GenericVariableType):
	'''Describes the Fanuc type $PULCO_IDATA'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pulco_idata_variable_type()
		else:
			self._instance = _internal

	@property
	def address(self) -> int:
		'''Value of variable $ADDRESS'''
		return self._instance.Address

	@property
	def data(self) -> typing.List[int]:
		'''Value of variable $DATA'''
		return self._instance.Data

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PulcoIdataVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
