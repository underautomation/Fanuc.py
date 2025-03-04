import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import LogDioVariableType as log_dio_variable_type

class LogDioVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = log_dio_variable_type()
		else:
			self._instance = _internal
	@property
	def rack(self) -> int:
		return self._instance.Rack
	@property
	def slot(self) -> int:
		return self._instance.Slot
	@property
	def mod_type(self) -> int:
		return self._instance.ModType
	@property
	def port_type(self) -> int:
		return self._instance.PortType
	@property
	def start_port(self) -> int:
		return self._instance.StartPort
	@property
	def end_port(self) -> int:
		return self._instance.EndPort
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
