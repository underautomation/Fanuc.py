import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ErNoautoVariableType as er_noauto_variable_type

class ErNoautoVariableType(GenericVariableType):
	'''Describes the Fanuc type ER_NOAUTO_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = er_noauto_variable_type()
		else:
			self._instance = _internal

	@property
	def noauto_enb(self) -> bool:
		'''Value of variable $NOAUTO_ENB'''
		return self._instance.NoautoEnb

	@property
	def noauto_num(self) -> int:
		'''Value of variable $NOAUTO_NUM'''
		return self._instance.NoautoNum

	@property
	def ps_noauto_c(self) -> int:
		'''Value of variable $PS_NOAUTO_C'''
		return self._instance.PsNoautoC

	@property
	def noauto_code(self) -> typing.List[int]:
		'''Value of variable $NOAUTO_CODE'''
		return self._instance.NoautoCode

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ErNoautoVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
