import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MixBgVariableType as mix_bg_variable_type

class MixBgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mix_bg_variable_type()
		else:
			self._instance = _internal
	@property
	def prog_name(self) -> str:
		return self._instance.ProgName
	@property
	def mode(self) -> int:
		return self._instance.Mode
	@property
	def status(self) -> int:
		return self._instance.Status
	@property
	def modify_time(self) -> int:
		return self._instance.ModifyTime
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
