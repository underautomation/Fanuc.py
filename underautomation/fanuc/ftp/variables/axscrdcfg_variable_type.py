import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AxscrdcfgVariableType as axscrdcfg_variable_type

class AxscrdcfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = axscrdcfg_variable_type()
		else:
			self._instance = _internal
	@property
	def card_exist(self) -> bool:
		return self._instance.CardExist
	@property
	def fssb_type(self) -> int:
		return self._instance.FssbType
	@property
	def chkbd_sel(self) -> int:
		return self._instance.ChkbdSel
	@property
	def diag_reg(self) -> typing.List[int]:
		return self._instance.DiagReg
	@property
	def slot_num(self) -> int:
		return self._instance.SlotNum
	@property
	def slot_prev(self) -> int:
		return self._instance.SlotPrev
	@property
	def debug(self) -> typing.List[int]:
		return self._instance.Debug
	@property
	def card_id(self) -> int:
		return self._instance.CardId
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
