import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FeatureVariableType as feature_variable_type

class FeatureVariableType(GenericVariableType):
	'''Describes the Fanuc type FEATURE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = feature_variable_type()
		else:
			self._instance = _internal

	@property
	def nam(self) -> typing.List[str]:
		'''Value of variable $NAM'''
		return self._instance.Nam

	@property
	def mod(self) -> typing.List[str]:
		'''Value of variable $MOD'''
		return self._instance.Mod

	@property
	def ver(self) -> typing.List[str]:
		'''Value of variable $VER'''
		return self._instance.Ver

	@property
	def mec(self) -> typing.List[str]:
		'''Value of variable $MEC'''
		return self._instance.Mec

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FeatureVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
