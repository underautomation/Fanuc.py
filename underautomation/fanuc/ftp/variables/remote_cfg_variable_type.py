import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import RemoteCfgVariableType as remote_cfg_variable_type

class RemoteCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = remote_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def remote_type(self) -> int:
		return self._instance.RemoteType
	@property
	def remoteiotyp(self) -> int:
		return self._instance.Remoteiotyp
	@property
	def remoteioidx(self) -> int:
		return self._instance.Remoteioidx
	@property
	def local_optyp(self) -> int:
		return self._instance.LocalOptyp
	@property
	def local_start(self) -> int:
		return self._instance.LocalStart
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
