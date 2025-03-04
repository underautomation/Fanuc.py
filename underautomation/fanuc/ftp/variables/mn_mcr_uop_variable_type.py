import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MnMcrUopVariableType as mn_mcr_uop_variable_type

class MnMcrUopVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mn_mcr_uop_variable_type()
		else:
			self._instance = _internal
	@property
	def uop_estop(self) -> bool:
		return self._instance.UopEstop
	@property
	def uop_hold(self) -> bool:
		return self._instance.UopHold
	@property
	def uop_sfspd(self) -> bool:
		return self._instance.UopSfspd
	@property
	def uop_cstop(self) -> bool:
		return self._instance.UopCstop
	@property
	def uop_reset(self) -> bool:
		return self._instance.UopReset
	@property
	def uop_start(self) -> bool:
		return self._instance.UopStart
	@property
	def uop_home(self) -> bool:
		return self._instance.UopHome
	@property
	def uop_enbl(self) -> bool:
		return self._instance.UopEnbl
	@property
	def uop_rsr1(self) -> bool:
		return self._instance.UopRsr1
	@property
	def uop_rsr2(self) -> bool:
		return self._instance.UopRsr2
	@property
	def uop_rsr3(self) -> bool:
		return self._instance.UopRsr3
	@property
	def uop_rsr4(self) -> bool:
		return self._instance.UopRsr4
	@property
	def uop_rsr5(self) -> bool:
		return self._instance.UopRsr5
	@property
	def uop_rsr6(self) -> bool:
		return self._instance.UopRsr6
	@property
	def uop_rsr7(self) -> bool:
		return self._instance.UopRsr7
	@property
	def uop_rsr8(self) -> bool:
		return self._instance.UopRsr8
	@property
	def uop_pnstrb(self) -> bool:
		return self._instance.UopPnstrb
	@property
	def uop_pdstrt(self) -> bool:
		return self._instance.UopPdstrt
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
