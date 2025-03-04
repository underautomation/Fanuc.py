import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DnsCfgVariableType as dns_cfg_variable_type

class DnsCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dns_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def primar_ip(self) -> str:
		return self._instance.PrimarIp
	@property
	def altern_ip(self) -> str:
		return self._instance.AlternIp
	@property
	def retries(self) -> int:
		return self._instance.Retries
	@property
	def wait_time(self) -> int:
		return self._instance.WaitTime
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
