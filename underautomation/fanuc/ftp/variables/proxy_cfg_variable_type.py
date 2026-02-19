import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ProxyCfgVariableType as proxy_cfg_variable_type

class ProxyCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type PROXY_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = proxy_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def list_port(self) -> int:
		'''Value of variable $LIST_PORT'''
		return self._instance.ListPort

	@property
	def proxy_enb(self) -> int:
		'''Value of variable $PROXY_ENB'''
		return self._instance.ProxyEnb

	@property
	def proxy_srv(self) -> str:
		'''Value of variable $PROXY_SRV'''
		return self._instance.ProxySrv

	@property
	def proxy_port(self) -> int:
		'''Value of variable $PROXY_PORT'''
		return self._instance.ProxyPort

	@property
	def direct1(self) -> str:
		'''Value of variable $DIRECT_1'''
		return self._instance.Direct1

	@property
	def direct2(self) -> str:
		'''Value of variable $DIRECT_2'''
		return self._instance.Direct2

	@property
	def direct3(self) -> str:
		'''Value of variable $DIRECT_3'''
		return self._instance.Direct3

	@property
	def direct4(self) -> str:
		'''Value of variable $DIRECT_4'''
		return self._instance.Direct4

	@property
	def direct5(self) -> str:
		'''Value of variable $DIRECT_5'''
		return self._instance.Direct5

	@property
	def direct6(self) -> str:
		'''Value of variable $DIRECT_6'''
		return self._instance.Direct6

	@property
	def direct7(self) -> str:
		'''Value of variable $DIRECT_7'''
		return self._instance.Direct7

	@property
	def direct8(self) -> str:
		'''Value of variable $DIRECT_8'''
		return self._instance.Direct8

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ProxyCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
