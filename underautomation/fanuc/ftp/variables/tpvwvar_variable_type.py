import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TpvwvarVariableType as tpvwvar_variable_type

class TpvwvarVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpvwvar_variable_type()
		else:
			self._instance = _internal
	@property
	def tpview_enb(self) -> bool:
		return self._instance.TpviewEnb
	@property
	def prev_rtn(self) -> bool:
		return self._instance.PrevRtn
	@property
	def edit_rtn(self) -> bool:
		return self._instance.EditRtn
	@property
	def vshwrk(self) -> int:
		return self._instance.Vshwrk
	@property
	def debug(self) -> int:
		return self._instance.Debug
	@property
	def display(self) -> int:
		return self._instance.Display
	@property
	def indent1(self) -> int:
		return self._instance.Indent1
	@property
	def indent2(self) -> int:
		return self._instance.Indent2
	@property
	def head1(self) -> str:
		return self._instance.Head1
	@property
	def head2(self) -> str:
		return self._instance.Head2
	@property
	def edit_key(self) -> int:
		return self._instance.EditKey
	@property
	def tcpspd_key(self) -> int:
		return self._instance.TcpspdKey
	@property
	def jmpcall_enb(self) -> bool:
		return self._instance.JmpcallEnb
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
