import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ProxyCfgVariableType as proxy_cfg_variable_type

class ProxyCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = proxy_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def list_port(self) -> int:
		return self._instance.ListPort
	@property
	def proxy_enb(self) -> int:
		return self._instance.ProxyEnb
	@property
	def proxy_srv(self) -> str:
		return self._instance.ProxySrv
	@property
	def proxy_port(self) -> int:
		return self._instance.ProxyPort
	@property
	def direct1(self) -> str:
		return self._instance.Direct1
	@property
	def direct2(self) -> str:
		return self._instance.Direct2
	@property
	def direct3(self) -> str:
		return self._instance.Direct3
	@property
	def direct4(self) -> str:
		return self._instance.Direct4
	@property
	def direct5(self) -> str:
		return self._instance.Direct5
	@property
	def direct6(self) -> str:
		return self._instance.Direct6
	@property
	def direct7(self) -> str:
		return self._instance.Direct7
	@property
	def direct8(self) -> str:
		return self._instance.Direct8
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
