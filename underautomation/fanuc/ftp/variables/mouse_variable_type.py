import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MouseVariableType as mouse_variable_type

class MouseVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mouse_variable_type()
		else:
			self._instance = _internal
	@property
	def action(self) -> int:
		return self._instance.Action
	@property
	def button(self) -> int:
		return self._instance.Button
	@property
	def row(self) -> int:
		return self._instance.Row
	@property
	def column(self) -> int:
		return self._instance.Column
	@property
	def time(self) -> int:
		return self._instance.Time
	@property
	def reserved(self) -> int:
		return self._instance.Reserved
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
