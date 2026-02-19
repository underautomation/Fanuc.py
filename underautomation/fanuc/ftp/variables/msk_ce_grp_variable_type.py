import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MskCeGrpVariableType as msk_ce_grp_variable_type

class MskCeGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type MSK_CE_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = msk_ce_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def t1_usercart(self) -> float:
		'''Value of variable $T1_USERCART'''
		return self._instance.T1Usercart

	@property
	def t1_userjnt(self) -> typing.List[float]:
		'''Value of variable $T1_USERJNT'''
		return self._instance.T1Userjnt

	@property
	def t1_cartvel(self) -> float:
		'''Value of variable $T1_CARTVEL'''
		return self._instance.T1Cartvel

	@property
	def t1_jntvel(self) -> typing.List[float]:
		'''Value of variable $T1_JNTVEL'''
		return self._instance.T1Jntvel

	@property
	def t1_warning(self) -> bool:
		'''Value of variable $T1_WARNING'''
		return self._instance.T1Warning

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MskCeGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
