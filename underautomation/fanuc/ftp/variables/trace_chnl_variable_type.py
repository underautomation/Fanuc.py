import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TraceChnlVariableType as trace_chnl_variable_type

class TraceChnlVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = trace_chnl_variable_type()
		else:
			self._instance = _internal
	@property
	def item_num(self) -> int:
		return self._instance.ItemNum
	@property
	def tcp_gp_num(self) -> int:
		return self._instance.TcpGpNum
	@property
	def visible(self) -> bool:
		return self._instance.Visible
	@property
	def style(self) -> int:
		return self._instance.Style
	@property
	def color(self) -> int:
		return self._instance.Color
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
