import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PingVariableType as ping_variable_type

class PingVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ping_variable_type()
		else:
			self._instance = _internal
	@property
	def timeout(self) -> int:
		return self._instance.Timeout
	@property
	def datalen(self) -> int:
		return self._instance.Datalen
	@property
	def npackets(self) -> int:
		return self._instance.Npackets
	@property
	def debug(self) -> bool:
		return self._instance.Debug
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
