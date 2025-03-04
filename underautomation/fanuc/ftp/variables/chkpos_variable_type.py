import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ChkposVariableType as chkpos_variable_type

class ChkposVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = chkpos_variable_type()
		else:
			self._instance = _internal
	@property
	def cont_flag(self) -> bool:
		return self._instance.ContFlag
	@property
	def pos_hdr(self) -> int:
		return self._instance.PosHdr
	@property
	def pos_hdr2(self) -> int:
		return self._instance.PosHdr2
	@property
	def jpos1(self) -> int:
		return self._instance.Jpos1
	@property
	def jpos2(self) -> int:
		return self._instance.Jpos2
	@property
	def jpos3(self) -> int:
		return self._instance.Jpos3
	@property
	def jpos4(self) -> int:
		return self._instance.Jpos4
	@property
	def jpos5(self) -> int:
		return self._instance.Jpos5
	@property
	def jpos6(self) -> int:
		return self._instance.Jpos6
	@property
	def jpos7(self) -> int:
		return self._instance.Jpos7
	@property
	def jpos8(self) -> int:
		return self._instance.Jpos8
	@property
	def jpos9(self) -> int:
		return self._instance.Jpos9
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
