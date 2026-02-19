import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TxramVariableType as txram_variable_type

class TxramVariableType(GenericVariableType):
	'''Describes the Fanuc type TXRAM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = txram_variable_type()
		else:
			self._instance = _internal

	@property
	def remote(self) -> bool:
		'''Value of variable $REMOTE'''
		return self._instance.Remote

	@property
	def pc(self) -> bool:
		'''Value of variable $PC'''
		return self._instance.Pc

	@property
	def pcjog(self) -> bool:
		'''Value of variable $PCJOG'''
		return self._instance.Pcjog

	@property
	def cur_ip_mem(self) -> int:
		'''Value of variable $CUR_IP_MEM'''
		return self._instance.CurIpMem

	@property
	def min_ip_mem(self) -> int:
		'''Value of variable $MIN_IP_MEM'''
		return self._instance.MinIpMem

	@property
	def ip_mem_size(self) -> int:
		'''Value of variable $IP_MEM_SIZE'''
		return self._instance.IpMemSize

	@property
	def ipaddr(self) -> int:
		'''Value of variable $IPADDR'''
		return self._instance.Ipaddr

	@property
	def plus_flag(self) -> int:
		'''Value of variable $PLUS_FLAG'''
		return self._instance.PlusFlag

	@property
	def os_version(self) -> str:
		'''Value of variable $OS_VERSION'''
		return self._instance.OsVersion

	@property
	def netf_ver(self) -> str:
		'''Value of variable $NETF_VER'''
		return self._instance.NetfVer

	@property
	def ip_tw(self) -> int:
		'''Value of variable $IP_TW'''
		return self._instance.IpTw

	@property
	def tablet_tp(self) -> bool:
		'''Value of variable $TABLET_TP'''
		return self._instance.TabletTp

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TxramVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
