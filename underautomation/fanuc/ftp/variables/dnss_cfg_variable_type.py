import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DnssCfgVariableType as dnss_cfg_variable_type

class DnssCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dnss_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def enabled(self) -> bool:
		return self._instance.Enabled
	@property
	def iface_num(self) -> int:
		return self._instance.IfaceNum
	@property
	def dbg_level(self) -> int:
		return self._instance.DbgLevel
	@property
	def dom_name(self) -> str:
		return self._instance.DomName
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
