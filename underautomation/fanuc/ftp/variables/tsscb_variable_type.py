import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TsscbVariableType as tsscb_variable_type

class TsscbVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tsscb_variable_type()
		else:
			self._instance = _internal
	@property
	def dsp_no(self) -> int:
		return self._instance.DspNo
	@property
	def dspax_no(self) -> int:
		return self._instance.DspaxNo
	@property
	def data_sel(self) -> int:
		return self._instance.DataSel
	@property
	def out_channel(self) -> int:
		return self._instance.OutChannel
	@property
	def address(self) -> int:
		return self._instance.Address
	@property
	def bit_shift(self) -> int:
		return self._instance.BitShift
	@property
	def use2ch(self) -> int:
		return self._instance.Use2ch
	@property
	def monitor(self) -> int:
		return self._instance.Monitor
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
