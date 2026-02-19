import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MndsppstlVariableType as mndsppstl_variable_type

class MndsppstlVariableType(GenericVariableType):
	'''Describes the Fanuc type MNDSPPSTL_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mndsppstl_variable_type()
		else:
			self._instance = _internal

	@property
	def loctol(self) -> float:
		'''Value of variable $LOCTOL'''
		return self._instance.Loctol

	@property
	def orienttol(self) -> float:
		'''Value of variable $ORIENTTOL'''
		return self._instance.Orienttol

	@property
	def exttol(self) -> float:
		'''Value of variable $EXTTOL'''
		return self._instance.Exttol

	@property
	def angtol(self) -> typing.List[float]:
		'''Value of variable $ANGTOL'''
		return self._instance.Angtol

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MndsppstlVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
