import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AxscrdcfgVariableType as axscrdcfg_variable_type

class AxscrdcfgVariableType(GenericVariableType):
	'''Describes the Fanuc type AXSCRDCFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = axscrdcfg_variable_type()
		else:
			self._instance = _internal

	@property
	def card_exist(self) -> bool:
		'''Value of variable $CARD_EXIST'''
		return self._instance.CardExist

	@property
	def fssb_type(self) -> int:
		'''Value of variable $FSSB_TYPE'''
		return self._instance.FssbType

	@property
	def chkbd_sel(self) -> int:
		'''Value of variable $CHKBD_SEL'''
		return self._instance.ChkbdSel

	@property
	def diag_reg(self) -> typing.List[int]:
		'''Value of variable $DIAG_REG'''
		return self._instance.DiagReg

	@property
	def slot_num(self) -> int:
		'''Value of variable $SLOT_NUM'''
		return self._instance.SlotNum

	@property
	def slot_prev(self) -> int:
		'''Value of variable $SLOT_PREV'''
		return self._instance.SlotPrev

	@property
	def debug(self) -> typing.List[int]:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def card_id(self) -> int:
		'''Value of variable $CARD_ID'''
		return self._instance.CardId

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AxscrdcfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
