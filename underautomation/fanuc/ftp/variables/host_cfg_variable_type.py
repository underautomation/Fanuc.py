import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import HostCfgVariableType as host_cfg_variable_type

class HostCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def comment(self) -> str:
		return self._instance.Comment
	@property
	def protocol(self) -> str:
		return self._instance.Protocol
	@property
	def port(self) -> str:
		return self._instance.Port
	@property
	def oper(self) -> int:
		return self._instance.Oper
	@property
	def state(self) -> int:
		return self._instance.State
	@property
	def mode(self) -> str:
		return self._instance.Mode
	@property
	def remote(self) -> str:
		return self._instance.Remote
	@property
	def reperrs(self) -> bool:
		return self._instance.Reperrs
	@property
	def timeout(self) -> int:
		return self._instance.Timeout
	@property
	def path(self) -> str:
		return self._instance.Path
	@property
	def strt_path(self) -> str:
		return self._instance.StrtPath
	@property
	def strt_remote(self) -> str:
		return self._instance.StrtRemote
	@property
	def username(self) -> str:
		return self._instance.Username
	@property
	def pwrd_timout(self) -> int:
		return self._instance.PwrdTimout
	@property
	def server_port(self) -> int:
		return self._instance.ServerPort
	@property
	def use_vis_prt(self) -> bool:
		return self._instance.UseVisPrt
	@property
	def use_udp(self) -> bool:
		return self._instance.UseUdp
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
