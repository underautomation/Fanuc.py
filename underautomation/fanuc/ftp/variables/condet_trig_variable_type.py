import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CondetTrigVariableType as condet_trig_variable_type

class CondetTrigVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = condet_trig_variable_type()
		else:
			self._instance = _internal
	@property
	def io_type(self) -> int:
		return self._instance.IoType
	@property
	def io_port(self) -> int:
		return self._instance.IoPort
	@property
	def io_style(self) -> int:
		return self._instance.IoStyle
	@property
	def delay(self) -> int:
		return self._instance.Delay
	@property
	def style_type(self) -> int:
		return self._instance.StyleType
	@property
	def style_port(self) -> int:
		return self._instance.StylePort
	@property
	def flag(self) -> int:
		return self._instance.Flag
	@property
	def debug(self) -> int:
		return self._instance.Debug
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
