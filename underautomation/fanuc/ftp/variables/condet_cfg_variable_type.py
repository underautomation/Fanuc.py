import typing
from underautomation.fanuc.ftp.variables.condet_data_variable_type import CondetDataVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CondetCfgVariableType as condet_cfg_variable_type

class CondetCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type CONDET_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = condet_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> int:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def state(self) -> int:
		'''Value of variable $STATE'''
		return self._instance.State

	@property
	def server_name(self) -> str:
		'''Value of variable $SERVER_NAME'''
		return self._instance.ServerName

	@property
	def port(self) -> int:
		'''Value of variable $PORT'''
		return self._instance.Port

	@property
	def mode(self) -> int:
		'''Value of variable $MODE'''
		return self._instance.Mode

	@property
	def protocol(self) -> int:
		'''Value of variable $PROTOCOL'''
		return self._instance.Protocol

	@property
	def peer_name(self) -> str:
		'''Value of variable $PEER_NAME'''
		return self._instance.PeerName

	@property
	def ext_mask(self) -> int:
		'''Value of variable $EXT_MASK'''
		return self._instance.ExtMask

	@property
	def ext_used(self) -> int:
		'''Value of variable $EXT_USED'''
		return self._instance.ExtUsed

	@property
	def ext_data(self) -> typing.List[CondetDataVariableType]:
		'''Value of variable $EXT_DATA'''
		return [CondetDataVariableType(x) for x in self._instance.ExtData]

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CondetCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
