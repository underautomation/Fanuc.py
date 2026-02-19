import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FluiDataVariableType as flui_data_variable_type

class FluiDataVariableType(GenericVariableType):
	'''Describes the Fanuc type FLUI_DATA_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = flui_data_variable_type()
		else:
			self._instance = _internal

	@property
	def future1(self) -> int:
		'''Value of variable $FUTURE1'''
		return self._instance.Future1

	@property
	def future2(self) -> int:
		'''Value of variable $FUTURE2'''
		return self._instance.Future2

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FluiDataVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
