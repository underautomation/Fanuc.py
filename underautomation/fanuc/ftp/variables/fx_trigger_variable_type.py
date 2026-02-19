import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FxTriggerVariableType as fx_trigger_variable_type

class FxTriggerVariableType(GenericVariableType):
	'''Describes the Fanuc type FX_TRIGGER_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fx_trigger_variable_type()
		else:
			self._instance = _internal

	@property
	def start_model(self) -> int:
		'''Value of variable $START_MODEL'''
		return self._instance.StartModel

	@property
	def start_step(self) -> int:
		'''Value of variable $START_STEP'''
		return self._instance.StartStep

	@property
	def start_prog(self) -> str:
		'''Value of variable $START_PROG'''
		return self._instance.StartProg

	@property
	def stop_model(self) -> int:
		'''Value of variable $STOP_MODEL'''
		return self._instance.StopModel

	@property
	def stop_step(self) -> int:
		'''Value of variable $STOP_STEP'''
		return self._instance.StopStep

	@property
	def stop_prog(self) -> str:
		'''Value of variable $STOP_PROG'''
		return self._instance.StopProg

	@property
	def axes(self) -> int:
		'''Value of variable $AXES'''
		return self._instance.Axes

	@property
	def data_type(self) -> int:
		'''Value of variable $DATA_TYPE'''
		return self._instance.DataType

	@property
	def datetime(self) -> int:
		'''Value of variable $DATETIME'''
		return self._instance.Datetime

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FxTriggerVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
