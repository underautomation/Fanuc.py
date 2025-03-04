import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TraceItemVariableType as trace_item_variable_type

class TraceItemVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = trace_item_variable_type()
		else:
			self._instance = _internal
	@property
	def prg_name(self) -> str:
		return self._instance.PrgName
	@property
	def var_name(self) -> str:
		return self._instance.VarName
	@property
	def desc(self) -> str:
		return self._instance.Desc
	@property
	def units(self) -> str:
		return self._instance.Units
	@property
	def type(self) -> int:
		return self._instance.Type
	@property
	def io_type(self) -> int:
		return self._instance.IoType
	@property
	def port_num(self) -> int:
		return self._instance.PortNum
	@property
	def square(self) -> float:
		return self._instance.Square
	@property
	def slope(self) -> float:
		return self._instance.Slope
	@property
	def intercept(self) -> float:
		return self._instance.Intercept
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
