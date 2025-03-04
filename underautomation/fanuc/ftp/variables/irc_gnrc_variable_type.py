import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import IrcGnrcVariableType as irc_gnrc_variable_type

class IrcGnrcVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = irc_gnrc_variable_type()
		else:
			self._instance = _internal
	@property
	def dostime(self) -> int:
		return self._instance.Dostime
	@property
	def msgtype(self) -> int:
		return self._instance.Msgtype
	@property
	def int1(self) -> int:
		return self._instance.Int1
	@property
	def int2(self) -> int:
		return self._instance.Int2
	@property
	def str1(self) -> str:
		return self._instance.Str1
	@property
	def str2(self) -> str:
		return self._instance.Str2
	@property
	def str3(self) -> str:
		return self._instance.Str3
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
