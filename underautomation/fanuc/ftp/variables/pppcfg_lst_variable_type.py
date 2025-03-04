import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PppcfgLstVariableType as pppcfg_lst_variable_type

class PppcfgLstVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pppcfg_lst_variable_type()
		else:
			self._instance = _internal
	@property
	def robotip(self) -> str:
		return self._instance.Robotip
	@property
	def peerip(self) -> str:
		return self._instance.Peerip
	@property
	def netmask(self) -> str:
		return self._instance.Netmask
	@property
	def mru(self) -> int:
		return self._instance.Mru
	@property
	def comp(self) -> int:
		return self._instance.Comp
	@property
	def devtype(self) -> int:
		return self._instance.Devtype
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
