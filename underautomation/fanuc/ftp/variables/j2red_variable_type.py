import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import J2redVariableType as j2red_variable_type

class J2redVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = j2red_variable_type()
		else:
			self._instance = _internal
	@property
	def exd_rtq(self) -> float:
		return self._instance.ExdRtq
	@property
	def exd_itp(self) -> int:
		return self._instance.ExdItp
	@property
	def exd_prg(self) -> int:
		return self._instance.ExdPrg
	@property
	def exd_line(self) -> int:
		return self._instance.ExdLine
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
