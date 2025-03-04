import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import OvrdslctVariableType as ovrdslct_variable_type

class OvrdslctVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ovrdslct_variable_type()
		else:
			self._instance = _internal
	@property
	def ovsl_enb(self) -> bool:
		return self._instance.OvslEnb
	@property
	def sdi_index1(self) -> int:
		return self._instance.SdiIndex1
	@property
	def sdi_index2(self) -> int:
		return self._instance.SdiIndex2
	@property
	def off_off_ovr(self) -> int:
		return self._instance.OffOffOvr
	@property
	def off_on_ovrd(self) -> int:
		return self._instance.OffOnOvrd
	@property
	def on_off_ovrd(self) -> int:
		return self._instance.OnOffOvrd
	@property
	def on_on_ovrd(self) -> int:
		return self._instance.OnOnOvrd
	@property
	def dummy(self) -> int:
		return self._instance.Dummy
	@property
	def dcs_ctl_enb(self) -> bool:
		return self._instance.DcsCtlEnb
	@property
	def dcs_ovrd(self) -> int:
		return self._instance.DcsOvrd
	@property
	def ovrd_zero(self) -> bool:
		return self._instance.OvrdZero
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
