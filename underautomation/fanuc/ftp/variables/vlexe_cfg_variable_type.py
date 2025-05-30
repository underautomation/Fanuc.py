import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VlexeCfgVariableType as vlexe_cfg_variable_type

class VlexeCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vlexe_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def enabled(self) -> bool:
		return self._instance.Enabled
	@property
	def date(self) -> int:
		return self._instance.Date
	@property
	def fldr_index(self) -> int:
		return self._instance.FldrIndex
	@property
	def file_index(self) -> int:
		return self._instance.FileIndex
	@property
	def rec_index(self) -> int:
		return self._instance.RecIndex
	@property
	def output_idx(self) -> bool:
		return self._instance.OutputIdx
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
