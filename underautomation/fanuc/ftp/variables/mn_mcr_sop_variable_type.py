import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MnMcrSopVariableType as mn_mcr_sop_variable_type

class MnMcrSopVariableType(GenericVariableType):
	'''Describes the Fanuc type MN_MCR_SOP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mn_mcr_sop_variable_type()
		else:
			self._instance = _internal

	@property
	def sop_emgop(self) -> bool:
		'''Value of variable $SOP_EMGOP'''
		return self._instance.SopEmgop

	@property
	def sop_reset(self) -> bool:
		'''Value of variable $SOP_RESET'''
		return self._instance.SopReset

	@property
	def sop_remote(self) -> bool:
		'''Value of variable $SOP_REMOTE'''
		return self._instance.SopRemote

	@property
	def sop_hold(self) -> bool:
		'''Value of variable $SOP_HOLD'''
		return self._instance.SopHold

	@property
	def sop_user1(self) -> bool:
		'''Value of variable $SOP_USER1'''
		return self._instance.SopUser1

	@property
	def sop_user2(self) -> bool:
		'''Value of variable $SOP_USER2'''
		return self._instance.SopUser2

	@property
	def sop_start(self) -> bool:
		'''Value of variable $SOP_START'''
		return self._instance.SopStart

	@property
	def sop_pdi8(self) -> bool:
		'''Value of variable $SOP_PDI8'''
		return self._instance.SopPdi8

	@property
	def sop_pdi9(self) -> bool:
		'''Value of variable $SOP_PDI9'''
		return self._instance.SopPdi9

	@property
	def sop_pdia(self) -> bool:
		'''Value of variable $SOP_PDIA'''
		return self._instance.SopPdia

	@property
	def sop_pdib(self) -> bool:
		'''Value of variable $SOP_PDIB'''
		return self._instance.SopPdib

	@property
	def sop_pdic(self) -> bool:
		'''Value of variable $SOP_PDIC'''
		return self._instance.SopPdic

	@property
	def sop_tpdsc(self) -> bool:
		'''Value of variable $SOP_TPDSC'''
		return self._instance.SopTpdsc

	@property
	def sop_tprel(self) -> bool:
		'''Value of variable $SOP_TPREL'''
		return self._instance.SopTprel

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MnMcrSopVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
