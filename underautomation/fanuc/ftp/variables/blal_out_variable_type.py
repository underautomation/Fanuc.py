import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import BlalOutVariableType as blal_out_variable_type

class BlalOutVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = blal_out_variable_type()
		else:
			self._instance = _internal
	@property
	def do_index(self) -> int:
		return self._instance.DoIndex
	@property
	def ps_batalm_o(self) -> int:
		return self._instance.PsBatalmO
	@property
	def batalm_or(self) -> bool:
		return self._instance.BatalmOr
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
