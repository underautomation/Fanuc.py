import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DhcpCtrlVariableType as dhcp_ctrl_variable_type

class DhcpCtrlVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dhcp_ctrl_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def ipuse(self) -> bool:
		return self._instance.Ipuse
	@property
	def retrate(self) -> int:
		return self._instance.Retrate
	@property
	def sethost(self) -> bool:
		return self._instance.Sethost
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
