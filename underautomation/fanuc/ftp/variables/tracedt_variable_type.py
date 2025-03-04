import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TracedtVariableType as tracedt_variable_type

class TracedtVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tracedt_variable_type()
		else:
			self._instance = _internal
	@property
	def ept_index(self) -> int:
		return self._instance.EptIndex
	@property
	def line_num(self) -> int:
		return self._instance.LineNum
	@property
	def file_ofst(self) -> int:
		return self._instance.FileOfst
	@property
	def exec_type(self) -> int:
		return self._instance.ExecType
	@property
	def line_st(self) -> int:
		return self._instance.LineSt
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
