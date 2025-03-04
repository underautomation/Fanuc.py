import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MrHistVariableType as mr_hist_variable_type

class MrHistVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mr_hist_variable_type()
		else:
			self._instance = _internal
	@property
	def group(self) -> int:
		return self._instance.Group
	@property
	def id(self) -> int:
		return self._instance.Id
	@property
	def type(self) -> int:
		return self._instance.Type
	@property
	def due_type(self) -> int:
		return self._instance.DueType
	@property
	def name(self) -> str:
		return self._instance.Name
	@property
	def due_act(self) -> int:
		return self._instance.DueAct
	@property
	def due_date(self) -> float:
		return self._instance.DueDate
	@property
	def warn_date(self) -> int:
		return self._instance.WarnDate
	@property
	def done(self) -> bool:
		return self._instance.Done
	@property
	def done_date(self) -> int:
		return self._instance.DoneDate
	@property
	def done_past(self) -> str:
		return self._instance.DonePast
	@property
	def recorded(self) -> bool:
		return self._instance.Recorded
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
