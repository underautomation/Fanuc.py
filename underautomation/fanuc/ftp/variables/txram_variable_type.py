import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TxramVariableType as txram_variable_type

class TxramVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = txram_variable_type()
		else:
			self._instance = _internal
	@property
	def remote(self) -> bool:
		return self._instance.Remote
	@property
	def pc(self) -> bool:
		return self._instance.Pc
	@property
	def pcjog(self) -> bool:
		return self._instance.Pcjog
	@property
	def cur_ip_mem(self) -> int:
		return self._instance.CurIpMem
	@property
	def min_ip_mem(self) -> int:
		return self._instance.MinIpMem
	@property
	def ip_mem_size(self) -> int:
		return self._instance.IpMemSize
	@property
	def ipaddr(self) -> int:
		return self._instance.Ipaddr
	@property
	def plus_flag(self) -> int:
		return self._instance.PlusFlag
	@property
	def os_version(self) -> str:
		return self._instance.OsVersion
	@property
	def netf_ver(self) -> str:
		return self._instance.NetfVer
	@property
	def ip_tw(self) -> int:
		return self._instance.IpTw
	@property
	def tablet_tp(self) -> bool:
		return self._instance.TabletTp
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
