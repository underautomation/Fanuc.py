import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PipeCfgVariableType as pipe_cfg_variable_type

class PipeCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pipe_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def sectors(self) -> int:
		return self._instance.Sectors
	@property
	def formatter(self) -> int:
		return self._instance.Formatter
	@property
	def recordsize(self) -> int:
		return self._instance.Recordsize
	@property
	def memtype(self) -> int:
		return self._instance.Memtype
	@property
	def format(self) -> int:
		return self._instance.Format
	@property
	def auxword(self) -> int:
		return self._instance.Auxword
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
