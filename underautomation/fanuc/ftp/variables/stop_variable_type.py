import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import StopVariableType as stop_variable_type

class StopVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stop_variable_type()
		else:
			self._instance = _internal
	@property
	def tick(self) -> int:
		return self._instance.Tick
	@property
	def spd(self) -> float:
		return self._instance.Spd
	@property
	def pos1(self) -> float:
		return self._instance.Pos1
	@property
	def pos2(self) -> float:
		return self._instance.Pos2
	@property
	def pos3(self) -> float:
		return self._instance.Pos3
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
