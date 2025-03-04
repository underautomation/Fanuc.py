import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import EdtRecentVariableType as edt_recent_variable_type

class EdtRecentVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = edt_recent_variable_type()
		else:
			self._instance = _internal
	@property
	def prog_name(self) -> str:
		return self._instance.ProgName
	@property
	def curr_line(self) -> int:
		return self._instance.CurrLine
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
