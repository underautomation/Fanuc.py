import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TpThrTableVariableType as tp_thr_table_variable_type

class TpThrTableVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tp_thr_table_variable_type()
		else:
			self._instance = _internal
	@property
	def thr_enb(self) -> bool:
		return self._instance.ThrEnb
	@property
	def di_no(self) -> int:
		return self._instance.DiNo
	@property
	def do_no(self) -> int:
		return self._instance.DoNo
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
