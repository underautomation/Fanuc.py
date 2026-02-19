import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import Tbj2GrpVariableType as tbj2_grp_variable_type

class Tbj2GrpVariableType(GenericVariableType):
	'''Describes the Fanuc type TBJ2_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbj2_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def enb_flim(self) -> bool:
		'''Value of variable $ENB_FLIM'''
		return self._instance.EnbFlim

	@property
	def lim_ftm1(self) -> int:
		'''Value of variable $LIM_FTM1'''
		return self._instance.LimFtm1

	@property
	def lim_ftm2(self) -> int:
		'''Value of variable $LIM_FTM2'''
		return self._instance.LimFtm2

	@property
	def reserve1(self) -> int:
		'''Value of variable $RESERVE1'''
		return self._instance.Reserve1

	@property
	def reserve2(self) -> int:
		'''Value of variable $RESERVE2'''
		return self._instance.Reserve2

	@property
	def reserve3(self) -> int:
		'''Value of variable $RESERVE3'''
		return self._instance.Reserve3

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Tbj2GrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
