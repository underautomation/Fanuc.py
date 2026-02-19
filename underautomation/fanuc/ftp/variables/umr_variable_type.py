import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UmrVariableType as umr_variable_type

class UmrVariableType(GenericVariableType):
	'''Describes the Fanuc type UMR_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = umr_variable_type()
		else:
			self._instance = _internal

	@property
	def gupr_p(self) -> int:
		'''Value of variable $GUPR_P'''
		return self._instance.GuprP

	@property
	def gmrr_p(self) -> int:
		'''Value of variable $GMRR_P'''
		return self._instance.GmrrP

	@property
	def gujr_p(self) -> int:
		'''Value of variable $GUJR_P'''
		return self._instance.GujrP

	@property
	def gmrr2_p(self) -> int:
		'''Value of variable $GMRR2_P'''
		return self._instance.Gmrr2P

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UmrVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
