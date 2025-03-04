import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FxTriggerVariableType as fx_trigger_variable_type

class FxTriggerVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fx_trigger_variable_type()
		else:
			self._instance = _internal
	@property
	def start_model(self) -> int:
		return self._instance.StartModel
	@property
	def start_step(self) -> int:
		return self._instance.StartStep
	@property
	def start_prog(self) -> str:
		return self._instance.StartProg
	@property
	def stop_model(self) -> int:
		return self._instance.StopModel
	@property
	def stop_step(self) -> int:
		return self._instance.StopStep
	@property
	def stop_prog(self) -> str:
		return self._instance.StopProg
	@property
	def axes(self) -> int:
		return self._instance.Axes
	@property
	def data_type(self) -> int:
		return self._instance.DataType
	@property
	def datetime(self) -> int:
		return self._instance.Datetime
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
