import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import RemoteCfgVariableType as remote_cfg_variable_type

class RemoteCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type REMOTE_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = remote_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def remote_type(self) -> int:
		'''Value of variable $REMOTE_TYPE'''
		return self._instance.RemoteType

	@property
	def remoteiotyp(self) -> int:
		'''Value of variable $REMOTEIOTYP'''
		return self._instance.Remoteiotyp

	@property
	def remoteioidx(self) -> int:
		'''Value of variable $REMOTEIOIDX'''
		return self._instance.Remoteioidx

	@property
	def local_optyp(self) -> int:
		'''Value of variable $LOCAL_OPTYP'''
		return self._instance.LocalOptyp

	@property
	def local_start(self) -> int:
		'''Value of variable $LOCAL_START'''
		return self._instance.LocalStart

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RemoteCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
