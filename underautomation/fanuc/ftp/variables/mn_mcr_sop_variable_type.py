import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MnMcrSopVariableType as mn_mcr_sop_variable_type

class MnMcrSopVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mn_mcr_sop_variable_type()
		else:
			self._instance = _internal
	@property
	def sop_emgop(self) -> bool:
		return self._instance.SopEmgop
	@property
	def sop_reset(self) -> bool:
		return self._instance.SopReset
	@property
	def sop_remote(self) -> bool:
		return self._instance.SopRemote
	@property
	def sop_hold(self) -> bool:
		return self._instance.SopHold
	@property
	def sop_user1(self) -> bool:
		return self._instance.SopUser1
	@property
	def sop_user2(self) -> bool:
		return self._instance.SopUser2
	@property
	def sop_start(self) -> bool:
		return self._instance.SopStart
	@property
	def sop_pdi8(self) -> bool:
		return self._instance.SopPdi8
	@property
	def sop_pdi9(self) -> bool:
		return self._instance.SopPdi9
	@property
	def sop_pdia(self) -> bool:
		return self._instance.SopPdia
	@property
	def sop_pdib(self) -> bool:
		return self._instance.SopPdib
	@property
	def sop_pdic(self) -> bool:
		return self._instance.SopPdic
	@property
	def sop_tpdsc(self) -> bool:
		return self._instance.SopTpdsc
	@property
	def sop_tprel(self) -> bool:
		return self._instance.SopTprel
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
