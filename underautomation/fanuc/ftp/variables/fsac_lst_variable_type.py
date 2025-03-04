import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FsacLstVariableType as fsac_lst_variable_type

class FsacLstVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fsac_lst_variable_type()
		else:
			self._instance = _internal
	@property
	def clnt_name(self) -> str:
		return self._instance.ClntName
	@property
	def ip_address(self) -> str:
		return self._instance.IpAddress
	@property
	def access_lvl(self) -> int:
		return self._instance.AccessLvl
	@property
	def apps(self) -> int:
		return self._instance.Apps
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
