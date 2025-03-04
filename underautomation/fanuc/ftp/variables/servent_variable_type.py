import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ServentVariableType as servent_variable_type

class ServentVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = servent_variable_type()
		else:
			self._instance = _internal
	@property
	def s_name(self) -> str:
		return self._instance.SName
	@property
	def s_port(self) -> int:
		return self._instance.SPort
	@property
	def s_proto(self) -> str:
		return self._instance.SProto
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
