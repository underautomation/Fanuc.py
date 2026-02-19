import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MnMcrUopVariableType as mn_mcr_uop_variable_type

class MnMcrUopVariableType(GenericVariableType):
	'''Describes the Fanuc type MN_MCR_UOP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mn_mcr_uop_variable_type()
		else:
			self._instance = _internal

	@property
	def uop_estop(self) -> bool:
		'''Value of variable $UOP_ESTOP'''
		return self._instance.UopEstop

	@property
	def uop_hold(self) -> bool:
		'''Value of variable $UOP_HOLD'''
		return self._instance.UopHold

	@property
	def uop_sfspd(self) -> bool:
		'''Value of variable $UOP_SFSPD'''
		return self._instance.UopSfspd

	@property
	def uop_cstop(self) -> bool:
		'''Value of variable $UOP_CSTOP'''
		return self._instance.UopCstop

	@property
	def uop_reset(self) -> bool:
		'''Value of variable $UOP_RESET'''
		return self._instance.UopReset

	@property
	def uop_start(self) -> bool:
		'''Value of variable $UOP_START'''
		return self._instance.UopStart

	@property
	def uop_home(self) -> bool:
		'''Value of variable $UOP_HOME'''
		return self._instance.UopHome

	@property
	def uop_enbl(self) -> bool:
		'''Value of variable $UOP_ENBL'''
		return self._instance.UopEnbl

	@property
	def uop_rsr1(self) -> bool:
		'''Value of variable $UOP_RSR1'''
		return self._instance.UopRsr1

	@property
	def uop_rsr2(self) -> bool:
		'''Value of variable $UOP_RSR2'''
		return self._instance.UopRsr2

	@property
	def uop_rsr3(self) -> bool:
		'''Value of variable $UOP_RSR3'''
		return self._instance.UopRsr3

	@property
	def uop_rsr4(self) -> bool:
		'''Value of variable $UOP_RSR4'''
		return self._instance.UopRsr4

	@property
	def uop_rsr5(self) -> bool:
		'''Value of variable $UOP_RSR5'''
		return self._instance.UopRsr5

	@property
	def uop_rsr6(self) -> bool:
		'''Value of variable $UOP_RSR6'''
		return self._instance.UopRsr6

	@property
	def uop_rsr7(self) -> bool:
		'''Value of variable $UOP_RSR7'''
		return self._instance.UopRsr7

	@property
	def uop_rsr8(self) -> bool:
		'''Value of variable $UOP_RSR8'''
		return self._instance.UopRsr8

	@property
	def uop_pnstrb(self) -> bool:
		'''Value of variable $UOP_PNSTRB'''
		return self._instance.UopPnstrb

	@property
	def uop_pdstrt(self) -> bool:
		'''Value of variable $UOP_PDSTRT'''
		return self._instance.UopPdstrt

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MnMcrUopVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
