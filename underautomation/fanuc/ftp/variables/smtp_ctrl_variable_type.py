import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SmtpCtrlVariableType as smtp_ctrl_variable_type

class SmtpCtrlVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = smtp_ctrl_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def server(self) -> str:
		return self._instance.Server
	@property
	def port(self) -> int:
		return self._instance.Port
	@property
	def timeout(self) -> int:
		return self._instance.Timeout
	@property
	def cc_addr(self) -> str:
		return self._instance.CcAddr
	@property
	def from_addr(self) -> str:
		return self._instance.FromAddr
	@property
	def rt_addr(self) -> str:
		return self._instance.RtAddr
	@property
	def post_dlvr(self) -> bool:
		return self._instance.PostDlvr
	@property
	def spare(self) -> int:
		return self._instance.Spare
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
