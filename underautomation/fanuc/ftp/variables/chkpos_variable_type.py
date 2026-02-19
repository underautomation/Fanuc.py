import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ChkposVariableType as chkpos_variable_type

class ChkposVariableType(GenericVariableType):
	'''Describes the Fanuc type CHKPOS_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = chkpos_variable_type()
		else:
			self._instance = _internal

	@property
	def cont_flag(self) -> bool:
		'''Value of variable $CONT_FLAG'''
		return self._instance.ContFlag

	@property
	def pos_hdr(self) -> int:
		'''Value of variable $POS_HDR'''
		return self._instance.PosHdr

	@property
	def pos_hdr2(self) -> int:
		'''Value of variable $POS_HDR2'''
		return self._instance.PosHdr2

	@property
	def jpos1(self) -> int:
		'''Value of variable $JPOS1'''
		return self._instance.Jpos1

	@property
	def jpos2(self) -> int:
		'''Value of variable $JPOS2'''
		return self._instance.Jpos2

	@property
	def jpos3(self) -> int:
		'''Value of variable $JPOS3'''
		return self._instance.Jpos3

	@property
	def jpos4(self) -> int:
		'''Value of variable $JPOS4'''
		return self._instance.Jpos4

	@property
	def jpos5(self) -> int:
		'''Value of variable $JPOS5'''
		return self._instance.Jpos5

	@property
	def jpos6(self) -> int:
		'''Value of variable $JPOS6'''
		return self._instance.Jpos6

	@property
	def jpos7(self) -> int:
		'''Value of variable $JPOS7'''
		return self._instance.Jpos7

	@property
	def jpos8(self) -> int:
		'''Value of variable $JPOS8'''
		return self._instance.Jpos8

	@property
	def jpos9(self) -> int:
		'''Value of variable $JPOS9'''
		return self._instance.Jpos9

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ChkposVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
