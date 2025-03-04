import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MixMkrVariableType as mix_mkr_variable_type

class MixMkrVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mix_mkr_variable_type()
		else:
			self._instance = _internal
	@property
	def line(self) -> typing.List[int]:
		return self._instance.Line
	@property
	def line_size(self) -> int:
		return self._instance.LineSize
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
