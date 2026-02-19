import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import HostCfgVariableType as host_cfg_variable_type

class HostCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type HOST_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = host_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def comment(self) -> str:
		'''Value of variable $COMMENT'''
		return self._instance.Comment

	@property
	def protocol(self) -> str:
		'''Value of variable $PROTOCOL'''
		return self._instance.Protocol

	@property
	def port(self) -> str:
		'''Value of variable $PORT'''
		return self._instance.Port

	@property
	def oper(self) -> int:
		'''Value of variable $OPER'''
		return self._instance.Oper

	@property
	def state(self) -> int:
		'''Value of variable $STATE'''
		return self._instance.State

	@property
	def mode(self) -> str:
		'''Value of variable $MODE'''
		return self._instance.Mode

	@property
	def remote(self) -> str:
		'''Value of variable $REMOTE'''
		return self._instance.Remote

	@property
	def reperrs(self) -> bool:
		'''Value of variable $REPERRS'''
		return self._instance.Reperrs

	@property
	def timeout(self) -> int:
		'''Value of variable $TIMEOUT'''
		return self._instance.Timeout

	@property
	def path(self) -> str:
		'''Value of variable $PATH'''
		return self._instance.Path

	@property
	def strt_path(self) -> str:
		'''Value of variable $STRT_PATH'''
		return self._instance.StrtPath

	@property
	def strt_remote(self) -> str:
		'''Value of variable $STRT_REMOTE'''
		return self._instance.StrtRemote

	@property
	def username(self) -> str:
		'''Value of variable $USERNAME'''
		return self._instance.Username

	@property
	def pwrd_timout(self) -> int:
		'''Value of variable $PWRD_TIMOUT'''
		return self._instance.PwrdTimout

	@property
	def server_port(self) -> int:
		'''Value of variable $SERVER_PORT'''
		return self._instance.ServerPort

	@property
	def use_vis_prt(self) -> bool:
		'''Value of variable $USE_VIS_PRT'''
		return self._instance.UseVisPrt

	@property
	def use_udp(self) -> bool:
		'''Value of variable $USE_UDP'''
		return self._instance.UseUdp

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
